def power(number: int, n: int) -> int:
    if n == 0:
        return 1
    else:
        return number * power(number, n - 1)
