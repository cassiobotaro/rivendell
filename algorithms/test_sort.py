import pytest

from sort import find_smallest, selection_sort


@pytest.mark.parametrize("items,expected", [
    ([1, 2], 0),
    ([3, 2, 1], 2),
    ([3, 1, 2], 1),
])
def test_find_smallest(items, expected):
    assert find_smallest(items) == expected


@pytest.mark.parametrize("items,expected", [
    ([1, 2], [1, 2]),
    ([3, 2, 1], [1, 2, 3]),
    ([3, 1, 2], [1, 2, 3]),
])
def test_selection_sort(items, expected):
    assert selection_sort(items) == expected
