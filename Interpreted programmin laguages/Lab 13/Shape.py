class Shape:


    def compare(self, x, y):
        if x.square() > y.square():
            print("Площадь " + x + " больше " + y)
        elif x.square() == y.square():
            print("Площади равны")
        else: print("Площадь " + y + " больше " + x)

    def is_intersect(self, x, y):
        pass

    def is_include(self, x, y):
        pass