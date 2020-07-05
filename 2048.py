# this is my first attempt at creating the game 2048 from memory
import random


# the 2048 board and its mechanics
class Board:
    grid = []
    chance_spawn_2 = 0.9

    # creates an empty board, then generates 2 tiles on it
    def initialize(self):
        random.seed()

        for x in range(16):
            self.grid.append(0)
        self.generate()
        self.generate()

    # displays the board
    def display(self):
        print(self.grid[0:4])
        print(self.grid[4:8])
        print(self.grid[8:12])
        print(self.grid[12:16])
        print()

    # generates either a 2 or 4 and returns true if grid has open tiles, returns false otherwise
    def generate(self):
        empty_tiles = self.grid.count(0)
        if empty_tiles == 0:
            self.display()
            return False
        else:
            if random.random() < self.chance_spawn_2:
                num = 2
            else:
                num = 4
            choose = int(random.random() * empty_tiles)
            index = 0
            while index < len(self.grid):
                if self.grid[index] == 0:
                    if choose == 0:
                        self.grid[index] = num
                        self.display()
                        return True
                    else:
                        choose -= 1
                index += 1

    # moves all tiles to upmost position
    def move_up(self):
        l1 = []
        l2 = []
        l3 = []
        l4 = []
        for x in range(4):
            l1.append(self.grid[4 * x])
            l2.append(self.grid[1 + 4 * x])
            l3.append(self.grid[2 + 4 * x])
            l4.append(self.grid[3 + 4 * x])

        if self.check(l1, -1) or self.check(l2, -1) or self.check(l3, -1) or self.check(l4, -1):
            self.move(l1)
            self.move(l2)
            self.move(l3)
            self.move(l4)
            for x in range(4):
                self.grid[4 * x] = l1[x]
                self.grid[1 + 4 * x] = l2[x]
                self.grid[2 + 4 * x] = l3[x]
                self.grid[3 + 4 * x] = l4[x]
            self.generate()

    # moves all tiles to downmost position
    def move_down(self):
        l1 = []
        l2 = []
        l3 = []
        l4 = []
        for x in range(4):
            l1.append(self.grid[12 - 4 * x])
            l2.append(self.grid[13 - 4 * x])
            l3.append(self.grid[14 - 4 * x])
            l4.append(self.grid[15 - 4 * x])
        if self.check(l1, -1) or self.check(l2, -1) or self.check(l3, -1) or self.check(l4, -1):
            self.move(l1)
            self.move(l2)
            self.move(l3)
            self.move(l4)
            for x in range(4):
                self.grid[12 - 4 * x] = l1[x]
                self.grid[13 - 4 * x] = l2[x]
                self.grid[14 - 4 * x] = l3[x]
                self.grid[15 - 4 * x] = l4[x]
            self.generate()

    # moves all tiles to leftmost position
    def move_left(self):
        l1 = []
        l2 = []
        l3 = []
        l4 = []
        for x in range(4):
            l1.append(self.grid[x])
            l2.append(self.grid[4 + x])
            l3.append(self.grid[8 + x])
            l4.append(self.grid[12 + x])
        if self.check(l1, -1) or self.check(l2, -1) or self.check(l3, -1) or self.check(l4, -1):
            self.move(l1)
            self.move(l2)
            self.move(l3)
            self.move(l4)
            for x in range(4):
                self.grid[x] = l1[x]
                self.grid[4 + x] = l2[x]
                self.grid[8 + x] = l3[x]
                self.grid[12 + x] = l4[x]
            self.generate()

    # moves all tiles to rightmost position
    def move_right(self):
        l1 = []
        l2 = []
        l3 = []
        l4 = []
        for x in range(4):
            l1.append(self.grid[3 - x])
            l2.append(self.grid[7 - x])
            l3.append(self.grid[11 - x])
            l4.append(self.grid[15 - x])
        if self.check(l1, -1) or self.check(l2, -1) or self.check(l3, -1) or self.check(l4, -1):
            self.move(l1)
            self.move(l2)
            self.move(l3)
            self.move(l4)
            for x in range(4):
                self.grid[3 - x] = l1[x]
                self.grid[7 - x] = l2[x]
                self.grid[11 - x] = l3[x]
                self.grid[15 - x] = l4[x]
            self.generate()

    # helper function that combines adjacent numbers and adjusts size of list
    def move(self, moved_numbers):
        while moved_numbers.count(0) != 0:
            moved_numbers.remove(0)
        if len(moved_numbers) == 0:
            for y in range(4):
                moved_numbers.append(0)
        else:
            prev = moved_numbers[0]
            for y in range(len(moved_numbers) - 1):
                if prev == moved_numbers[y + 1]:
                    moved_numbers[y] *= 2
                    moved_numbers.pop(y + 1)
                    moved_numbers.append(0)
                    prev = 0
                else:
                    prev = moved_numbers[y + 1]
        for y in range(4 - len(moved_numbers)):
            moved_numbers.append(0)

    def check(self, lst, prev):
        if len(lst) == 0:
            return False
        elif lst[0] == 0:
            return lst.count(0) != len(lst)
        elif lst[0] == prev:
            return True
        else:
            return self.check(lst[1:], lst[0])

# Prints out menu options
def menu():
    print("What would you like to do?")
    print("1. Move Up")
    print("2. Move Down")
    print("3. Move Left")
    print("4. Move Right")
    print("5. Start a New Board")
    print("6. Quit")


run = True
game = Board()
game.initialize()
while run:
    menu()
    option = int(input())
    if option == 1:
        game.move_up()
    elif option == 2:
        game.move_down()
    elif option == 3:
        game.move_left()
    elif option == 4:
        game.move_right()
    elif option == 5:
        game = Board()
        game.initialize()
    elif option == 6:
        run = False
