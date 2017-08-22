# Write a small program to ask for a name and an age.
# When both values have been entered, check if the person
# is the right age to go on an 18-30 holiday (they must be
# over 18 and under 31).
# If they are, welcome them to the holiday, otherwise print
# a message refusing them entry.

Name = input("What is your name? ")
age = int(input("What is your age? {} ".format(Name)))

if 18 < age < 30:
    print("You are welcome to the party {}".format(Name))
else:
    print("You are not old enough to come {}".format(Name))