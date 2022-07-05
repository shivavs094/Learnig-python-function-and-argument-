class computer:

    def __init__(self):
        self.name="shiva"
        self.Age=27
    def update(self):
        self.Age=30
    def compare(self,other):
        if self.Age==other.Age:
            return True
        else:
            return False

c1=computer()
c2=computer()
c2.update()
c2.Age=30

if c1.compare(c2):
    print('Both Are Similar Aged')
else:
    print( 'Not Similar')



print(c1.Age)
print(c2.name)