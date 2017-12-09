number = "9,342,654,254,67,4563,5"
cleanedNumber = ''

# augmented assignment is het gebruik van += om iets aan de list te appenden
# other possibility is -= /= *=
for i in range(0, len(number)):
    if number[i] in '0123456789':
        cleanedNumber += number[i]

newNumber = int(cleanedNumber)
print("the number is {}".format(newNumber))

x = 23
x += 1

print(x)

x -= 4

print(x)

x *= 5

print(x)

x /= 4

print(x)
# ** is to the power of
x **= 2

print(x)
# %= is the remainder of
x %= 60
print(x)

greeting = "good "
greeting += "morning "
print(greeting)

greeting *= 5

print(greeting)