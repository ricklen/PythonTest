# listOne = []
# listTwo = list()
#
# print("list 1: {}".format(listOne))
# print("list 2: {}".format(listTwo))
#
# if listOne == listTwo:
#     print("The lists are equal")
#
# print(list("The lists are equal"))

even = [2, 4, 6, 8]

# another_even = even
# print(even is another_even)
# # this function is called on the original even, actually on both because another_even refers to even
# another_even.sort(reverse=True)
# print(even)

odd = [1, 3, 5, 7, 9]

numbers = [even, odd]

for numberset in numbers:
    print(numberset)
    for value in numberset:
        print(value)