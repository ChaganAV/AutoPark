import data as d
import model as m

# вывод списка команд
def SelectCommands():
    commands = "Список команд:\n\
            1 - Вывод автобусов\n\
            2 - Добавление автобуса\n\
            3 - Вывод водителей\n\
            4 - Добавление водителя\n\
            5 - Вывод маршрута\n\
            6 - Добавление маршрута\n\
            7 - Выход\n\
            8 - Список команд\n"
    print(commands)

def AddBus():
    busId = input("Введите id: ")
    busIn = input("Введите модель: ")
    busGN = input("Введите госномер: ")
    bus = m.Bus(busId,busIn,busGN)
    d.fbus.write(f"{bus.Id},{bus.Model},{bus.GNumber}\n")
    d.fbus.close()

def AddDriver():
    id = input("Введите id: ")
    name = input("Введите водителя: ")
    driver = m.Driver(id,name)
    d.fDriver.write(f"{driver.Id},{driver.Name}\n")
    d.fDriver.close()

def AddRoute():
    id = input("Введите id: ")
    number = input("Введите номер маршрута: ")
    bus_id = input("Введите id автобуса: ")
    driver_id = input("Введите id водителя: ")
    d.fRoute.write(f"{id},{bus_id},{driver_id}\n")
    d.fRoute.close()

def PrintBus():
    file = d.fileBus
    lines = FileToList(file)
    for line in lines:
        strLine = ""
        for l in line:
            strLine = strLine + l + " "
        print(strLine.strip())

def PrintDriver():
    file = d.fileDriver
    lines = FileToList(file)
    for line in lines:
        strLine = ""
        for l in line:
            strLine = strLine + l + " "
        print(strLine.strip())

# вывод в список
def FileToList(file):
    mod = 'r'
    file = m.File(file,mod)
    file.Open()
    lists = []
    while True:
        line = file.ReadLine()
        if not line:
            break
        else:
            lists.append(line.split(','))
    file.Close()
    return lists