# 8-13 uzunlugunda parol teyin etmeyi teleb etmeyi
""" a = input("Parol teyin edin: ")
length= len(a)
if len(a)>=8 and len(a)<=13:
    print("Parolunuz teleb olundugu uzunluqdadir")
else:
    print("Parolunuz teleb olundugu uzunluqda deil.Xais olunur 8-13 uzunluqunda parol teyin edin")
 """
#teyin edilen parolu 3 defe cehd ile daxil etmek
""" parol = input("Parol teyin edin: ")
a = input("Parolunuzu daxil edin: ")
result = 1
if parol ==a:
    print("Parolunuz duzdur")
else:
    while result<=3:
        print("Yanlisdir.Bir daha cehd edin")
        b = input("Parolunuzu daxil edin: ")
        result += 1
        if b == parol:
           print("Parolunuz duzdur")
           break
    if result==4:
       print("artiq cehd ede bilmezsiniz") """

#Kalkulyator proqrami qurmaq
while True:
    try:
        eded_1 = int(input("Birinci ededi daxil edin: "))
        eded_2 = int(input("Ikinci ededi daxil edin: "))
        operation = input("hansi emeliyyati yerine yetirmeliyik? +,-,*,/ :  ")
    except ValueError:
        print("Sadece eded daxil edin!")
        continue
    if operation == '+':
        print("{0} + {1} = {2}".format(eded_1,eded_2,eded_1+eded_2))
    elif operation == '-':
        print("{0} - {1} = {2}".format(eded_1,eded_2,eded_1-eded_2))
    elif operation == '*':
        print("{0} * {1} = {2}".format(eded_1,eded_2,eded_1*eded_2))
    elif operation == '/':
         if eded_2 == 0:
            print("Sifira bolmek olmaz")
         else:
            print("{0} / {1} = {2}".format(eded_1,eded_2,eded_1/eded_2))
    else:
        print("Bele bir emeliyyatimiz yoxdur")
    a = input("proqrami bitirmek ucun x duymesine basin, davam etmek ucun istenilen duymmeye basin: ")
    if a == 'x':
       break
#bolmede sifira bolmeni nezere al


         



 
