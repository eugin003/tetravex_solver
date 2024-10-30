import random

class TetravexSolver:
    def __init__(self, size, tiles):
        self.size = size
        self.tiles = tiles
        self.board = [[-1 for _ in range(size)] for _ in range(size)] 
        self.print_board = [[-1 for _ in range(size)] for _ in range(size)]
        self.used_tiles = set()  
        self.solution_found = False
        self.attempts = 0
        self.color_map = {
            0: '\033[91m',  # Red
            1: '\033[92m',  # Green
            2: '\033[93m',  # Yellow
            3: '\033[94m',  # Blue
            4: '\033[95m',  # Magenta
            5: '\033[96m',  # Cyan
            6: '\033[97m',  # White
            7: '\033[31m',  # Dark Red
            8: '\033[32m',  # Dark Green
            9: '\033[36m',  # Teal
        }

    def solve(self):
        attempts = 0
        while not self.solution_found:
            self.attempts += 1
            self.backtrack(0, 0)
            if self.attempts >= 10:
                attempts += 1
                print(f"\033[97mNo solution found after {attempts} attempts.")
                self.attempts = 0
                self.used_tiles.clear()
                self.board = [[-1 for _ in range(self.size)] for _ in range(self.size)]
                self.tiles = [[random.randint(0, 9) for _ in range(4)] for _ in range(self.size ** 2)]

    def is_valid_move(self, row, col, tile):
        if row > 0 and self.board[row - 1][col][2] != tile[0]:
            return False
        if col > 0 and self.board[row][col - 1][1] != tile[3]:
            return False
        return True

    def backtrack(self, row, col):
        if self.solution_found:
            return

        if row == self.size:
            self.solution_found = True
            self.print_solution()
            return

        for tile_index, tile in enumerate(self.tiles):
            if tile_index in self.used_tiles:
                continue

            if self.is_valid_move(row, col, tile):
                self.board[row][col] = tile
                self.used_tiles.add(tile_index)

                if col < self.size - 1:
                    self.backtrack(row, col + 1)
                else:
                    self.backtrack(row + 1, 0)

                if self.solution_found:  
                    return  

                self.board[row][col] = -1
                self.used_tiles.remove(tile_index)
    
    def print_tiles(self):
        print("\nPrinting Puzzle:\n")
        for i in range(self.size):
            for j in range(self.size):
                tile = self.tiles[i * self.size + j]
                print(f"{self.color_map[tile[0]]}+--{tile[0]}--+ ", end="")
            print("\n")
            for j in range(self.size):
                tile = self.tiles[i * self.size + j]
                if j == 0:
                    print(f"{self.color_map[tile[3]]}|{tile[3]}   {self.color_map[tile[1]]}{tile[1]}| \033[0m", end="")
                else:
                    print(f"{self.color_map[tile[3]]}|{tile[3]}   {self.color_map[tile[1]]}{tile[1]}| \033[0m", end="")
            print("\n")
            for j in range(self.size):
                tile = self.tiles[i * self.size + j]
                print(f"{self.color_map[tile[2]]}+--{tile[2]}--+ ", end="")
            print("\n")



    def print_solution(self):
        self.print_tiles()
        print("\n\033[97mTetravex Puzzle Solution:\n\n")
        for row_index, row in enumerate(self.board):
            for col_index, tile in enumerate(row):
                print(f"{self.color_map[tile[0]]}+--{tile[0]}--+ ", end="")
            print("\n")
            for col_index, tile in enumerate(row):
                if col_index == 0:
                    print(f"{self.color_map[tile[3]]}|{tile[3]}   {self.color_map[tile[1]]}{tile[1]}| \033[0m", end="")
                else:
                    print(f"{self.color_map[tile[3]]}|{tile[3]}   {self.color_map[tile[1]]}{tile[1]}| \033[0m", end="")
            print("\n")
            for col_index, tile in enumerate(row):
                print(f"{self.color_map[tile[2]]}+--{tile[2]}--+ ", end="")
            print("\n")
        print("\n")


# Example usage:

size = int(input("Puzzle Size (nxn)\n"))
tiles = [[random.randint(0, 9) for _ in range(4)] for _ in range(size ** 2)]
"""

Size 3 example

size = 3
tiles = [
    [5,6,2,3],[4,3,7,6],[2,8,9,3],
    [8,6,8,0],[9,1,3,6],[7,3,9,6],
    [8,6,1,5],[9,6,6,2],[1,2,9,7]
]


Size 4 example

size = 4
tiles = [
    [6,1,0,9],[2,4,4,3],[3,9,2,2],[8,2,1,8],
    [1,8,3,1],[7,1,8,7],[1,3,6,5],[4,5,0,1],
    [9,3,1,8],[7,5,6,3],[1,7,1,5],[6,7,7,3],
    [9,3,9,1],[0,9,6,5],[3,5,3,1],[6,1,3,7]
]


Size 5 example

size = 5
tiles = [
    [8,8,5,6],[0,2,7,4],[0,8,0,2],[1,6,3,1],[8,2,3,9],
    [2,6,1,3],[5,2,5,0],[4,3,8,0],[9,9,8,5],[9,3,7,9],
    [5,0,4,1],[7,4,0,0],[1,1,5,4],[5,0,6,8],[3,5,5,2],
    [7,4,7,5],[5,1,5,8],[6,8,8,8],[4,8,9,5],[8,5,3,2],
    [6,2,0,1],[0,1,7,6],[8,9,6,6],[5,6,4,3],[3,6,8,2]
]


Size 6 example

size = 6
tiles = [
    [6,3,4,1],[2,6,3,7],[4,2,1,3],[5,1,9,2],[6,4,2,4],[8,9,9,4],
    [2,8,9,0],[6,1,6,9],[4,1,6,3],[1,1,0,1],[6,9,3,5],[5,6,4,3],
    [5,8,2,0],[3,4,2,1],[9,3,6,7],[2,9,9,6],[9,2,5,9],[9,6,2,2],
    [3,2,3,6],[9,0,2,4],[3,1,0,2],[3,1,1,7],[0,1,4,7],[4,7,5,6],
    [4,2,1,3],[8,7,6,1],[6,6,0,1],[2,8,4,1],[9,3,3,6],[9,4,6,2],
    [1,2,3,2],[4,0,8,4],[0,4,8,1],[2,7,9,4],[4,4,9,2],[2,7,5,7]
]
"""

solver = TetravexSolver(size, tiles)
solver.solve()