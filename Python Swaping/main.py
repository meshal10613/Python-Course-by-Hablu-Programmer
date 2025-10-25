# swaping
a = 50
b = 40
a, b = b, a # swap a to b and b to a
# print(a, b)

# user input
# username = input("Enter your username: ")
# password = input("Enter your password: ")
# # print("My name is", username)
# print(password)

# type casting - str(), float(), int()
roll = 10
newRoll = str(roll)
# print(newRoll)

# List data type
fruits = ["apple", "banana", "lemon"]
fruits[2] = "mango"

# add list item
fruits.append("lemon") # add to the last in the list
fruits.insert(1, "cherry") # add to the given index number location, but didn't remove the previous index
print(fruits)

# remove list item
li = [1, 2, 3, 4, 5, 6]
li.remove(2) # write the specific item to remove
li.pop(3) # remove items through index number and if I didn't write any index number it will remove the last item
del li[0] # also remove through index number and if I didn't write any index number it will remove/delete the entire list
li.clear() # remove all item from the list and it will be empty list []
print(li)