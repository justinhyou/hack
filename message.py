class Message(object):
    """
       Instance attributes: id
                            title
                            text
    """
    idgenerator = 0

    # Constructors
    def __init__(self, title='', text=''):
        Message.idgenerator = Message.idgenerator + 1
        self.id = Message.idgenerator
        self.title = title
        self.text = text

    # Generating a string representation of a Student object
    def __str__(self):
       return '(%d, %s, %s)' % (self.id, self.title, self.text)
    
    def get_title(self):
        return self.title

    def get_text(self):
        return self.text

    def set_title(self, title):
        self.title = title
        
    def set_text(self, text):
        self.text = text

    def reset(self):
        Message.idgenerator = 0
