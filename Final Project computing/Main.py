"""Main code/Menu
for final project"""

#import all ciphers and converters
#they were all made as classes to not confuse the encrypt methods with each other
#import * for classes
from A1Z26 import *
from Caesar import *
from Combined import *
from MorseCode import *
from OneTimePad import *
from Vigenere import *
from Binary import *
from Hex import *
from Octal import *

#create instances of each class
a1 = A1()
caesar = Caesar()
comb = Combined()
morse = Morse()
otp = OneTimePad()
vig = Vigenere()
binary = Binary()
hexa = Hexa()
octal = Octal()

#in order to avoid long if statements, functions/methods added to lists
encFunc = [vig.encrypt, otp.encrypt, caesar.encrypt, a1.encrypt,
           morse.encrypt, comb.encrypt]
decFunc = [vig.decrypt, otp.decrypt, caesar.decrypt, a1.decrypt,
           morse.decrypt, comb.decrypt]

#need encode and decode list and convert to and convert from lists
cvtFunc = [binary.encrypt, octal.encrypt, hexa.encrypt]
dcvtFunc = [binary.decrypt, octal.decrypt, hexa.decrypt]

###---main---###
def main():
    #while loop to ensure proper button pressed
    keepGoing = True
    while keepGoing:
        #response brings up menu function
        response = menu()

        #each button press brings up main function for encode/decode/convert to/convert from
        if response == "1":
            encodeMain()
        elif response == "2":
            decodeMain()
        elif response == "3":
            convertToMain()
        elif response == "4":
            convertFromMain()
        #if 0 pressed, program exits
        elif response == "0":
            print ("""
Fly, you fool!""")
            keepGoing = False
        #if invalid button pressed, tell user to re-enter number    
        else:
            print("""
Dude, just type a number 0 - 4...it shouldn't be that hard.

""")
            

###---menu function---###
def menu():
    #print out the menu
    print("""

CIPHER MENU

0) Exit
1) Encrypt
2) Decode
3) Convert to Binary/Octal/Hex
4) Convert from Binary/Octal/Hex

""")

    #create input variable, and return it
    choice = input("""What would you like to do? Please enter a number:

""")

    return (choice)


###---encode menu function---###
def encodeMenu():
    #similar to menu function, print out cipher choice menu
    print("""

Please choose the cipher you'd like to encrypt with:

0) Vigenere Cipher
1) One Time Pad
2) Caesar Cipher
3) A1Z26 Cipher
4) Morse Code
5) Combined Cipher
6) Go Back

""")

    #create input variable, and return it
    choice = input("""What would you like to do? Please enter a number:

""")
    
    return (choice)


###---encode main---###
def encodeMain():
    keepGoing = True
    #while loop to ensure valid button press
    while keepGoing ==True:
        #response = encodeMenu() called function
        response = encodeMenu()

        #if response is 6, go back to main Menu
        if response == "6":
            keepGoing = False
        #if response is 0 through 5, call function from encFunc[response]
        #when that is done, go back to main menu
        elif 0 <= int(response) <=5:
            encFunc[int(response)]()
            keepGoing = False
        #if invalid key is entered, make them re-enter response
        else:
            print ("""
I have no idea what you wanted to do...
Please try again and enter a number:
""")


###---decode menu---###
def decodeMenu():
    #print out menu
    print("""

Please choose the cipher you'd like to decrypt with:

0) Vigenere Cipher
1) One Time Pad
2) Caesar Cipher
3) A1Z26 Cipher
4) Morse Code
5) Combined Cipher
6) Go Back

""")

    #input choice and return it
    choice = input("""What would you like to do? Please enter a number:

""")
    
    return (choice)


###---decode main---###    
def decodeMain():
    keepGoing = True
    #same while loop as encode main, but use decFunc list instead
    while keepGoing ==True:
        response = decodeMenu()

        if response == "6":
            keepGoing = False
        elif 0 <= int(response) <=5:
            decFunc[int(response)]()
            keepGoing = False
        else:
            print ("""
I have no idea what you wanted to do...
Please try again and enter a number:
""")


###---convert to menu---###
def convertToMenu():
    #print menu choices
    print ("""

Please choose what to convert to:

0) Binary
1) Octal
2) Hex
3) Go Back

""")

    #input choice and return it
    choice = input("""What would you like to do? Please enter a number:

""")

    return (choice)


###---convert to main---###
def convertToMain():
    keepGoing = True
    #while loop similar to other mains
    while keepGoing == True:
        #response brings up converttomenu
        response = convertToMenu()

        #if 3, goes back to main
        if response == "3":
            keepGoing = False
        #if response between 0 and 2, call cvtFunc[index] function, then back to main
        elif 0 <= int(response) <=2:
            cvtFunc[int(response)]()
            keepGoing = False
        #if response invalid, re-enter response
        else:
            print ("""
I have no idea what you wanted to do...
Please try again and enter a number:
""")


###---convert from menu---###            
def convertFromMenu():
    #print conversion menu
    print ("""

Please choose what to convert from:

0) Binary
1) Octal
2) Hex
3) Go Back

""")

    #input choice and return it
    choice = input("""What would you like to do? Please enter a number:

""")

    return (choice)


###---convert from main---###
def convertFromMain():
    keepGoing = True
    #same loop as convert to menu, but uses dcvtFunc[response]
    while keepGoing == True:
        response = convertFromMenu()

        if response == "3":
            keepGoing = False
        elif 0 <= int(response) <=2:
            dcvtFunc[int(response)]()
            keepGoing = False
        else:
            print ("""
I have no idea what you wanted to do...
Please try again and enter a number:
""")



#call main if name = main
if __name__ == "__main__":
    #print basic instructions and intro
    print("""
Hello! Ready to have fun with encryption and converting messages with different
ciphers?  Or maybe you would like to convert messages to binary, octal, or hex
(which are basically ciphers to anyone who doesn't know them...)?

Well, I can help! Just follow the prompts on the screen.  Menu selections can be
made by just typing in the number of what you'd like to do!  After encrypting,
decrypting, or converting, the program will show the outcome and bring you back
to the main menu.  Here you can choose to do something else or exit.

Start with encrypting a message.  If you already have an encrypted message, and
know the cipher, you can then choose decrypt! Have fun!
Keep it secret, Keep it safe!""")
    #then run main
    main()

