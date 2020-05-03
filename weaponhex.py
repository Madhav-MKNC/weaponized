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
Logo="""\033[36m

██╗    ██╗███████╗ █████╗ ██████╗  ██████╗ ███╗   ██╗    ██╗  ██╗███████╗██╗  ██╗
██║    ██║██╔════╝██╔══██╗██╔══██╗██╔═══██╗████╗  ██║    ██║  ██║██╔════╝╚██╗██╔╝
██║ █╗ ██║█████╗  ███████║██████╔╝██║   ██║██╔██╗ ██║    ███████║█████╗   ╚███╔╝
██║███╗██║██╔══╝  ██╔══██║██╔═══╝ ██║   ██║██║╚██╗██║    ██╔══██║██╔══╝   ██╔██╗
╚███╔███╔╝███████╗██║  ██║██║     ╚██████╔╝██║ ╚████║    ██║  ██║███████╗██╔╝ ██╗
 ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝╚═╝      ╚═════╝ ╚═╝  ╚═══╝    ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
           【This】 【Tool】 【is】【Created】 【By】 【CybSec NITW】
           
               \033[33m[+] https://github.com/CybSec-NITW [+]

               \033[91m[!] \033[32mThis Tool is Only For Educational Purpose
               Please Don\'t use for \033[91mAny illegal Activity [!]
    \033[97m """

#         STRUCTURE OF THIS TOOL
#   MAIN MENU -> CATEGORY MENU -> TOOL MENU (with instruction on each menu)

def menu():
    print(Logo + """\033[0m
        \033[36m[+] \033[32mThis Tool Must Run as a Root..\033[36m[+]\033[32m
        [01] \033[36mReverse Engineering \033[32m
        [02] \033[36mPwning \033[32m
        [03] \033[36mForensics \033[32m
        [04] \033[36mCryptography \033[32m
        [05] \033[36mWeb Exploitation \033[32m
        [06] \033[36mOSINT \033[32m
        [99] \033[36mExit
        """)

    choice = input("\033[35mEnter your choice  =>> \033[32m")
    if choice == "1" or choice == "01":
        clearScr()
        print(Logo)
        reverse()
    elif choice == "2" or choice == "02":
        clearScr()
        print(Logo)
        pwning()
    elif choice == "3" or choice == "03":
        clearScr()
        print(Logo)
        forensic()
    elif choice == "4" or choice == "04":
        clearScr()
        print(Logo)
        crypto()
    elif choice == "5" or choice == "05":
        clearScr()
        print(Logo)
        web()
    elif choice == "6" or choice == "06":
        clearScr()
        print(Logo)
        osint()
    elif choice == "99" :
        clearScr(), sys.exit()
        exit()
    elif choice == "":
        menu()
    else:
        print("\033[31mWrong Input...!!")
        time.sleep(3)
        menu()

# we have to complete each function one by one
#
# For REVERSE
#  - Quick SCAN includes STRING, ltrace, etc. Integrate it with python Options - Scan, back; Take argument as file. Print instruction that file should be in same directory
#  - Binany ninja - menu option Install, Run, Back
#  - Ghidra - same as binary ninja

def reverse():
    print("""
        \033[32m[1]  \033[36mQuick Scan
        \033[32m[2]  \033[36mBinary Ninja
        \033[32m[3]  \033[36mGhidra
        \033[32m[99] \033[36mBack
        """)
    choice = input("\033[35mEnter your choice =>>\033[32m")
    if choice == "1":
        clearScr()
        rscan()
    elif choice == "2":
        clearScr()
        bninja()
    elif choice == "3":
        clearScr()
        ghidr()
    elif choice == "99":
        menu()
    else :
        menu()

# For PWN
#
# - Buffer Overflow Script
#       - Custom Overflow
#       - Bruteforce
# - some pwn related tools
#

def pwning():
    print("""
        \033[32m[1]  \033[36mBuffer Overflow Scan
        \033[32m[2]  \033[36mAdd more tools
        \033[32m[99] \033[36mBack
        """)
    choice = input("\033[35mEnter your choice =>>\033[32m")
    if choice == "1":
        clearScr()
        bscan()
    elif choice == "2":
        clearScr()
        moretool()
    elif choice == "99":
        menu()
    else :
        menu()

# Forensics
#  - Normal forensic scan It will include a script which will search that flag format by trying combinations like string picture, exif tool it, trying to rectify hexedit(I will make hexedit part - $root), think more
#  - Image Forensics Tool
#  - Disk Forensics Tool (Autopsy)
#  Think more

def forensic():
    print("""
        \033[32m[1]  \033[36mForensics Scan
        \033[32m[2]  \033[36mAutopsy
        \033[32m[3]  \033[36mAdd more tools
        \033[32m[99] \033[36mBack
        """)
    choice = input("\033[35mEnter your choice =>>\033[32m")
    if choice == "1":
        clearScr()
        forenscan()
    elif choice == "2":
        clearScr()
        mretools()
    elif choice == "99":
        menu()
    else :
        menu()

# CRYPTOGRAPHY
# - Crypto Scan bruteforcing with popular encryption like base64
# - vigenere
# - caesar
# - some popular and easy to implement encryption decryption scripts
# - RSA tool from github
# - think more

def crypto():
    print("""
        \033[32m[1]  \033[36mCrypto Scan
        \033[32m[2]  \033[36mVigenere
        \033[32m[3]  \033[36mCaesar
        \033[32m[4]  \033[36mMore Tools
        \033[32m[99] \033[36mBack
        """)
    choice = input("\033[35mEnter your choice =>>\033[32m")
    if choice == "1":
        clearScr()
        cryscan()
    elif choice == "2":
        clearScr()
        vigenere()
    elif choice == "3":
        clearScr()
        caesar()
    elif choice == "4":
        clearScr()
        moretool()
    elif choice == "99":
        menu()
    else :
        menu()

# Web Attack
# Somewhere I have seen that curl helps in some challenges. Try implementing it. Try making script to steal cookies
# Add tools here like burp wireshark, etc, see kaumodaki web attack part.
#

def web():
    print("""
        \033[32m[1]  \033[36mSelfmade WebScript
        \033[32m[2]  \033[36mBurp Suite
        \033[32m[3]  \033[36mAdd more tools
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
        \033[32m[1]  \033[36mOSINT Scan
        \033[32m[1]  \033[36mSome Tools
        \033[32m[1]  \033[36mBack
        """)
    choice = input("\033[35mEnter your choice =>>\033[32m")
    if choice == "1":
        clearScr()
        oscan()
    elif choice == "2":
        clearScr()
        mrtools()
    elif choice == "99":
        menu()
    else :
        menu()

def clearScr():
    if system() == 'Linux':
        os.system('clear')
    if system() == 'Windows':
        os.system('cls')

if __name__ == "__main__":
    try:
        if system() == 'Linux':
            if path.exists("/home/"):
                os.chdir("/home")
                if os.path.isdir('WeaponHEX'):
                    os.chdir("/home/WeaponHEX/")
                    menu()
                else :
                    os.system("mkdir WeaponHEX")
                    os.chdir("/home/WeaponHEX/")
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
