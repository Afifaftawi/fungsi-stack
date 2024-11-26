stack = []
stack.append (10)
stack.append (20)
stack.append (30)

print ("stack setela push :",stack)

elemen = stack.pop()
print ("elemen yang di pop :",elemen)
print ("stack setelah pop :",stack)
if stack :
    print ("elemen teratas :",stack[-1])
else :
    print ("stack kosong")

