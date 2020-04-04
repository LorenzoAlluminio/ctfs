import string, sys, hashlib, binascii
from Crypto.Cipher import AES
#import requests 
#import re 
#from HTMLParser import HTMLParser

def is_hex(s):
     hex_digits = set(string.hexdigits)
     return all(c in hex_digits for c in s)

def fibseq(n):
    out = [0, 1]
    for i in range(2, n):
        out += [out[(i - 1)] + out[(i - 2)]]

    return out

data = "5ef9d8bce2063a7b528b1abdbbedb8277e0c50ec3f7ebb52ee236bfdee950e629f246105c975017b2502d07ae43e126068f6753de7d3bae23f2850e6e3ebe82604043a044d749b2980e626c3d7bb31dff57b8f613d40f1b1ef36223d37c91085ecde0f47273b57f9ec768bf09ef636342521ecf49aadd69dd60f2f8d2d4e547fe562075faa7fc6a8c802e275cf20747a6c55736058b984390134a0fbca7123497e289085f3a886058f49b1a566f9c3f43284c80ee6e90b6da99566cedb986841c02acb2270ef35e852623233697961aa026efca58a2633c6885f0f2a783b6ec869aa3d54cb57a7ccec4b40893daec35688d97835bcc762cb7c9cad8bc44076a5b3a643ef1db07add94163894e8225fb7a0e302b5f8af391cbc7babf98b7678d0c1a48f8e8c8237de59b7a5d7371d910b25f953c8d5f267faab3eae18ab50b4bea83f529ef7cf1bb31f3078d66600e70c4dedae9c83575571e2653767c901f62fb78c70df06b2bf5895a7a7a606759a3b4d78c936f3be7f1252c62baba54968d15855311dacf96dc207db31c7b60c6d3b591276afa6f2e4b9d1b18f37160bacdde40d5c1a444b04765abe1435977cca24b1a0ed5e897b2b39300bb8c8c2ab5b4ae58deba06beb261775eb248c483ca30cd57cee26a41ce586092648c7c3280f578569d76aebb4aba97e66e68b2dd512fa31c09c7551a5cbebd36bf67fc1572b800104fae06fd9b0e9c5e407691c90a22db10f77f28d57ddee91c8aae8a1cf3fc5b112fe07058e2589a81233aa19838f492fca289a0e877371666f8fa3506085809427b44ace49d73d0a8ea350e132474998562667f9eb3cc2ba906d7ae034309de45a6bf6a91b34f9b19e6a3b702a54ff1b0c557f3e7861dcae0e1799743065aabb4011dad3ddd5b247500ed051568bc915249515f2a4330cd1f6a414ccc080726010ad250b81540f8dfd309e0a341a1fdb330d6f0815ca8e4baf67bfd845e24c59a14e30f93cd08d8d4252803ce68666f909d80a5d166d7e8f65ee41d836ce4d932f77d55078604b2c5878d198325f039aa00d3f5ee37b032b44a341833358306e3a3def32329fab03318e183d9adb32709229f2449f5767ffaeebdf9163e29ad26866bab424a1f598e92cce0e33fd53018cff693813890735e6c6758db6670823c8e014583d89b128bf33fe10178b8b776a919aeb69d1e31925ea3b67897e69acfb29f13f033636c436f5a5e491a78426e1bb6efeaf91f47c136c2995641be76b5b200855c3baed4be3603aa661b689dac462726618891f597e4cab5d5cb1eb65edfeb119ec73882f96e68abdba715c824822cb54bd5af334f2799d4b2b91a140f64e2a1bf6f9a897f6f44a96920a791c9eec814ec629158782e8ded48ca677bd758a61481b47bf8eac47f532b4c9f776c07f3aea105ec07afb8d30de19875eea73ac8aab1169c4ce9f7709cbc5576fe930184c153aa01f3945c5e2a43bb7ad1222fe0a0f89793f266a4497a373969017f73063ffa772b168c9d41fe09e282a14bfcb34b8d43c3818c33c87173b4894934e212c38dfb15649dc34cd7be63c5e028fae0cb35d85ec7b935a7bc6ba1c75383e516154642499461931a64184966a8e5a1e863f26b1f11af7735c265b50573730c7e1100a8dc63ab0bd1a5386bcc47f2a47cd84256a81185d14591e9068cee124d0c0746c52b4e449e1bdd842bc2f5aa1615562ac27355240873af12b96fb30e2402db03ef5bd405d3ae903493e068263208c6b5b02cc8f002b825b819cce41fed1c63dfc2602402dd49d4e8d19bfa078708962e272dfd617533d7308918c41c4f6ecac55c928ba727093cb562bb373640568a1b5a346c76b0f11defbefacb04447f8ccc3bbce349400dfba800c726a6c4a571774c1bc750abd231ffb958596f568d8e284091a2d4c2ae8f8154dfe90e5669dfb1c2c79714d78fb11ffb7055f0c0ace21c11e83b2567363ca9c87be9104732d65ba1bee7c8c397af1dc13447c199339a74592032da29b44c771c8273a88371a68da58dc546885900c9755ba98a026aea426751e618f79e11b0c4d6216c8ec400433e07c3e9caad8c0162557d1c3d9599728bbad4a07b450d36d399aa16cfb3ae2cdba9c9c404a8a18d33c54ea58941aff98a7acce76169ba2824e7ac4d0875569bbed307f8dc1725b120adaec2eb9828f2cc72fabc77f13a334444c9cae5169389e3512f461195ec970cf74c3d8b144c4afe4bdf00a5540ca6af9a8af0457449fb8b6ab630de8c787bab6719bcf50c79d444bf414d3e93510ba488b40e5ea4a5f95810949cf9307a63c8e97a927c4c8956156d301c8891b5c64c962cf8736efdebc6bcf483dd148a6b85623b46f72c54219d14f7a281f6d24713199c5341492799861275d57f58209752bdeaee713ca94b9d4a6508e159a3b3f1f34fb27d040a206983b633d9a1b5ecfe66b7a9f6b834dd65728b29a80d03f9b7892a219349d3420fa0f79b694555ffb60710c0eaefd3eac4edbe8216a36d5ee6bb5c1bdcf5138c78ad94aeb8c00220e7632041bfd86cfe9f131a07559e4abe2166a0313b5b2599f170280da80a65aa03910f415c9aff86f0423fa0ae7b5801b002bb9e105d6300cd8afb4ae81879443bb37f74808c6ca7fbf678cc49d831c7290ef7dffb319e98f050906cc68148897a478617f1d5c18d66f19deba389722b98c0b16152975a81b662c76df625e6d6efe0fb4c2eea61c7bebf62174a49ee1288e0c87b66a988c257e91aec3d9e9a7cc377ab6d49dca15b1f28e9ce2847387afb295f3218500b0e60d48039e3b3027e9b7ba22c8a9efaf440c197843ad277e3a143ced868342c9261a3a7c5965bd05c12ede442d1193844da029e7c7a1491024c5a23304a98dfa13aec5cd2d48208f8222b171f14beab134f1d469ed51a49f075b11936042e279b4949cf9270eb98c4c2061b8ea5a439d0c05c47ceb2e428238059287a71322315e547418907a88aa0ba27b69c54b958e18c3e1c26e64313d4462474b51e050e7b7fd82fd3737271f689b56ea503909ef14822c023b5fb815eab5174d8e86348ad1db14d2c9d084649c90163d79690c65375f266ffb66e033e2af0586629dc3526643a94b75cf55e3c89d612b19b3448b03ab80bb56e004a4cdead91f4ecea587db92fdae1e0e23a1f61095a84a87f41376e878e5ba36e1d03f2f81b8e717761544efccace111c2ea9723fc176d7cec0136674666ff94a3acec1a425e7edab7a1b7f94853f045c0c36c1667e699e21214ef59177b83ad8b689aa7842742f2959cd6098fd38ba875711f5203547bd06bd948227dc9e29d5572c1a2edcce5aec00ef593517f641ef481a93b3e74e4966df0601cc459d7eb46b0f7fdb212cd9d491fda5271a7a533e2ed5a51c937655e4030e492b257ce871393199eed36c2f1caab469cca23ffeae4a55815faa14fb7364b3297176a3a1373d3fabda592027d477bdba8bd4e6ee5d2c4c3110fd6b92a8213d23b5c4dfb317350568d333c8f0eb3d381ccef172dc5b390fc3ee8444580dbab4223ef7dba81b13aa37c655b2dd6934d631ae9673add2f04550c03313a054c4a7fc23d2cdd8eac63bd666c6613015b88965fd49283aa59cff24ca4f7fba34435148dcfbc14b2ba45a99e45d5cb59a3d705df532cced04d1d680c7095bbcd77400da4275a0cda7ec2f99714c4b8415020a8b9d64f615692dc16ff522dd5e2e209cdf2d599332579f95c8f5ae651579ec6d08c67015e49b6ae49e344b714e8514cb5f973a27dd8bec0e65639b811fc12dabfe575de08a617e752405e2ac62b1389febf71aa6c9a5b09c2922880d89623c35f4ed0ccee62b61193f3d83d58126a90f4b4668d71552b98de42b5727309b16bf3700cd6a450c33d0967d19a1d247979efe83e794ff1d0b778560c9ab79d1455cbd41586b8e40bb8e103b4654ef795997ebfff51d00f6de8b080c75df00bead7ac804c719312ef0f9fa22f50b66f1131f390f89a1b01a2970219fa4dc6f8d293ac35c2f08391e447974da02e81c33e2681937eb3d0e1c79113c3c36327195fd408073c90d6edc4f27877a7de77a02ac0e1f3f8d3d81ab3f128145f296698361e5862139baaa69e3d62809fe54f8ff30ddfd11a91720b602eaeb063394bef9e973851f2a598ef901ca7fa4639125c140e60f61b6bddeffc3351c923d432334783ab1cf73a364f93261f3d2a5ee1e2eabe0da982f7440c8620d7184b3718ae7d2077b416b3f9bbdd8ff232bbb57a0e2d3944578d7bebdcb64a436fcccd1f6932f17a9beb67336435b74f95c2106114b014accbc4892672fe6ec06b44265ce1cc3c3255cb0e571e1be49bff5bd42f8910f63bc03c808bdc54d6938ef598db1d99d347ddc7f9533d6cc75f9fe0c981c9d2311c8dc8d43ae5f9cc9ecdadf3b0fd4d41b82e504c6ff68ecb1dd7aa2d1f7153d625a541d2b866db940079822b11dbff79a0555fce1cf6cd0a6f52639d3430dcf73dd4119e69a265b3992fdff987fa59503bd93bb7783d9b585819ae33855f8d5d990b7af2de04982b9618dba0738484f9fcbfc7a7eec81eb9b979d2410c7eb6d6104f64c3e2c4330c383991"

