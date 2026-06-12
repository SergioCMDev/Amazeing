*This project has been created as part of the 42 curriculum by scristau, adrvarga*

**Desctiption**
The goal of this project is to generate a procedural maze based on parameters read from an editable `.txt` file. The program parses the file, generates the maze grid, calculates its solution, and prints everything in the terminal using ASCII characters and ANSI colors to highlight the path.

**Instructions**
Compile the project using the following command:
make
After that, you will see a display with all the comands that you ca n do.
If you want to see the maze, choose "make run".
Now you will see the generic maze and under the maze a few options to generate another mazes, change colors, show/hide solutions, an exit.
You can modify the config.txt to change the configuration of the maze.
To finish the proyect you will recieve output_maze.txt. Here you have the hexadecimal last maze that you saw, the start and finish poin and the solution in coordinates N, S, E, W.
**Resources**
The knowledge of the others students in 42 Malaga.
https://maestraonline.com/simbolos-ascii-e-iconos-para-todos-los-gustos/ 3/6/2026
https://www.youtube.com/watch?v=6DCueDFA9Eg 20/5/2026.
The IA to help us with litle things like calculate the terminal size or to search information about libreries.
**Structure of config file**
WIDTH=50
HEIGHT=40
ENTRY=5,2
EXIT=4,4
OUTPUT_FILE=utils.py
PERFECT=FALSE
**Maze Generation Algorithm**
Algorithm: dfs.
Reason: It's the algorithm that fits better with the characteristics of this proyect.
**Reusable Code**
Matrix Utilities: The functions designed to allocate and safely free memory for the 2D grid array without leaks.
**Team and Project Management**
adrvarga: Algorithm generation, pathfinding solver, and ASCII/ANSI rendering.
scristau: File parser, input validation, and error management.
**Planning and Evolution**

