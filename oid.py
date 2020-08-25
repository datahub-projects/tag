import sys
from hashlib import sha256
from base64 import b32encode

def get_oid(s):
    return "oid1"+b32encode(sha256(s).digest()[:20]).decode().lower() #+ 160 bits of sha256, base32 encoded, converted to lowercase

if __name__=="__main__":
    f = open(sys.argv[1], 'rb')
    s = f.read()
    f.close()
    print (get_oid(s))
