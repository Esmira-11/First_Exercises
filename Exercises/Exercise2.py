# 8-13 uzunlugunda parol teyin etmeyi teleb etmeyi
a = input("Parol teyin edin: ")
length= len(a)
if len(a)>=8 and len(a)<=13:
    print("Parolunuz teleb olundugu uzunluqdadir")
else:
    print("Parolunuz teleb olundugu uzunluqda deil.Xais olunur 8-13 uzunluqunda parol teyin edin")
