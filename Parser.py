# Andrew Xia
# Nov 13 2017
# HTML Parser for FB messages

import datetime
from bs4 import BeautifulSoup

from Message import Message
import SetupDB # a bit messy but...
dbName = SetupDB.dbName
del SetupDB
from DatabaseManager import DatabaseManager

class MessengerParser():

  def __init__(self,filename):
    self.filename = filename
    self.participants = []
    self.messages = [] # is an array the correct data strux?
    self.dbManager = DatabaseManager(dbName)

  def parse(self):
    print "parsing " + self.filename
    dataname = "data/messages/" + self.filename + ".html"
    data = open(dataname, "r").read()
    self.soup = BeautifulSoup(data, 'html.parser')

    self.__updateParticipants(str(self.soup.title.get_text()))

    # print(self.soup.prettify())

    messages = self.soup.find_all('div', class_ = 'message')

    for m in reversed(messages):
      # get messages in chronological order
      user = m.find('span', class_ = 'user').get_text()
      time = m.find('span', class_ = 'meta').get_text()
      time = self.__parseTimestamp(time)
      text = m.next_sibling.get_text()
      self.messages.append(Message(user,time,text))

  def __updateParticipants(self,peopleStr):
    conv = "Conversation with "
    if peopleStr.find(conv) != 0:
      raise("Title not consistent")

    peopleStr = peopleStr[len(conv):]
    self.participants = peopleStr.split(", ")

  def __parseTimestamp(self, timestamp_string):
    # TODO: which timezone?
    return datetime.datetime.strptime(timestamp_string, '%A, %B %d, %Y at %I:%M%p %Z')

  def insertIntoDB(self):
    # insert self.messages [] into a db titled by self.filename
    self.dbManager.insertIntoConversations(
      self.filename,
      "fbmes",
      "; ".join(self.participants)
      )
    self.dbManager.insertMessages(
      self.filename,
      self.messages)

  def printMessages(self):
    for message in self.messages:
      print message

if __name__ == '__main__':
  message = "10208511297112180" # test; Juju thread
  # message = "1180098468702450" # a group thread
  message = "455947847896220" #cws

  parser = MessengerParser(message)
  parser.parse()

  # parser.printMessages()
  parser.insertIntoDB()
