import re, binascii

def Encrypt(text):
    print "Encryption"
    E = []
    for i in text:
        en = format(ord(i), "x")
        E.append(en)
    print ''.join(E)

def Decrypt(encryption):
    print "Decryption"
    D = ''
    for i in range((len(encryption)/2)):
        de = re.findall(r'.{1,2}', encryption, re.DOTALL)
    D = D+str(''.join(de))
    print binascii.unhexlify(D)

choice = raw_input("(e)ncryption, (d)ecryption or (q)uit")

if choice == 'e':
    text = raw_input("What text would you like to encrypt")
    Encrypt(text)
elif choice == 'd':
    encryption = raw_input("What text would you like to decrypt")
    Decrypt(encryption)
elif choice == 'q':
    exit()
else:
    print "Invalid input"