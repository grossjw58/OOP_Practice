'''
We're going to build hit-box logic for our game step by step, starting with a simple Rectangle.

Complete the __init__() method. Configure the class to have properties matching the variables passed into the constructor in this order:

x1
y1
x2
y2
'''

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2