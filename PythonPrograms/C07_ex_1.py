fh = open('Using Python to Access Web Data/mbox.txt')

filetext = fh.read()

filetext = filetext.rstrip()
filetext = filetext.upper()

print(filetext)
