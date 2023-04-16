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

    {GREEN} [01] {BLUE}Reverse Engineering 
    {GREEN} [02] {BLUE}Pwning 
    {GREEN} [03] {BLUE}Forensics 
    {GREEN} [04] {BLUE}Cryptography 
    {GREEN} [05] {BLUE}Web Exploitation 
    {GREEN} [06] {BLUE}OSINT 
    {GREEN} [99] {BLUE}Exit
    {WHITE}"""




if __name__ == "__main__":

    print(BANNER)
    print(MENU)

