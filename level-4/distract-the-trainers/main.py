from solution import solution, is_infinite_pair, is_infinite_pair_naive, is_power_of_two, gcd

# for i in range(1, 20):
#     for j in range(1, 20):
#         if not i == j and is_infinite_pair(i, j):
#             print('({}, {}) --> {} | sum: {} | sum bin: {}'.format(i, j, is_infinite_pair(i, j), i + j, bin(i + j)))
for i in range(1000, 1100):
    for j in range(1000, 1200):
        result = is_infinite_pair(i, j)
        result_naive = is_infinite_pair_naive(i, j)
        if not result == result_naive:
            print('ERROR! ({}, {}) ===> result: {} | result_naive: {}'.format(i, j, result, result_naive))

        # if not i == j and is_infinite_pair(i, j):
        # if is_infinite_pair(i, j):
        # print('({}, {}) --> {} | sum: {} | gcd: {} | sum/gcd: {}'.format(i, j, is_infinite_pair(i, j), i + j, gcd(i, j), (i + j) / gcd(i, j)))

# print('({}, {}) --> {}'.format(9, 3, is_infinite_pair(9, 3)))

# is_infinite_pair(1000, 8)
# is_power_of_two(1)
# for i in range(1, 65):
#     print('is_power_of_two | {} | {}'.format(i, is_power_of_two(i)))

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
