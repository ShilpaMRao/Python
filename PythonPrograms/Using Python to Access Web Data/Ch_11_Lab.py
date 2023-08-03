import re

fileHandle = open ("regex_sum_1853211.txt")

count = 0
total = 0

for line in fileHandle:
    line = line.rstrip()
    x = re.findall('[0-9]+',line); # checks for decimal digits
    for num in x:
        print(num)
        count = count +1
        total = total + int(num)
print("Number of values : ",count)
print("Total of the numbers :", total)
    
