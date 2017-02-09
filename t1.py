from __future__ import print_function


def main(arg):
    """ return 1 to 9 number

    >>> main(10)
    1 2 3 4 5 6 7 8 9
    """

    for i in range(1, arg):
        print(i, end=' ')


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    main(10)
