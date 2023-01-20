import controller as c

def InputClient():
    print("==Автобусный парк==") 
    c.SelectCommands()
    while True:
        res = int(input("Введите номер действия: \n> "))
        if res == 1: 
            c.PrintBus()
        elif res == 2:
            c.AddBus()
        elif res == 3:
            c.PrintDriver()
        elif res == 4:
            c.AddDriver()
        elif res == 5:
            break
        elif res == 6:   
            c.AddRoute()
        elif res == 7:
            break
        else:
            c.SelectCommands()