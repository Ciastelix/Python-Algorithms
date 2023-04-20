def numbers(n: int) -> None:
    if n >= 0:
        print(n)
        return numbers(n - 1)
    else:
        return


numbers(5)
