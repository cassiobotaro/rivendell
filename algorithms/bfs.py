'''Breadth-First Search module.  '''
from collections import deque

GRAPH = {}
GRAPH["you"] = ["alice", "bob", "claire"]
GRAPH["bob"] = ["anuj", "peggy"]
GRAPH["alice"] = ["peggy"]
GRAPH["claire"] = ["thom", "jonny"]
GRAPH["anuj"] = []
GRAPH["peggy"] = []
GRAPH["thom"] = []
GRAPH["jonny"] = []


def _sells_mango(person):
    return person.endswith("m")


def search(name):
    '''Search people who sells mango'''
    search_queue = deque()
    search_queue += GRAPH[name]
    verified = []
    while search_queue:
        person = search_queue.popleft()
        if person not in verified:
            if _sells_mango(person):
                print(f"{person} sells mango!")
                return True
            search_queue += GRAPH[person]
            verified.append(person)
    return False


def search_path_bookstyle(name):
    '''Returns path to people who sells mango, empty if not found.'''
    search_queue = deque([(name, [name]), ])
    verified = []
    while search_queue:
        person, path = search_queue.popleft()
        if person not in verified:
            if _sells_mango(person):
                return path
            search_queue += ((next_, path + [next_])
                             for next_ in GRAPH[person])
            verified.append(person)
    return []


def search_path(name):
    '''Returns path to people who sells mango, empty if not found.'''
    search_queue = deque([(name, [name]), ])
    while search_queue:
        person, path = search_queue.popleft()
        for next_ in set(GRAPH[person]) - set(path):
            if _sells_mango(next_):
                return path + [next_]
            search_queue.append((next_, path + [next_]))
    return []


def main():
    '''Search people who sells mango starting from you.'''
    search("you")
    print(search_path_bookstyle("you"))
    print(search_path("you"))


if __name__ == "__main__":
    main()
