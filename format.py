#ad = input("Adinizi daxil edin: ")
#soyad = input("Soyadinizi daxil edin: ")
#print("Xos gelmisen {1} {0}".format(ad,soyad))
#print(ad)

#print("{:c}".format(65))
#print(chr(65))
#print("{:o}".format(65))
#print("{:,}".format(268243891648))


#1 nece sozden ibaret stringin ilk 2 ve son 2 sinvolu birlesdirib ekrana cixarin
#a = 'riyaziyyat'
#b = a[:2] + a[-2:]
#print(b)

a = 'asdf'
b = 'zxcv'
c= a
a = a[:len(a)-1]+b[-1]
b = b[:len(b)-1]+c[-1]
print("a={}".format(a))
print("b={}".format(b))