def Q1():
    """
    >>> x = [1, 2, 3]
    >>> y = x
    >>> x += [4]
    >>> x
    [1, 2, 3, 4]
    >>> y
    [1, 2, 3, 4]

    >>> x = [1, 2, 3]
    >>> y = x
    >>> x = x + [4]
    >>> x
    [1, 2, 3, 4]
    >>> y
    [1, 2, 3]

    >>> s1 = [1, 2, 3]
    >>> s2 = s1
    >>> s1 is s2
    True

    >>> s2.extend([5, 6])
    >>> s1[4]
    6

    >>> s1.append([-1, 0, 1])
    >>> s2[5]
    [-1, 0, 1]

    >>> s3 = s2[:]
    >>> s3.insert(3, s2.pop(3))
    >>> len(s1)
    5

    >>> s1[4] is s3[6]
    True

    >>> s3[s2[4][1]]
    1

    >>> s1[:3] is s2[:3]
    False

    >>> s1[:3] == s2[:3]
    True

    >>> s1[4].append(2)

    >>> s3[6][3]
    2
    """
    pass


def add_this_many(x, el, s):
    """ Adds el to the end of s the number of times x occurs in s.
    >>> s = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """
    k = 0
    for e in s:
        if e == x:
            k = k + 1
    for _ in range(k):
        s.append(el)

def Q3():
    """
    >>> s = "cs61a"
    >>> s_iter = iter(s)
    >>> next(s_iter)
    'c'

    >>> next(s_iter)
    's'

    >>> list(s_iter)
    ['6', '1', 'a']

    >>> s = [[1, 2, 3, 4]]
    >>> i = iter(s)
    >>> j = iter(next(i))
    >>> next(j)
    1

    >>> s.append(5)

    >>> next(i)
    5

    >>> next(j)
    2

    >>> list(j)
    [3, 4]

    >>> next(i)
    Traceback (most recent call last):
    ...
    StopIteration

    """
    pass


def Q4():
    """

    >>> def infinite_generator(n):
    ...     yield n
    ...     while True:
    ...         n += 1
    ...         yield n

    >>> next(infinite_generator)
    Traceback (most recent call last):
    ...
    TypeError: 'function' object is not an iterator


    >>> gen_obj = infinite_generator(1)
    >>> next(gen_obj)
    1

    >>> next(gen_obj)
    2

    # >>> list(gen_obj)

    """
    pass


def filter_iter(iterable, f):
    """
    >>> is_even = lambda x: x % 2 == 0
    >>> list(filter_iter(range(5), is_even)) # a list of the values yielded from the call to filter_iter
    [0, 2, 4]
    >>> all_odd = (2*y-1 for y in range(5))
    >>> list(filter_iter(all_odd, is_even))
    []
    >>> naturals = (n for n in range(1, 100))
    >>> s = filter_iter(naturals, is_even)
    >>> next(s)
    2
    >>> next(s)
    4
    """
    for e in iterable:
        if f(e):
            yield e

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def helper(i):
        if i > (n ** 0.5): # Could replace with i == n
            return True
        elif n % i == 0:
            return False
        return helper(i + 1)
    return helper(2)

def primes_gen(n):
    """Generates primes in decreasing order.
    >>> pg = primes_gen(7)
    >>> list(pg)
    [7, 5, 3, 2]
    """
    if n == 1:
        return
    if is_prime(n):
        yield n
    yield from primes_gen(n-1)

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def preorder(t):
    """Return a list of the entries in this tree in the order that they
    would be visited by a preorder traversal (see problem description).

    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> preorder(numbers)
    [1, 2, 3, 4, 5, 6, 7]
    >>> preorder(tree(2, [tree(4, [tree(6)])]))
    [2, 4, 6]
    """
    return sum([preorder(b) for b in branches(t)], [label(t)])

def generate_preorder(t):
    """Yield the entries in this tree in the order that they
    would be visited by a preorder traversal (see problem description).

    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> gen = generate_preorder(numbers)
    >>> next(gen)
    1
    >>> list(gen)
    [2, 3, 4, 5, 6, 7]
    """
    yield label(t)
    for b in branches(t):
        yield from generate_preorder(b)

