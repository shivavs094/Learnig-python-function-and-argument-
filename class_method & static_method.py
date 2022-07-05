class student:
    school = 'telusko'

    def __init__(self,m1,m2,m3,m4):
        self.m1=m1
        self.m2 = m2
        self.m3 = m3
        self.m4 = m4

    def avg (self):
        return (self.m1+self.m2+self.m3+self.m4)/3
    @classmethod
    def getschool (cls):
        return cls.school

    @staticmethod
    def info ():
        print("this is student class in static modules")

s1=student(55,66,44,22)
s2=student(66,55,44,77)

print(s2.avg())
print(student.getschool())
student.info()