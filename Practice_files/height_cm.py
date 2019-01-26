import sys
def convertion(arg1, arg2):
    arg2 += arg1*12
    h_cm = round(arg2*2.54, 1)
    return h_cm
try:
    h_ft = eval(input("enter the height in Feet:-"))
    h_inch = eval(input("enter the height in Inches:-"))
except:
    error = sys.exc_info()[0]
    print(error)
else:
    print(convertion(h_ft,h_inch))
