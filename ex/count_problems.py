# base case
#   1. n = 1 最后一步要跨一格
#   2. n = 2 最后一步要跨两格
# recursive step
#   剩下一格 + 剩下两格
def count_stair_ways(n):
    """Returns the number of ways to climb up a flight of
    n stairs, moving either 1 step or 2 steps at a time.
    >>> count_stair_ways(4)
    5
    """
    if n == 1:
        return 1
    elif n == 2:
        return 2
    return count_stair_ways(n-1) + count_stair_ways(n-2)

#  二叉树 
# base case
#   1. n = 0 步数等于阶梯 合法路径
#   2. n < 0 步数超过阶梯 非法路径
def count_stair_ways_alt(n):
    """Returns the number of ways to climb up a flight of
    n stairs, moving either 1 step or 2 steps at a time.
    >>> count_stair_ways_alt(4)
    5
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    return count_stair_ways(n-1) + count_stair_ways(n-2)

# k叉树
# base case
#   1. 合法的路径 return 1
#   2. 非法的路径 return 0
def count_k(n, k):
    """ Counts the number of paths up a flight of n stairs
    when taking up to and including k steps at a time.
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    total, i = 0, 1
    while i <= k:
        total += count_k(n-i, k)
        i += 1
    return total

def mario_number(level):
    """Return the number of ways that Mario can perform a sequence of steps
    or jumps to reach the end of the level without ever landing in a Piranha
    plant. Assume that every level begins and ends with a space.

    >>> mario_number(' P P ')   # jump, jump
    1
    >>> mario_number(' P P  ')   # jump, jump, step
    1
    >>> mario_number('  P P ')  # step, jump, jump
    1
    >>> mario_number('   P P ') # step, step, jump, jump or jump, jump, jump
    2
    >>> mario_number(' P PP ')  # Mario cannot jump two plants
    0
    >>> mario_number('    ')    # step, jump ; jump, step ; step, step, step
    3
    >>> mario_number('    P    ')
    9
    >>> mario_number('   P    P P   P  P P    P     P ')
    180
    """
    def ways(n):
        if n == len(level) - 1:
            return 1
        elif n >= len(level) or level[n] == 'P':
            return 0
        else:
            return ways(n+1) + ways(n+2)
    
    return ways(0)

