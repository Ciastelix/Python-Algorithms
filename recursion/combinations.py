def combinations_helper(
    n: int, current: list[int], available: list[bool]
) -> list[list[int]]:
    if len(current) == 2 * n:
        return [current]

    result = []
    for i in range(1, n + 1):
        if available[i]:
            idx = len(current)
            if idx - i - 1 >= 0 and current[idx - i - 1] == i:
                available[i] = False
                next_current = current + [i]
                result += combinations_helper(n, next_current, available)
                available[i] = True

    return result


def combinations(n: int) -> list[list[int]]:
    if n <= 0:
        return []
    return combinations_helper(n, [], [True] * (n + 1))
