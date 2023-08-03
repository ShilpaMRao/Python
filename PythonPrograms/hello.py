fname = input("Enter a file : ")
try:
    fhandle = open(fname)
except:
    print("File can't be opened.", fname)
    quit()

count = 0
for line in fhandle:
    count = count + 1

print("Line Count : ", count)
