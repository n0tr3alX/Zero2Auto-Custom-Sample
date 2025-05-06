import binascii
from arc4 import ARC4
import pefile

def rc4_decrypt(key, data):
    cipher = ARC4(key)
    decrypted = cipher.decrypt(data)
    return decrypted

def config_extract(filename):
    pe = pefile.PE(filename)
    for section in pe.sections:
        if(".rsrc" in section.Name.decode()):
            return section.get_data()
            
    #print(pe)

def main():
    filename = input("Filename: ")
    data = config_extract(filename)
    key = data[108:123]
    #print(key)
    data = data[124:]
    #print(data)
    decrypted = rc4_decrypt(key, data)
    with open ("decrypted.bin", 'wb') as o:
        o.write(decrypted)

if __name__ == '__main__':
    main()