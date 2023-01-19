import data as d
import model as m

def InsertBus():
    busId = input("Введите id: ")
    busIn = input("Введите модель: ")
    bus = m.Bus(busId,busIn)
    d.fbus.write(f"{bus.ID},{bus.Model}")
    d.fbus.close()

def PrintBus():

    buses = list(d.fbus.readlines())
    d.fbus.close()
    for bus in buses:
        print(f"{bus[0]},{bus[1]}")

# вывод в список
def FileToList(file):
    file = d.File(file,'r')
    file.Open()
    listFio = []
    while True:
        line = file.ReadLine()
        if not line:
            break
        else:
            listFio.append(line.split(','))
    file.Close()
    return listFio