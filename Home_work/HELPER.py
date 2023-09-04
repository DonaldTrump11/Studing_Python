ПРИМЕР РАБОТЫ МЕТОДА КЛВССА "А" ВНУТРИ МЕТОДА КЛАССА "В"

_____________________________________________
class A:
    def __init__(self):
        pass

    def method(self, b):
        self.b = b
        b = b*2
        return b


class B:

    def __init__(self):
        self.a = A()

    def method2(self, e, b):
        self.d = e
        self.b = b
        b = self.a.method(b)
        return b*e
        

________________________________________
dsa = B()
dsa.method2(2,3)
