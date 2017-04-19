"""from Crypto.Cipher import ARC4

key = key_entry.encode('utf-8')

split_name = file.split('/')
# docname = split_name[len(split_name)-1]

encryp = ARC4.new(key)
lastPeriod = file.rfind('.')

try:
    fr = open(file, 'rb')
    fw = open("testText.enc", 'wb')
    # fw = open(file[:lastPeriod] + ".enc", 'wb')
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
print("encryptfile here")
"""