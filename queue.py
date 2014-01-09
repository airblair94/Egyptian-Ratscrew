"""
    Queue ADT represented as a (shallow) list
    John Dougherty & Dave Wonnacott   Haverford College
    
An imperative-style queue, as per the textbook and every other reference.

Examples:

>>> q = Queue()
>>> q.put('first')
>>> q.put('second')
>>> q.put('third')
>>> # or, equivalently, q = Queue(['first', 'second', 'third'])
>>> q.get()
'first'
>>> q.get()
'second'
>>> q.put('fourth')
>>> q.empty()
False
>>> q.get()
'third'
>>> q.get()
'fourth'
>>> q.empty()
True
>>> g = Queue()
>>> g.put('hi')
>>> g.put('hello')
>>> g
['hi', 'hello']
>>> len(g)
2
>>> print g
['hi', 'hello']
"""

class Queue:
    # constructor (queue, with a list of stuff )
    def __init__(self, initial_list=[]):
        self.rep = initial_list
        
    def __repr__(self):
        return str(self.rep)

    def empty(self):
        return self.rep == []

    def put(self, v):
        self.rep.append(v)

    def get(self):
        return self.rep.pop(0)
    
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
