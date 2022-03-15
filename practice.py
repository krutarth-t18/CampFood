'''lst1 = []

lst = [1, 2, 3, [4, 5], [-1, [-2, -4]]]

def check_list(lst):
    if type(lst) is list:
        for i in lst:
            check_list(i)
    else:
        lst1.append(lst)


for i in lst:
    if type(i) is list:
        check_list(i)
    else:
        lst1.append(i)
print(lst1)
'''

# lst1 = ["hey", "bye", "hey", "bye"]
# lst2 = ['hello' if x == 'hey' else 'cya' for x in lst1]
#
# print(lst2)


# votes = ["ABC", "ACB", "ABC", "ACB", "ACB"]
# # Output: "ACB"
# st = ""
# lst = []

# def word_to_char(st):


# for word in votes:
#     st += word  # "ABC"
#     for i in st:
#         lst += [i]
#     st = ""
# print(lst)

# A = []
# B = []
# C = []
# for i in range(len(lst)):
#     x = 0
#     y = 3
#     for j in range(0, 3):
#         index = lst[j]
#         # myList.index(myNum)
#         x = y
#         y += 3
#
#
# a = [1, 2, 3, 4]


for i in range(1,6):
    for j in range(1,i+1):
        print(j, end="")
    print()