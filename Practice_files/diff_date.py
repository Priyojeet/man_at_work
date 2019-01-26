from datetime import date
f_y=int(input("enter 1st the year:-"))
f_m=int(input("enter 1st the month"))
f_d=int(input("enter 1st the date:-"))
l_y=int(input("enter 2nd the year:-"))
l_m=int(input("enter 2nd the month"))
l_d=int(input("enter 2nd the date:-"))
f_date = date(f_y, f_m, f_d)
l_date = date(l_y, l_m, l_d)
delta = l_date -f_date
print(delta)
print(delta.days)
