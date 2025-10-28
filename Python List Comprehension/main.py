# list comprehension------------------
fruits = ["apple", "banana", "cherry", "mango", "lemon"]
newFruits = []

for x in fruits:
    if "a" in x:
        newFruits.append(x)

# print(newFruits)

li = [1, 2, 3, 4, 5]
newLi = []

for x in li:
    x = x * 2
    newLi.append(x)

Double = [i * 2 for i in li]

# print(Double)

# List sorting
# fruits.sort()  # ascending through alphanumerically
# fruits.sort(reverse=True) #descending through alphanumerically
# fruits.reverse() # reverse the list
# print(fruits)



# copy list--------------------
# coppiedLi = fruits.copy()
# newCopy = list(fruits)
# anotherCopy = fruits[:]
# print(anotherCopy)

# Join 2 Lists-----------------
num1 = [1, 2, 4]
num2 = [3, 5, 6]
# print(num1[-1]) #access the last item in the list
# num3 = num1 + num2
num1.extend(num2) # combine 2 list in 1
# print(num1)

# List Excersize----------------------
