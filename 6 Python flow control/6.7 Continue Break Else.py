# shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
#
# # continue stops processing any more lines in the block
#
# for item in shopping_list:
#     if item == "spam":
#         continue
#     print("buy " + item)
#
# print("")
#
# # break is quiting the for loop and the program stops running
# for item in shopping_list:
#     if item == "spam":
#         break
#     print("buy " + item)

meal = ["milk", "bacon", "spam", "sausages", "bread", "rice"]
nastyFoodItem = ""

# else in a for loop is also possible
for item in meal:
    if item == "spam":
        nastyFoodItem = item
        break
else:
    print("I'll have a plate of that, then, please")

if nastyFoodItem:
    print("can't i have anything without spam in it")
