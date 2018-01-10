# Using itemgetter
from operator import itemgetter
original = {1: 2, 2: 3, 3: 1}
ordered = dict(sorted(original.items(), key=itemgetter(1)))
print(ordered)

# Using lambda function
# Ascending
ordered = dict(sorted(original.items(), key=lambda x: x[1]))
print(ordered)

# Descending
ordered = dict(sorted(original.items(), key=lambda x: -x[1]))
print(ordered)
