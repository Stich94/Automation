import mymodule


def highest_num(list):
    highestNum = 0
    for i in list:
        if i > highestNum:
            highestNum = i
    return highestNum


print(highest_num([1, 3, 6, 7, 9, 12, 11, 14, 3, 5]))


def highest_even(list):
    highest_even = 0
    for i in list:
        if i > highest_even and i % 2 == 0:
            highest_even = i
    return highest_even


print(highest_even([1, 3, 6, 7, 9, 2, 6, 23, 35, 12, 45]))


a = "hellllooooo"

# the length of a is stored in n which we can use later
if ((n := len(a)) > 10):
    print(f"too long {n} elements")

while ((n := len(a)) > 1):
    print(n)
    a = a[:-1]  # every time we slice the last element from a

b = 12
print(f"before: {b}")


def globStuff():
    global b
    b += 1


globStuff()
print(b)


def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner: " + x)

    inner()
    print("outer: " + x)


x = "Hello"
x.upper
[0]

if 5 > 2:
    print("Five is greater than two!")


car = {"brand": "Ford"}
print(car["brand"])


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


print(dir(mymodule))
