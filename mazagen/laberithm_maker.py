import random
from mazagen.Cell import Cell
from mazagen.utils import get_value_of_positions
from mazagen.dictionary import Dictionary
from mazagen.constants import WallPosition, CELL_INITIAL_VALUE, MIN_SIZE_42


class MazeGenerator:
    def __init__(self, config: Dictionary, seed: int | None = None):
        self.height: int = config.get_height() or 10
        self.width: int = config.get_width() or 10
        self.entry: tuple = config.get_entry() or (1, 1)
        self.exit: tuple = config.get_exit() or (1, 2)
        self.perfect: bool = bool(config.get_is_perfect())
        self.seed: int

        if seed is None:
            self.seed = random.randrange(1000000)
        else:
            self.seed = seed
        random.seed(self.seed)

        self.matrix: list[list[Cell]] = []
        self.solution: list[tuple] = []
        self.movements: list[str] = []

        self.directions_list: list[tuple[int, int, int, str]] = ([
            (-1, 0, 1, 'N'),
            (1, 0, 4, 'S'),
            (0, 1, 2, 'E'),
            (0, -1, 8, 'W')])

    def create_matrix(self) -> None:
        self.matrix = []
        value = CELL_INITIAL_VALUE
        for height_it in range(0, self.height):
            row: list[Cell] = []
            for widht_it in range(0, self.width):
                current_cell_value: int = value
                if (widht_it == 0):
                    current_cell_value &= ~(get_value_of_positions(
                        [WallPosition.WEST]))
                row.append(Cell(current_cell_value))
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

    def get_42_pos(self) -> list[tuple[int, int]]:
        list_pos: list[tuple[int, int]] = []
        pixel_1: tuple[int, int] = (self.height // 2 - 2, self.width // 2 - 3)
        pixel_2: tuple[int, int] = (self.height // 2 - 1, self.width // 2 - 3)
        pixel_3: tuple[int, int] = (self.height // 2, self.width // 2 - 3)
        pixel_4: tuple[int, int] = (self.height // 2, self.width // 2 - 2)
        pixel_5: tuple[int, int] = (self.height // 2, self.width // 2 - 1)
        pixel_6: tuple[int, int] = (self.height // 2 + 1, self.width // 2 - 1)
        pixel_7: tuple[int, int] = (self.height // 2 + 2, self.width // 2 - 1)
        pixel_8: tuple[int, int] = (self.height // 2 - 2, self.width // 2 + 1)
        pixel_9: tuple[int, int] = (self.height // 2 - 2, self.width // 2 + 2)
        pixel_10: tuple[int, int] = (self.height // 2 - 2, self.width // 2 + 3)
        pixel_11: tuple[int, int] = (self.height // 2 - 1, self.width // 2 + 3)
        pixel_12: tuple[int, int] = (self.height // 2, self.width // 2 + 3)
        pixel_13: tuple[int, int] = (self.height // 2, self.width // 2 + 2)
        pixel_14: tuple[int, int] = (self.height // 2, self.width // 2 + 1)
        pixel_15: tuple[int, int] = (self.height // 2 + 1, self.width // 2 + 1)
        pixel_16: tuple[int, int] = (self.height // 2 + 2, self.width // 2 + 1)
        pixel_17: tuple[int, int] = (self.height // 2 + 2, self.width // 2 + 2)
        pixel_18: tuple[int, int] = (self.height // 2 + 2, self.width // 2 + 3)
        list_pos.append(pixel_1)
        list_pos.append(pixel_2)
        list_pos.append(pixel_3)
        list_pos.append(pixel_4)
        list_pos.append(pixel_5)
        list_pos.append(pixel_6)
        list_pos.append(pixel_7)
        list_pos.append(pixel_8)
        list_pos.append(pixel_9)
        list_pos.append(pixel_10)
        list_pos.append(pixel_11)
        list_pos.append(pixel_12)
        list_pos.append(pixel_13)
        list_pos.append(pixel_14)
        list_pos.append(pixel_15)
        list_pos.append(pixel_16)
        list_pos.append(pixel_17)
        list_pos.append(pixel_18)

        return list_pos

    def add_42(
            self, visited: list[tuple],
            list_pos42: list[tuple[int, int]]) -> None:

        self.matrix[int(list_pos42[0][0])][int(list_pos42[0][1])].value &= ~(
            get_value_of_positions([WallPosition.SOUTH]))
        self.matrix[int(list_pos42[1][0])][int(list_pos42[1][1])].value &= ~(
            get_value_of_positions([WallPosition.SOUTH, WallPosition.NORTH]))
        self.matrix[int(list_pos42[2][0])][int(list_pos42[2][1])].value &= ~(
            get_value_of_positions([WallPosition.NORTH, WallPosition.EAST]))
        self.matrix[int(list_pos42[3][0])][int(list_pos42[3][1])].value &= ~(
            get_value_of_positions([WallPosition.WEST, WallPosition.EAST]))
        self.matrix[int(list_pos42[4][0])][int(list_pos42[4][1])].value &= ~(
            get_value_of_positions([WallPosition.SOUTH, WallPosition.WEST]))
        self.matrix[int(list_pos42[5][0])][int(list_pos42[5][1])].value &= ~(
            get_value_of_positions([WallPosition.SOUTH, WallPosition.NORTH]))
        self.matrix[int(list_pos42[6][0])][int(list_pos42[6][1])].value &= ~(
            get_value_of_positions([WallPosition.NORTH]))
        self.matrix[int(list_pos42[7][0])][int(list_pos42[7][1])].value &= ~(
            get_value_of_positions([WallPosition.EAST]))
        self.matrix[int(list_pos42[8][0])][int(list_pos42[8][1])].value &= ~(
            get_value_of_positions([WallPosition.WEST, WallPosition.EAST]))
        self.matrix[int(list_pos42[9][0])][int(list_pos42[9][1])].value &= ~(
            get_value_of_positions([WallPosition.WEST, WallPosition.SOUTH]))
        self.matrix[int(list_pos42[10][0])][int(list_pos42[10][1])].value &= ~(
            get_value_of_positions([WallPosition.SOUTH, WallPosition.NORTH]))
        self.matrix[int(list_pos42[11][0])][int(list_pos42[11][1])].value &= ~(
            get_value_of_positions([WallPosition.WEST, WallPosition.NORTH]))
        self.matrix[int(list_pos42[12][0])][int(list_pos42[12][1])].value &= ~(
            get_value_of_positions([WallPosition.WEST, WallPosition.EAST]))
        self.matrix[int(list_pos42[13][0])][int(list_pos42[13][1])].value &= ~(
            get_value_of_positions([WallPosition.SOUTH, WallPosition.EAST]))
        self.matrix[int(list_pos42[14][0])][int(list_pos42[14][1])].value &= ~(
            get_value_of_positions([WallPosition.SOUTH, WallPosition.NORTH]))
        self.matrix[int(list_pos42[15][0])][int(list_pos42[15][1])].value &= ~(
            get_value_of_positions([WallPosition.NORTH, WallPosition.EAST]))
        self.matrix[int(list_pos42[16][0])][int(list_pos42[16][1])].value &= ~(
            get_value_of_positions([WallPosition.WEST, WallPosition.EAST]))
        self.matrix[int(list_pos42[17][0])][int(list_pos42[17][1])].value &= ~(
            get_value_of_positions([WallPosition.WEST]))
        for it_list in list_pos42:
            visited.append(it_list)

    def count_wall_opened(self, value: int) -> int:
        counter: int = 0
        for bit in [1, 2, 4, 8]:
            if (value & bit) == 0:
                counter += 1
        return counter

    def make_the_maze(self) -> None:
        visited: list[tuple] = []
        temp_matrix: list[list[Cell]] = self.matrix
        list_42_cells = self.get_42_pos()
        if (self.entry in list_42_cells or self.exit in list_42_cells
           or self.height <= MIN_SIZE_42 or self.width <= MIN_SIZE_42):
            self.matrix = temp_matrix
            print("IMPOSSIBLE PRINT 42")
            visited = []
        else:
            self.add_42(visited, list_42_cells)
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
                if random_direc == up:
                    self.matrix[current_cord[0]][current_cord[1]].value &= ~(
                        get_value_of_positions([WallPosition.NORTH]))
                    if (current_cord[0] - 1 >= 0):
                        self.matrix[
                            current_cord[0] - 1][current_cord[1]].value &= ~(
                            get_value_of_positions([WallPosition.SOUTH]))
                    found_valid = True
                elif random_direc == down:
                    self.matrix[current_cord[0]][current_cord[1]].value &= ~(
                        get_value_of_positions([WallPosition.SOUTH]))
                    if (current_cord[0] + 1 < self.height):
                        self.matrix[
                            current_cord[0] + 1][current_cord[1]].value &= ~(
                            get_value_of_positions([WallPosition.NORTH]))
                    found_valid = True
                elif random_direc == right:
                    self.matrix[current_cord[0]][current_cord[1]].value &= ~(
                        get_value_of_positions([WallPosition.EAST]))
                    if (current_cord[1] + 1 < self.width):
                        self.matrix[
                            current_cord[0]][current_cord[1] + 1].value &= ~(
                            get_value_of_positions([WallPosition.WEST]))
                    found_valid = True
                elif random_direc == left:
                    self.matrix[current_cord[0]][current_cord[1]].value &= ~(
                        get_value_of_positions([WallPosition.WEST]))
                    if (current_cord[1] - 1 >= 0):
                        self.matrix[
                            current_cord[0]][current_cord[1] - 1].value &= ~(
                            get_value_of_positions([WallPosition.EAST]))
                    found_valid = True
                stack.append(current_cord)
                current_cord = temp_cord

                break
            if not found_valid:
                if len(stack) > 0:
                    current_cord = stack.pop()
        if not self.perfect:
            self.break_random_wall(visited, list_42_cells)

    def break_random_wall(self, visited: list[tuple],
                          list_42_cells: list[tuple[int, int]]) -> None:
        for cell in visited:
            if cell in list_42_cells:
                continue
            cell_in_matrix = self.matrix[int(cell[0])][int(cell[1])]
            if cell_in_matrix.value == 0:
                continue
            cell_value = cell_in_matrix.value
            for py, px, bit, movement in self.directions_list:
                if (cell_value & bit == 0):
                    continue
                if bit == 1:
                    if int(cell[0]) - 1 < 0:
                        continue
                    cell_to_move = self.matrix[int(cell[0]) - 1][int(cell[1])]

                    if cell_to_move in list_42_cells:
                        continue
                    else:
                        cell_in_matrix.value &= ~(
                            get_value_of_positions([WallPosition.NORTH]))
                        cell_to_move.value &= ~(
                            get_value_of_positions([WallPosition.SOUTH]))
                        return
                if bit == 2:
                    if int(cell[1]) + 1 >= self.width:
                        continue
                    cell_to_move = self.matrix[int(cell[0])][int(cell[1] + 1)]
                    if cell_to_move in list_42_cells:
                        continue
                    else:
                        cell_in_matrix.value &= ~(
                            get_value_of_positions([WallPosition.EAST]))
                        cell_to_move.value &= ~(
                            get_value_of_positions([WallPosition.WEST]))
                        return
                if bit == 4:
                    if int(cell[0]) + 1 >= self.height:
                        continue
                    cell_to_move = self.matrix[int(cell[0]) + 1][int(cell[1])]
                    if cell_to_move in list_42_cells:
                        continue
                    else:
                        cell_in_matrix.value &= ~(
                            get_value_of_positions([WallPosition.SOUTH]))
                        cell_to_move.value &= ~(
                            get_value_of_positions([WallPosition.NORTH]))
                        return
                if bit == 8:
                    if int(cell[1]) - 1 < 0:
                        continue
                    cell_to_move = self.matrix[int(cell[0])][int(cell[1] - 1)]
                    if cell_to_move in list_42_cells:
                        continue
                    else:
                        cell_in_matrix.value &= ~(
                            get_value_of_positions([WallPosition.WEST]))
                        cell_to_move.value &= ~(
                            get_value_of_positions([WallPosition.EAST]))

                        return

    def find_the_way(self) -> tuple[list[tuple[int, int]], list[str]]:
        the_way: list[tuple[int, int]] = [self.entry]
        visited: list[tuple] = []
        backup: list[tuple[tuple[int, int],
                           list[tuple[int, int]],
                           list[str]]] = [(self.entry, the_way, [])]

        while (len(backup) != 0):
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
            for py, px, bit, movement in self.directions_list:
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

    def generate(self) -> tuple[list[list[Cell]], list[tuple], list[str]]:
        while (len(self.solution) == 0):
            self.create_matrix()
            self.make_the_maze()
            self.solution, self.movements = self.find_the_way()

        return self.matrix, self.solution, self.movements
