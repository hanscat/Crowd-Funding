
from Crypto.Cipher import ARC4
import json


def encrypt(file, inp):

    key = inp.encode('utf-8')

    split_name = file.split('/')
   # docname = split_name[len(split_name)-1]

    encryp = ARC4.new(key)
    lastPeriod = file.rfind('.')


    try:
        fr = open(file, 'rb')
        fw = open("testText.enc", 'wb')
        #fw = open(file[:lastPeriod] + ".enc", 'wb')
    except FileNotFoundError:
        print("file not found")
        return False

    text = fr.read()
    data = encryp.encrypt(text)
    fw.write(data)
    fr.close()
    fw.close()
    print("File Encrypted. Saved as " + file[:lastPeriod] + ".enc")
    print()

    fr2 = open("testText.enc",'rb')
    #fr2 = open(file[:lastPeriod] + ".enc",'rb')
    fw2 = open("done.txt", 'wb')

    text2 = fr2.read()
    data = encryp.decrypt(text2)
    fw2.write(data)

    fr2.close()
    fw2.close()



    return True

def decrypt_file(lines, key, name):
    """ decrypt a .enc file to a DEC_ file using the given key """
    dec = ARC4.new(key)
    fw = open("downloads/"+name, 'wb')
    for line in lines:
	    enc_text = line.encode('latin-1')
	    text = dec.decrypt(enc_text)
	    fw.write(text)
    return True


if __name__ == "__main__":
    inp = input("Enter Key")
    filename = input("Enter filename: ")
    #filename = C:/Users/Student/Documents/HCI/Second Test/textbook+-+chapter5.pdf
    #file = open(filename, 'rb')
    encrypt(filename, inp)

