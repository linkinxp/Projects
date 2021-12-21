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
result = client.post('/domain/zone/linkinxp.com/refresh')



print(result)

#  Cron 0 12 * * *
