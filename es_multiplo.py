def is_multiple(n: int, m: int) -> bool:
    if m == 0:
        return False
    elif n % m != 0:
        return False
    else:
        return True