# Order a dict by values

Given a dictionary, I want to sort its elements by their values, not by their keys.

E.g. {1:2, 2:1} becomes {2:1, 1:2}.

Firstly we get dict elements using function `items()`. The return is a list of tuples containing it's keys and values.
Then we sort this list based on second element of the tuple.
Finnaly we transform this list into a dict again.

Remembering that only works with python 3.6+.
