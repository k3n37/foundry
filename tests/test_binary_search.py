from foundations_lab.binary_search import binary_search


def test_binary_search_returns_index_for_existing_value() -> None:
    assert binary_search([1, 3, 5, 8, 13], 8) == 3


def test_binary_search_returns_negative_one_for_missing_value() -> None:
    assert binary_search([1, 3, 5, 8, 13], 7) == -1
