print("Setup and activation of Termux-Lock")

import os,sys
import os
import sys
import time
import datetime
import random
import compileall
os.chdir('/data/data/com.termux/files/usr/etc')

opr = open('bash.bashrc','a')
opr.write("\nalias txl='python /data/data/com.termux/files/home -l'\n")
opr.write('txl\n')
opr.close()

##############################################################
c = ['\033[1;30m','\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m','\033[1;37m']
##############################################################

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(00000.02)
##############################################################




logo = """
\033[1;34m      __  __ _   _   _   _    _    ____ _  __
\033[1;34m     |  \/  | | | | | | | |  / \  / ___| |/ /
\033[1;37m     | |\/| | |_| | | |_| | / _ \| |   | ' /
\033[1;37m     | |  | |  _  | |  _  |/ ___ \ |___| . \

\033[1;33m     |_|  |_|_| |_| |_| |_/_/   \_\____|_|\_\

"""
##############################################################
print(logo)
time.sleep(0.9)
##############################################################


os.system('pkg update -y')
os.system('pkg upgrade -y')
os.system('pkg install python -y')
os.system('pkg install python2 -y')
os.system('pkg install python2-dev -y')
os.system('pkg install python3')
os.system('pkg install ruby -y')
os.system('pkg install git -y')
os.system('pkg install php -y')
os.system('pkg install perl -y')
os.system('pkg install nmap -y')
os.system('pkg install clang -y')
os.system('pkg install nano -y')
os.system('pkg install hydra -y')
os.system('pkg install figlet -y')
os.system('pkg install curl -y')
os.system('pkg install unzip -y')
os.system('pkg install tor -y')
os.system('pkg install wget-y')
os.system('pkg install unrar -y')
os.system('pkg install toilet -y')
os.system('pkg install proot -y')
os.system('pkg install net-tools -y')
os.system('pkg install golang -y')
os.system('termux-chroot')
os.system('pkg install openssl -y')
os.system('pkg install cmatrix -y')
os.system('pkg install openssh -y')
os.system('apt update && apt upgrade -y') 



