def check_vowel(arg):
    vowel = 'aeiouAEIOU'
    for i in range(len(vowel)):
        if(vowel[i] == arg):
            return True
    else:
        return False


char = str(input("enter the character you want to check:-"))
print(check_vowel(char))
