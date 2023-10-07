# variables
lucky_numbers = [4, 8, 17, 60, 24, 67]
friends = ["Joyce", "Eric", "Lewis", "Tim"]
##### list functions ######
# Extend() - adding a list to another
friends.extend(lucky_numbers)
print(friends)

# append() - add an item at the end of a list
friends.append("Joy")
print(friends)

# insert()- add an item ata a specific index in a list
friends.insert(1, "Kim")
print(friends)

# Remove() - remove an item from a list
friends.remove("Eric")
print(friends)

# clear() - remove all items from a list
friends.clear()
print(friends)

# pop() - removes the last item in a list
lucky_numbers.pop()
print(lucky_numbers)

# index() - gets the index of an item. throws an error if item isnt in the list
# print(lucky_numbers.index(20))
print(lucky_numbers.index(60))

# sort() - gives a list in ascending or alphabetical order
lucky_numbers.sort()
print(lucky_numbers)

# reverse() - gives a reverse order of a list (from backwards)
lucky_numbers.reverse()
print(lucky_numbers)

# copy() - creates  copy of an existing list
friends2 = friends.copy()
print(friends2)

lucky_numbers2 = lucky_numbers.copy()
print(lucky_numbers2)
