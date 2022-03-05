# from ast import If


# picture = [
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 1, 1, 1, 0, 0],
#     [0, 1, 1, 1, 1, 1, 0],
#     [1, 1, 1, 1, 1, 1, 1],
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 1, 0, 0, 0]
# ]

# # for i in range(len(picture)):
# #     for j in range(len(picture[i])):
# #         if j == 0:
# #             j = " "
# #     print(picture[i][j])

# for row in picture:
#     for pixel in row:
#         if pixel == 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print("")  # for a new line after every row

# # output
# #    *
# #   ***
# #  *****
# # *******
# #    *
# #    *

# fill = "$"
# empty = ""
# for row in picture:
#     for pixel in row:
#         if pixel:
#             print(fill, end="")
#             print(fill, end="")
#             print(fill, end="")
#         else:
#             print(empty, end="")
#             print(empty, end="")
#     print("")


# ckeck for dubplicates without using Sets
some_list = ["a", "b", "c", "d", "n", "n", "b", "t"]

duplicates = []

for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

# print only the duplicates
print(duplicates)

print(some_list.count("b"))
