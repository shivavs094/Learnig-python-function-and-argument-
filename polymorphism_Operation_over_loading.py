class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self, other):
        m1=self.m1+other.m1
        m2 = self.m2 + other.m2
        s3=student(m1,m2)
        return s3
    def __gt__(self, other):
        r1=self.m1+other.m2
        r2=self.m1+other.m2
        if r1>r2:
            return True
        else:
            False

    def __str__(self):
        return '{},{}'.format(self.m1,self.m2)

s1 = student(56,85)
s2=student(78,64)

s3=s1+s2

if s1>s2:
    print("S1 Got win")
else:
    print("S2 ot win")


print(s3.m1,s3.m2)
print(s1)