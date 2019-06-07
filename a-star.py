# The algorithm is implemeanted followed wikipedia
# https://en.wikipedia.org/wiki/A*_search_algorithm


def reconstruct_path(cameFrom, current):
    total_path = [current]
    while current in cameFrom.keys():
        current = cameFrom[current]
        total_path.append(current)
    return total_path


def get_neighbors()
def dist_between(current, neighbor):
    return 1

def A_star(start, goal):
    closeSet = {}
    openSet = {start}

    cameFrom = {}
    gScore = {}
    gScore[start] = 0

    fScore = {}
    fScore[start] = heuristic_cost(start, goal)

    while openSet:
        current = min(node for node in openSet, key=lambda node: fScore[node])
        if current == goal:
            return reconstruct_path(cameFrom, current)

        openSet.remove(current)
        closeSet.add(current)

        for neighbor in get_neighbors(current):
            if neighbor in closeSet:
                continue
            tentative_gScore = gScore[current] + dist_between(current, neighbor)
            if neighbor not in openSet:
                openSet.add(neighbor)
            elif tentative_gScore >= gScore[neighbor]:
                continue
            cameFrom[neighbor] = current
            gScore[neighbor] = tentative_gScore
            fScore[neighbor] = gScore[neighbor] + heuristic_cost(neighbor, goal)
