# Andrew

import sqlite3
import sys

class DatabaseManager():
  def __init__(self, dbName):
    self.dbName = dbName
    self.active = False

  def insertIntoConversations(self,id,platform,participants):
    # create a row in conversations signifying the new table
    # and create a new table with name m + id
    try:
      conn = sqlite3.connect(self.dbName)
      c = conn.cursor()
      c.execute("REPLACE INTO conversations VALUES (?,?,?)",
        (int(id),platform,participants))

      query = "CREATE TABLE IF NOT EXISTS m" + id
      query2 = ''' (id integer primary key autoincrement,
               message text,
               sender text,
               ts time,
               attachment text,
               unique(id))'''
      query = query + query2
      c.execute(query)

      conn.commit()
      conn.close()
    except:
      print "Unexpected error:", sys.exc_info()[0]
      raise

  def insertMessages(self,id,messages):
    # insert all messages into table with name m + id
    # TODO: check duplicates?
    try:
      conn = sqlite3.connect(self.dbName)
      c = conn.cursor()

      for m in messages:
        query = "INSERT INTO m" + id + " (message, sender, ts, attachment) VALUES (?,?,?,?)"
        c.execute(query, (m.text, m.sender, m.ts,""))

      conn.commit()
      conn.close()
    except:
      print "Unexpected error:", sys.exc_info()[0]
      raise

  def getMessages(self,id):
    # get messages
    pass

  def deleteMessages(self,id):
    # delete the message and its corresponding value inside conversations
    try:
      conn = sqlite3.connect(self.dbName)
      c = conn.cursor()

      query = "DROP TABLE m" + id
      c.execute(query)

      query = "DELETE from conversations where id =?"
      c.execute(query,(id))

      conn.commit()
      conn.close()
    except:
      print "Unexpected error:", sys.exc_info()[0]
      raise

  def getCursor(self):
    conn = sqlite3.connect(self.dbName)
    return conn.cursor()
