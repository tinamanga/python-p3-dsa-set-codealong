class MySet:
    def __init__(self,enumerable=[]):
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True

    def has(self, value):
        return value in self.dictionary

    def add(self, value):
        self.dictionary[value] = True
        return self

    def delete(self, value):
        self.dictionary.pop(value, None)
        return self

    def size(self):
        return len(self.dictionary)

    def clear(self):
        self.dictionary.clear()
        return self

    def __str__(self):
        # Creates a comma-separated list of keys
        set_list = [str(key) for key in self.dictionary]
        return f'MySet: {{{", ".join(set_list)}}}'
