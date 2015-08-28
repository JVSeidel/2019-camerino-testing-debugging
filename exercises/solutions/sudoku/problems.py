"""Example Sudoku problems and solutions."""


# keys of problems that are easy to solve by brute force
# used by the tests
TEST_KEYS = ['easy1', 'hard1', 'hard2', 'swordfish1']

# ##### Example Sudoku problems

# Notes:
# 1) 'swordfish1' requires the complicated swordfish manoeuver
#    http://www.sudokuoftheday.com/pages/techniques-9.php
# 2) it takes a *long* time to solve 'minimal1' or 'minimal2' with
#    my brute-force solver

sudoku_problems = {'easy1': [[0,0,3,7,0,0,0,5,0],
                             [0,7,0,0,5,0,8,0,0],
                             [1,0,0,0,0,6,0,0,4],
                             [5,0,2,0,0,0,0,0,0],
                             [8,0,0,9,0,4,0,0,6],
                             [0,0,0,0,0,0,9,0,2],
                             [3,0,0,5,0,0,0,0,7],
                             [0,0,4,0,9,0,0,6,0],
                             [0,2,0,0,0,7,4,0,0]],
                   'hard1': [[0,0,0,0,5,8,0,0,9],
                             [5,0,8,3,0,0,0,0,6],
                             [0,0,3,4,0,0,0,0,0],
                             [7,0,0,0,0,4,3,5,0],
                             [8,0,0,0,0,0,0,0,2],
                             [0,4,1,5,0,0,0,0,8],
                             [0,0,0,0,0,3,8,7,0],
                             [0,0,0,0,0,5,0,0,0],
                             [3,2,0,8,1,0,0,6,0]],
                   'hard2': [[5,0,1,2,8,0,0,0,0],
                             [8,0,0,0,0,0,7,0,2],
                             [2,0,0,0,0,0,1,8,5],
                             [0,1,4,7,0,0,5,0,0],
                             [0,0,0,4,0,0,0,2,0],
                             [0,2,6,0,0,0,0,0,0],
                             [1,0,0,0,3,6,0,0,0],
                             [4,0,0,0,0,0,0,5,1],
                             [6,0,0,0,4,1,0,0,0]],
                   'minimal1':
                            [[0,0,0,0,0,0,0,1,0],
                             [4,0,0,0,0,0,0,0,0],
                             [0,2,0,0,0,0,0,0,0],
                             [0,0,0,0,5,0,4,0,7],
                             [0,0,8,0,0,0,3,0,0],
                             [0,0,1,0,9,0,0,0,0],
                             [3,0,0,4,0,0,2,0,0],
                             [0,5,0,1,0,0,0,0,0],
                             [0,0,0,8,0,6,0,0,0]],
                   'minimal2':
                            [[2,0,0,4,0,8,0,0,0],
                             [1,0,0,0,0,0,0,3,0],
                             [0,0,0,0,0,0,0,0,0],
                             [0,6,0,0,4,0,0,0,0],
                             [0,0,0,2,0,0,0,5,0],
                             [0,8,5,0,0,0,0,0,0],
                             [0,0,0,1,0,0,2,0,0],
                             [7,0,0,3,0,0,0,0,0],
                             [0,0,0,0,0,0,5,0,8]],
                   'swordfish1':
                            [[0,0,0,4,7,0,6,0,0],
                             [0,0,4,0,0,0,3,0,5],
                             [9,2,0,0,0,0,0,0,0],
                             [0,3,1,0,0,0,0,0,0],
                             [0,0,0,9,3,6,0,0,0],
                             [0,0,0,0,0,0,2,8,0],
                             [0,0,0,0,0,0,0,1,6],
                             [4,0,8,0,0,0,9,0,0],
                             [0,0,7,0,5,2,0,0,0]]
                    }

# ##### Solutions to problems
sudoku_solutions = {'easy1': [[4,8,3,7,1,2,6,5,9],
                              [2,7,6,4,5,9,8,1,3],
                              [1,5,9,8,3,6,7,2,4],
                              [5,9,2,6,7,3,1,4,8],
                              [8,3,1,9,2,4,5,7,6],
                              [6,4,7,1,8,5,9,3,2],
                              [3,6,8,5,4,1,2,9,7],
                              [7,1,4,2,9,8,3,6,5],
                              [9,2,5,3,6,7,4,8,1 ]],
                    'hard1': [[4,6,2,7,5,8,1,3,9],
                              [5,7,8,3,9,1,4,2,6],
                              [9,1,3,4,6,2,5,8,7],
                              [7,9,6,2,8,4,3,5,1],
                              [8,3,5,1,7,9,6,4,2],
                              [2,4,1,5,3,6,7,9,8],
                              [1,5,9,6,2,3,8,7,4],
                              [6,8,7,9,4,5,2,1,3],
                              [3,2,4,8,1,7,9,6,5]],
                    'hard2': [[5,7,1,2,8,4,9,6,3],
                              [8,6,3,1,9,5,7,4,2],
                              [2,4,9,6,7,3,1,8,5],
                              [3,1,4,7,6,2,5,9,8],
                              [7,8,5,4,1,9,3,2,6],
                              [9,2,6,3,5,8,4,1,7],
                              [1,9,2,5,3,6,8,7,4],
                              [4,3,8,9,2,7,6,5,1],
                              [6,5,7,8,4,1,2,3,9]],
                    'minimal1':
                             [[6,9,3,7,8,4,5,1,2],
                              [4,8,7,5,1,2,9,3,6], 
                              [1,2,5,9,6,3,8,7,4],
                              [9,3,2,6,5,1,4,8,7],
                              [5,6,8,2,4,7,3,9,1],
                              [7,4,1,3,9,8,6,2,5],
                              [3,1,9,4,7,5,2,6,8],
                              [8,5,6,1,2,9,7,4,3],
                              [2,7,4,8,3,6,1,5,9]],
                    'swordfish1':
                             [[3,1,5,4,7,9,6,2,8],
                              [7,8,4,2,6,1,3,9,5],
                              [9,2,6,5,8,3,1,4,7],
                              [5,3,1,7,2,8,4,6,9],
                              [8,4,2,9,3,6,5,7,1],
                              [6,7,9,1,4,5,2,8,3],
                              [2,5,3,8,9,4,7,1,6],
                              [4,6,8,3,1,7,9,5,2],
                              [1,9,7,6,5,2,8,3,4]]
                    }
