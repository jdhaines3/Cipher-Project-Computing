""" Vigenere Cipher
    for final project"""

"""Vigenere Cipher consists of a series of Caesar shifts, based on index of both
letter in message, and index of letter from key.  This shifting allows duplicate
letters to be encoded as different letters, making the cipher harder to crack"""

#make Vigenere class to import into main
#initialize self and object
class Vigenere(object):
    def __init__(self):
        object.__init__(self)

        #create alphabet variable--make private so it can't be changed by user
        self.__alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


###---encrypt method---###
    def encrypt(self):
        #define cipherText and empty string, will be adding letters through for loop
        cipherText = ""
        keepGoing = True
            
        #ask user to enter message to be encrypted, store in variable
        encode = input("""
Please enter the message you would like to encrypt.
Don't include punctuation:

""")
        #input key 
        key = input("""
Now please create and enter your key.
Key length must be less characters than your message, not including spaces,
and only have letters in it:

""")
        #make sure key is valid
        while keepGoing == True:
            #key can only be alphabetical with no spaces
            if key.isalpha():

                #make sure letters in key is less than or equal to # of letters in message
                #message must have spaces removed from len count        
                if len(key)>(len(encode) - encode.count(" ")):

                    key = input("""
Key must have less characters than your message.
Please enter new key:

""")
            
                else:
                    #once key < message, set key to uppercase
                    #define key letter Index
                    keepGoing = False
                    keyInd = 0
                    key = key.upper()

            else:
                key = input("""
Key must contain only letters and no spaces.
Please enter new key:

""")
                
        #for loop for encoding: go through each character in encode
        for char in encode:
            #if uppercase character is in alpha, find the char's index in alpha
            if char.upper() in self.__alpha:
                ordinal = self.__alpha.find(char.upper())
                #then add the index of key letter to index of char in alpha
                ordinal += self.__alpha.find(key[keyInd])
                #ordinal variable must be between 1 and 26 (or 0 and 25)
                #so if outside bounds, mod ordinal by letters in alpha
                ordinal %= len(self.__alpha)

                #add letter in alpha with index of ordinal variable
                if char.isupper():
                    cipherText += self.__alpha[ordinal]
                elif char.islower():
                    cipherText += self.__alpha[ordinal].lower()

                #go to next letter of key
                #key must repeat until len key repeated = len encode
                keyInd += 1
                #so if the key letter index = total length of key, set to 0 to repeat
                if keyInd == len(key):
                    keyInd = 0

            #if character isn't in alpha, skip it
            else:
                pass

        #print cipherText
        print ("""
Your encoded message is:

{}""".format(cipherText))


###---Decrypt method---###
    def decrypt(self):
        keepGoing = True
        plainText = ""

        decode = input("""Please enter the message you would like to decrypt:

""")

        #same key validation as encryption
        key = input("""
Now please enter your key:

""")

        while keepGoing == True:
            if key.isalpha():

                if len(key)>(len(decode) - decode.count(" ")):

                    key = input("""
Key must have less characters than your message.
Please enter new key:

""")
                else:
                    keepGoing = False
                    keyInd = 0
                    key = key.upper()

            else:
                key = input("""
Key must contain only letters and no spaces.
Please enter new key:

""")

        #same for loop as encryption;
        #except instead of adding key index to ordinal, the program subtracts
        for char in decode:
            if char.upper() in self.__alpha:
                ordinal = self.__alpha.find(char.upper())
                ordinal -= self.__alpha.find(key[keyInd])

                ordinal %= len(self.__alpha)

                if char.isupper():
                    plainText += self.__alpha[ordinal]
                elif char.islower():
                    plainText += self.__alpha[ordinal].lower()

                keyInd += 1
                if keyInd == len(key):
                    keyInd = 0

            else:
                pass

        print ("""
Your decoded message is:

{}""".format(plainText))
        


##--testing--###

def main():
    c = Vigenere()
    c.encrypt()
    c.decrypt()

    
if __name__ == "__main__":
    main()
        

        
        
        
    

    
