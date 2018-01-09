from operator import itemgetter
original = {1: 2, 2: 3, 3: 1}
ordered = dict(sorted(original.items(), key=itemgetter(1)))
print(ordered)
