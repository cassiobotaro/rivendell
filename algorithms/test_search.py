import pytest

from search import binary_search, linear_search


@pytest.mark.parametrize("list_,item,expected,algorithm", [
    ([1, 2], 2, 1, linear_search),
    ([1, 2, 3, 4], 3, 2, linear_search),
    ([1, 2, 3], 1, 0, linear_search),
    ([1], 1, 0, linear_search),
    ([1, 2], 2, 1, binary_search),
    ([1, 2, 3, 4], 3, 2, binary_search),
    ([1, 2, 3], 1, 0, binary_search),
    ([1], 1, 0, binary_search),
])
def test_find_element_returns_index(list_, item, expected, algorithm):
    assert algorithm(list_, item) == expected


@pytest.mark.parametrize("list_,item,algorithm", [
    ([], 2, linear_search),
    ([], -1, linear_search),
    ([], 0, linear_search),
    ([], 2, binary_search),
    ([], -1, binary_search),
    ([], 0, binary_search),
])
def test_search_dont_find_returns_None(list_, item, algorithm):
    assert algorithm(list_, item) is None
