# Maths Module

This module is not very useful, but it was a part of my start to programming in python.

The Maths Module is a Python Module that contains several functions, a lot of them doing with math or related things.
The Maths Module also contains several helpfull functions commonly used in Cat-Ink's Programs.

## Version information:
Version 0.0.1:
Initial release

Version 0.0.2:
Magor bug fixes

Version 0.0.3:
Bug fix for Windows because os.uname does not exist on windows for some reson

## Usage:
### setPrime
Sets the prime number used for hashing
'''maths.setPrime(number)'''

### getnums
GetNums makes text strings into  number-strings
'''maths.getnums(str)'''

### getext(nums)
GetText makes number-strings back into a text strings
'''maths.getext(numstring)'''
Note: it is advised not to do int() on the number.

### partquotes
PartQuotes is a powerfull program that can find single-quote-enclosed text, and then returns the part you choose.
text is whatever wou want searched
witch is whatever set of quotes you want
how is default False.
how = False: Returns the quoted text you choose (normal opperation)
how = True:  Returns how many quoted text segments there are
'''maths.partquotes(text, witch, how = False)'''

### seperate
Seperate seperates text by space charecters
'''maths.seperate(text)'''

### mkplain
MkPlain makes word into super plain text and strips numbers
'''mkplain(word)'''

### timeCalc
TimeCalc Calculates Time and returns a tuple of (days, hours, minutes, secconds)
'''timeCalc(totalsecs)'''

### gethashed
GetHashed Takes the entered text, hashes it, and returns the hash
'''maths.gethashed(text)'''

### hashfile
HashFile hashes files. Boom.
'''maths.gethashed(filename)'''

### encrypt
Encrypt encrypts text with a given key.
'''maths.encrypt(key, msg)'''

### decrypt
Decrypts decrypts text with a given key.
'''maths.decrypt(key, encryped)'''

### RadixText
RadixText Sorts text with the RadixLSD Module
'''maths.RadixText(data):'''

### seplist
SepList makes lists into text, seperated by given values
'''maths.seplist(readlist, sepby)'''

### strlist
StrList makes str()-ed lists back into true lists
'''maths.strlist(stredlist)'''

### sysinfo
SysInfo returns a tuple of the System Name, Device Name, and the Current Folder the program is in)
'''maths.sysinfo()'''

### findwhole
FindWhole returns whatever whole number the given percent and part of whole came from
'''maths.findwhole(percent, part)'''

### findpercent
FindPercent returns whatever the percentage the given part of whole of whole are
'''maths.findpercent(part, whole)'''

### findpart
FindPart returns whatever part of the given percent of the whole number is
'''maths.findpart(percent, whole)'''
