def alpha_6k1(n: int, k: int) -> int:
    """a(n) = ( 9*n + q + 2 ) / 6"""
    return k + ((n + (n << 1) + 1) >> 1)


def gamma_6k1(n: int, k: int) -> int:
    """g(n) = ( 9*n + 2*q - 2 ) / 12"""
    return k + ((n + (n << 1)) >> 2)


def sigma_6k1(n: int) -> int:
    """s(n) = ( n - 2 ) / 4"""
    return (n - 2) >> 2


def alpha_6k5(n: int, k: int) -> int:
    """a(n) = ( 9*n + q + 1 ) / 6"""
    return k + ((n + (n << 1) + 2) >> 1)


def gamma_6k5(n: int, k: int) -> int:
    """g(n) = ( 9*n + 2*q - 1 ) / 12"""
    return k + ((n + (n << 1) + 3) >> 2)


def sigma_6k5(n: int) -> int:
    """s(n) = ( n - 1 ) / 4"""
    return (n - 1) >> 2


def col_6k1(n: int, k: int = 1) -> int:
    if (n & 1) == 1:
        return alpha_6k1(n, k)
    elif (n & 3) == 0:
        return gamma_6k1(n, k)
    else:
        return sigma_6k1(n)


def col_6k5(n: int, k: int = 1) -> int:
    if (n & 1) == 0:
        return alpha_6k5(n, k)
    elif (n & 3) == 3:
        return gamma_6k5(n, k)
    else:
        return sigma_6k5(n)


def is_a_divisible_by_b(a: int, b: int) -> bool:
    """
    Checks if 'a' is divisible by 'b' with the condition that 'b'
    must be congruent to either 1 or 5 modulo 6 and 'a' >= 'b'.

    Note:
        This function utilizes a Python set to keep track of visited values during the checking process. 
        Consequently, it may consume a significant amount of memory when testing numbers 
        that produce very large loops.
    """

    assert a >= b
    assert (b % 6 == 1) or (b % 6 == 5)

    if (b % 6) == 1:
        G = int((2 * b - 2) / 3)
        k = int((b - 1) / 6)
        col = lambda n: col_6k1(n, k)
    else:
        G = int((2 * b - 1) / 3)
        k = int((b - 5) / 6)
        col = lambda n: col_6k5(n, k)

    visited = set()
    n = a + G

    while True:
        n = col(n)
        if n in visited:
            break
        else:
            visited.add(n)

    if n == G:
        return True
    else:
        return False


def main() -> None:
    print(is_a_divisible_by_b(55, 55))


if __name__ == "__main__":
    main()
