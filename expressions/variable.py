class Variable:
    def __init__(self, name):
        """
        Creates a new variable with a given name

        >>> x = Variable('x')
        >>> x.name
        'x'
        """
        self.name = name

    def __str__(self):
        """
        String representation to print

        >>> x = Variable('X')
        >>> str(x)
        'X'
        """
        return self.name


def test():
    print('Testing')
    import doctest
    doctest.testmod()
    print('Done')

if __name__ == '__main__':
    test()
