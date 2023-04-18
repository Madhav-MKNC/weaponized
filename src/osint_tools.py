# OSINT tools



def social_scan():
    pass

def data_sploit():
    pass

def recon_spider():
    pass




# ////////////////////////////

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