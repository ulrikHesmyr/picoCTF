#Output that we got from the server
ourEncodedFlag = "9692350-804b000-80489c3-f7fa9d80-ffffffff-1-9690160-f7fb7110-f7fa9dc7-0-9691180-5-9692330-9692350-6f636970-7b465443-306c5f49-345f7435-6d5f6c6c-306d5f79-5f79336e-35343036-64303664-ffcf007d-f7fe4af8-f7fb7440"

#The string we will store our flag in
s = ""

#Iterating through each hex value in ourEncodedFlag
for i in ourEncodedFlag.split('-'):

    #If the length of the string is 8, we know it is valid hex value that stores a character
    if len(i) == 8:
        a = bytearray.fromhex(i)

        #Iterating through each byte in the bytearray and reversing it because of endianness
        for b in reversed(a):

            #If the byte is a valid ascii character, we add it to our string
            if b > 32 and b < 128:
                s += chr(b)


print(s)    #output: qpicoCTF{I_l05t_4ll_my_m0n3y_6045d60d}J@t