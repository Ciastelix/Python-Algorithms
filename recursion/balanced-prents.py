def generate_parentheses_helper(left: int, right: int, current: str) -> list[str]:
    if left == 0 and right == 0:
        return [current]

    result = []
    if left > 0:
        result += generate_parentheses_helper(left - 1, right, current + "(")

    if right > left:
        result += generate_parentheses_helper(left, right - 1, current + ")")

    return result


def balanced_parentheses(n: int) -> list[str]:
    if n % 2 != 0:
        return []
    return generate_parentheses_helper(n // 2, n // 2, "")
