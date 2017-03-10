import sqlite3

conn = sqlite3.connect('store.db')

# conn.execute("delete from MailingList")
# conn.commit()

d = conn.execute("select * from MailingList")
for row in d:
    print row[0], " ", row[1], " ", row[2]
