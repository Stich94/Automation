my_list = [1, 2, 3, 4, 5, 6, 6]
counter = 0

for i in my_list:
    counter += 1

print(counter)


for i in range(0, 100):  # exclusive max number - up to 99 in this case
    print(i)

# step is now set to two - 2, 4, 6...
for _ in range(0, 10, 2):
    print(_)

# when we want to step back we need -1
for _ in range(10, 0, -1):
    print(_)

# if we want to reverse and include steps we need -2
for _ in range(10, 0, -2):
    print(_)


# enumerate
for i, char in enumerate("Helllloooo"):
    print(i, char)

# output
# 0 H
# 1 e
# 2 l
# 3 l
# 4 l
# 5 l
# 6 o
# 7 o
# 8 o
# 9 o

for i, char in enumerate(list(range(100))):
    if char == 50:
        print(f"index of 50 is: {i}")

i = 0
while i < len([1, 3, 5]):
    print(i)
    i += 1
