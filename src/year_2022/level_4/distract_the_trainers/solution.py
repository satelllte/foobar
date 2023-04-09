# Technique used: https://en.wikipedia.org/wiki/Blossom_algorithm

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def is_power_of_two(x):
    return x & (x - 1) == 0

def is_infinite_pair(x, y):
    return not is_power_of_two(int((x + y) / gcd(x, y)))

def create_graph(items):
    graph = { i: [] for i in range(len(items)) }

    for i in range(len(items)):
        for j in range(i, len(items)):
            if i == j:
                continue
            if is_infinite_pair(items[i], items[j]):
                graph[i].append(j)
                graph[j].append(i)

    return graph

def calculate_max_matches(graph):
    max_matches = 0

    while len(graph) > 1:
        min_path = min(graph, key=lambda x: len(graph[x]))

        if (len(graph[min_path])) < 1:
            del graph[min_path]
        else:
            pair = [len(graph[graph[min_path][0]]) + 1, 1]

            for node in graph[min_path]:
                if len(graph[node]) < pair[0]:
                    pair = [len(graph[node]), node]

                for i in range(len(graph[node])):
                    if graph[node][i] == min_path:
                        del graph[node][i]
                        break

            for node in graph[pair[1]]:
                for i in range(len(graph[node])):
                    if graph[node][i] == pair[1]:
                        del graph[node][i]
                        break

            del graph[min_path]
            del graph[pair[1]]
            max_matches += 2

    return max_matches

def solution(items):
    graph = create_graph(items)
    max_matches = calculate_max_matches(graph)
    return len(items) - max_matches
