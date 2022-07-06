class student :
    def __init__(self,name,roll_no):
        self.name = name
        self.roll_no= roll_no
        self.laptop = self.laptop()

    def show(self):
        print(self.name,self.roll_no)
        self.laptop.show()

    class laptop():
        def __init__(self):
            self.com="acer"
            self.pro="i5"
            self.ram=20

        def show(self):
            print(self.com,self.pro,self.ram)

s1=student("shiva",3)


s1.show()