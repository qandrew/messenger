# Andrew Xia
# Nov 13 2017
# HTML Parser for FB messages

from Message import Message
from HTMLParser import HTMLParser
import datetime
from bs4 import BeautifulSoup

# class MessageParser(HTMLParser):

#   def __init__(self):
#     HTMLParser.__init__(self)
#     self.participants = []
#     self.messages = []

#   def handle_starttag(self, tag, attrs):
#     print "Encountered a start tag:", tag

#   def handle_endtag(self, tag):
#     print "Encountered an end tag :", tag

#   def handle_data(self, data):
#     print "Encountered some data  :", data

class DataManager():

  def __init__(self,filename):
    self.filename = filename
    self.participants = []
    self.messages = [] # is an array the correct data strux?

  def parse(self):
    data = open(self.filename, "r").read()
    self.soup = BeautifulSoup(data, 'html.parser')

    # print(self.soup.prettify())

    messages = self.soup.find_all('div', class_ = 'message')

    for m in messages:
      # metadata
      user = m.find('span', class_ = 'user').get_text()
      time = m.find('span', class_ = 'meta').get_text()
      time = self.__parse_timestamp(time)
      text = m.next_sibling.get_text()
      self.messages.append(Message(user,time,text))

  def __parse_timestamp(self, timestamp_string):
    # TODO: which timezone?
    return datetime.datetime.strptime(timestamp_string, '%A, %B %d, %Y at %I:%M%p %Z')

  def print_messages(self):
    for message in self.messages:
      print message



if __name__ == '__main__':
  message = "data/messages/10208511297112180.html" # test; Juju thread

  dataManager = DataManager(message)
  dataManager.parse()

  dataManager.print_messages()
  # dataManager.run()

  # data = open(message, "r").read()

  # soup = BeautifulSoup(data, 'html.parser')

  # print(soup.prettify())