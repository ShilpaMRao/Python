import sqlite3
import re

conn = sqlite3.connect('orgcountdb.sqlite')
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS Counts")

cur.execute('''CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input("Enter file name: ")

if len(fname) < 1:
    fname = 'mbox.txt'

fh = open(fname)

org_counts = {}

for line in fh:
    # Skip empty lines
    if line.strip() == '':
        continue
    
    # Extract email addresses with '@' or domain names without '@'
    org_list = re.findall(r'@(\S+)|(?:\b\w+\.)+\w+', line)
    for org in org_list:
        # Convert to lowercase for case-insensitive counting
        org = org.lower()
        print(":---->", org)
        org_counts[org] = org_counts.get(org, 0) + 1

for org, count in org_counts.items():
    cur.execute('INSERT INTO Counts (org, count) VALUES (?, ?)', (org, count))

conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC'

for row in cur.execute(sqlstr):
    print(row[0], row[1])

cur.close()
