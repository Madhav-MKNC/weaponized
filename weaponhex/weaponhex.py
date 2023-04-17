##!/usr/bin/env python3
# -*- coding: UTF-8 -*-



import os
import sys
import argparse
import threading
import webbrowser
import requests
# import urllib
import time
import http.client
import urllib.request
import sys
import json
import telnetlib
import glob
# import urllib2
import socket
import base64
from getpass import getpass
# from command import *
import subprocess
from sys import argv
import random
import queue
import subprocess
import re
import getpass
from os import path
from platform import system
from urllib.parse import urlparse
from xml.dom import minidom
from optparse import OptionParser
from time import sleep
from platform import system


# from scripts
from scripts.constants import *
from scripts.utils import clearScreen, printScreen

def menu():
    print(BANNER)
    print(MENU)

    choice = input(f"{PURPLE} [+] Enter your choice  =>> {WHITE}").strip()
    printScreen()

    if choice not in ["1", "2", "3", "4", "5", "6", "99"]:
        print(f"{RED} [-] '{choice}' is an invalid input {WHITE}")
        time.sleep(2)
        menu()

    if choice == "1": reverse()

    elif choice == "2": pwning()

    elif choice == "3": forensic()

    elif choice == "4": crypto()  

    elif choice == "5": web()

    elif choice == "6": osint()

    elif choice == "99": Exit()


# we have to complete each function one by one
#
# For REVERSE
#  - Quick SCAN includes STRING, ltrace, etc. Integrate it with python Options - Scan, back; Take argument as file. Print instruction that file should be in same directory
#  - Binany ninja - menu option Install, Run, Back
#  - Ghidra - same as binary ninja
# 

def reverse():
    print(REVERSE_MENU)

    choice = input(f"{PURPLE} [+] Enter your choice  =>> {WHITE}").strip()
    printScreen()
    
    if choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "0", "99"]:
        print(f"{RED} [-] '{choice}' is an invalid input {WHITE}")
        time.sleep(2)
        menu()

    if choice == "1": rscan()

    elif choice == "2": bninja()

    elif choice == "3": ghidr()

    elif choice == "4": IDA()

    elif choice == "5": uncompyle6()

    elif choice == "6": gdb()

    elif choice == "7": radare2()

    elif choice == "8": apktool()

    elif choice == "99": Exit()

    elif choice == "0": menu()


# For PWN
#
# - Buffer Overflow Script
#       - Custom Overflow
#       - Bruteforce
# - some pwn related tools
#

def pwning():
    print(PWNING_MENU)
    
    choice = input(f"{PURPLE} [+] Enter your choice  =>> {WHITE}").strip()
    printScreen()
    
    if choice not in ["1", "2", "3", "4", "5", "6", "7", "0", "99"]:
        print(f"{RED} [-] '{choice}' is an invalid input {WHITE}")
        time.sleep(2)
        menu()

    if choice == "1": pwnscan()

    elif choice == "2": pwn_tools()

    elif choice == "3": pwndbg()

    elif choice == "4": IPython()

    elif choice == "5": welpwn()

    elif choice == "6": glibc()

    elif choice == "7": an_important_link()

    elif choice == "99": Exit()

    elif choice == "0": menu()


# Forensics
#  - Normal forensic scan It will include a script which will search that flag format by trying combinations like string picture, exif tool it, trying to rectify hexedit(I will make hexedit part - $root), think more
#  - Image Forensics Tool
#  - Disk Forensics Tool (Autopsy)
#  Think more
# 

def forensic():
    print(FORENSIC_MENU)

    choice = input(f"{PURPLE} [+] Enter your choice  =>> {WHITE}").strip()
    printScreen()
    
    if choice not in ["1", "2", "3", "4", "5", "6", "7", "8", "0", "99"]:
        print(f"{RED} [-] '{choice}' is an invalid input {WHITE}")
        time.sleep(2)
        menu()

    if choice == "1": forenscan()

    elif choice == "2": hexedit()

    elif choice == "3": binwalk()

    elif choice == "4": exiftool()

    elif choice == "5": steg_tools()

    elif chioce == "6": PNGcheck()

    elif choice == "7": PDFparser()

    elif choice == "8": autospy()

    elif choice == "99": Exit()

    elif choice == "0": menu()


# CRYPTOGRAPHY
# - Crypto Scan bruteforcing with popular encryption like base64
# - vigenere
# - caesar
# - some popular and easy to implement encryption decryption scripts
# - RSA tool from github
# - think more

