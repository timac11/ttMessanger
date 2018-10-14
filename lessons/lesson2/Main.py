from Item import Item as item

item1 = item(1)
item2 = item(1)
item3 = item1

print(item1 == item2)
print(item1 == item1)
print(item1 is item3)
print(item1 == item3)

list1 = [None]
print(list1[0])