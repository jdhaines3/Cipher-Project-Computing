"""Binary/String Conversion
for final project"""


#create binary class
class Binary(object):
    def __init__(self):
        object.__init__(self)


    ###---encrypt method---###
    def encrypt(self):
        binText = ""

        encode = input("""
Please enter the message you would like to convert to binary:

""")

        #for each char in encode, convert char to binary, seperate by -
        #use ord(), to find ASCII code and display in binary
        binText = "-".join(format(ord(char), "b") for char in encode)

        #print converted message
        print ("""
Your converted message is:

{}""".format(binText))


    ###---decrpyt method---###
    def decrypt(self):
        plainText = ""

        decode = input("""
Please enter the binary message you would like to convert.
Characters are seperated by a '-':

""")

        #for each binary item in decode...(use split("-") to seperate binary
        #characters) convert binary number to string
        #use chr() to find ASCII character for number
        #binary string must be converted to decimal int
        for item in decode.split("-"):
            i = chr(int(item, base=2))

            plainText += i

        print("""
Your converted message is:

{}""".format(plainText))


###---testing main---###            
def main():
    c = Binary()
    c.encrypt()
    c.decrypt()

if __name__ == "__main__":
    main()

                    
