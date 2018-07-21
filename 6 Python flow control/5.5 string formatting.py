age = 24
print("My age is " + str(age) + " years")

print("My age is {0} years".format(age))


print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}".format(31, "january", "march",  "May"
                                                                          , "May", "May", "May", "May"))

print("""January: {2}
February: {0}
March: {1}
""".format(28, 30, 31))

print("My age is %d years" % age)

# %d is for integer and %s is for string
# the use of percentages is mainly used in python 2 and should not really be used in python 3
print("My age is %d %s, %d %s" % (age, "years", 6, "months"))

for i in range(1, 12):
    print("No. %2d squared is %4d and cubed is %4d" % (i, i ** 2, i ** 3))

print("Pi is approximately %12f" % (22 / 7))

print("Pi is approximately %12.50f" % (22 / 7))

# first value between {} is the number of the field and the second number is the width
for i in range(1, 12):
    print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i ** 2, i ** 3))

for i in range(1, 12):
    print("No. {0:2} squared is {1:<4} and cubed is {2:<4}".format(i, i ** 2, i ** 3))

print("Pi is approximately {0:12.50f}".format(22 / 7))



