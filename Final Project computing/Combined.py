"""Combined Cipher
for final project"""

"""This 'cipher' runs the message through a series of multiple ciphers instead
of just one.  This can help create more secure messages due to the need to know
what ciphers are used as well as the specific order.  For this combined cipher,
we will first run the message through Vigenere, followed by an Atbash encryption
of the result (a = z, b = y, etc), followed by converting to A1Z26."""


#create Combined class
class Combined(object):
    def __init__(self):
        object.__init__(self)

        #need private alphabet and reverse alphabet variables
        #reverse is for atbash
        self.__alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.__reverse = "ZYXWVUTSRQPONMLKJIHGFEDCBA"


    ###---encrypt method---###
    def encrypt(self):
        #need variables for each cipher step and keepGoing for the while loop
        vigText = ""
        atbText = ""
        cipherText = ""

        keepGoing = True
        
        encode = input("""
Please enter the message you would like to encrypt:
Don't include punctuation.

""")

        #key input for Vigenere, key must be less than or equal to
        #length of message - spaces
        key = input("""
Now please create and enter your key,
Key must have less characters than your message, not including
spaces, and be only letters:

""")

        #while loop to create key, only way to exit loop is to create valid key
        while keepGoing == True:
            #if key is alphabetical, and if the character length is correct
            #then keepGoing = False, key turns into uppercase, index variable set to 0
            if key.isalpha():

                if len(key)>(len(encode) - encode.count(" ")):

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

        #run Vigenere and output to vigText variable
        #for documentation on Vigenere, see Vigenere.py
        for char in encode:
            if char.upper() in self.__alpha:
                ordinal = self.__alpha.find(char.upper())
                ordinal += self.__alpha.find(key[keyInd])

                ordinal %= len(self.__alpha)

                vigText += self.__alpha[ordinal]

                keyInd += 1
                if keyInd == len(key):
                    keyInd = 0

            else:
                pass

        #now do atbash cipher on vigenere output
        #for each character in vigText, find the index of the char in alpha
        #then use that index to find char in reverse and add to atbText
        for char in vigText:
            if char in self.__alpha:
                
                index = self.__alpha.find(char.upper())
                
                atbText += self.__reverse[index]

            else:
                pass


        #now run A1Z26 cipher on Atbash output
        #for A1Z26 documentation, see A1Z26.py
        for char in atbText:
            if char in self.__alpha:
                ordinal = self.__alpha.find(char.upper())
                cipherText += str(ordinal) + "-"

            else:
                pass

        cipherText = cipherText[:-1]

        print("""
Your encoded message is:

{}""".format(cipherText))


    ###---decrypt method---###
    def decrypt(self):
        #similar to encrypt method, add 3 empty string variables and keepGoing
        a1Text = ""
        atbText = ""
        plainText = ""

        keepGoing = True

        #must go in reverse, so A1Z26 decryption first
        decode = input("""
Please enter your message to be decoded
Enter dashes between numbers:

""")

        #must enter key now for final Vigenere decryption
        #check to see if it is valid
        key = input("""
Now please enter your key,
Key must have less characters than your message:

""")

        while keepGoing == True:
            if key.isalpha():

                if len(key)>(len(decode) - decode.count("-")):

                    key = input("""
Key must have less characters than your message.
Please re-enter key:

""")
                else:
                    keepGoing = False
                    keyInd = 0
                    key = key.upper()

            else:
                key = input("""
Key must contain only letters and no spaces.
Please re-enter key:

""")

        #decrypt A1Z26 cipher
        #see A1Z26.py for documentation
        for num in decode.split("-"):
            n = int(num)
            if 0<= n <= 25:
                a1Text += self.__alpha[n]

            else:
                pass

        #decrypt output of A1Z26 with Atbash
        #find index of each char in self.__reverse
        #use index to find char in alpha and add to atbText
        for char in a1Text:
            if char.upper() in self.__reverse:
                index = self.__reverse.find(char)

                atbText += self.__alpha[index]

        #for ea char in atbText, run it through Vigenere
        #see Vigenere.py for documentation
        for char in atbText:
            if char.upper() in self.__alpha:
                ordinal = self.__alpha.find(char.upper())
                ordinal -= self.__alpha.find(key[keyInd])

                ordinal %= len(self.__alpha)

                plainText += self.__alpha[ordinal]

                keyInd +=1
                if keyInd == len(key):
                    keyInd = 0

            else:
                pass

        print("""
Your decoded message is:

{}""".format(plainText))


###---testing main---### 
def main():
    c = Combined()
    c.encrypt()
    c.decrypt()

if __name__ == "__main__":
    main()


        
