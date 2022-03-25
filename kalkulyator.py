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