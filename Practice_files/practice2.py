bob = [['name', 'Bob Smith'], ['age', 42], ['pay', 10000]]
sue = [['name', 'Sue Jones'], ['age', 45], ['pay', 20000]]
people = [bob, sue]
for person in people:
    print(person[0][1], person[2][1])  # name,pay
print([person[0][1] for person in people])
for