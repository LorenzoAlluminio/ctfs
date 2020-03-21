#f = open("fr3sh_h4rv3st.jpg", "r")
# pace 0x70 0x61 0x63 0x65
data = "1921754512366910363569105a73727c592c5e5701715e571b76304d3625317c1b72744d0d1d354d0d1d73131c2c655e".decode('hex')
strs = ""
j = 0
    #a = ord(i)^0x	
for i in data:
    
    if j==0:
        a = ord(i)^0x69
    elif j==1:
        a = ord(i)^0x42
    elif j==2:
        a = ord(i)^0x01
    elif j==3:
        a = ord(i)^0x23
   
    if a < 256:
       strs += chr(a)
    j  = (j + 1) % 4

print strs

#fo = open("prova","w")
#fo.write(strs)
#print strs
