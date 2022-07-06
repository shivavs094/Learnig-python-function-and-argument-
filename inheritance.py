class A:
    def feature_1 (self):
        print(("feature_1 is working"))

    def feature_2(self):
        print(("feature_2 is working"))

class B: #B(A) single level inheritance
    def feature_3(self):
        print(("feature_3 is working"))

    def feature_4(self):
        print(("feature_4 is working"))


class c(A,B): # multi lvel inheritance
    def feature_5(self):
        print(("feature_5 is working"))

    def feature_6(self):
        print(("feature_6 is working"))
c1=c()
c1.feature_2()