from p29_01_search_in_sorted_array import search_in_sorted_array


def test_finds_target_index():
    assert search_in_sorted_array([1, 3, 5, 7, 9], 5) == 2


def test_missing_returns_minus_one():
    assert search_in_sorted_array([1, 3, 5, 7, 9], 4) == -1
