import random
from Cell import Cell
from matrix_drawer import print_matrix
from constants import WallPosition
from utils import get_value_of_positions
from dictionary import Dictionary
def take_start_point(total_height_size: int, total_width_size: int, visited: list[tuple]) -> tuple[int, int]:
    while True:
        random_w = random.randint(1, total_width_size -1)
        if random_w % 2 != 0:
            break
    while True:
        random_h = random.randint(0, total_height_size -1)
        if random_h % 2 != 0:
            break
    if (random_h, random_w) not in visited:
        return (random_h, random_w)
    else:
        return take_start_point(total_height_size, total_width_size, visited)


def add_42(num_matrix: list[list[Cell]], visited: list[tuple], total_height_size: int, total_width_size: int) -> list[list[int]]:
    pixel_1: tuple[int, int] = (total_height_size / 2 - 2, total_width_size / 2 - 3)
    pixel_2: tuple[int, int] = (total_height_size / 2 - 1, total_width_size / 2 - 3)
    pixel_3: tuple[int, int] = (total_height_size / 2, total_width_size / 2 - 3)
    pixel_4: tuple[int, int] = (total_height_size / 2, total_width_size / 2 - 2)
    pixel_5: tuple[int, int] = (total_height_size / 2, total_width_size / 2 - 1)
    pixel_6: tuple[int, int] = (total_height_size / 2 + 1, total_width_size / 2 - 1)
    pixel_7: tuple[int, int] = (total_height_size / 2 + 2, total_width_size / 2 - 1) # hasta aqui el 4
    pixel_8: tuple[int, int] = (total_height_size / 2 - 2, total_width_size / 2 + 1)
    pixel_9: tuple[int, int] = (total_height_size / 2 - 2, total_width_size / 2 + 2)
    pixel_10: tuple[int, int] = (total_height_size / 2 - 2, total_width_size / 2 + 3)
    pixel_11: tuple[int, int] = (total_height_size / 2 - 1, total_width_size / 2 + 3)
    pixel_12: tuple[int, int] = (total_height_size / 2, total_width_size / 2 + 3)
    pixel_13: tuple[int, int] = (total_height_size / 2, total_width_size / 2 + 2)
    pixel_14: tuple[int, int] = (total_height_size / 2, total_width_size / 2 + 1)
    pixel_15: tuple[int, int] = (total_height_size / 2 + 1, total_width_size / 2 + 1)
    pixel_16: tuple[int, int] = (total_height_size / 2 + 2, total_width_size / 2 + 1)
    pixel_17: tuple[int, int] = (total_height_size / 2 + 2, total_width_size / 2 + 2)
    pixel_18: tuple[int, int] = (total_height_size / 2 + 2, total_width_size / 2 + 3) # hasta aqui el 2                 
    num_matrix[int(pixel_1[0])][int(pixel_1[1])].value += get_value_of_positions([WallPosition.SOUTH]) # 4 solo abajo
    num_matrix[int(pixel_2[0])][int(pixel_2[1])].value += get_value_of_positions([WallPosition.SOUTH, WallPosition.NORTH]) # 4 + 1 abajo y arriba
    num_matrix[int(pixel_3[0])][int(pixel_3[1])].value += get_value_of_positions([WallPosition.NORTH]) # 1 +2 arriba y derecha
    num_matrix[int(pixel_4[0])][int(pixel_4[1])].value += get_value_of_positions([WallPosition.WEST])#8 +2 derecha e izq
    num_matrix[int(pixel_5[0])][int(pixel_5[1])].value += get_value_of_positions([WallPosition.SOUTH, WallPosition.WEST]) # 8 + 4 izq y abajo
    num_matrix[int(pixel_6[0])][int(pixel_6[1])].value += get_value_of_positions([WallPosition.SOUTH, WallPosition.NORTH])  # abajo y arriba
    num_matrix[int(pixel_7[0])][int(pixel_7[1])].value += get_value_of_positions([WallPosition.NORTH], ) # arriba
    num_matrix[int(pixel_8[0])][int(pixel_5[1])].value += get_value_of_positions([WallPosition.EAST])
    num_matrix[int(pixel_9[0])][int(pixel_9[1])].value += get_value_of_positions([WallPosition.WEST]) # 8 + 4 izq y abajo
    num_matrix[int(pixel_10[0])][int(pixel_10[1])].value += get_value_of_positions([WallPosition.WEST, WallPosition.SOUTH])
    num_matrix[int(pixel_11[0])][int(pixel_11[1])].value += get_value_of_positions([WallPosition.SOUTH, WallPosition.NORTH])
    num_matrix[int(pixel_12[0])][int(pixel_12[1])].value += get_value_of_positions([WallPosition.WEST])
    num_matrix[int(pixel_13[0])][int(pixel_13[1])].value += get_value_of_positions([WallPosition.WEST])
    num_matrix[int(pixel_14[0])][int(pixel_14[1])].value += get_value_of_positions([WallPosition.SOUTH, WallPosition.NORTH])
    num_matrix[int(pixel_15[0])][int(pixel_15[1])].value += get_value_of_positions([WallPosition.SOUTH, WallPosition.NORTH])
    num_matrix[int(pixel_16[0])][int(pixel_16[1])].value += get_value_of_positions([WallPosition.NORTH])
    num_matrix[int(pixel_17[0])][int(pixel_17[1])].value += get_value_of_positions([WallPosition.WEST])
    num_matrix[int(pixel_18[0])][int(pixel_18[1])].value += get_value_of_positions([WallPosition.WEST])
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
    return num_matrix


