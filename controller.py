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

def InsertBus():
    busId = input("Введите id: ")
    busIn = input("Введите модель: ")
    busGN = input("Введите госномер: ")
    bus = m.Bus(busId,busIn,busGN)
    d.fbus.write(f"{bus.ID},{bus.Model},{bus.GNumber}")
    d.fbus.close()

def PrintBus(file,mod):
    lines = FileToList(file,mod)
    for line in lines:
        print(line)
        # for l in line:
        #     print(f"{l}")


# вывод в список
def FileToList(file,mod):
    file = m.File(d.fileBus,mod)
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