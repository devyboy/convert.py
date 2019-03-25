#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

def decToBinary(num):
    try:
        return bin(int(num)).replace("0b", "")
    except ValueError:
        return "Invalid decimal number\n" 

def decToHex(num):
    try:
        return "0x" + hex(int(num)).split('x')[-1]
    except ValueError:
        print("Invalid decimal number\n")
        exit()

def binToDecimal(num):
    try:
        return int(num, 2)
    except ValueError:
        print("Invalid binary number\n")
        exit()

def binToHex(num):
    try:
        return hex(int(num, 2))
    except ValueError:
        print("Invalid binary number\n")
        exit()

def hexToDec(num):
    try:
        return int(num, 16)
    except ValueError:
        print("Invalid hex number\n")
        exit()

def hexToBin(num):
    try:
        return bin(int(num, 16))[2:]
    except ValueError:
        print("Invalid binary number\n")
        exit()
    
def main():
    helpText = "Please enter a number and what to convert it to\n"
    if len(sys.argv) < 3:
        print(helpText)
    else:
        convert = sys.argv[1]
        number = sys.argv[2]
        if convert == "-db":
            print(decToBinary(number) + "\n")
        elif convert == "-dh":
            print(decToHex(number) + "\n")
        elif convert == "-bd":
            print(binToDecimal(number) + "\n")
        elif convert == "-bh":
            print(binToHex(number) + "\n")
        elif convert == "-hd":
            print(hexToDec(number) + "\n")
        elif convert == "-hb":
            print(hexToBin(number) + "\n")
        else:
            print("Conversion not supported\n")

if __name__ == "__main__":
    main()