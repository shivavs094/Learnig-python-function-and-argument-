class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self. m2= m2

    def sum (self,a,*b):
        c=a
        for i in b:
            c=c+i
        return c
        if b != None:
            return a


s1=student(58,65)
print((s1.sum(2,)))


###################################################################
######################################################################################

#mathod over writting
class A:
    def show(self):
        print("In A show")
class B(A):#used inheritance method
    pass
a1=B()
a1.show()

