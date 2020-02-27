"""Octal converter
for final project"""

#create octal class
class Octal(object):
    def __init__(self):
        object.__init__(self)


    ###---encrypt method---###
    def encrypt(self):
        octText = ""

        encode = input("""
Please enter the message you would like to convert to octal:

""")

        #for each char in encode, find the ASCII number with ord()
        #format the number into octal, join each one with a -
        octText = "-".join(format(ord(char), "o") for char in encode)

        #print converted message
        print ("""
Your converted message is:

{}""".format(octText))


    ###---decrypt method---###
    def decrypt(self):
        plainText = ""

        decode = input("""
Please enter the octal message you would like to convert.
Characters are seperated by a '-':

""")

        #split each octal number by a -, for each number, convert to decimal int
        #convert int to ASCII character with chr()
        for item in decode.split("-"):
            i = chr(int(item, base=8))

            plainText += i

        print("""
Your converted message is:

{}""".format(plainText))
        

###---testing main---###            
def main():
    c = Octal()
    c.encrypt()
    c.decrypt()

if __name__ == "__main__":
    main()
