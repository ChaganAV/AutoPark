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
    file = d.fileBus
    fbus = m.File(file,'a')
    fbus.Open()
    fbus.Write(f"{bus.Id},{bus.Model},{bus.GNumber}\n")
    fbus.Close()

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
    d.fRoute.write(f"{id},{number},{bus_id},{driver_id}\n")
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

def PrintRoute():
    file = d.fileRoute
    lines = FileToList(file)
    for line in lines:
        if len(line[0].strip())>0:
            driver = FindDriver(line[3].strip())
            bus = FindBus(line[2].strip())
            print(f"{line[0]} маршрут {line[1]}, {bus}, водитель: {driver}")
        

def FindDriver(id):
    file = d.fileDriver
    lines = FileToList(file)
    driver = ""
    for line in lines:
        if line[0].strip() == id:
            driver = line[1].strip()
            break
    return driver

def FindBus(id):
    file = d.fileBus
    lines = FileToList(file)
    bus = ()
    for line in lines:
        if line[0].strip()==id:
            bus = (f"{line[1]} гос.номер: {line[2].strip()}")
            break
    return bus
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