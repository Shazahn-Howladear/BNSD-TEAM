
# Decompiled by HTR-TECH | SHAZAHN
# Github : https://github.com/shazahn-howladear
#---------------------------------------
# Auto Dis Parser 2.2.0
# Source File : patched.pyc
# Bytecode Version : 2.7
# Time : Mon Feb  1 07:55:44 2021
#---------------------------------------
# -*- coding: utf-8 -*-
try:
    import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass,mechanize,requests,bhotnine
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
    from mechanize import Browser
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    os.system("pip2 install bhotnine")
    time.sleep(1)
    os.system('python2 .main.py')
reload(sys)
sys.setdefaultencoding('utf8')
os.system("clear")


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)
		
		

##### LOGO #####
logo="""
\033[1;96m ------------------------
 \033[1;32m < OFFICIAL CODER MEHEDI >
 \033[1;96m ------------------------ 
    
██████╗░███╗░░██╗░██████╗██████╗░
██╔══██╗████╗░██║██╔════╝██╔══██╗
██████╦╝██╔██╗██║╚█████╗░██║░░██║
██╔══██╗██║╚████║░╚═══██╗██║░░██║
██████╦╝██║░╚███║██████╔╝██████╔╝
╚═════╝░╚═╝░░╚══╝╚═════╝░╚═════╝░

████████╗███████╗░█████╗░███╗░░░███╗
╚══██╔══╝██╔════╝██╔══██╗████╗░████║
░░░██║░░░█████╗░░███████║██╔████╔██║
░░░██║░░░██╔══╝░░██╔══██║██║╚██╔╝██║
░░░██║░░░███████╗██║░░██║██║░╚═╝░██║
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝                                       
\033[1;93m        IT'S NOT JUST A NAME, IT'S A BRAND
\033[1;97m--------------------------------------------------
\033[1;95m
 AUTHOR     : SHAZAHN HOWLADEAR
 FACEBOOK   : FACEBOOK.COM/SHAZAHN HOWLADEAR
 YOUTUBE    : YOUTUBE.COM/SHAZAHN HOWLADEAR
 GITHUB     : GITHUB.COM/SHAZAHN-HOWLADEAR
\033[1;32m
--------------------------------------------------
                                """

cusr = "shazahm"
cpwd = "shazahn"
def u():
    os.system("clear")
    print(logo)
    print "\033[1;97mSECOND STEP OF LOGIN"
    print "\033[1;97m--------------------"
    print "\033[1;97m "
    usr=raw_input("          \033[1;94mTOOL USERNAME : ")
    if usr == cusr:
        p()
    else:
        os.system("clear")
        print(logo)
        print "\033[1;97mSECOND STEP OF LOGIN"
        print "\033[1;97m--------------------"
        print "\033[1;97m "
        print("          \033[1;94mTOOL USERNAME : "+usr+" (wrong)")
        time.sleep(1)
        os.system('xdg-open https://youtube.com/channel/UC3WcGIpTdNldsXAYWED7BuQ')
        u()
def p():
    os.system("clear")
    print(logo)
    print "\033[1;97mSECOND STEP OF LOGIN"
    print "\033[1;97m--------------------"
    print "\033[1;97m "
    print("          \033[1;94mTOOL USERNAME : MASTER TRICK (correct)")
    pwd=raw_input("          \033[1;93mTOOL PASSWORD : ")
    if pwd == cpwd:
        z()
    else:
        os.system("clear")
        print(logo)
        print "\033[1;97mSECOND STEP OF LOGIN"
        print "\033[1;97m--------------------"
        print "\033[1;97m "
        print("          \033[1;94mTOOL USERNAME : GAME OVER (correct)")
        print("          \033[1;93mTOOL PASSWORD : "+pwd+" (wrong)")
        time.sleep(1)
        os.system('xdg-open https://youtube.com/channel/UC3WcGIpTdNldsXAYWED7BuQ')
        p()
    
def z():
    os.system("clear")  
    print(logo)
    print "\033[1;97mSECOND STEP OF LOGIN"
    print "\033[1;97m--------------------"
    print "\033[1;97m "
    print("          \033[1;94mTOOL USERNAME : MASTER TRICK (correct)")
    print("          \033[1;93mTOOL PASSWORD : SUBSCRIBE NOW (correct)")
    print(" \033[1;92mLogin Successfull\033[0m")
    jalan("\033[1;93mPlease Wait 5 Minutes, All Packages Are Checking.....")
  
    time.sleep(1)
    os.system("python2 .README.md")
if __name__=="__main__":
    u()
