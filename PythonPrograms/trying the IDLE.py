fname = input("Enter file name: ")
fh = open(fname)

lst = list()
final = list()
for line in fh:
    print(line)
    line.rstrip()
    lst = line.split()
    print("list : ",lst)
    for word in lst:
        if word in final:
            continue
        else:
            final.append(word)

final.sort()
print(final)
