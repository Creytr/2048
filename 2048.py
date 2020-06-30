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

    # generates either a 2 or 4 and returns true if grid has open tiles, returns false otherwise
    def generate(self):
        empty_tiles = self.grid.count(0)
        if empty_tiles == 0:
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
                        return True
                    else:
                        choose -= 1
                index += 1

    # displays the board
    def display(self):
        print(self.grid[0:4])
        print(self.grid[4:8])
        print(self.grid[8:12])
        print(self.grid[12:16])

    # moves all tiles to upmost position
    def move_up(self):
        for x in range(4):
            list = []
            for y in range(4):
                if self.grid[x + y * 4] != 0:
                    list.append(self.grid[x + y * 4])
                    
            for


game = Board()
game.initialize()
game.display()

print("ded")

game.generate()
game.display()