md5_list = []
key_list = []

print "Start bruteforcing AES"

for i in range(0,len(data),64):
	chunk = data[i:i+64]
    	#print "CHUNK--> " + chunk + " " + str(len(chunk))
	raw_chunk = binascii.unhexlify(chunk)
    	#print "RAW_CHUNK--> " + raw_chunk + " " + str(len(raw_chunk))
	for z in range(0,255):
		for j in range(0,255):
			key_piece = chr(z)+chr(j)
			key = key_piece*16
			#print "KEY--> " + key + " " + str(len(key))
		        cipher = AES.new(key, AES.MODE_ECB)
    			dec = cipher.decrypt(raw_chunk)
			if(is_hex(dec)):
				md5_list.append(dec)
				key_list.append(key_piece)
				#print "BLOCK NUMBER " + str(i/64)
				#print "DEC--> " + dec + " " + str(len(dec))

print key_list

FIBOFFSET = 4919
lenkey = 42
lendata = 204
MAXFIBSIZE = lenkey + lendata + FIBOFFSET
FIB = fibseq(MAXFIBSIZE)
i=0
flag = list("\x00"*lendata)

for key in key_list:
	index1 = ((i + FIB[(FIBOFFSET + i)]) % lenkey)
	i += 1
	index2 = ((i + FIB[(FIBOFFSET + i)]) % lenkey)
	i += 1
	flag[index1] = key[0]
	flag[index2] = key[1]

