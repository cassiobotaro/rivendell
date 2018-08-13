''' Dijkstra's algorithm module'''

# the graph
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["end"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["end"] = 5

graph["end"] = {}

# the costs table
inendity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["end"] = inendity

# the parents table
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["end"] = None

processed = []


def find_lowest_cost_node(costs):
    '''Find the lowest cost node.'''
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def search(graph, costs, parents):
    '''Find the lowest-cost in a pounded graph.'''
    node = find_lowest_cost_node(costs)
    while node:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)


def path(parents):
    '''Draw path from start to end'''
    parent = parents["end"]
    path = ["end"]
    while parent:
        path.insert(0, parent)
        parent = parents.get(parent)
    return path


def main():
    '''Search shortest path from start to end.'''
    search(graph, costs, parents)
    print("Path: ", " -> ".join(path(parents)))


if __name__ == "__main__":
    main()
