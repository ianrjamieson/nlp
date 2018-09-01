import sqlite3

conn = sqlite3.connect('database.sqlite')

cursor = conn.execute("SELECT body FROM May2015 WHERE score > 5000")
output = ""
for row in cursor:
    output = output + row[17]

with open('result.text', 'w') as file:
    file.write(output)
    

