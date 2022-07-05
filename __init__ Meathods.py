class computer:

    def __init__(self,ram, cpu):
        self.ram=ram
        self.cpu=cpu

    def config(self):
        print(" config is ",self.ram,self.cpu)

comp1= computer('intel i5',20)
comp2= computer('Ryzone 5', 20)

comp2.config()

comp1.config()