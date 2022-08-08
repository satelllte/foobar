def solution(map):
    w = len(map)
    h = len(map[0])

    # (x,y,d):
    # x - x-axis position
    # y - y-axis position
    # d - number of wall destroyers left

    step_positions = {(0,0,1)}
    cache = {(0,0,1)}

    step = 0

    while True:
        finish = False
        step += 1
        next_step_positions = set()

        for position in step_positions:
            x,y,d = position

            position_t = (x, y - 1, d)
            position_b = (x, y + 1, d)
            position_l = (x - 1, y, d)
            position_r = (x + 1, y, d)

            for possible_position in [position_t, position_b, position_l, position_r]:
                x,y,d = possible_position

                if x < 0 or x >= w:
                    continue
                if y < 0 or y >= h:
                    continue

                if map[x][y] and d:
                    d -= 1
                    possible_position = (x,y,d)

                if possible_position in cache:
                    continue

                next_step_positions.add(possible_position)
                cache.add(possible_position)

                if x == w-1 and y == h-1:
                    finish = True
                    break

        step_positions = next_step_positions

        if finish:
            break

    return step + 1
