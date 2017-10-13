number = "9,435,354,345,345345,353"
cleanedNumber = ''

for char in number:
    if char in '123456789':
        cleanedNumber = cleanedNumber + char

newNumber = int(cleanedNumber)

print("The new number is {}".format(newNumber))

for state in ("not pinin", "no more", "a stiff", "benefit of life"):
    print("This parrot is " + state)
    # or print("This parrot is {}".format(state))

for i in range(0, 100, 5):
    print("i is {}".format(i))

for i in range(1, 13):
    for j in range (1, 13):
        print("{0} times {1} is {2}".format(i, j, i*j), end='\t')
    #print("=============
    print("")

