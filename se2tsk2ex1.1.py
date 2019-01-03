class Triangle():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def take_side(self):
        self.a = int(input("enter the side for a:-"))
        self.b = int(input("enter the side for b:-"))
        self.c = int(input("enter the side for c:-"))
class Calculate_area(Triangle):
    def __init__(self):
        pass

    def area(self):
        s = (self.a+self.b+self.c)/2
        area = (s*(s-self.a)*(s-self.b)*(s-self.c))**0.5
        print(area)
t = Calculate_area()
t.take_side()
t.area()