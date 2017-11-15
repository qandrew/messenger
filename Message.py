# Andrew Xia
# Nov 13 2017
# message

class Message:
    def __init__(self, sender, ts, text):
        self.sender = sender
        self.ts = ts #timestamp
        self.text = text

    def __str__(self):
        return str(self.ts) + '; ' + self.sender.encode('utf-8') + ': ' + self.text.encode('utf-8')
    
    def __eq__(self, other):
        return (self.sender, self.ts, self.text) == (other.sender, other.ts, other.text)

    def __ne__(self, other):
        return not self.__eq__(other)

    # Splits message by whitespace and newline and returns list of words in message
    def words(self):
        return re.split('[ \n]+', self.text)