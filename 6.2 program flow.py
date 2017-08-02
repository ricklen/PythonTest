# name = input("Plz enter your name: ")
#
#
# # integer data conversion
# age = int(input("how old are you, {0}? ".format(name)))
# print(age)
#
# if age >= 18:
#     print("You are old enough to vote")
# else:
#     print("Please come back in {0} years".format(18 - age))

print("Please guess a number between 1 and 10: ")
guess = int(input())

if guess != 5:
    if guess < 5:
        print("Please guess higher")

    else:
        print("please guess lower")
    guess = int(input())
    if guess == 5:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correct")