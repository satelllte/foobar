from solution import solution

arr = [2,2,2,2,4]
print('arr: {} | solution: {}'.format(arr, solution(arr)))

assert solution([1, 7, 3, 21, 13, 19]) == 0
assert solution([7, 1, 3, 21, 13, 19]) == 0
assert solution([7, 3, 1, 21, 13, 19]) == 0
assert solution([7, 3, 1, 13, 19, 21]) == 0

assert solution([1, 1]) == 2
assert solution([2, 2]) == 2
assert solution([3, 3]) == 2
assert solution([19, 19]) == 2
assert solution([19214, 19214]) == 2
assert solution([1073741822, 1073741822]) == 2
assert solution([1073741823, 1073741823]) == 2

assert solution([3, 3, 3, 3]) == 4
assert solution([27000, 27000, 27000, 27000]) == 4

assert solution([3, 3, 3, 3, 3]) == 5
assert solution([6, 6, 6, 6, 6]) == 5

assert solution([1, 4]) == 0
assert solution([4, 1]) == 0

assert solution([3, 5]) == 2
assert solution([5, 3]) == 2

assert solution([3, 5, 5, 3, 5]) == 5
assert solution([3, 5, 5, 3]) == 4
assert solution([3, 5, 5, 3, 5, 3, 3, 5]) == 8

assert solution([2,2,4]) == 1
assert solution([2,4,2]) == 1
assert solution([2,4,2,2,2]) == 3

"""
Combinations (N) = N!
Pairs at a time (N) = floor(N/2)

-----

N = 1
Elements = [1]

= 1 combination
= 0 pairs

-----

N = 2
Elements = [1,2]

= 2 combinations
= 1 pair

-----

N = 3
Elements = [1,2,3]

[1,2]
[1,3]
[2,3]

= 6 combinations
= 3 pair combinations
= 1 pair at a time

-----

N = 4
Elements = [1,2,3,4]

[1,2] -> [3,4]
[1,3] -> [2,4]
[1,4] -> [2,3]

= 24 combinations
= 3 pair combinations
= 2 pairs at a time

-----

N = 5
Elements = [1,2,3,4,5]

[1,2] -> [3,4], [3,5]
[1,3] -> [2,4], [2,5]
[1,4] -> [2,3], [2,5]
[1,5] -> [2,3], [2,4]

= 120 combinations
= 8 pair combinations
= 2 pairs at a time

-----

N = 6
Elements = [1,2,3,4,5,6]

[1,2] -> [3,4] -> [5,6]
[1,2] -> [3,5] -> [4,6]
[1,2] -> [3,6] -> [4,5]

[1,3] -> [2,4] -> [5,6]
[1,3] -> [2,5] -> [4,6]
[1,3] -> [2,6] -> [4,5]

[1,4] -> [2,3] -> [5,6]
[1,4] -> [2,5] -> [3,6]
[1,4] -> [2,6] -> [3,5]

[1,5] -> [2,3] -> [4,6]
[1,5] -> [2,4] -> [3,6]
[1,5] -> [2,6] -> [3,4]

[1,6] -> [2,3] -> [4,5]
[1,6] -> [2,4] -> [3,5]
[1,6] -> [2,5] -> [3,4]

= 720 combinations
= 15 pair combinations
= 3 pairs at a time


"""
