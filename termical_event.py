'''This module contains Event class that represents single event in calendar.'''

class Event():
    '''Representation of a single calendar event.'''
    

    def __init__(self, title, start_date, start_time=None, end_date=None,
                 end_time=None, location='', note=''):
        '''Initialize attributes.'''
        self.instance_variables = {}
        self.title = title
        self.instance_variables['title'] = self.title
        self.start_date = start_date
        if start_time:
            self.start_time = start_time
            self.start_date_and_time = self.start_date + ': ' + self.start_time
            self.instance_variables['start date'] = self.start_date_and_time
        elif not start_time:
            self.instance_variables['start date'] = self.start_date
        self.end_date = end_date
        if end_time:
            self.end_time = end_time
            self.end_date_and_time = self.end_date + ': ' + self.end_time
            self.instance_variables['end date'] = self.end_date_and_time
        elif not end_time:
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

    def __next__(self) -> list:
        '''Access one attribute at a time.'''

        '''It returns list that cotains name of the attribute and
        its value.'''
        self.return_list = []
        if self.count == self.index:
            self.count = 0
            raise StopIteration
        self.return_list.append(self.keys[self.count])
        self.return_list.append(self.values[self.count])
        self.count += 1
        return self.return_list

