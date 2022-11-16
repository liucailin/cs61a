def babylonian_sqrt(x):
    """ 巴比伦算法/牛顿法
    """
    def isclose(a, b):
        return a == b or abs(a-b) <= 0.0000001

    def update(guess):
        if isclose(guess * guess, x):
            return guess
        next_guess = (guess + x / guess) / 2
        return update(next_guess)

    return update(1)
