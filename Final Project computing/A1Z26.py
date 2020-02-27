"""A1Z26 Cipher
for final project"""

"""This cipher replaces each letter with numbers.  Again, simple substitution,
but numbers must be separated somehow. """

#create A1Z26 class
class A1(object):
    def __init__(self):
        object.__init__(self)

        #make private variable for alpha including space
        self.__alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "


    ###---encrypt method---###
    def encrypt(self):
        #create empty string variable for cipher message
        cipherText = ""

        encode = input("""
Please enter message to be encoded:

""")

        #run through each character in encode variable
        #if that char is in alpha, find the index of it in the string
        #add that index number to ciphertext, and seperator '-'
        for char in encode:
            if char.upper() in self.__alpha:
                ordinal = self.__alpha.find(char.upper())
                cipherText += str(ordinal) + "-"

            #if char not in alpha, leave it out
            else:
                pass

        #cipherText needs to have last - removed because decoder won't work with it on
        cipherText = cipherText[:-1]

        #print encoded message
        print("""
Your encoded message is:

{}""".format(cipherText))


    ###---decrypt method---###
    def decrypt(self):
        #same empty plainText string
        plainText = ""

        decode = input("""
Please enter message to be decoded
(enter dashes between numbers, numbers start at 0):

""")

        #for each number between dashes...(must split decode variable by dashes)
        #change each number to int, if that number is between 0 and 26...
        #add alpha[number]
        for num in decode.split("-"):
            n = int(num)
            if 0 <= n <= 26:
                plainText += self.__alpha[n]

            else:
                pass

        #print decoded message
        print("""
Your decoded message is:

{}""".format(plainText))

        
            
###---testing main---###
def main():
    c = A1()
    c.encrypt()
    c.decrypt()

if __name__ == "__main__":
    main()
