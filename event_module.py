class Event():
    '''Representation of a single calendar event.'''
    
    def __init__(self, title, start_date, end_date=None, location='', note=''):
        '''Initialize attributes.'''
        self.title = title
        self.start_date = start_date
        self.end_date = end_date
        self.location = location
        self.note = note

    def display_attributes(self, *attributes):
        '''Display specified attribute(s).'''
        for attribute in attributes:
            print(self.attribute)

    def edit_attribute(self, **attributes):
        '''Edit specified attribute(s).'''
        for attribute in attributes:
            self.attribute = attributes[attribute]


event1 = Event('mazury', 'pon', 'sroda')
