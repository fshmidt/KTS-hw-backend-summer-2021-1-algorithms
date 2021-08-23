__all__ = (
    'even_odd',
)


def even_odd(arr: list[int]) -> float:
    a = 0
    even_sum = 0
    odd_sum = 0
    while (len(arr) - a):
        if arr[a] % 2 == 0:
            even_sum += arr[a]
        else:
            odd_sum += arr[a]
        a += 1
    if odd_sum == 0.0:
        return 0.0
    return even_sum / odd_sum