def count_partitions(n, m):
    """Count the ways to partition n using parts up to m.
    >>> count_partitions(6, 4)
    9
    >>> count_partitions(5, 5)
    7
    >>> count_partitions(10, 10)
    42
    >>> count_partitions(15, 15)
    176
    >>> count_partitions(20, 20)
    627
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        return count_partitions(n-m, m) + count_partitions(n, m-1)

def count_partitions(n, m):
    """Count partitions.

    >>> count_partitions(6, 4)
    9
    """
    if n < 0 or m == 0:
        return 0
    else:
        exact_match = 0
        if n == m:
            exact_match = 1
        with_m = count_partitions(n-m, m) 
        without_m = count_partitions(n, m-1)
        return exact_match + with_m + without_m

def partitions(n, m):
    """List partitions.

    >>> for p in partitions(6, 4): print(p)
    2 + 4
    1 + 1 + 4
    3 + 3
    1 + 2 + 3
    1 + 1 + 1 + 3
    2 + 2 + 2
    1 + 1 + 2 + 2
    1 + 1 + 1 + 1 + 2
    1 + 1 + 1 + 1 + 1 + 1
    """
    if n <= 0:
        return []
    elif m == 0:
        return []
    else:
        exact_match = []
        if n == m:
            exact_match = [str(m)]
        with_m = [p + ' + ' + str(m) for p in partitions(n-m, m)]
        without_m = partitions(n, m-1)
        return exact_match + with_m + without_m

def partitions_list(n, m):
    """List partitions.

    >>> for p in partitions_list(6, 4): print(p)
    2 + 4
    1 + 1 + 4
    3 + 3
    1 + 2 + 3
    1 + 1 + 1 + 3
    2 + 2 + 2
    1 + 1 + 2 + 2
    1 + 1 + 1 + 1 + 2
    1 + 1 + 1 + 1 + 1 + 1
    """
    if n <= 0:
        return [[]]
    elif m == 0:
        return [[]]
    else:
        exact_match = []
        if n == m:
            exact_match = [m]
        with_m = [p + [m] for p in partitions_list(n-m, m)]
        without_m = partitions_list(n, m-1)
        return exact_match + with_m + without_m


def yield_partitions(n, m):
    """Yield_partitions.

    >>> for p in yield_partitions(6, 4): print(p)
    2 + 4
    1 + 1 + 4
    3 + 3
    1 + 2 + 3
    1 + 1 + 1 + 3
    2 + 2 + 2
    1 + 1 + 2 + 2
    1 + 1 + 1 + 1 + 2
    1 + 1 + 1 + 1 + 1 + 1
    """
    if n > 0 and m > 0:
        if n == m:
            yield str(m)
        for p in yield_partitions(n-m, m):
            yield p + ' + ' + str(m)
        yield from yield_partitions(n, m-1)

def yield_partitions_list(n, m):
    """Yield_partitions.

    >>> for p in yield_partitions_list(6, 4): print(p)
    [4, 2]
    [4, 1, 1]
    [3, 3]
    [3, 2, 1]
    [3, 1, 1, 1]
    [2, 2, 2]
    [2, 2, 1, 1]
    [2, 1, 1, 1, 1]
    [1, 1, 1, 1, 1, 1]
    """
    if n == 0:
        yield []
    elif n > 0 and m > 0:
        for p in yield_partitions_list(n-m, m):
            yield [m] + p
        yield from yield_partitions_list(n, m-1)


def count_coins(change):
    """Return the number of ways to make change using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> count_coins(200)
    1463
    """

    def next_larger_coin(coin):
        """Returns the next larger coin in order.
        >>> next_larger_coin(1)
        5
        >>> next_larger_coin(5)
        10
        >>> next_larger_coin(10)
        25
        >>> next_larger_coin(2) # Other values return None
        """
        if coin == 1:
            return 5
        elif coin == 5:
            return 10
        elif coin == 10:
            return 25

    def next_smaller_coin(coin):
        """Returns the next smaller coin in order.
        >>> next_smaller_coin(25)
        10
        >>> next_smaller_coin(10)
        5
        >>> next_smaller_coin(5)
        1
        >>> next_smaller_coin(2) # Other values return None
        """
        if coin == 25:
            return 10
        elif coin == 10:
            return 5
        elif coin == 5:
            return 1


    def constrained_count(change, smallest_coin):
        if change == 0:
            return 1
        if change < 0:
            return 0
        if smallest_coin == None:
            return 0
        without_coin = constrained_count(change, next_larger_coin(smallest_coin))
        with_coin = constrained_count(change - smallest_coin, smallest_coin)
        return without_coin + with_coin
    return constrained_count(change, 1)

    # Alternate solution: using next_smaller_coin
    def constrained_count_small(change, largest_coin):
        if change == 0:
            return 1
        if change < 0:
            return 0
        if largest_coin == None:
            return 0
        without_coin = constrained_count_small(change, next_smaller_coin(largest_coin))
        with_coin = constrained_count_small(change - largest_coin, largest_coin)
        return without_coin + with_coin
    return constrained_count_small(change, 25)


def knapsack(weights, values, c):
    """
    >>> w = [2, 6, 3, 3]
    >>> v = [1, 5, 3, 3]
    >>> knapsack(w, v, 6)
    6
    """

    if weights == []:
        return 0

    first_weight, rest_weights = weights[0], weights[1:]
    first_value, rest_values = values[0], values[1:]
    with_first = first_value + knapsack(rest_weights, rest_values, c - first_weight)
    without_first = knapsack(rest_weights, rest_values, c)
    if first_weight <= c:
        return max(with_first, without_first)
    return without_first
    

