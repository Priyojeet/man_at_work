def near_thousend(n):
    return ((abs(1000-n)<=100) or (abs(2000-n)<100))
print(near_thousend(900))
print(near_thousend(2200))
