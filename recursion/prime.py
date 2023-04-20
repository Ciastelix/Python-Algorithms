def prime(n: int, i: int = 2) -> bool:
    if i * i > n:
        return True
    if n % i == 0:
        return False
    return prime(n, i + 1)
