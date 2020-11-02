#Script to search google for CPU ID when hunting for Ryzen 7 5800X

from sys import argv
def CPUSearch(CPUquery):
    print("Searching......")
    found = False
    try: 
        from googlesearch import search 
    except ImportError:  
        print("No module found, make sure it is imported") 
#Iterate
    for j in search(CPUquery, tld="com", num=10, stop=10, pause=2): 
        if ".ca" in j:
            print(j)
            found = True
    if found == False:
        print("No links found yet......")

CPUSearch(*argv[1:])