import pyping
import time
import playsound


pingsec = input("Enter the Time in seconds:")

ip = raw_input("Enter the ip address:")

t = time.time()



try:
    while time:
        if time.time()-t>pingsec:
            response = pyping.ping(ip)

            if response.ret_code == 0:
                print("successful")
                t = time.time()

            else:
                play = playsound.playsound("/root/Downloads/Siren.mp3")
                
except:
    print("link failure")




