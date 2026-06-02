import random
from mazagen.Cell import Cell
from mazagen.utils import get_value_of_positions
from mazagen.dictionary import Dictionary
from mazagen.constants import WallPosition, CELL_INITIAL_VALUE


class MazeGenerator:
    def __init__(self, config: Dictionary, seed: int = None):
        self.height = config.get_height()
        self.width = config.get_width()
        self.entry = config.get_entry()
        self.exit = config.get_exit()
        self.perfect = config.get_is_perfect()

        if seed is None:
            self.seed = random.randrange(1000000)
        else:
            self.seed = seed
        random.seed(self.seed)

        self.matrix: list[list[Cell]] = []
        self.solution: list[tuple] = []
        self.movements: list[str] = []

    def create_matrix(self) -> None:
        self.matrix = []

        print(f"Total height {self.height} | Total width {self.width}")
        value = CELL_INITIAL_VALUE
        for height_it in range(0, self.height):
            row: list[Cell] = []
            for widht_it in range(0, self.width):
                if (widht_it == 0):
                    value += get_value_of_positions(WallPosition.EAST)
                row.append(Cell(value))
            self.matrix.append(row)

    def take_start_point(self, visited: list[tuple]) -> tuple[int, int]:
        while True:
            random_w = random.randint(1, self.width - 1)
            if random_w % 2 != 0:
                break
        while True:
            random_h = random.randint(0, self.height - 1)
            if random_h % 2 != 0:
                break
        if (random_h, random_w) not in visited:
            return (random_h, random_w)
        else:
            return self.take_start_point(visited)

    def add_42(self, visited: list[tuple]) -> None:
        pixel_1: tuple[int, int] = (self.height / 2 - 2, self.width / 2 - 3)
        pixel_2: tuple[int, int] = (self.height / 2 - 1, self.width / 2 - 3)
        pixel_3: tuple[int, int] = (self.height / 2, self.width / 2 - 3)
        pixel_4: tuple[int, int] = (self.height / 2, self.width / 2 - 2)
        pixel_5: tuple[int, int] = (self.height / 2, self.width / 2 - 1)
        pixel_6: tuple[int, int] = (self.height / 2 + 1, self.width / 2 - 1)
        pixel_7: tuple[int, int] = (self.height / 2 + 2, self.width / 2 - 1)
        pixel_8: tuple[int, int] = (self.height / 2 - 2, self.width / 2 + 1)
        pixel_9: tuple[int, int] = (self.height / 2 - 2, self.width / 2 + 2)
        pixel_10: tuple[int, int] = (self.height / 2 - 2, self.width / 2 + 3)
        pixel_11: tuple[int, int] = (self.height / 2 - 1, self.width / 2 + 3)
        pixel_12: tuple[int, int] = (self.height / 2, self.width / 2 + 3)
        pixel_13: tuple[int, int] = (self.height / 2, self.width / 2 + 2)
        pixel_14: tuple[int, int] = (self.height / 2, self.width / 2 + 1)
        pixel_15: tuple[int, int] = (self.height / 2 + 1, self.width / 2 + 1)
        pixel_16: tuple[int, int] = (self.height / 2 + 2, self.width / 2 + 1)
        pixel_17: tuple[int, int] = (self.height / 2 + 2, self.width / 2 + 2)
        pixel_18: tuple[int, int] = (self.height / 2 + 2, self.width / 2 + 3)
        self.matrix[int(pixel_1[0])][int(pixel_1[1])].value += (
            get_value_of_positions([WallPosition.SOUTH]))
        self.matrix[int(pixel_2[0])][int(pixel_2[1])].value += (
            get_value_of_positions([WallPosition.SOUTH, WallPosition.NORTH]))
        self.matrix[int(pixel_3[0])][int(pixel_3[1])].value += (
            get_value_of_positions([WallPosition.NORTH]))
        self.matrix[int(pixel_4[0])][int(pixel_4[1])].value += (
            get_value_of_positions([WallPosition.WEST]))
        self.matrix[int(pixel_5[0])][int(pixel_5[1])].value += (
            get_value_of_positions([WallPosition.SOUTH, WallPosition.WEST]))
        self.matrix[int(pixel_6[0])][int(pixel_6[1])].value += (
            get_value_of_positions([WallPosition.SOUTH, WallPosition.NORTH]))
        self.matrix[int(pixel_7[0])][int(pixel_7[1])].value += (
            get_value_of_positions([WallPosition.NORTH]))
        self.matrix[int(pixel_8[0])][int(pixel_5[1])].value += (
            get_value_of_positions([WallPosition.EAST]))
        self.matrix[int(pixel_9[0])][int(pixel_9[1])].value += (
            get_value_of_positions([WallPosition.WEST]))
        self.matrix[int(pixel_10[0])][int(pixel_10[1])].value += (
            get_value_of_positions([WallPosition.WEST, WallPosition.SOUTH]))
        self.matrix[int(pixel_11[0])][int(pixel_11[1])].value += (
            get_value_of_positions([WallPosition.SOUTH, WallPosition.NORTH]))
        self.matrix[int(pixel_12[0])][int(pixel_12[1])].value += (
            get_value_of_positions([WallPosition.WEST]))
        self.matrix[int(pixel_13[0])][int(pixel_13[1])].value += (
            get_value_of_positions([WallPosition.WEST]))
        self.matrix[int(pixel_14[0])][int(pixel_14[1])].value += (
            get_value_of_positions([WallPosition.SOUTH, WallPosition.NORTH]))
        self.matrix[int(pixel_15[0])][int(pixel_15[1])].value += (
            get_value_of_positions([WallPosition.SOUTH, WallPosition.NORTH]))
        self.matrix[int(pixel_16[0])][int(pixel_16[1])].value += (
            get_value_of_positions([WallPosition.NORTH]))
        self.matrix[int(pixel_17[0])][int(pixel_17[1])].value += (
            get_value_of_positions([WallPosition.WEST]))
        self.matrix[int(pixel_18[0])][int(pixel_18[1])].value += (
            get_value_of_positions([WallPosition.WEST]))
        visited.append(pixel_1)
        visited.append(pixel_2)
        visited.append(pixel_3)
        visited.append(pixel_4)
        visited.append(pixel_5)
        visited.append(pixel_6)
        visited.append(pixel_7)
        visited.append(pixel_8)
        visited.append(pixel_9)
        visited.append(pixel_10)
        visited.append(pixel_11)
        visited.append(pixel_12)
        visited.append(pixel_13)
        visited.append(pixel_14)
        visited.append(pixel_15)
        visited.append(pixel_16)
        visited.append(pixel_17)
        visited.append(pixel_18)

    def count_wall_opened(self, value: int) -> int:
        counter: int = 0
        for bit in [1, 2, 4, 8]:
            if (value & bit) == 0:
                counter += 1
        return counter

    def make_the_maze(self) -> list[list[Cell]]:
        visited: list[tuple] = []
        temp_matrix: list[list[Cell]] = self.matrix
        self.add_42(visited)
        for a in visited:
            if a == self.entry or a == self.exit:
                self.matrix = temp_matrix
                print("IMPOSSIBLE PRINT 42")
        start_point: tuple[int, int] = self.take_start_point(visited)
        stack: list[tuple] = []
        up: tuple[int, int] = (-1, 0)
        down: tuple[int, int] = (1, 0)
        right: tuple[int, int] = (0, 1)
        left: tuple[int, int] = (0, -1)
        directions: list[tuple] = [up, down, right, left]
        current_cord: tuple[int, int] = start_point
        temp_cord: tuple[int, int]
        while len(visited) != (self.height * self.width):
            random.shuffle(directions)
            found_valid: bool = False
            if (current_cord not in visited):
                visited.append(current_cord)
            for random_direc in directions:
                temp_cord = (current_cord[0] + random_direc[0],
                             current_cord[1] + random_direc[1])
                if not (0 <= temp_cord[0] < self.height and
                        0 <= temp_cord[1] < self.width):
                    continue
                if temp_cord in visited:
                    continue
                if self.perfect and self.count_wall_opened(
                     self.matrix[temp_cord[0]][temp_cord[1]].value) >= 2:
                    continue
                if random_direc == up:
                    self.matrix[current_cord[0]][current_cord[1]].value += (
                        get_value_of_positions([WallPosition.NORTH]))
                    if (current_cord[0] - 1 >= 0):
                        self.matrix[
                            current_cord[0] - 1][current_cord[1]].value += (
                            get_value_of_positions([WallPosition.SOUTH]))
                    found_valid = True
                elif random_direc == down:
                    self.matrix[current_cord[0]][current_cord[1]].value += (
                        get_value_of_positions([WallPosition.SOUTH]))
                    if (current_cord[0] + 1 < self.height):
                        self.matrix[
                            current_cord[0] + 1][current_cord[1]].value += (
                            get_value_of_positions([WallPosition.NORTH]))
                    found_valid = True
                elif random_direc == right:
                    self.matrix[current_cord[0]][current_cord[1]].value += (
                        get_value_of_positions([WallPosition.EAST]))
                    if (current_cord[1] + 1 < self.width):
                        self.matrix[
                            current_cord[0]][current_cord[1] + 1].value += (
                            get_value_of_positions([WallPosition.WEST]))
                    found_valid = True
                elif random_direc == left:
                    self.matrix[current_cord[0]][current_cord[1]].value += (
                        get_value_of_positions([WallPosition.WEST]))
                    if (current_cord[1] - 1 >= 0):
                        self.matrix[
                            current_cord[0]][current_cord[1] - 1].value += (
                            get_value_of_positions([WallPosition.EAST]))
                    found_valid = True
                stack.append(current_cord)
                current_cord = temp_cord
                break
            if not found_valid:
                if len(stack) > 0:
                    current_cord = stack.pop()

    def find_the_way(self) -> list[tuple[int, int], list[str]]:
        the_way: list[tuple[int, int]] = [self.entry]
        visited: list[tuple] = []
        backup: list = [(self.entry, the_way, [])]
        directions: list[tuple[int, int, int]] = [(-1, 0, 1, 'N'),
                                                  (1, 0, 4, 'S'),
                                                  (0, 1, 2, 'E'),
                                                  (0, -1, 8, 'W')]
        while len(backup) != 0:
            actual = backup.pop(0)
            if actual[0] == self.exit:
                for coord in actual[1]:
                    self.matrix[coord[0]][coord[1]].solution_path = True
                if len(actual[1]) > 0:
                    self.matrix[self.entry[0]][self.entry[1]].is_entry = True
                    self.matrix[self.exit[0]][self.exit[1]].is_exit = True
                return actual[1], actual[2]
            if actual[0] in visited:
                continue
            visited.append(actual[0])
            for py, px, bit, movement in directions:
                next_pos = (actual[0][0] + py, actual[0][1] + px)
                if (0 <= next_pos[0] < len(self.matrix) and
                    0 <= next_pos[1] < len(self.matrix[0]) and
                    next_pos not in visited and
                    (self.matrix[
                        actual[0][0]][actual[0][1]].value & bit) == 0):
                    new_way: list = actual[1] + [next_pos]
                    new_mov = actual[2] + [movement]
                    backup.append((next_pos, new_way, new_mov))
        return [], []

    def generate(self) -> tuple[list[list[Cell]], list[tuple], list[str], int]:
        self.create_matrix()
        self.make_the_maze()
        self.solution, self.movements = self.find_the_way()
        return self.matrix, self.solution, self.movements, self.seed
