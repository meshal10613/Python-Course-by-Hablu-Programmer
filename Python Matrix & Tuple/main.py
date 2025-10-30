# Matrix-----------------------
li = [
    [1, 2, 3, 4, 5], 
    [6, 7, 8, 9, 10],
    15
]

# print(li[0][1])

# Tuples-----------------------
myTuple = ("Apple", "Banana", "Cherry", "Jackfruit")
apple = myTuple[0] #access tuple with index
jackfruit = myTuple[-1] #access the last item of the tuple with -index
rangeAccess = myTuple[1: 3] # that means index 1 to index 3 - 1 = 2
# print(rangeAccess)


# Update Tuples----------------
# 1st Convert into a list
thisTuple = (1, 2, 3, 4)
y = list(thisTuple)
y.append(5)
newTuple = tuple(y)
# print(newTuple)

# 2nd add tuple to a tuple
anotherTuple = (5,)
thisTuple += anotherTuple
# print(thisTuple)

# Unpack Tuple-----------------
fruits = ("Apple", "Banana", "Cherry")
(a, b, c) = fruits # need to structure all
(apple, *others) = fruits # if use *,Remaining all items will be in there
print(others) 