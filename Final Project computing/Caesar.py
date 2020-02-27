""" Caesar Cipher
for Final Project"""

"""Caesar Cipher is a basic substitution cipher
involving a shifting of letters x amount.  Ex: a = l, b = m, c = n, etc.
This will be shifted 10"""

#create caesar cipher class, initialize self and object
class Caesar(object):
    def __init__(self):
        object.__init__(self)

        #key/shift will stay same for encoding and decoding; as well as alphabet
        #create variables that are private for both
        self.__alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.__key = 10


###---encrypt method---###
    def encrypt(self):
        #create blank string variable that the for loop adds cipher letters to
        cipherText = ""

        #enter message to be encrypted
        encode = input("""
Please enter the message you would like to encrypt:

""")

        #go through each letter in message 
        for char in encode:
            #if the upper case char is in alpha, find the index
            if char.upper() in self.__alpha:
                ordinal = self.__alpha.find(char.upper())
                #add the key # to the char's index to get a new index
                ordinal += self.__key

                #in case the new index goes over 26 (index 0 - 25), mod ordinal variable
                #by the length of alpha, this way the number stays within bounds
                ordinal %= len(self.__alpha)

                #add alpha letter at [ordinal] to end cipherText string
                if char.isupper():
                    cipherText += self.__alpha[ordinal]
                elif char.islower():
                    cipherText += self.__alpha[ordinal].lower()

            #if char is not in alpha, skip it
            else:
                pass

        #print cipherText
        print("""
Your encoded message is:

{}""".format(cipherText))


###---decrypt method---###
    def decrypt(self):
        #will be similar to encrypt
        plainText = ""
        decode = input("""
Please enter the message you would like decoded:

""")

        #difference is that the ordinal variable (new index) will be:
        #the char index MINUS the key (to shift back)
        for char in decode:
            if char.upper() in self.__alpha:
                ordinal = self.__alpha.find(char.upper())
                ordinal -= self.__key

                ordinal %= len(self.__alpha)

                if char.isupper():
                    plainText += self.__alpha[ordinal]
                elif char.islower():
                    plainText += self.__alpha[ordinal].lower()

            else:
                pass

        print("""
Your decoded message is:

{}""".format(plainText))


###---testing---###

def main():
    c = Caesar()
    c.encrypt()
    c.decrypt()

if __name__ == "__main__":
    main()

