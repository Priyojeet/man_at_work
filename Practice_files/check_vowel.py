char = str(input("enter the character you want to check:-"))
def check_vowel(arg):
    vowels = "AaEeIiOoUu"
    for i in vowels:
        if i==arg:
            #pass
            print("vowel")
            break
        else:
            print("not")




check_vowel(char)