print "".join(flag)

''' try to bruteforce decrypt
print "Start bruteforcing MD5 hashes"

for offset in range(0,1000):
	FIBOFFSET = 4919
	lenkey = 42
	lendata = 191+offset
	MAXFIBSIZE = lenkey + lendata + FIBOFFSET
	FIB = fibseq(MAXFIBSIZE)
	i=0
	flag = list("\x00"*lendata)
	reversed_letters = []
	skip=0

	for hash_index in range(0,len(md5_list)): 
		index1 = (FIB[i] % lendata)
	    	i += 1
		index2 = (FIB[i] % lendata)
	    	i += 1
		found = 0
		for x in range(0,256):
			for y in range(0,256):
				data1 = chr(x)
				data2 = chr(y)
	    			mdhash = hashlib.md5(data1+data2).hexdigest()
				if(mdhash == md5_list[hash_index]):
					if(flag[index1]!="\x00" and flag[index2]!="\x00" and  flag[index1] != data1 and flag[index2] != data2):
						skip=1
						break
					flag[index1] = data1
					flag[index2] = data2
					found = 1
					reversed_letters.append(str(index1))
					reversed_letters.append(data1)
					reversed_letters.append(str(index2))
					reversed_letters.append(data2)
					break
			if(found):
				break
			if(skip):
				break
		if(skip):	
			break;
	if(skip):	
		#print "skip length " + str(lendata) + " due to sovrapposition"
		continue;

	print "".join(flag)
	#print reversed_letters
'''


''' attempt to reverse through lookup

	URL = "https://md5.gromweb.com/"
	h = HTMLParser()

	PARAMS = {'md5':hhash} 
	r = requests.get(url = URL, params = PARAMS) 
	response = r.text
	print "HASH --> " + hhash
	x = re.findall("<em class=\"long-content string\">(.*)</em></p>",response)
	if x:
		print "RESPONSE --> " + x[0]
		print "INDEX1 --> " + str(index1)
		print "INDEX2 --> " + str(index2)
		letters = h.unescape(x[0])
		print "LETTERS[0] --> " + letters[0]
		print "LETTERS[1] --> " + letters[1]
		flag[index1]=letters[0]
		flag[index2]=letters[1]
	else:
		print "UNRESOLVED HASH --> " + hhash
	#raw_input()	
	#print flag
'''		

