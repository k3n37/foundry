from collections.abc import Sequence


def binary_search(values: Sequence[int], target: int) -> int:
    """Return the index of target in a sorted sequence or -1 if absent."""
    left = 0
    right = len(values) - 1

    while left <= right:
        middle = (left + right) // 2
        candidate = values[middle]

        if candidate == target:
            return middle
        if candidate < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1
