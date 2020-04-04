# uncompyle6 version 3.6.5
# Python bytecode 3.6 (3379)
# Decompiled from: Python 2.7.12 (default, Oct  8 2019, 14:14:10) 
# [GCC 5.4.0 20160609]
# Warning: this version has problems handling the Python 3 byte type in contants properly.

# Embedded file name: pybonhash.py
# Compiled at: 2020-03-28 14:11:38
# Size of source mod 2**32: 1017 bytes
import string, sys, hashlib, binascii
from Crypto.Cipher import AES

key="123456789abcdefghijklmnopqrstuvwxyzABCDEFG"

if not len(key) == 42:
    raise AssertionError
else:
    data = open(sys.argv[1], 'rb').read()
    if not len(data) >= 191:
        raise AssertionError
FIBOFFSET = 4919
MAXFIBSIZE = len(key) + len(data) + FIBOFFSET

def fibseq(n):
    out = [0, 1]
    for i in range(2, n):
        out += [out[(i - 1)] + out[(i - 2)]]

    return out


FIB = fibseq(MAXFIBSIZE)
i = 0
output = ''
while i < len(data):
    print "ITERATION " + str(i) + " -------------------------------------"   
    data1 = data[(FIB[i] % len(data))]
    print "DATA1--> " + data1 + " " + str(len(data1))
    key1 = key[((i + FIB[(FIBOFFSET + i)]) % len(key))]
    print "KEY1--> " + key1 + " " + str(len(key1))
    i += 1
    data2 = data[(FIB[i] % len(data))]
    print "DATA2-> " + data2 + " " + str(len(data2))
    key2 = key[((i + FIB[(FIBOFFSET + i)]) % len(key))]
    print "KEY2--> " + key2 + " " + str(len(key2))
    i += 1
    tohash = bytes([data1, data2])
    print "TOHASH--> " + tohash + " " + str(len(tohash))
    mdhash = hashlib.md5(tohash)
    toencrypt = mdhash.hexdigest()
    print "TOENCRYPT--> " + toencrypt + " " + str(len(toencrypt))
    thiskey = (key1+key2) * 16 
    print "THISKEY--> " + thiskey + " " + str(len(thiskey))
    cipher = AES.new(thiskey, AES.MODE_ECB)
    enc = cipher.encrypt(toencrypt)
    print "ENC--> " + enc + " " + str(len(enc))
    enc_ascii = binascii.hexlify(enc).decode('ascii')
    print "ENC_ASCII--> " + enc_ascii + " " + str(len(enc_ascii))
    output += enc_ascii
    raw_input()

print(output)
# okay decompiling pybonhash.cpython-36.pyc
