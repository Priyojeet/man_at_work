class conversion(object):
    def to_int(self, arg):
        s = arg.upper()
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for j in rom_val:
            if j not in s:
                print("please enter a valid roman number:-")
                break
            else:
                for i in range(len(s)):
                    if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                        int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
                    else:
                        int_val += rom_val[s[i]]
                return int_val

    def to_roman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        roman_num = ''
        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num

c = conversion()

degit = eval(input("enter the number in any:-"))
if(isinstance(degit,str)):
    print(c.to_int(degit))
else:
    print(c.to_roman(degit))
