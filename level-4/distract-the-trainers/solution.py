def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def is_power_of_two(x):
    return x & (x - 1) == 0

def is_infinite_pair(x, y):
    return not is_power_of_two((x + y) / gcd(x, y))

def graph_comparator(graph):
    """
    Compare the graph elements by the length of each of their nodes.
    """
    return lambda x: len(graph[x])


def distract_the_trainers(graph):
    """
    Pair up the trainers in such a way that the maximum number of trainers go into an infinite thumb wrestling loop.
    We don't pair off trainers with the same number of bananas (if we do, their game will end and they will go back to
    work). We know enough trainer psychology to know that the one who has more bananas always gets over-confident and
    loses. Once a match begins, the pair of trainers will continue to thumb wrestle and exchange bananas, until both
    of them have the same number of bananas. Once that happens, both of them will lose interest and go back to
    supervising the bunny workers, and you don't want THAT to happen!
    The following proved useful and interesting for this implementation:
    References:
    Micali, S. and Vazirani, V.V., 1980, October. "An O (v| v| c| E|) algorithm for finding maximum matching in general
    graphs". In 21st Annual Symposium on Foundations of Computer Science (SFCS 1980) (pp. 17-27). IEEE.
    Wikipedia. Blossom Algorithm. https://en.wikipedia.org/wiki/Blossom_algorithm
    Wolfram. Blossom Algorithm. https://mathworld.wolfram.com/BlossomAlgorithm.html
    :param graph: a graph
    :return: the number of trainers that have gone into an infinite thumb wrestling loop and are now distracted
    """
    distracted_trainers = 0
    remaining_nodes = len(graph)

    while len(graph) > 1 and remaining_nodes >= 1:
        # Find the first min-length path in the graph. Note, there might be multiple paths of the same shortest length.
        min_length_path = min(graph, key=graph_comparator(graph))

        if (len(graph[min_length_path])) < 1:
            del graph[min_length_path]
        else:
            matched_pair = [len(graph[graph[min_length_path][0]]) + 1, 1]

            for node in graph[min_length_path]:
                if len(graph[node]) < matched_pair[0]:
                    matched_pair = [len(graph[node]), node]

                for i in range(len(graph[node])):
                    if graph[node][i] == min_length_path:
                        # We don't pair off trainers with the same number of bananas
                        del graph[node][i]
                        break

            for node in graph[matched_pair[1]]:
                for i in range(len(graph[node])):
                    if graph[node][i] == matched_pair[1]:
                        # We don't pair off trainers with the same number of bananas
                        del graph[node][i]
                        break

            del graph[min_length_path]
            del graph[matched_pair[1]]
            distracted_trainers += 2

        if len(graph) > 1:
            remaining_nodes = len(graph)

    return distracted_trainers

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

def solution(items):
    graph = create_graph(items)
    distracted_trainers = distract_the_trainers(graph)
    remaining_trainers = len(items) - distracted_trainers
    return remaining_trainers
