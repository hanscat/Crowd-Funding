__author__ = 'pbs5kx'
#some code from http://www.laurentluce.com/posts/python-and-cryptography-with-pycrypto/
import os
import Crypto
import hashlib
from Crypto.Cipher import ARC4
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Hash import SHA256
from Crypto.Hash import MD5

#takes in a string and key and returns encrypted string
def secret_string(str, publickey):
    if not(isinstance(publickey, RSA._RSAobj)):
        print("Not a valid key")
        return False
    str=str.encode('utf-8')
    encrypted = publickey.encrypt(str, 32)
    return encrypted

#takes in file and key and writes to make an encrypted file
def encrypt_file(filename, pubkey):
    key = hashlib.sha256(pubkey.encode('utf-8')).digest()
    obj = ARC4.new(key)
    try:
        with open(filename, 'rb') as in_file:
            with open(filename+".enc", 'wb') as out_file:
                while True:
                    chunk = in_file.read(8192)
                    if len(chunk) == 0:
                        break
                    out_file.write(obj.encrypt(chunk))
        return True
    except FileNotFoundError:
        print("Wrong file or file path")
        return False

#takes in encrypted file and key; decrypts the file and writes to make a new decrypted file
def decrypt_file(filename, pubkey):
    key = hashlib.sha256(pubkey.encode('utf-8')).digest()
    out=filename.replace(".enc","")
    out="DEC_"+out
    obj = ARC4.new(key)
    try:
        with open(filename, 'rb') as in_file:
            with open(out, 'wb') as out_file:
                while True:
                    chunk = in_file.read(8192)
                    if len(chunk) == 0:
                        break
                    out_file.write(obj.decrypt(chunk))
        return True
    except FileNotFoundError:
        print("Wrong file or file path")
        return False

def checksum(filename):
    h = MD5.new()
    chunk_size = 8192
    with open(filename, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if len(chunk) == 0:
                break
            h.update(chunk)
    return h.hexdigest()

def equal(x,y):
    if(x==y):
        print("The files are equal")
    else:
        print("The files are not equal")


if __name__ == '__main__':
    random_generator = Random.new().read
    x= RSA.generate(1024, random_generator)
    public_key = x.publickey()
    enc=secret_string("waterBoat", public_key)
    #print(enc)
    dec=x.decrypt(enc)
    print(dec)
    encrypt_file("enpt.py", "hellobob")
    decrypt_file("qweqwe", "hellobob")
    encrypt_file("file.txt", "hellobob")
    decrypt_file("file.txt.enc", "hellobob")
    encrypt_file("testcase-doc-hw3.xlsx", "hellobob")
    decrypt_file("testcase-doc-hw3.xlsx.enc", "hellobob")
    encrypt_file("logo.jpg", "hellobob")
    decrypt_file("logo.jpg.enc", "hellobob")
    encrypt_file("class10.pdf", "hellobob")
    decrypt_file("class10.pdf.enc", "hellobob")
    encrypt_file("vlsi.ppt", "BLABLA")
    decrypt_file("vlsi.ppt.enc", "BLABLA")
    encrypt_file("1st.PNG", "hellobob")
    decrypt_file("1st.PNG.enc", "hellobob")
    encrypt_file("encrypt.py", "hellobob")
    decrypt_file("encrypt.py.enc","hellobob")
    equal(checksum("file.txt"),checksum("DEC_file.txt"))
    equal(checksum("logo.jpg"), checksum("DEC_logo.jpg"))
    equal(checksum("testcase-doc-hw3.xlsx"), checksum("DEC_testcase-doc-hw3.xlsx"))
    equal(checksum("Class10.pdf"), checksum("DEC_Class10.pdf"))
    equal(checksum("vlsi.ppt"), checksum("DEC_vlsi.ppt"))
    equal(checksum("1st.PNG"), checksum("DEC_1st.PNG"))
    equal(checksum("encrypt.py"),checksum("DEC_encrypt.py"))