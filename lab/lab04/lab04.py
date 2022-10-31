from operator import le, truediv
import re


HW_SOURCE_FILE = __file__


def summation(n, term):
    """Return the sum of numbers 1 through n (including n) wíth term applied to each number.
    Implement using recursion!

    >>> summation(5, lambda x: x * x * x) # 1^3 + 2^3 + 3^3 + 4^3 + 5^3
    225
    >>> summation(9, lambda x: x + 1) # 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    54
    >>> summation(5, lambda x: 2**x) # 2^1 + 2^2 + 2^3 + 2^4 + 2^5
    62
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'summation',
    ...       ['While', 'For'])
    True
    """
    assert n >= 1
    if n == 1:
        return term(1)
    else:
        return term(n) + summation(n-1, term)


def pascal(row, column):
    """Returns the value of the item in Pascal's Triangle
    whose position is specified by row and column.
    >>> pascal(0, 0)    # The top left (the point of the triangle)
    1
    >>> pascal(0, 5)	# Empty entry; outside of Pascal's Triangle
    0
    >>> pascal(3, 2)	# Row 3 (1 3 3 1), Column 2
    3
    >>> pascal(4, 2)     # Row 4 (1 4 6 4 1), Column 2
    6
    """
    if column > row:
        return 0
    if row <= 0 or column <= 0:
        return 1
    return pascal(row-1, column) + pascal(row-1, column-1)


def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    
    def helper(x, y):
        if x > m:
            return 0
        elif y > n:
            return 0
        elif x == m and y == n:
            return 1
        else:
            return helper(x+1, y) + helper(x, y+1)

    return helper(1, 1)

def path_no_helper(m, n):
    """ from topright to bottomleft
    just change the direction, get rid of the helper function
    """
    if m == 1 and n == 1:
        return 1
    if m < 1 or n < 1:
        return 0
    return path_no_helper_faster(m - 1, n) + path_no_helper_faster(m, n - 1)

def path_no_helper_faster(m, n):
    """ from topright to bottomleft
    if reach edge the found the way because can only move one way left
    """
    if m == 1 or n == 1:
        return 1
    return path_no_helper_faster(m - 1, n) + path_no_helper_faster(m, n - 1)
    



def couple(s, t):
    """Return a list of two-element lists in which the i-th element is [s[i], t[i]].

    >>> a = [1, 2, 3]
    >>> b = [4, 5, 6]
    >>> couple(a, b)
    [[1, 4], [2, 5], [3, 6]]
    >>> c = ['c', 6]
    >>> d = ['s', '1']
    >>> couple(c, d)
    [['c', 's'], [6, '1']]
    """
    assert len(s) == len(t)
    return [[s[i],t[i]] for i in range(len(s))]


def double_eights(n):
    """ Returns whether or not n has two digits in row that
    are the number 8. Assume n has at least two digits in it.

    >>> double_eights(1288)
    True
    >>> double_eights(880)
    True
    >>> double_eights(538835)
    True
    >>> double_eights(284682)
    False
    >>> double_eights(588138)
    True
    >>> double_eights(78)
    False
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'double_eights', ['While', 'For'])
    True
    """
    def helper(n, last):
        if n == 0:
            return False
        elif n % 10 == 8 and last == 8:
            return True
        return helper(n // 10, n % 10)

    return helper(n, 0)

def double_eights_no_helper(n):
    """ simpler think one more step
    """
    last, second_last = n % 10, n // 10 % 10
    if n < 100:
        return False
    return (last == 8 and second_last == 8) or double_eights_no_helper(n // 10)




def coords(fn, seq, lower, upper):
    """
    >>> seq = [-4, -2, 0, 1, 3]
    >>> fn = lambda x: x**2
    >>> coords(fn, seq, 1, 9)
    [[-2, 4], [1, 1], [3, 9]]
    """
    return [[x,fn(x)] for x in seq if lower <= fn(x) <= upper]


def riffle(deck):
    """Produces a single, perfect riffle shuffle of DECK, consisting of
    DECK[0], DECK[M], DECK[1], DECK[M+1], ... where M is position of the
    second half of the deck.  Assume that len(DECK) is even.
    >>> riffle([3, 4, 5, 6])
    [3, 5, 4, 6]
    >>> riffle(range(20))
    [0, 10, 1, 11, 2, 12, 3, 13, 4, 14, 5, 15, 6, 16, 7, 17, 8, 18, 9, 19]
    """
    "*** YOUR CODE HERE ***"
    return [deck[i//2 if i % 2 == 0 else len(deck)//2 + i// 2] for i in range(len(deck))]
