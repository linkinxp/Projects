$isitcharging = Get-WmiObject win32_Battery | Select-Object -ExpandProperty BatteryStatus
$time = Get-Date

if ($isitcharging -eq "2") 
{
$currentvalue = Get-Ciminstance -Namespace root/WMI -ClassName WmiMonitorBrightness | Select-Object -ExpandProperty CurrentBrightness
(Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,85)
"Laptop is charging --- Current brightness is " + $currentvalue + " brightness set to 85"  + " at " + $time | Out-File -Append -FilePath C:\bin\Logs\Brightness.log
}
else
{
    
$setvalue = "65"
$currentvalue = Get-Ciminstance -Namespace root/WMI -ClassName WmiMonitorBrightness | Select-Object -ExpandProperty CurrentBrightness
(Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,$setvalue)
if ($setvalue -eq $currentvalue){
"Laptop is not charging --- Current brightness is " + $currentvalue + " brightness remains the same" + " at " + $time | Out-File -Append -FilePath C:\bin\Logs\Brightness.log
}
else{
"Laptop is not charging --- Current brightness is " + $currentvalue + " brightness set to $setvalue" + " at " + $time | Out-File -Append -FilePath C:\bin\Logs\Brightness.log
}}
exit
