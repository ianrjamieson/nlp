import sqlite3

conn = sqlite3.connect('reddit.db')

cursor = conn.execute("SELECT body FROM May2015 WHERE score > 5000")
output = ""
for row in cursor:
    output = output + cursor
    

