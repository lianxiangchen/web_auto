class A(object):

    def __init__(self):
        self.__Gender()
        self.Name()

    def __Gender(self):
        print("A.__Gender()")   # A类私有

    def Name(self):
        print("A.Name()")


class B(A):

    def __Gender(self):
        print("B.__Gender()")   # B类私有

    def Name(self):
        print("B.Name()")
b = B()
