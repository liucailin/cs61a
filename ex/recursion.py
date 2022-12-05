def collapse(n):
    """For non-negative N, the result of removing all digits that are equal
    to the digit on their right, so that no adjacent digits are the same.
    >>> collapse(1234)
    1234
    >>> collapse(12234441)
    12341
    >>> collapse(0)
    0
    >>> collapse(3)
    3
    >>> collapse(11200000013333)
    12013
    """
    left, last = n // 10, n % 10
    if left == 0:
        return last
    elif last == left % 10:
        return collapse(left)
    else:
        return collapse(left) * 10 + last

def repeat_digits(n):
    """Given a positive integer N, returns a number with each digit repeated.
    >>> repeat_digits(1234)
    11223344
    """
    last, rest = n % 10, n // 10
    if rest == 0:
        return last * 10 + last
    return repeat_digits(rest) * 100 + last * 10 + last

def pal(n):
    """Return a palindrome starting with n.
    >>> pal(12430)
    1243003421
    >>> pal(1)
    11
    """
    m = n
    while m:
        n, m = n * 10 + m % 10 , m//10
    return n

def reverseN(n):
    """ reverseN
    >>> reverseN(0)
    0
    >>> reverseN(12)
    21
    """
    num = 0
    while (n):
        num, n = num * 10 + n % 10, n // 10
    return num
    

def pal2(n):
    """ Return a palindrome starting with n.
    >>> pal2(1)
    11
    >>> pal2(12)
    1221
    """
    d = 0
    k = n
    while k:
        d = d + 1
        k = k // 10 
    return n * 10 ** d + reverseN(n)
    