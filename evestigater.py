import os
import sys 
import time
import requests

os.system("clear")
print """ 
========================================================================
=  ______       _                     _   _             _              =
= |  ____|     (_)                   | | (_)           | |             =
= | |__         _ _ ____   _____  ___| |_ _  __ _  __ _| |_ ___ _ __   =
= |  __| ====  | | '_ \ \ / / _ \/ __| __| |/ _` |/ _` | __/ _ \ '__|  =
= | |____      | | | | \ V /  __/\__ \ |_| | (_| | (_| | ||  __/ |     =
= |______|     |_|_| |_|\_/ \___||___/\__|_|\__, |\__,_|\__\___|_|     =
=                                            __/ |                     =
=                                           |___/                      =
========================================================================                                        
"""
print """
=========== MENU ===================
       Code  |     Tool 
------------------------------------
        1    |  Traceroute
        2    |  Ping Test
        3    |  DNS Lookup
        4    |  Reverse DNS
        5    |  Find DNS Host
        6    |  Find Shared DNS
        7    |  Zone Transfer
        8    |  Whois Lookup
        9    |  IP Location Lookup
        10   |  Reverse IP Lookup
        11   |  TCP Port Scan
        12   |  Subnet Lookup
        13   |  HTTP Header Check
        14   |  Extract Page Links
        15   |  Exit
=====================================
"""
def run():

    try:
        choice = input("Enter option code: ")

        if choice == 1:
            print("\n")
            print("== Traceroute ==")
            target = raw_input("[+] Target : ")
            print("\n")
            url = "https://api.hackertarget.com/mtr/?q=" + target
            request = requests.get(url)
            txt = request.text
            print(txt)

        elif choice == 2:
            print("\n")
            print("== Ping ==")
            target = raw_input("[+] Target : ")
            print("\n")
            url = "https://api.hackertarget.com/nping/?q=" + target
            request = requests.get(url)
            txt = request.text
            print(txt)

        elif choice == 3:
            print("\n")
            print("== DNS Lookup ==")
            target = raw_input("[+] Target : ")
            print("\n")
            url = "https://api.hackertarget.com/dnslookup/?q=" + target
            request = requests.get(url)
            txt = request.text
            print(txt)

        elif choice == 4:
            print("\n")
            print("== Reverse DNS ==")
            target = raw_input("[+] Target : ")
            print("\n")
            url = "https://api.hackertarget.com/reversedns/?q=" + target
            request = requests.get(url)
            txt = request.text
            print(txt)

        elif choice == 5:
            print("\n")
            print("== Find DNS Host ==")
            target = raw_input("[+] Target : ")
            print("\n")
            url = "https://api.hackertarget.com/hostsearch/?q=" + target
            request = requests.get(url)
            txt = request.text
            print(txt)

        elif choice == 6:
            print("\n")
            print("== Find Shared DNS ==")
            target = raw_input("[+] Target : ")
            print("\n")
            url = "https://api.hackertarget.com/findshareddns/?q=" + target
            request = requests.get(url)
            txt = request.text
            print(txt)

        elif choice == 7:
            print("\n")
            print("== Zone Transfer ==")
            target = raw_input("[+] Target : ")
            print("\n")
            url = "https://api.hackertarget.com/zonetransfer/?q=" + target
            request = requests.get(url)
            txt = request.text
            print(txt)

        elif choice == 8:
            print("\n")
            print("== Whois Lookup ==")
            target = raw_input("[+] Target : ")
            print("\n")
            url = "https://api.hackertarget.com/whois/?q=" + target
            request = requests.get(url)
            txt = request.text
            print(txt)

        elif choice == 9:
            print("\n")
            print("== IP Location Lookup ==")
            target = raw_input("[+] Target : ")
            print("\n")
            url = "https://api.hackertarget.com/geoip/?q=" + target
            request = requests.get(url)
            txt = request.text
            print(txt)

        elif choice == 10:
            print("\n")
            print("== Reverse IP Lookup ==")
            target = raw_input("[+] target : ")
            print("\n")
            url = "https://api.hackertarget.com/reverseiplookup/?q=" + target
            request = requests.get(url)
            txt = request.text
            print(txt)

        elif choice == 11:
            print("\n")
            print("== TCP Port Scan ==")
            target = raw_input("[+] Target : ")
            print("\n")
            url = "https://api.hackertarget.com/nmap/?q=" + target
            request = requests.get(url)
            txt = request.text
            print(txt)

        elif choice == 12:
            print("\n")
            print("== Subnet Lookup ==")
            target = raw_input("[+] Target : ")
            print("\n")
            url = "https://api.hackertarget.com/subnetcalc/?q=" + target
            request = requests.get(url)
            txt = request.text
            print(txt)

        elif choice == 13:
            print("\n")
            print("== HTTP Header Check script running ==")
            target = raw_input("[+] Target : ")
            print("\n")
            url = "https://api.hackertarget.com/httpheaders/?q=" + target
            request = requests.get(url)
            txt = request.text
            print(txt)

        elif choice == 14:
            print("\n")
            print("== Extract Page Links ==")
            target = raw_input("[+] Target : ")
            print("\n")
            url = "https://api.hackertarget.com/pagelinks/?q=" + target
            request = requests.get(url)
            txt = request.text
            print(txt)

        elif choice == 15:
            exit()

    except KeyboardInterrupt:
        print("\nAborted!")
        quit()
    except:
        print("Invalid Optioin !\n")
        return run()
run()
