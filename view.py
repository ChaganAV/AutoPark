import controller as c

def InputClient():
    print("==Автобусный парк==") 
    c.SelectCommands()
    while True:
        res = int(input("Введите номер действия: \n> "))
        if res == 1: 
            break
            # c.DictPrint(fin)
        elif res == 2:
            name = input("Введите фамилию: ")
            break
        elif res == 3:
            break
        elif res == 4:
            break
        elif res == 5:
            break
        elif res == 6:   
            break
        elif res == 7:
            break
        else:
            c.SelectCommands()