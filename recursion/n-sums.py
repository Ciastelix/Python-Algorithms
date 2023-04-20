def n_sums(n: int, current: str = "", even_sum: int = 0, odd_sum: int = 0) -> list[int]:
    if n <= 0:
        return []
    if len(current) == n:
        if even_sum == odd_sum:
            return [int(current)]
        else:
            return []

    result = []
    for i in range(10):
        next_current = current + str(i)
        if len(next_current) % 2 == 0:
            next_even_sum = even_sum + i
            next_odd_sum = odd_sum
        else:
            next_even_sum = even_sum
            next_odd_sum = odd_sum + i

        result += n_sums(n, next_current, next_even_sum, next_odd_sum)

    return result
