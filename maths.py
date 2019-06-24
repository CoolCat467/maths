#!/usr/bin/env python3
# Maths Modual for Cat Inc Programs.
#
# All Thanks to Anivargi's Twin prime calculator at
# Scratch.mit.edu/projects/128640110/ for the program that finds out
# if it is prime or not.
#
# Copywrite Cat Inc, All rights reserved.
# Programmed by CoolCat467, member of Cat Inc.

import os, sys, time, math
global pyinstallered
global PRIMENUMBER
PRIMENUMBER = 2227501 # For Hashing
pyinstallered = False

def isPrime(num):
    # Anivargi's program that finds out if it is prime or not. See top
    isPrime = True
    if num < 3 or num == 3:
        isPrime = True
    else:
        divideNumber = 2
        while isPrime == True and divideNumber != math.ceil(math.sqrt(num + 1)):
            if num % divideNumber == 0:
                isPrime = False
            else:
                divideNumber = divideNumber + 1
    return isPrime

def timeCalc(totalsec):
    # Calculate Time
    # Min Calc
    if totalsec >= 60:
        totalmin = totalsec / 60
        if totalmin < 1:
            totalmin = 0
        else:
            totalmin = int(round(totalmin))
    else:
        totalmin = 0
        totalhr = 0
    # Hr Calc
    if totalmin >= 60:
        totalhr = totalmin / 60
        if totalhr < 0:
            totalhr = 0
        else:
            totalhr = int(round(totalhr))
    else:
        totalhr = 0
    # Update min value
    for i in range(totalhr):
        totalmin = totalmin - 60
    # Update sec value
    i = None
    for i in range(totalmin):
        totalsec = totalsec - 60
    return ('Total Time Running: %s hrs, %s mins, %s secs' % (totalhr, totalmin, totalsec))

def getnums(text):
    # make a string into a number string
    nums = ''
    for letter in text.upper():
        num = ord(letter) - 32
        if num < 10:
            num = '0' + str(num)
        nums = str(nums) + str(num)
    return int(nums)

def getext(nums):
    # make a number string into text
    control = 1
    prev = ''
    text = ''
    for number in str(nums):
        if bool(control):
            prev = str(number)
            control = 0
        else:
            if prev == 0:
                num = number
            else:
                num = prev + str(number)
            text = str(text)
            if num == '0':
                text = text + ' '
            else:
                text = text + chr(int(num) + 32)
            control = 1
    return text

def gethashed(text):
    # Take the entered text, hash it, and return it
    intstr = getnums(text)
    choose = 2
    data = ''
    intstr = int(intstr) * PRIMENUMBER
    for num in str(intstr):
        if choose % 2 != '0':
            data = str(data) + str(num)
        choose = choose + 1
    intstr = int(data) * PRIMENUMBER
    
    while len(str(intstr)) < 20:
        intstr = intstr * PRIMENUMBER
    if len(str(intstr)) > 20:
        choose = 0
        data = ''
        for i in str(intstr):
            choose = choose + 1
            if choose < 20:
                data = str(data) + str(i)
            else:
                data = int(data) * (int(i) + 1)
                #data = data
        intstr = int(data)
    return getext(intstr)

def hashfile(filename):
    data = []
    try:
        with open(filename, 'r') as readfile:
            for line in readfile:
                data.append(line)
            readfile.close()
    except FileNotFoundError:
        return 'Error'
    else:
        for i in range(len(data)):
            data.append(gethashed(str(data[0])))
            del data[0]
        data = str(''.join(data))
        data = str(gethashed(data))
        data = list(str(data))
        if ' ' in data or "'" in data or '"' in data:
            sel = 0
            for i in range(len(data) - 1):
                if data[sel] == ' ' or data[sel] == "'" or data[sel] == '"':
                    del data[sel]
                else:
                    sel += 1
        data = str(''.join(data))
        return data

def partquotes(text, witch, how = False):
    # Program that can retrieve sections of data that are within
    # single quotes. Helpfull for list -> str -> list
    try:
        ftimes = 0
        found = False
        for i in text:
            if not found:
                if i == "'":
                    found = True
                    ftimes = ftimes + 1
                    var = 'l' + str('i' * ftimes)
                    exec("%s = ''" % var)
                    to = "%s = %s + " % (var, var)
            else:
                if i != "'":
                    exec(str(to) + "'" + i + "'")
                else:
                    found = False
        var = 'l' + str('i' * int(witch))
        if not how:
            toreturn = eval(var)
        else:
            toreturn = ftimes
        return toreturn
    except SyntaxError:
        return 'Error'

def seperate(text):
    # Will seperate text by spaces.
    ftimes = 0
    scan = str(' ' + str(text))
    for i in scan:
        if str(i) == ' ':
            ftimes = ftimes + 1
            what = str('tmp' + str('i' * int(ftimes)))
            exec(str(what + " = ''"))
        else:
            what = str('tmp' + str('i' * int(ftimes)))
            tostore = str(eval(what) + str(i))
            exec(str(what + " = '" + tostore + "'"))
    tmp = []
    for i in range(ftimes):
        what = str('tmp' + str('i' * int(i + 1)))
        tmp.append(str(eval(what)))
    return list(tmp)

def encrypt(key, msg):
    encryped = []
    for i, c in enumerate(msg):
        key_c = ord(key[i % len(key)])
        msg_c = ord(c)
        encryped.append(chr((msg_c + key_c) % 127))
    return ''.join(encryped)

def decrypt(key, encryped):
    msg = []
    for i, c in enumerate(encryped):
        key_c = ord(key[i % len(key)])
        enc_c = ord(c)
        msg.append(chr((enc_c - key_c) % 127))
    return ''.join(msg)

def main():
    # Set some globals
    global SYSNAME
    global NODENAME
    global CURFOLD
    global runningMain
    SYSNAME = partquotes(str(os.uname()), 1)
    NODENAME = partquotes(str(os.uname()), 2)
    CURFOLD = partquotes(str(os.path.split(str(os.getcwd()))), 2)
    folder = partquotes(str(os.path.split(os.getcwd())), 2)
    
def terminate():
    sys.exit()
    exit()

# Activation Program
if __name__ == '__main__':
    startTime = time.time()
    print("Copywrite Cat Inc, All rights reserved.")
    print("Programmed by CoolCat467, member of Cat Inc.")
    main()
