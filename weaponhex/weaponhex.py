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

Logo="""\033[33m

██╗    ██╗███████╗ █████╗ ██████╗  ██████╗ ███╗   ██╗    ██╗  ██╗███████╗██╗  ██╗
██║    ██║██╔════╝██╔══██╗██╔══██╗██╔═══██╗████╗  ██║    ██║  ██║██╔════╝╚██╗██╔╝
██║ █╗ ██║█████╗  ███████║██████╔╝██║   ██║██╔██╗ ██║    ███████║█████╗   ╚███╔╝
██║███╗██║██╔══╝  ██╔══██║██╔═══╝ ██║   ██║██║╚██╗██║    ██╔══██║██╔══╝   ██╔██╗
╚███╔███╔╝███████╗██║  ██║██║     ╚██████╔╝██║ ╚████║    ██║  ██║███████╗██╔╝ ██╗
 ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝╚═╝      ╚═════╝ ╚═╝  ╚═══╝    ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
           \033[36m【This】 【Tool】 【is】【Created】 【By】 【CybSec NITW】
           
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
        \033[32m[1]  \033[36mReverse Scan
        \033[32m[2]  \033[36mGhidra
        \033[32m[3]  \033[36mBinary Ninja
        \033[32m[4]  \033[36mIDA
        \033[32m[4]  \033[36muncompyle6
        \033[32m[4]  \033[36mgdb
        \033[32m[4]  \033[36mradare2
        \033[32m[4]  \033[36mapktool
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
        \033[32m[1]  \033[36mPwn Scan
        \033[32m[2]  \033[36mpwntools
        \033[32m[4]  \033[36mpwndbg
        \033[32m[4]  \033[36mIPython
        \033[32m[4]  \033[36mwelpwn
        \033[32m[4]  \033[36mglibc-all-in-one
        \033[32m[4]  \033[36mAn important link
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
        \033[32m[2]  \033[36mhexedit
        \033[32m[3]  \033[36mbinwalk
        \033[32m[4]  \033[36mexiftool
        \033[32m[4]  \033[36mSteganography Tools
        \033[32m[4]  \033[36mPNGcheck
        \033[32m[4]  \033[36mPDFparser
        \033[32m[4]  \033[36mAutopsy
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
        \033[32m[1]  \033[36mRSACTFTool
        \033[32m[2]  \033[36mFeatherDuster
        \033[32m[3]  \033[36mXORTool
        \033[32m[4]  \033[36mHashCat
        \033[32m[4]  \033[36mJohnTheRipper
        \033[32m[4]  \033[36mCryptool
        \033[32m[4]  \033[36mAn important link
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
            

def clearScr():
    if system() == 'Linux':
        os.system('clear')
    if system() == 'Windows':
        os.system('cls')

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
