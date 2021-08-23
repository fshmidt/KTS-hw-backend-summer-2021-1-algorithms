__all__ = (
    'is_prime',
)


def is_prime(number: int) -> bool:
    a = 2
    status = 0
    if number == 2:
        return True
    if number > 2:
        while number > a:
            if number % a == 0:
                return False
            else:
                return True
        a += 1
    else:
        return False
