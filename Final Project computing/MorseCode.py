""" Morse Code
for Final Project"""

"""The simple code of dashes and dots represents letters.  While this cipher is
basic substitution, the program must output spaces between letters,
while the user must be reminded to insert spaces between letters when decrypting.
Else, there is no way to distinguish when the dots should end.  A symbol will be used
to separate words as well."""

#create Morse code class
class Morse(object):
    def __init__(self):
        object.__init__(self)

        #create private variables for alpha and morse
        #morse variable will be list, alpha just a string
        #spaces will be equal to / in morse
        self.__alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
        self.__morse = [".-", "-...", "-.-.","-..", ".", "..-.", "--.",
                        "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
                        ".--.", "--.-", ".-.", "...", "-", "..-", "...-",
                        ".--", "-..-", "-.--", "--..", "/"]


    ###---encrypt method---###    
    def encrypt(self):
        #empty cipherText variable to add to
        cipherText = ""

        encode = input("""
Please enter message to be encoded:

""")

        #for each char in message, if that char is in __alpha,
        #find the index of the char in alpha, then add __morse[index] + space to cipherText
        for char in encode:
            if char.upper() in self.__alpha:
                ordinal = self.__alpha.find(char.upper())
                cipherText += self.__morse[ordinal] + " "

            #if char not in alpha, skip it
            else:
                pass

        #print final cipherText
        print("""
Your encoded message is:

{}""".format(cipherText))


    ###---decrypt method---###
    def decrypt(self):
        plainText = ""
        
        decode = input("""
Please enter message to be decoded,
(use space between letters and '/' between words):

""")

        #split message by spaces, each item between spaces, if it is in __morse,
        #find the index, and add the char with the same index from alpha
        for item in decode.split(' '):
            if item in self.__morse:
                ordinal = self.__morse.index(item)
                plainText += self.__alpha[ordinal]

            #if it's not in __morse, skip it
            else:
                pass

        print("""
Your decoded message is:

{}""".format(plainText))


###---testing main---###        
def main():
    c = Morse()
    c.encrypt()
    c.decrypt()

if __name__ == "__main__":
    main()
