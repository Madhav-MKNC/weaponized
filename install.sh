#!/bin/bash
clear

BLACK='\e[30m'
RED='\e[31m'
GREEN='\e[32m'
YELLOW='\e[33m'
BLUE='\e[34m'
PURPLE='\e[35m'
CYAN='\e[36m'
WHITE='\e[37m'
NC='\e[0m'

echo -e "${CYAN} "
echo ""

echo "██╗    ██╗███████╗ █████╗ ██████╗  ██████╗ ███╗   ██╗    ██╗  ██╗███████╗██╗  ██╗";
echo "██║    ██║██╔════╝██╔══██╗██╔══██╗██╔═══██╗████╗  ██║    ██║  ██║██╔════╝╚██╗██╔╝";
echo "██║ █╗ ██║█████╗  ███████║██████╔╝██║   ██║██╔██╗ ██║    ███████║█████╗   ╚███╔╝ ";
echo "██║███╗██║██╔══╝  ██╔══██║██╔═══╝ ██║   ██║██║╚██╗██║    ██╔══██║██╔══╝   ██╔██╗ ";
echo "╚███╔███╔╝███████╗██║  ██║██║     ╚██████╔╝██║ ╚████║    ██║  ██║███████╗██╔╝ ██╗";
echo " ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝╚═╝      ╚═════╝ ╚═╝  ╚═══╝    ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝";
echo ""                     
echo -e "${CYAN}    【This】 【Tool】 【is】【Created】 【By】 【CybSec NITW】 ";
echo ""
echo -e "${YELLOW}                       Github.com/CybSec-NITW ${NC}"
echo ""
echo -e "${CYAN}                  [+]${GREEN} This Tool Must Run As ROOT ${CYAN}[+]${NC}"
echo ""
echo -e "${GREEN}    [>] Press ${PURPLE}ENTER${GREEN} to Install WeaponHEX, ${PURPLE}CTRL+C${GREEN} to Abort.${NC}"
read INPUT
echo ""

if [ "$PREFIX" = "/data/data/com.termux/files/usr" ]; then
    INSTALL_DIR="$PREFIX/usr/share/doc/WeaponHEX"
    BIN_DIR="$PREFIX/usr/bin/"
    pkg install -y git python3
else
    INSTALL_DIR="/usr/share/doc/WeaponHEX"
    BIN_DIR="/usr/bin/"
fi

echo "[✔] Checking directories...";
if [ -d "$INSTALL_DIR" ]; then
    echo "[!] A Directory WeaponHEX Was Found.. Do You Want To Replace It ? [y/n]:" ;
    read mama
    if [ "$mama" = "y" ]; then
        rm -R "$INSTALL_DIR"
    else
        exit
    fi
fi

echo "[✔] Installing ...";
echo "";
git clone https://github.com/CybSec-NITW/WeaponHEX.git "$INSTALL_DIR";
echo "#!/bin/bash
python3 $INSTALL_DIR/weaponhex.py" '${1+"$@"}' > weaponhex;
chmod +x weaponhex;
sudo cp weaponhex /usr/bin/;
rm weaponhex;


if [ -d "$INSTALL_DIR" ] ;
then
    echo "";
    echo "[✔][✔]========================================================================$[✔]";
    echo "$[✔][✔] Successfuly Installed !!! [✔]";
    echo "";

 
    echo "[✔][✔]========================================================================$[✔]";
    echo "$[✔][✔] ✔✔✔ All Is Done!! you can execute tool by typing weaponhex !! ✔✔✔ $[✔]";
    echo "[✔][✔]========================================================================[✔]";
    echo "";
else
    echo "[✘] Installation Failed !!! [✘]";
    exit
fi
