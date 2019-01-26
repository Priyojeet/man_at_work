def is_vowel(char):
    all_vowels = "aeiouAEIOU"
    return char in all_vowels

ch = str(input("enter the char you want to check:-"))
print(is_vowel(ch))
