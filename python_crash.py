print(7**4)
s = "hi there sam!"
print(s.split())
planet = 'earth'
diameter = 12742
print("the diameter of {} is {} kilometer.".format(planet,diameter))
lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(lst[3][1][2][0])
d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
print(d['k1'][3]["tricky"][3]['target'][3])

def getdomain(email):
    print("domain is:"+email.split('@')[-1])


email = input("ente your email:-")
getdomain(email)


def findDog(arg):
    if 'dog' in arg.lower():
        print("True")
    else:
        print("False")


st = input("Please key a string: >")
findDog(st)

string = input("Please enter your string: ")


def countdogs(arg):
    count = 0
    for word in arg.lower().split():
        if word == 'dog' or word == 'dogs':
            count = count + 1
            print(count)


countdogs(string)

seq = ['soup','dog','salad','cat','great']
print(list(filter(lambda word: word[0]=='s',seq)))


print("Please enter the speed(km/h)(only number please): \n")
speed = int(input("> "))

print("Please enter your birthday: (in DD/MM/YYYY format)\n")
birthday = str(input("> "))

def speeding(speed, birthday):
    if birthday == '29/08/1989':
        s = speed - 5
    else:
        s = speed

    if s <= 60:
        print("You pass.")
    elif s > 61 and s <= 80:
        print("You get a small ticket")
    else:
        print("You get a big ticket.")

speeding(speed, birthday)