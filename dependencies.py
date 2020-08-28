#!usr/bin/env/python

import os
import time

Y = set(['yes', 'y', 'YES', 'Y'])
N = set(['no', 'n', 'NO', 'N'])

os.system("apt install figlet")
os.system("figlet AGREEMENT")
agree = input("this tool needs some dependenecies are you sure you want to install it Y / N ")

def agreement():
  if agree in Y:
    os.system("figlet INSTALLING")
    time.sleep(0.5)
    os.system("apt update")
    os.system("apt install git python python2 -y")
    os.system("git clone https://github.com/htr-tech/pakcrack.git")
    os.system("cd pakcrack")
    os.system("python2 crack.py")
  elif agree in N:
    os.system("figlet SORRY")
    print("this tool needs some dependenecies run dependencies.py")
    print("EXITING....")
    exit()
agreement()
