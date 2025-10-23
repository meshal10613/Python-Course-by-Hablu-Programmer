# int type data
Meshal = 25
# print(type(Meshal)) #type check with type()

# float type data
hello = 1.0613
# print(type(hello))

# complex type data
com = 1j  # only j in last will work for complex type
# print(type(com))

# concat variable
yourName = "Eshan"
myName = "Meshal"
# print(yourName + myName)
# print("My name is" + " " + myName)

# bool type data
Bool = True
# print(Bool)

x = 8
y = 10
# print(x > y)

# text formating
num1 = 20
num2 = 50
# print(f"this the sum {num1 + num2}")  # need to write f before the the string

# binary type data bytes
binaryList = [1, 2, 3, 4, 5, 255]  # min 0/ max 255
b = bytes(binaryList)  # bytes immutable
# print(b)

# binary type data byteArray
bytearrayList = [1, 2, 3, 4, 5, 255]  # min 0/ max 255
b1 = bytearray(bytearrayList)  # bytearray mutable
b1[0]  # 0 no index
# print(b1)

# none type data
x = None
# print(type(x))

# sequence type data 3- list, tuple, range
# list / mutable (changeable)
li = ["One", "Two", "Three"]
# print(li)

# tuple / immutable (unchangeable)
tup = ("One", "Two", "Three")
# print(tup)

# rangle
ran = range(6)
print(ran)

for i in ran:
    print(i)
