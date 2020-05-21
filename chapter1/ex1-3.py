def sq(x):

    return x * x


def sq_larger(x, y):

    if x > y:
        return sq(x)
    else:
        return sq(y)


def sq_larger_two(x, y, z):

    if x > y:
        return sq(x) + sq_larger(y, z)
    else:
        return sq(y) + sq_larger(x, z)


if __name__ == "__main__":

    x = 5
    y = 4
    z = 3

    print(sq_larger_two(x, y, z))


