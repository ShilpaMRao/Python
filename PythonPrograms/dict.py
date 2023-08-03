name = input("File Name : ")
handle = open(name)
counts = dict()
for line in handle:
    
    if line.startswith("From:"):
        words = line.split()
        sender = words[1]
        counts[sender] = counts.get(sender,0)+1


bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
             bigword = word
             bigcount = count
print(bigword,bigcount)        
