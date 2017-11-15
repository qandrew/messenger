# Andrew Xia
# Nov 14 2017
# Sqlite database setup
# attempting to follow design/Database.md

import sqlite3
from datetime import datetime, date

dbName = 'db/test.db'

if __name__ == '__main__':

  conn = sqlite3.connect(dbName)

  c = conn.cursor()

  # Create table
  c.execute('''CREATE TABLE IF NOT EXISTS conversations
               (id integer primary key,
               platform text,
               participants text,
               unique(id))''')

  # Insert a row of data
  c.execute("INSERT INTO conversations VALUES (1,'test','Andrew Xia; Simon Zheng')")

  # TODO: maybe autoincrement is bad
  c.execute('''CREATE TABLE IF NOT EXISTS m1
               (id integer primary key autoincrement,
               message text,
               sender text,
               ts time,
               attachment text,
               unique(id))''')

  d = date(2000,1,1)

  # Insert a row of data
  c.execute("INSERT INTO m1 (message, sender, ts, attachment) VALUES (?,?,?,?)", ('hello world','Simon Zheng',d,""))

  # Save (commit) the changes
  conn.commit()

  # We can also close the connection if we are done with it.
  # Just be sure any changes have been committed or they will be lost.
  conn.close()