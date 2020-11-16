#Script to change brightness
#s!/usr/bin/env python3
import os
f = open("/sys/class/power_supply/ACAD/online","r")
contents = f.read()
commandtoruncon = "xrandr --output eDP --brightness 1.0"
commandtorundis = "xrandr --output eDP --brightness 0.6"

if "1" in contents:
    print("Connected to power")
    os.system(commandtoruncon)
else:
    print("Not connected")
    os.system(commandtorundis)
