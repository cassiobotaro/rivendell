#!/usr/bin/env python3


def Σ(lower_bound, upper_bound, function):
    '''Summation is a math operator to easily represent a great sum of terms,
    even infinity.

    It's represented with the greek letter sigma.
    Sum terms from lower_bound until upper_bound, applying some function on
    each term.

    >>> Σ(1,5,lambda x:x)  # 1 + 2 + 3 + 4 + 5 = 15
    15
    '''
    return sum(function(index) for index in range(lower_bound,
                                                   upper_bound + 1))
