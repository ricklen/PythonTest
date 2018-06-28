import os
import csv

fpath = os.path.join('C:\\Users\Rick Lenderink\Documents', "testFile.txt")
csvpath = os.path.join('C:\\Users\Rick Lenderink\Documents', "testCsv.csv")


temp = open(fpath).read().splitlines()

# for element in temp:
#     print(element)

with open(csvpath, "w", newline='') as f:
    writer = csv.writer(f)
    for element in temp:
        writer.writerow([element])




