import random
from Cell import Cell
from a_maze_ing import print_matrix

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


def add_42(num_matrix: list[list[int]], visited: list[tuple], total_height_size: int, total_width_size: int) -> list[list[int]]:
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
    num_matrix[int(pixel_1[0])][int(pixel_1[1])] = Cell(1)
    num_matrix[int(pixel_2[0])][int(pixel_2[1])] = Cell(3)
    num_matrix[int(pixel_3[0])][int(pixel_3[1])] = Cell(4)
    num_matrix[int(pixel_4[0])][int(pixel_4[1])] = Cell(12)
    num_matrix[int(pixel_5[0])][int(pixel_5[1])] = Cell(9)
    num_matrix[int(pixel_6[0])][int(pixel_6[1])] = Cell(3)
    num_matrix[int(pixel_7[0])][int(pixel_7[1])] = Cell(2)
    num_matrix[int(pixel_8[0])][int(pixel_8[1])] = Cell(4)
    num_matrix[int(pixel_9[0])][int(pixel_9[1])] = Cell(12)
    num_matrix[int(pixel_10[0])][int(pixel_10[1])] = Cell(9)
    num_matrix[int(pixel_11[0])][int(pixel_11[1])] = Cell(3)
    num_matrix[int(pixel_12[0])][int(pixel_12[1])] = Cell(10)
    num_matrix[int(pixel_13[0])][int(pixel_13[1])] = Cell(12)
    num_matrix[int(pixel_14[0])][int(pixel_14[1])] = Cell(5)
    num_matrix[int(pixel_15[0])][int(pixel_15[1])] = Cell(3)
    num_matrix[int(pixel_16[0])][int(pixel_16[1])] = Cell(6)
    num_matrix[int(pixel_17[0])][int(pixel_17[1])] = Cell(12)
    num_matrix[int(pixel_18[0])][int(pixel_18[1])] = Cell(8)
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


def make_the_maze(total_height_size: int, total_width_size: int) -> list[list[Cell]]:  # añadir matrix: list[list[Cell]],
    num_matrix: list[list[Cell]] = []
    for _ in range(0, total_height_size):
        row: list[Cell] = []
        for _ in range(0, total_width_size):
            row.append(Cell())
        num_matrix.append(row)
    visited: list[tuple] = []
    random.seed(1) # Cambiar
    num_matrix = add_42(num_matrix, visited, total_height_size, total_width_size)
    start_point: tuple[int, int] = take_start_point(total_height_size, total_width_size, visited)
    visited.append(start_point)
    #num_matrix[start_point[0]][start_point[1]] = 20
    trash: list[tuple] = [start_point]
    up: tuple[int, int] =  (-1, 0)      # + 2
    down: tuple[int, int] = (1, 0)      # + 1
    right: tuple[int, int] = (0, 1)     # + 4
    left: tuple[int, int] = (0, -1)     # + 8
    direcctions: list[tuple] = [up, down, right, left]
    current_cord: tuple[int, int] = start_point
    temp_cord: tuple[int, int]
    print(f"initial visited len {len(visited)}") #TODO borrar
    while len(visited) != (total_height_size * total_width_size):
        random.shuffle(direcctions)
        found_valid: bool = False
        for random_direc in direcctions:
            temp_cord = (current_cord[0] + random_direc[0], current_cord[1] + random_direc[1])
            if temp_cord in visited:
                continue
            if not (0 <= temp_cord[0] < total_height_size and 0 <= temp_cord[1] < total_width_size):
                continue
            
            current_cord = temp_cord
            if random_direc == up:
                visited.append(current_cord)
                trash.append(current_cord)
                num_matrix[current_cord[0]][current_cord[1]].value += 1      #vacio!
                num_matrix[current_cord[0]+ 1][current_cord[1]].value += 2   #rompo pared de abajo y    juntanterior con este
                found_valid = True
            elif random_direc == down:
                visited.append(current_cord)
                trash.append(current_cord)
                num_matrix[current_cord[0]][current_cord[1]].value += 2       #vacio
                num_matrix[current_cord[0] - 1][current_cord[1]].value += 1    #rompo pared de arriba y junto anterior con este
                found_valid = True
            elif random_direc == right:
                visited.append(current_cord)
                trash.append(current_cord)
                num_matrix[current_cord[0]][current_cord[1]].value += 4        #vacio
                num_matrix[current_cord[0]][current_cord[1] - 1].value += 8    #rompo pared de izquierda y junto con lo anterior
                found_valid = True
            elif random_direc == left:
                visited.append(current_cord)
                trash.append(current_cord)
                num_matrix[current_cord[0]][current_cord[1]].value += 8        #vacio 
                num_matrix[current_cord[0]][current_cord[1]+ 1].value += 4     #rompo pared de derecha y junto con lo anterior
                found_valid = True
            break
        if not found_valid:
            current_cord = trash.pop()    
    print(f"2 - {len(visited)}") #TODO borrar

    
    print_matrix(num_matrix, total_height_size, total_width_size)
    #for a in num_matrix:
    #    print(a)
    
    return num_matrix

