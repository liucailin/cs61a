def min_abs_indices(s):
    """Indices of all elements in list s that have the smallest absolute value.

    >>> min_abs_indices([-4, -3, -2, 3, 2, 4])
    [2, 4]
    >>> min_abs_indices([1, 2, 3, 4, 5])
    [0]
    """
    min_abs = min(map(abs, s))
    return [i for i in range(len(s)) if abs(s[i]) == min_abs]


def largest_adj_sum(s):
    """Largest sum of two adjacent elements in a list s.

    >>> largest_adj_sum([-4, -3, -2, 3, 2, 4])
    6
    >>> largest_adj_sum([-4, 3, -2, -3, 2, -4])
    1
    """
    return max([a + b for a, b in zip(s[:-1], s[1:])])
    return max([s[i] + s[i+1] for i in range(len(s)-1)])


def digit_dict(s):
    """Map each digit d to the lists of elements in s that end with d.

    >>> digit_dict([5, 8, 13, 21, 34, 55, 89])
    {1: [21], 3: [13], 4: [34], 5: [5, 55], 8: [8], 9: [89]}
    """
    last_digits = list(map(lambda x: x % 10, s))
    return {i: [x for x in s if x % 10 == i] for i in range(10) if i in last_digits}


def all_have_an_equal(s):
    """Does every element equal some other element in s?

    >>> all_have_an_equal([-4, -3, -2, 3, 2, 4])
    False
    >>> all_have_an_equal([4, 3, 2, 3, 2, 4])
    True
    """
    return min([sum([1 for y in s if x == y]) for x in s]) > 1
    return all([s[i] in s[:i] + s[i+1:] for i in range(len(s))])
