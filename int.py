#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

def decToBinary(num):
    try:
        return bin(int(num)).replace("0b", "")
    except ValueError:
        return "\nError: Invalid decimal number\n" 

def decToHex(num):
    try:
        return "0x" + hex(int(num)).split('x')[-1]
    except ValueError:
        print("\nError: Invalid decimal number\n")
        exit()

def binToDecimal(num):
    try:
        return int(num, 2)
    except ValueError:
        print("\nError: Invalid binary number\n")
        exit()

def binToHex(num):
    try:
        return hex(int(num, 2))
    except ValueError:
        print("\nError: Invalid binary number\n")
        exit()

def hexToDec(num):
    try:
        return int(num, 16)
    except ValueError:
        print("\nError: Invalid hex number\n")
        exit()

def hexToBin(num):
    try:
        return bin(int(num, 16))[2:]
    except ValueError:
        print("\nError: Invalid binary number\n")
        exit()
    
def main():
    print('''
 _____       _____  _____  
   |   |\  |   |    |____| \  /
 __|__ |  \|   |  . |       \/
                            /
Implicit Number Transcoder
________________________________________
    ''')
    helpText = "\nError: Please enter a number and what to convert it to\n"
    if len(sys.argv) < 3:
        print(helpText)
    else:
        convert = sys.argv[1]
        number = sys.argv[2]
        if convert == "-db":
            print(str(decToBinary(number)) + "\n")
        elif convert == "-dh":
            print(str(decToHex(number)) + "\n")
        elif convert == "-bd":
            print(str(binToDecimal(number)) + "\n")
        elif convert == "-bh":
            print(str(binToHex(number)) + "\n")
        elif convert == "-hd":
            print(str(hexToDec(number)) + "\n")
        elif convert == "-hb":
            print(str(hexToBin(number)) + "\n")
        else:
            print("\nError: Conversion not supported\n")

if __name__ == "__main__":
    main()