def find_the_way(num_matrix: list[list[int]], start_point: tuple[int, int], end_point: tuple[int, int]) -> list[tuple[int, int]]:
    the_way: list[tuple[int, int]] = []
    the_way.append(start_point)
    while the_way[-1] != end_point:
        current_cord: tuple[int, int] = start_point
        if start_point == end_point:
            return the_way
        if num_matrix[current_cord[0]][current_cord[1]] == 0:
            return []
        if num_matrix[current_cord[0]][current_cord[1]] == 1 or num_matrix[
            current_cord[0]][current_cord[1]] == 3 or num_matrix[
                current_cord[0]][current_cord[1]] == 5 or num_matrix[
                    current_cord[0]][current_cord[1]] == 7 or num_matrix[
                        current_cord[0]][current_cord[1]] == 9 or num_matrix[
                            current_cord[0]][current_cord[1]] == 11 or num_matrix[
                                current_cord[0]][current_cord[1]] == 13 or num_matrix[
                                    current_cord[0]][current_cord[1]] == 15 and num_matrix[current_cord[0] - 1][current_cord[1]] not in the_way:
            current_cord = (current_cord[0] - 1, current_cord[1])
            the_way.append(current_cord)
        elif num_matrix[current_cord[0]][current_cord[1]] == 2 or num_matrix[
            current_cord[0]][current_cord[1]] == 3 or num_matrix[
                current_cord[0]][current_cord[1]] == 6 or num_matrix[
                    current_cord[0]][current_cord[1]] == 7 or num_matrix[
                        current_cord[0]][current_cord[1]] == 10 or num_matrix[
                            current_cord[0]][current_cord[1]] == 11 or num_matrix[
                                current_cord[0]][current_cord[1]] == 14 or num_matrix[
                                    current_cord[0]][current_cord[1]] == 15 and num_matrix[current_cord[0] + 1][current_cord[1]] not in the_way:
            current_cord = (current_cord[0] + 1, current_cord[1])
            the_way.append(current_cord)
        elif num_matrix[current_cord[0]][current_cord[1]] == 4 or num_matrix[
            current_cord[0]][current_cord[1]] == 5 or num_matrix[
                current_cord[0]][current_cord[1]] == 6 or num_matrix[
                    current_cord[0]][current_cord[1]] == 7 or num_matrix[
                        current_cord[0]][current_cord[1]] == 12 or num_matrix[
                            current_cord[0]][current_cord[1]] == 13 or num_matrix[
                                current_cord[0]][current_cord[1]] == 14 or num_matrix[
                                    current_cord[0]][current_cord[1]] == 15 and num_matrix[current_cord[0]][current_cord[1] + 1] not in the_way:
            current_cord = (current_cord[0], current_cord[1] + 1) 
            the_way.append(current_cord)
        elif (num_matrix[current_cord[0]][current_cord[1]] == 8
                or num_matrix[current_cord[0]][current_cord[1]] == 9
                or num_matrix[current_cord[0]][current_cord[1]] == 10
                or num_matrix[current_cord[0]][current_cord[1]] == 11
                or num_matrix[current_cord[0]][current_cord[1]] == 12
                or num_matrix[current_cord[0]][current_cord[1]] == 13
                or num_matrix[current_cord[0]][current_cord[1]] == 14
                or num_matrix[current_cord[0]][current_cord[1]] == 15
                and num_matrix[current_cord[0]][current_cord[1] -1] not in the_way):
            current_cord = (current_cord[0], current_cord[1] - 1)
            the_way.append(current_cord)
        else:
            the_way.pop()
            
        
    return []

make_the_maze(16, 16)




#coas del chatgpt para revisardef find_the_way(num_matrix: list[list[int]], start_point: tuple[int, int], end_point: tuple[int, int]) -> list[tuple[int, int]]:
    #def can_go(direction: int, current_value: int) -> bool:
    #    """Verifica si puedes ir en esa dirección según el valor de la celda"""
    #    # up=1, down=2, right=4, left=8
    #    return (current_value & direction) != 0
    
    #def dfs(current: tuple[int, int], path: list[tuple[int, int]], visited: set) -> list[tuple[int, int]]:
    #    if current == end_point:
    #        return path
        
    #    current_value = num_matrix[current[0]][current[1]]
    #    directions = [(-1, 0, 1), (1, 0, 2), (0, 1, 4), (0, -1, 8)]  # (dy, dx, bit)
        
    #    for dy, dx, bit in directions:
    #        next_pos = (current[0] + dy, current[1] + dx)
            
    #        # Verifica si es válido, no está visitado y puedes ir en esa dirección
    #        if (0 <= next_pos[0] < len(num_matrix) and 
    #            0 <= next_pos[1] < len(num_matrix[0]) and
    #            next_pos not in visited and
    #            can_go(bit, current_value)):
                
    #            visited.add(next_pos)
    #            result = dfs(next_pos, path + [next_pos], visited)
    #            if result:
    #                return result
    #            visited.remove(next_pos)  # Backtracking: deshace la visita
        
    #    return None
    
    #visited = {start_point}
    #path = dfs(start_point, [start_point], visited)
    #return path if path else []
