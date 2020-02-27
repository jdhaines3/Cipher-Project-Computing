"""Hex converter
for final project"""

#create Hexa class
class Hexa(object):
    def __init__(self):
        object.__init__(self)


    ###---encrypt method---###
    def encrypt(self):
        #create hexText variable
        hexText = ""

        encode = input("""
Please enter the message you would like to convert to Hex:

""")

        #similar to binary conversion, just change ord number to hex
        #see binary.py documentation
        hexText = "-".join(format(ord(char), "x") for char in encode)

        print("""
Your converted message is:

{}""".format(hexText))


    ###---decrypt method---###
    def decrypt(self):
        #plainText blank str
        plainText = ""

        decode = input("""
Please enter the hexadecimal message you would like to convert.
Characters are seperated by a '-':

""")

        #split each hex item by -, convert hex to decimal int
        #find chr() of that int and add to plainText
        #chr finds the ASCII value associated to number
        for item in decode.split("-"):
            i = chr(int(item, base=16))

            plainText += i

        print ("""
Your converted message is:

{}""".format(plainText))


###---testing main---###
def main():
    c = Hexa()
    c.encrypt()
    c.decrypt()

if __name__ == "__main__":
    main()
