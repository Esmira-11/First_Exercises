#teyin edilen parolu 3 defe cehd ile daxil etmek
parol = input("Parol teyin edin: ")
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
       print("artiq cehd ede bilmezsiniz")