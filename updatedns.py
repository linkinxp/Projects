import json
import ovh
from requests import get

newip = get('https://api.ipify.org').text
client = ovh.Client(config_file='api.conf')

#WG entry
result = client.put('/domain/zone/linkinxp.com/record/5001270970', subDomain='wg', target=newip, ttl=0,)
#Emby entry
result = client.put('/domain/zone/linkinxp.com/record/5002083523', subDomain='emby', target=newip, ttl=0,)


#  Cron 0 12 * * *