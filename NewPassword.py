import random
index = 'abcdefghijklmnopqrstuvABCDEFGHIJKLMNOPQRSTUV1234567890!@#$%^&*'

bool = True
num = eval(input("length: "))
while(bool):
    pw = ""

    for c in range(num):
        ch = index[random.randrange(62)]
        b = True
        c = False
        while b:
            if ch.isalpha() and random.random() > .8 or c:
                c = True
                #print(ch + " " + str(ch.isalpha()))
                ch = index[random.randrange(62)]
                if not ch.isalpha():
                    b = False
                    #print(ch + "\n")
                    break
                #print(ch + " " + str(ch.isalpha()))
            else:
                b = False
                c = False
        pw = pw+ch
    print("***************\n")
    print(pw)
    print("\n***************")

    again = input("\nagain? Y/N or L to change length \n")

    if again.lower() == 'y':
        bool = True
    elif again.lower() == 'l':
        num = eval(input("length: "))
        bool = True
    else:
        bool = False