"""
    Stack ADT represented as a (shallow) list
    John Dougherty & Dave Wonnacott   Haverford College
    
An imperative-style stack, as per the textbook and every other reference.

Examples:

>>> s = Stack()
>>> s.push('bottom')   # push(s, 'bottom')
>>> s.push('middle')
>>> s.push('top')
>>> s.pop()
'top'
>>> s.pop()
'middle'
>>> s.push('new middle')
>>> s.empty()
False
>>> s.pop()
'new middle'
>>> s.pop()
'bottom'
>>> s.empty()
True
"""

class Stack:
    # constructor (empty stack)
    def __init__(self):
        self.rep = []
        
    def __repr__(self):
        return str(self.rep)

    def empty(self):
        return self.rep == []

    def push(self, v):
        self.rep.append(v)

    def pop(self):
        return self.rep.pop()
     
    def __len__(self):
        counter = 1
        for i in range(len(self.rep)-1):
            counter = counter + 1
        return counter

# mostly copied from  http://docs.python.org/lib/module-doctest.html
def _test():
    import doctest
    result = doctest.testmod()
    # print "Result of doctest is:", result
    if result[0] == 0:
        print "Wahoo! Passed all", result[1], "tests!"
    else:
        print "Rats!"

if __name__ == "__main__":
    _test()
