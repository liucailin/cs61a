def slow_pow(base, exp):
    """ slow pow
    >>> slow_pow(2, 8)
    256
    >>> slow_pow(2, 15)
    32768
    >>> slow_pow(2, 0)
    1
    >>> slow_pow(1, 100)
    1
    """
    if exp == 0:
        return 1
    return base * slow_pow(base, exp - 1)


def slow_pow_iter(base, exp):
    """ slow pow
    >>> slow_pow_iter(2, 5)
    32
    >>> slow_pow_iter(2, 0)
    1
    >>> slow_pow_iter(1, 100)
    1
    """
    if exp == 0:
        return 1
    
    result = base
    while exp > 1:
        exp = exp - 1
        result = result * base
    
    return result


def fast_pow(base, exp):
    """ fast_pow
    >>> fast_pow(2, 8)
    256
    >>> fast_pow(2, 15)
    32768
    >>> fast_pow(2, 5)
    32
    >>> fast_pow(1, 100)
    1
    """
    if exp == 0:
        return 1
    elif exp % 2 == 0:
        n = fast_pow(base, exp // 2)
        return n * n
    else:
        return base * fast_pow(base, exp - 1)

def fast_pow_iter(base, exp):
    """ fast_pow
    >>> fast_pow_iter(2, 8)
    256
    >>> fast_pow_iter(2, 15)
    32768
    >>> fast_pow_iter(2, 5)
    32
    >>> fast_pow_iter(1, 100)
    1
    """
    ans = 1
    while exp:
        if exp & 1:
            ans *= base
        exp >>= 1
        base *= base
    return ans

fast_pow_iter(2,8)

if __name__ == '__main__':
    import timeit
    base, exp = 2, 100
    f1 = timeit.timeit(lambda: fast_pow(base, exp))
    f2 = timeit.timeit(lambda: fast_pow_iter(base, exp))
    f3 = timeit.timeit(lambda: slow_pow(base, exp))
    f4 = timeit.timeit(lambda: slow_pow_iter(base, exp))
    b = timeit.timeit(lambda: pow(base, exp))

    print(f"timeit of pow({base}, {exp})\nbuiltin:{b}\nfast_pow:{f1}\nfast_pow_iter:{f2}\nslow_pow:{f3}\nslow_pow_iter:{f4}")