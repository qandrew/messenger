# Andrew Xia
# Nov 13 2017
# message

class Message:
    def __init__(self, user, timestamp, text):
        self.user = user
        self.timestamp = timestamp
        self.text = text

    def __str__(self):
        return str(self.timestamp) + '; ' + self.user.encode('utf-8') + ': ' + self.text.encode('utf-8')
    
    def __eq__(self, other):
        return (self.user, self.timestamp, self.text) == (other.user, other.timestamp, other.text)

    def __ne__(self, other):
        return not self.__eq__(other)

    # Splits message by whitespace and newline and returns list of words in message
    def words(self):
        return re.split('[ \n]+', self.text)