import random
def make_the_maze(total_height_size: int, total_width_size: int) -> list[list[int]]:  # añadir matrix: list[list[Cell]],
    num_matrix: list[list[int]] = []
    for heigth_it in range(0, total_height_size):
        row: list[int] = []
        for widht_it in range(0, total_width_size):
            row.append(0)
        num_matrix.append(row)

    while True:
        random_w = random.randint(1, total_width_size -1)
        if random_w % 2 != 0:
            break
    while True:
        random_h = random.randint(0, total_height_size -1)
        if random_h % 2 != 0:
            break
    start_point: tuple[int, int] = random_h, random_w
    num_matrix[start_point[0]][start_point[1]] = 20
    trash: list[tuple] = [start_point]
    visited: list[tuple] = [start_point]
    up: tuple[int, int] =  (-1, 0)      # + 2
    down: tuple[int, int] = (1, 0)      # + 1
    right: tuple[int, int] = (0, 1)     # + 4
    left: tuple[int, int] = (0, -1)     # + 8
    direcctions: list[tuple] = [up, down, right, left]
    random_direc: tuple = random.choice(direcctions)
    current_cord: tuple = start_point
    temp_cord: tuple
    flag: bool = True
    while len(visited) != (total_height_size * total_width_size):
        temp_cord = current_cord + random_direc
        if random_direc == up:
            if current_cord[0] + random_direc[0] > 0:
                for h in visited:
                    if temp_cord == h:
                        flag = False
                if flag:
                    current_cord = temp_cord
                    visited.append(current_cord)
                    num_matrix[current_cord[0]][current_cord[1]] += 1      #vacio!
                    num_matrix[current_cord[0]+ 1][current_cord[1]] += 2   #rompo pared de abajo y    juntanterior con este
        elif random_direc == down:
            if current_cord[0] + random_direc[0] < total_height_size:
                for h in visited:
                    if temp_cord == h:
                        flag = False
                if flag:
                    current_cord = temp_cord
                    visited.append(current_cord)
                    num_matrix[current_cord[0]][current_cord[1]] += 2       #vacio
                    num_matrix[current_cord[0 - 1]][current_cord[1]] += 1    #rompo pared de arriba y junto anterior con este
        elif random_direc == right:
            if current_cord[1] + random_direc[1] < total_width_size:
                for h in visited:
                    if temp_cord == h:
                        flag = False
                if flag:
                    current_cord = temp_cord
                    visited.append(current_cord)
                    num_matrix[current_cord[0]][current_cord[1]] += 4        #vacio
                    num_matrix[current_cord[0]][current_cord[1] - 1] += 8    #rompo pared de izquierda y junto con lo anterior
        elif random_direc == left:
            if random_direc[1] + random_direc[1] > 2:
                for h in visited:
                    if temp_cord == h:
                        flag = False
                if flag:
                    current_cord = temp_cord
                    visited.append(current_cord)
                    num_matrix[current_cord[0]][current_cord[1]] += 8        #vacio 
                    num_matrix[current_cord[0]][current_cord[1]+ 1] += 4     #rompo pared de derecha y junto con lo anterior
        random_direc = random.choice(direcctions)
    
    
    
    for a in num_matrix:
        print(a)
    
    return num_matrix

make_the_maze(15, 15)

