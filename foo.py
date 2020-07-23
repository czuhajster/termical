class Haha:
    '''A simple class.'''
    i =12345

    def go(self):
        print("haha")

haha = Haha()
print(f"{haha.i}, {haha.go}")
print(f"{haha.__doc__}")



sentence = ['My', 'name', 'is', 'Arek']

def list_to_string(list_to_convert):
    for item in list_to_string:
        yield item

converted = ' '
converted = converted.join(sentence)
print(converted)

sentence_1 = 'Arek'

converted = ' '
converted = converted.join(sentence_1)
print(converted)
