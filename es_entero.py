def is_integer(value: float) -> bool:
    if value != int(value):
        return False
    else:
        return True