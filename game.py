import pprint
import random

LETTERS = ['A', 'B', 'C', 'D']#, 'E', 'F']

class Element:
    def __init__(self, x, y, letter):
        self.x = x
        self.y = y
        self.letter = letter
        self.burst = False
        self.friends = []

    def destroy(self):
        self.burst = False
        self.letter = " "

    def __repr__(self):
        if self.burst:
            return "{}{}".format(self.letter, '*').ljust(2)
        else:
            return "{}".format(self.letter).ljust(2)

class Grid:
    def __init__(self, height, width, elements):
        self.height = height
        self.width = width
        self.elements = elements
        self.grid = [[Element(y, x, random.choice(self.elements)) for x in range(width) ] for y in range(height)]

    def clean(self):
        for row in self.grid:
            for element in row:
                self.valid_y(element)
                #self.remove_friends()
                self.valid_x(element)

        self.show()

    def fill_elements(self):
        for row in self.grid:
            for element in row:
                self.fill_element(element)

        self.show()


    def fill_element(self, element):
        if element.letter == " ":
            element.letter = random.choice(self.elements)

    def burst_elements(self):
        for row in self.grid:
            for element in row:
                if element.burst:
                    element.destroy()

        self.show()

    def mark_two_friends(self):
        for row in self.grid:
            for element in row:
                if element.friends > 2:
                    element.burst = True

    def valid_y(self, element):
        if len(element.friends) > 2:
            for friend in element.friends:
                friend.burst = True

            element.burst = True

            return

        for point_x in [element.x -1, element.x + 1]:
            potential = self.safe_element(point_x, element.y)
            if potential and potential.letter == element.letter:
                element.friends += [potential]
                #print "hello"
                self.valid_y(potential)
            else:
                return

    def valid_x(self, element):
        if len(element.friends) > 2:
            for friend in element.friends:
                friend.burst = True

            return

        for point_y in [element.y -1, element.y + 1]:
            #print point_y
            potential = self.safe_element(element.x, point_y)
            #print potential
            if potential and potential.letter == element.letter:
                element.friends += [potential]
                #print "hello"
                self.valid_x(potential)
            else:
                return

    def safe_element(self, x, y):
        # ignore negative numbers
        if x < 0 or y < 0:
            return None

        try:
            element = self.grid[x][y]
            return element
        except IndexError:
            return None

    def remove_friends(self):
        for row in self.grid:
            for element in row:
                element.friends = []
                element.burst = False

    def on_grid(self, element):
        try:
            self.grid[element.x][element.y]
            return True
        except IndexError:
            return False

    def has_burstable_elements(self):
        for row in self.grid:
            for element in row:
                if element.burst:
                    return True

        return False

    def show(self):
        pprint.pprint(self.grid)

grid = Grid(6,6, LETTERS)
#grid.show()
counter = 0
while True:
    if counter == 5:
        break 

    grid.clean()
    if grid.has_burstable_elements():
        counter +=1
        #grid.clean()
        grid.burst_elements()
        grid.fill_elements()
        grid.remove_friends()
        #grid.clean()
    else:
        break

