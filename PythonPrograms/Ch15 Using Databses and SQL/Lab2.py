import sqlite3
import re

conn = sqlite3.connect('orgcountdb.sqlite')
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS Counts")

cur.execute('''CREATE TABLE Counts (org VARCHAR, count INTEGER)''')

fname = input("Enter file name : " )


if(len(fname) <  1): fname = 'mbox.txt'

fh = open(fname)

for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    org = re.findall(r'@(\S+)', email)
    print(org[0]) # org comes in the form "['gmail.com']". So to  extract only the gmail.com part we have to use org[0]

    cur.execute('SELECT count FROM Counts WHERE org = ?', (org[0],))
    row = cur.fetchone()

    if row is None:
        cur.execute('''INSERT INTO Counts (org,count) VALUES (?,1)''',(org[0],))
    else:
        cur.execute('''UPDATE Counts SET count = count + 1 WHERE org = ?''',(org[0],))

    conn.commit()
#https://www.sqlite.org/lang_select.html

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC'

for row in cur.execute(sqlstr):
    print(str(row[0]),row[1])

cur.close()
          
                    

    
