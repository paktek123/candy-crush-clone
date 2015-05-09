import pprint
import random

LETTERS = ['A', 'B', 'C']

class Element:
    def __init__(self, x, y, letter):
        self.x = x
        self.y = y
        self.letter = letter
        self.burst = False
        self.friends = []

    def __repr__(self):
        if self.burst:
            return "{}{}".format(self.letter, '*').ljust(2)
        else:
            return "{}".format(self.letter).ljust(2)

class Grid:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.grid = [[Element(y, x, random.choice(LETTERS)) for x in range(width) ] for y in range(height)]

    def clean(self):
        for row in self.grid:
            for element in row:
                self.valid(element)

        self.show()


    def valid(self, element):
        if len(element.friends) > 2:
            for friend in element.friends:
                friend.burst = True

            return

        for point_x in [element.x -1, element.x + 1]:
            potential = self.safe_element(point_x, element.y)
            if potential and potential.letter == element.letter:
                element.friends += [potential]
                #print "hello"
                self.valid(potential)
            else:
                return

    def safe_element(self, x, y):
        try:
            element = self.grid[x][y]
            return element
        except IndexError:
            return None

    def on_grid(self, element):
        try:
            self.grid[element.x][element.y]
            return True
        except IndexError:
            return False

    def show(self):
        pprint.pprint(self.grid)

grid = Grid(6,6)
grid.show()
grid.clean()

