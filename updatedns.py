import json
import ovh
from requests import get

newip = get('https://api.ipify.org').text
#client = ovh.Client(config_file='api.conf')

client = ovh.Client(
    endpoint='ovh-ca',
    application_key='X',    
    application_secret='X', 
    consumer_key='X',      
)


#WG entry
result = client.put('/domain/zone/linkinxp.com/record/5001270970', subDomain='wg', target=newip, ttl=0,)
#Emby entry
result = client.put('/domain/zone/linkinxp.com/record/5002083523', subDomain='emby', target=newip, ttl=0,)
#Zoneminder entry
result = client.put('/domain/zone/linkinxp.com/record/5002349260', subDomain='zm', target=newip, ttl=0,)
result = client.post('/domain/zone/linkinxp.com/refresh')



print(result)

#5001270962
#5001270963
#5001270964
#5002083523
#5002199119
#5001270970
#5001270967
#5001270965
#5002018009
#5001270966
#5001270969
#5002349260
#5002018008
#5001270968