def make_the_maze(num_matrix : list[list[Cell]], total_height_size: int, total_width_size: int, dict : Dictionary) -> list[list[Cell]]: 
    visited: list[tuple] = []
    random.seed(1) # Cambiar
    num_matrix = add_42(num_matrix, visited, total_height_size, total_width_size)
    start_point: tuple[int, int] = take_start_point(total_height_size, total_width_size, visited)
    start_point = (2,3)
    stack: list[tuple] = []
    up: tuple[int, int] =  (-1, 0)      # + 2
    down: tuple[int, int] = (1, 0)      # + 1
    right: tuple[int, int] = (0, 1)     # + 4
    left: tuple[int, int] = (0, -1)     # + 8
    directions: list[tuple] = [up, down, right, left]
    current_cord: tuple[int, int] = start_point
    temp_cord: tuple[int, int]
    solution: list = []
    # print(f"initial visited len {len(visited)}") #TODO borrar
    #print_matrix(num_matrix, total_height_size, total_width_size, solution)

    while len(visited) != (total_height_size * total_width_size):
        random.shuffle(directions)
        found_valid: bool = False
        if (not current_cord in visited):
            visited.append(current_cord)
        #print(f"VISITED {current_cord} --- {len(visited)}")
        for random_direc in directions:
            temp_cord = (current_cord[0] + random_direc[0], current_cord[1] + random_direc[1])
            if not (0 <= temp_cord[0] < total_height_size and 0 <= temp_cord[1] < total_width_size):
                continue
            if temp_cord in visited:
                continue
            #print(f"CURRENT {current_cord}")
            if random_direc == up:
                num_matrix[current_cord[0]][current_cord[1]].value += get_value_of_positions([WallPosition.NORTH])
                if (current_cord[0] - 1 >= 0):
                    num_matrix[current_cord[0] - 1][current_cord[1]].value += get_value_of_positions([WallPosition.SOUTH])   #rompo pared de abajo y    juntanterior con este
                found_valid = True
            elif random_direc == down:
                num_matrix[current_cord[0]][current_cord[1]].value += get_value_of_positions([WallPosition.SOUTH])         
                if (current_cord[0] + 1 < total_height_size):
                    num_matrix[current_cord[0] + 1][current_cord[1]].value += get_value_of_positions([WallPosition.NORTH])      #rompo pared de arriba y junto anterior con este
                found_valid = True
            elif random_direc == right:
                num_matrix[current_cord[0]][current_cord[1]].value += get_value_of_positions([WallPosition.EAST])       
                if (current_cord[1] + 1 < total_width_size):
                    num_matrix[current_cord[0]][current_cord[1] + 1].value += get_value_of_positions([WallPosition.WEST])   #rompo pared de izquierda y junto con lo anterior
                found_valid = True
            elif random_direc == left:
                num_matrix[current_cord[0]][current_cord[1]].value += get_value_of_positions([WallPosition.WEST])
                if (current_cord[1]- 1 >= 0 ):
                    num_matrix[current_cord[0]][current_cord[1]- 1].value += get_value_of_positions([WallPosition.EAST])
                found_valid = True
            stack.append(current_cord)
            current_cord = temp_cord
            break
        if not found_valid:
            if len(stack) > 0:
                current_cord = stack.pop() 
                break  


    
    
    print("\n Matriz de numeros")
    for a in num_matrix:
         print([cell.value for cell in a])
    print("\n Matriz real con laberinto")
    #print_matrix(num_matrix, total_height_size, total_width_size, solution)
    ENTRY: tuple =     dict.get_entry()
    EXIT: tuple =     dict.get_exit()
    solution = find_the_way(num_matrix, ENTRY, EXIT) 
    return solution


# make_the_maze(16, 16)

def find_the_way(num_matrix: list[list[Cell]], start_point: tuple[int, int],
                 end_point: tuple[int, int]) -> list[tuple[int, int],]:
    the_way: list[tuple[int, int]] = [start_point]
    visited: list[tuple] = []
    backup: list = [(start_point, the_way, [])]
    directions: list[tuple[int,int,int]] = [(-1, 0, 1, 'N'),
                                            (1, 0, 4, 'S'),
                                            (0, 1, 2, 'E'),
                                            (0, -1, 8, 'W')]
    while len(backup) != 0:
        actual = backup.pop(0)
        if actual[0] == end_point:
            for coord in actual[1]:
                num_matrix[coord[0]][coord[1]].solution_path = True
            return actual[1]

        if actual[0] in visited:
            continue
        visited.append(actual[0])
        for py, px, bit, movement in directions:
            next_pos = (actual[0][0] + py, actual[0][1] + px)
            if (0 <= next_pos[0] < len(num_matrix) and 0 <= next_pos[1] < len(num_matrix[0]) 
                and next_pos not in visited
                and (num_matrix[actual[0][0]][actual[0][1]].value & bit) != 0):
                new_way: list = actual[1] + [next_pos]
                new_mov = actual[2] + [movement]
                backup.append((next_pos, new_way, new_mov))
    return []
    
    


