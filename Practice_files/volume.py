from math import pi
radius = int(input("enter the radius:-"))
def volume(arg):
    r = arg**3
    vol = 4/3*pi*r
    print(vol)

volume(radius)