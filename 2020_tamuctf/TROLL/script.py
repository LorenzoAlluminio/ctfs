import ctypes
from pwn import *
import time

libc = ctypes.CDLL('libc.so.6')
 
p = remote("challenges.tamuctf.com",4765)
#p = process("./troll")

t = libc.time(None)
libc.srand(t)
	
print p.recvuntil('?')	
p.sendline("ulla")	
print p.recvuntil('?')	

for i in range(0,100):
	print p.recvline()	
	n = libc.rand()	% 100000 + 1;	
	p.sendline(str(n))
	print p.readline()
 
p.interactive()
