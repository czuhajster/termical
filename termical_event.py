'''This module contains Event class that represents single event in calendar.'''

class Event():
    '''Representation of a single calendar event.'''
    

    def __init__(self, title, start_date, end_date=None, location='', note=''):
        '''Initialize attributes.'''
        self.instance_variables = {}
        self.title = title
        self.instance_variables['title'] = self.title
        self.start_date = start_date
        self.instance_variables['start date'] = self.start_date
        self.end_date = end_date
        self.instance_variables['end date'] = self.end_date
        self.location = location
        if location:
            self.instance_variables['location'] = self.location
        self.note = note
        if note:
            self.instance_variables['note'] = self.note
        self.id = ''
        # self.instance_variables.append(self.id)
        self.keys = []
        self.values = []
        self.count = 0
        for key, value in self.instance_variables.items():
            self.keys.append(key)
            self.values.append(value)
        self.index = len(self.keys)


    def display_attributes(self, *attributes):
        '''Display specified attribute(s).'''
        for attribute in attributes:
            print(self.attribute)

    def edit_attribute(self, **attributes):
        '''Edit specified attribute(s).'''
        for attribute in attributes:
            self.attribute = attributes[attribute]

    def __iter__(self):
        '''Create an iterator.'''
        return self

    def __next__(self):
        '''Access one element at a time.'''
        self.return_list = []
        if self.count == self.index:
            self.count = 0
            raise StopIteration
        self.return_list.append(self.keys[self.count])
        self.return_list.append(self.values[self.count])
        self.count += 1
        return self.return_list

