"""One Time Pad
for final project"""

"""The One Time Pad, if used correctly, is said to be impossible to break.
A message is matched with a key. The key must be the same number of characters
as the plainText.  The key is usually randomly generated. Also, the key must
only be used one time, then never used again. Other than that, it is basically
a Vigenere cipher with modular addition or subtraction."""

#import random module for key
import random

#create OTP class
class OneTimePad(object):
    def __init__(self):
        object.__init__(self)

        #create private variable for alpha
        self.__alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


    ###---encrypt method---###
    def encrypt(self):
        #set up similar to Vigenere, blank var for cipher, keyIndex = 0
        cipherText = ""
        keyInd = 0
        
        encode = input("""
Please enter the message you would like to encrypt.
Don't include any punctuation:

""")
        #key created randomly. use SystemRandom for true randomness, see Python random documentation
        #key only created with letters from alpha
        #take random choice from alpha for # of char in encode - spaces
        key = "".join(random.SystemRandom().choice(self.__alpha) for i in range(
            len(encode) - encode.count(" ")))

        #exact same encryption as Vigenere
        #for documentation on how code was created, see Vigenere.py
        for char in encode:
            if char.upper() in self.__alpha:
                ordinal = self.__alpha.find(char.upper())
                ordinal += self.__alpha.find(key[keyInd])
                ordinal %= len(self.__alpha)

                #matches case of characters
                if char.isupper():
                    cipherText += self.__alpha[ordinal]
                elif char.islower():
                    cipherText += self.__alpha[ordinal].lower()

                keyInd += 1

            else:
                pass

        #print randomly generated key
        print("""
Your randomly generated key is:

{}""".format(key))

        #print encoded message
        print("""
Your encoded message is:

{}""".format(cipherText))


    ###---decrypt method---###
    def decrypt(self):
        #similar decode to Vigenere, again see Vigenere.py for documentation
        plainText = ""
        keyInd = 0
        keepGoing = True
        
        decode = input("""
Please enter your message to be decoded:

""")

        key = input("""
Next, Please enter your key:

""")

        #check to see if key is valid
        while keepGoing == True:
            if key.isalpha():

                if len(key)!=(len(decode) - decode.count(" ")):
                    key = input("""
The key must be the number of characters as your message.
Please try re-entering your key:

""")
                else:
                    keepGoing = False
                    key = key.upper()

            else:
                key = input("""
Key must contain only letters and no spaces.
Please try re-entering your key:

""")

        #decrypt vigenere for loop
        for char in decode:
            if char.upper() in self.__alpha:
                ordinal = self.__alpha.find(char.upper())
                ordinal -= self.__alpha.find(key[keyInd])

                ordinal %= len(self.__alpha)

                if char.isupper():
                    plainText += self.__alpha[ordinal]
                elif char.islower():
                    plainText += self.__alpha[ordinal].lower()

                keyInd +=1

            else:
                pass

        #print decoded message
        print("""
Your decoded message is:

{}""".format(plainText))



###---testing main---###

def main():
    c = OneTimePad()
    c.encrypt()
    c.decrypt()

if __name__ == "__main__":
    main()
