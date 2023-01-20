import controller as c

try:
    def InputClient():
        print("==Автобусный парк==") 
        c.SelectCommands()
        while True:
            res = int(input("Введите номер действия: \n> "))
            if res == 1: 
                c.PrintBus()
            elif res == 2:
                bus = c.AddBus()
                bus.Print()
            elif res == 3:
                c.PrintDriver()
            elif res == 4:
                driver = c.AddDriver()
                driver.Print()
            elif res == 5:
                c.PrintRoute()
            elif res == 6:   
                route = c.AddRoute()
                route.Print()
            elif res == 7:
                break
            else:
                c.SelectCommands()
except:
    print("В view ошибка!")