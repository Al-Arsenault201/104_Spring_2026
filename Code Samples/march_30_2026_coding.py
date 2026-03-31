# in-class coding from Monday, March 30

groceries = []
print(len(groceries))
groceries.append("milk")
print(groceries)
groceries.append("eggs")
print(groceries)
groceries.append("grapes")
groceries.append("broccoli")
groceries.append("bread")
print (groceries)




groceries.insert(2, "ice cream")
print(groceries)

for i in range(len(groceries)):
    print("index ", i, "value ", groceries[i])

groceries.remove("milk")
for i in range(len(groceries)):
    print("index ", i, "value ", groceries[i])

#groceries.remove("milk") program crashes because it's not there

groceries.pop(3)
print(groceries)
