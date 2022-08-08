from solution import solution

assert solution([
    [0, 1, 1, 0],
    [0, 0, 0, 1],
    [1, 1, 0, 0],
    [1, 1, 1, 0],
]) == 7

assert solution([
    [0, 0, 0, 0, 0, 0], 
    [1, 1, 1, 1, 1, 0], 
    [0, 0, 0, 0, 0, 0], 
    [0, 1, 1, 1, 1, 1], 
    [0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0],
]) == 11

assert solution([
    [0, 0],
    [0, 0],
]) == 3

assert solution([
    [0, 1],
    [0, 0],
]) == 3

assert solution([
    [0, 0],
    [1, 0],
]) == 3

assert solution([
    [0, 1],
    [1, 0],
]) == 3
