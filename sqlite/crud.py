
# A crud example in memory using sqlite and python

import sqlite3

users = [(1, 'John'),(2, 'Frank'),(3, 'Claire')]

db = sqlite3.connect(':memory:')

#Create Example
cursor = db.cursor()
cursor.execute(''' CREATE TABLE users(id INTEGER PRIMARY KEY, name varchar(20))''')
cursor.executemany(''' INSERT INTO users(id, name) VALUES(?,?)''', users)
db.commit()

#Read Example
print("Three rows inserted")
cursor.execute('''SELECT * FROM users ''')

resultSet = cursor.fetchall()
for row in resultSet:
    print('{0} : {1}'.format(row[0], row[1]))

#Update Example
print("\nrow 1 updated")
new_user = ['Dimitri', 1]
cursor.execute("UPDATE users SET name = '%s' WHERE id = 1 " % new_user[0])


cursor.execute('''SELECT * FROM users ''')
resultSet = cursor.fetchall()
for row in resultSet:
    print('{0} : {1}'.format(row[0], row[1]))

#Delete Example
print("\nrow 1 deleted")
cursor.execute("DELETE from users WHERE id = %d" % 1)

cursor.execute('''SELECT * FROM users ''')
resultSet = cursor.fetchall()
for row in resultSet:
    print('{0} : {1}'.format(row[0], row[1]))

db.close()