class Bus:
    def __init__(self,id,model,number):
        self.ID = id
        self.Model = model
        self.GNumber = number

class Driver:
    def __init__(self,id,name):
        self.ID = id
        self.Name = name

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


    