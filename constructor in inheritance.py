class A:

    def feature_1 (self):
        print(("feature_1 is working"))

    def feature_2(self):
        print(("feature_2 is working"))

class B: #B(A) single level inheritance

    def __init__(self):
        super().__init__() # super () will work while inhertance B(A)
        # it will call Both
        print ("init from class B")

    def feature_3(self):
        print(("feature_3 is working"))

    def feature_4(self):
        print(("feature_4 is working"))


class C(A,B): # multi lvel inheritance
    def __init__(self):
        super().__init__()
        print ("init from class C")
    def feature_5(self):
        print(("feature_5 is working"))

    def feature_6(self):
        print(("feature_6 is working"))

    def feat(self):
        super().feature_2()
c1=C()
c1.feat()