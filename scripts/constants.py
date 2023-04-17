# constants for ../weaponhex.py


# for colored output
BLACK = "\u001b[30m"
RED = "\u001b[31m"
GREEN = "\u001b[32m"
YELLOW = "\u001b[33m"
BLUE = "\u001b[34m"
CYAN = "\u001b[36m"
WHITE = "\u001b[37m"
LGREEN = '\033[92m'
CLEAR = '\033[0m'
BOLD = '\033[01m'
CYAN = '\033[96m'
PURPLE = '\033[35m'


# banner
BANNER = f"""
    {YELLOW}
    ██╗    ██╗███████╗ █████╗ ██████╗  ██████╗ ███╗   ██╗    ██╗  ██╗███████╗██╗  ██╗
    ██║    ██║██╔════╝██╔══██╗██╔══██╗██╔═══██╗████╗  ██║    ██║  ██║██╔════╝╚██╗██╔╝
    ██║ █╗ ██║█████╗  ███████║██████╔╝██║   ██║██╔██╗ ██║    ███████║█████╗   ╚███╔╝
    ██║███╗██║██╔══╝  ██╔══██║██╔═══╝ ██║   ██║██║╚██╗██║    ██╔══██║██╔══╝   ██╔██╗
    ╚███╔███╔╝███████╗██║  ██║██║     ╚██████╔╝██║ ╚████║    ██║  ██║███████╗██╔╝ ██╗
    ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝╚═╝      ╚═════╝ ╚═╝  ╚═══╝    ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
    {BLUE}
    ======================>【This】 【Tool】 【is】【Created】 【By】 【CybSec NITW】
    {YELLOW}
        [+] https://github.com/CybSec-NITW [+]
    {RED}
        [!] {GREEN}This Tool is Only For Educational Purpose
            Please Don\'t use for {RED}Any illegal Activity [!]
    {WHITE}"""


MENU = f"""
    {LGREEN} [+] This Tool Must Run as a Root..[+]

    {GREEN} [01] {BLUE} Reverse Engineering 
    {GREEN} [02] {BLUE} Pwning 
    {GREEN} [03] {BLUE} Forensics 
    {GREEN} [04] {BLUE} Cryptography 
    {GREEN} [05] {BLUE} Web Exploitation 
    {GREEN} [06] {BLUE} OSINT 
    {GREEN} [99] {RED} Exit
    {WHITE}"""


REVERSE_MENU = f"""
    {GREEN} [0]  {GREEN} Back
    {GREEN} [1]  {BLUE} Reverse Scan
    {GREEN} [2]  {BLUE} Ghidra
    {GREEN} [3]  {BLUE} Binary Ninja
    {GREEN} [4]  {BLUE} IDA
    {GREEN} [5]  {BLUE} uncompyle6
    {GREEN} [6]  {BLUE} gdb
    {GREEN} [7]  {BLUE} radare2 
    {GREEN} [8]  {BLUE} apktool
    {GREEN} [99] {RED} Exit
    {WHITE}"""


PWNING_MENU = f"""
    {GREEN} [0]  {GREEN} Back
    {GREEN} [1]  {BLUE} Pwn Scan
    {GREEN} [2]  {BLUE} pwntools
    {GREEN} [3]  {BLUE} pwndbg
    {GREEN} [4]  {BLUE} IPython
    {GREEN} [5]  {BLUE} welpwn
    {GREEN} [6]  {BLUE} glibc-all-in-one
    {GREEN} [7]  {BLUE} An important link
    {GREEN} [99] {RED} Exit
    {WHITE}"""


FORENSIC_MENU = f"""
    {GREEN} [0]  {GREEN} Back
    {GREEN} [1]  {BLUE} Forensics Scan
    {GREEN} [2]  {BLUE} hexedit
    {GREEN} [3]  {BLUE} binwalk
    {GREEN} [4]  {BLUE} exiftool
    {GREEN} [5]  {BLUE} Steganography Tools
    {GREEN} [6]  {BLUE} PNGcheck
    {GREEN} [7]  {BLUE} PDFparser
    {GREEN} [8]  {BLUE} Autopsy
    {GREEN} [99] {RED} Exit
    {WHITE}"""


CRYPTO_MENU = f"""
    {GREEN} [0]  {GREEN} Back
    {GREEN} [1]  {BLUE} RSACTFTool
    {GREEN} [2]  {BLUE} FeatherDuster
    {GREEN} [3]  {BLUE} XORTool
    {GREEN} [4]  {BLUE} HashCat
    {GREEN} [5]  {BLUE} JohnTheRipper
    {GREEN} [6]  {BLUE} Cryptool
    {GREEN} [7]  {BLUE} An important link
    {GREEN} [99] {RED} Exit
    {WHITE}"""


WEB_MENU = f"""
    {GREEN} [0]  {GREEN} Back
    {GREEN} [1]  {BLUE} Burp Suite
    {GREEN} [2]  {BLUE} Wireshark
    {GREEN} [3]  {BLUE} sqlmap
    {GREEN} [4]  {BLUE} dsniff
    {GREEN} [5]  {BLUE} subbrute
    {GREEN} [6]  {BLUE} gobuster
    {GREEN} [7]  {BLUE} w3af
    {GREEN} [8]  {BLUE} AXSSer
    {GREEN} [99] {RED} Exit
    {WHITE}"""


OSINT_MENU = f"""
    {GREEN} [0]  {GREEN} Back
    {GREEN} [1]  {BLUE} Social Scan
    {GREEN} [2]  {BLUE} DataSploit
    {GREEN} [3]  {BLUE} ReconSpider
    {GREEN} [99] {RED} Exit
    {WHITE}"""



if __name__ == "__main__":

    for i in [BANNER, MENU, REVERSE_MENU, PWNING_MENU, FORENSIC_MENU, CRYPTO_MENU, WEB_MENU, OSINT_MENU]:
        print(i)

