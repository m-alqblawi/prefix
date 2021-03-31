class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []  # if empty rerurn 1  else 0

    def push(self, item):
        self.items.append(item)

    # OR
    # def push (self, item):
    #     self.items.insert(0, item)

    def pop(self):  # Give error if the stack empty
        return self.items.pop()

    # OR
    # def pop (self):
    #     return self.items.pop(0)

    # like pop but but don't move or take any element but just returns elements. 
    def peek(self):  # Give error if the stack empty
        return self.items[len(self.items) - 1]
        # OR

    # def peek(self):
    #     return self.items[0] 
    def size(self):
        return len(self.items)
