import itertools

fibs = [1, 0]

class Fibs:
    def __iter__(self):
        self.cur_val = 0
        self.next_val = 1
        return self
    
    def __next__(self):
        tmp = self.next_val
        self.next_val = self.cur_val + self.next_val
        self.cur_val = tmp
        return tmp
