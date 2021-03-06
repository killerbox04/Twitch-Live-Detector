#main.py

import wget, time, os
from datetime import *

mainDir = "/home/trident/Documents/Python/Twitch-Live-Detector)"
mainDirCont = os.listdir(mainDir)

for item in mainDirCont:
    if item.endswith(".tmp"):
        os.remove(os.path.join(mainDir, item ))

global targets
targets = ("nymn", "forsen", "zoil")


while True:
    for target in targets:
    
        url = f"https://www.twitch.tv/{target}"
        output = f"/home/trident/Documents/Python/Twitch-Live-Detector/{target}"

        wget.download(url = url, out = target, bar = None)
        
        outputOpen = open(target, "r")
        
        print(datetime.now().strftime("%H:%M:%S"))
        
        for line in outputOpen:  
            #checking string is present in line or not
            if "live_user" in line:
                outputOpen.close()
                print(f"{target} is Live")
                os.remove(target)
                break
            else:
                outputOpen.close()
                print(f"{target} is Not Live")
                os.remove(target)
                break
            print("test")
   
    
    time.sleep(3)
    print("\n")