def crypto():
    print(CRYPTO_MENU)

    choice = input(f"{PURPLE} [+] Enter your choice  =>> {WHITE}").strip()
    printScreen()
    
    if choice not in ["1", "2", "3", "4", "5", "6", "7", "0", "99"]:
        print(f"{RED} [-] '{choice}' is an invalid input {WHITE}")
        time.sleep(2)
        menu()

    if choice == "1": cryscan() # RSACTFTool

    elif choice == "2": vigenere() # feather duster

    elif choice == "3": caesar() # XOR tool

    elif choice == "4": hashcat()

    elif choice == "5": john()

    elif choice == "6": cryptool()

    elif choice == "7": an_important_link()

    elif choice == "99": Exit()

    elif choice == "0": menu()


# Web Attack
# Somewhere I have seen that curl helps in some challenges. Try implementing it. Try making script to steal cookies
# Add tools here like burp wireshark, etc, see kaumodaki web attack part.
#

def web():
    print("""
        \033[32m[1]  \033[36mBurp Suite
        \033[32m[2]  \033[36mWireshark
        \033[32m[2]  \033[36msqlmap
        \033[32m[2]  \033[36mdsniff
        \033[32m[2]  \033[36msubbrute
        \033[32m[2]  \033[36mgobuster
        \033[32m[2]  \033[36mw3af
        \033[32m[3]  \033[36mAXSSer
        \033[32m[99] \033[36mBack
        """)
    choice = input("\033[35mEnter your choice =>>\033[32m")
    if choice == "1":
        clearScr()
        webscan()
    elif choice == "2":
        clearScr()
        mortools()
    elif choice == "99":
        menu()
    else :
        menu()

# OSINT
# There are some popular tools of OSINT, refer those tools here.
#
# Also try to use api here, if it can work.
#

def osint():
    print("""
        \033[32m[1]  \033[36mSocial Scan
        \033[32m[2]  \033[36mDataSploit
        \033[32m[3]  \033[36mReconSpider
        \033[32m[99]  \033[36mBack
        """)
    choice = input("\033[35mEnter your choice =>>\033[32m")
    if choice == "1":
        clearScr()
        soscan()
    elif choice == "2":
        clearScr()
        dtsploit()
    elif choice == "3":
        clearScr()
        reconspider()
    elif choice == "99":
        menu()
    else :
        menu()
        
def soscan():
    print("\033[32mSocial Scan Tool is a tool which scans username on most of the popular social media websites.")
    usname = input("\033[35mEnter username =>>\033[32m")
    os.system("./socialscan.sh " + usname + " -fu")
    
def dtsploit():
    print("An OSINT framework to perform various recon techniques on Companies, People, Phone, Number, \nBitcoin Addresses, etc aggregate all the raw data, and give data in multiple formats.")
    print("""
        \033[32m[1]   \033[36mInstall
        \033[32m[99]  \033[36mBack
        """)
    dtchoice = input("\033[35mEnter your choice =>>\033[32m")
    if dtchoice == "1":
        os.system("sudo git clone https://github.com/DataSploit/datasploit.git")
        os.system("cd datasploit && pip install --upgrade --force-reinstall -r requirements.txt")
        print("\033[32m[+]  \033[33mDataSploit Installed Successfully.")
    elif dtchoice == "99":
        osint()
    else:
        menu()
        
def reconspider():
    print("ReconSpider is most Advanced Open Source Intelligence (OSINT) Framework for scanning IP Address, \nEmails, Websites, Organizations and find out information from different sources.")
    print("""
        \033[32m[1]   \033[36mInstall
        \033[32m[2]   \033[36mRun
        \033[32m[99]  \033[36mBack
        """)
    rspidchoice = input("\033[35mEnter your choice =>>\033[32m")
    if rspidchoice == "1":
        os.system("sudo git clone https://github.com/bhavsec/reconspider.git")
        os.system("sudo apt install python3 python3-pip && cd reconspider && sudo python3 setup.py install")
        print("\033[32m[+]  \033[33mReconSpider Installed Successfully.")
    elif rspidchoice == "2":
        os.system("cd reconspider && python3 reconspider.py")
    elif rspidchoice == "99":
        osint()
    else :
        menu()
    

if __name__ == "__main__":
    try:
        if system() == 'Linux':
            if path.exists("/home/"):
                os.chdir("/home/groot/Desktop")
                if os.path.isdir('WeaponHEX'):
                    os.chdir("/home/groot/Desktop/WeaponHEX/")
                    menu()
                else :
                    os.system("mkdir WeaponHEX")
                    os.chdir("/home/groot/Desktop/WeaponHEX/")
                    menu()
        elif path.exists('/data'):
            os.chdir("data/data/com.termux/files/home/")
            if os.path.isdir('WeaponHEX'):
                os.chdir("data/data/com.termux/files/home/WeaponHEX/")
                menu()
            else :
                os.system("mkdir WeaponHEXstore")
                os.chdir("data/data/com.termux/files/home/WeaponHEX/")
                menu()
    except KeyboardInterrupt:
        print(" Terminating ..!!!")
        time.sleep(1)

if __name__ == "__main__":
    print(Logo)