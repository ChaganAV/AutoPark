try:
    class Bus:
        def __init__(self,id,model,number):
            self.Id = id
            self.Model = model
            self.GNumber = number
        def Print(self):
            print(f"{self.Id}, {self.Model}, {self.GNumber}")

    class Driver:
        def __init__(self,id,name):
            self.Id = id
            self.Name = name
        def Print(self):
            print(f"{self.Id}, {self.Name}")
    class Route:
        def __init__(self,id,number,bus_id,driver_id):
            self.Id = id
            self.Number = number
            self.Bus_id = bus_id
            self.Driver_id = driver_id
        def Print(self):
            print(f"{self.Id}, {self.Number}, {self.Bus_id}, {self.Driver_id}")
    class File:
        def __init__(self,file,mod):
            self.file = file
            self.mod = mod
            # self.encoding = cp
        def Open(self):
            self.data = open(self.file,self.mod,encoding='utf8')
        def Close(self):
            self.data.close()
        def Read(self):
            return self.data.read()
        def ReadLine(self):
            return self.data.readline()
        def Write(self,str1):
            self.data.write(str1)
except:
    print("В model ошибка!")
    