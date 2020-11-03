#Script to search google for CPU ID when hunting for Ryzen 7 5800X
from sys import argv
import sys
import config
from pushbullet import Pushbullet   
pb = Pushbullet(config.pbtoken)
def CPUSearch(CPUquery,searchstring=".ca"):
    print("Searching......")
    found = False
    try: 
        from googlesearch import search 
    except ImportError:  
        print("No module found, make sure it is imported") 
    for j in search(CPUquery, tld="com", num=10, stop=10, pause=2): 
        if searchstring in j:
            print(j)
            push = pb.push_note("AMD CPU", "The link is " + j)
            found = True
    if found == False:
        print("No links found yet......")



CPUSearch(*argv[1:])