class Variable:
    def __init__(self, name):
        """
        Creates a new variable with a given name
        Constant names are all upper case

        >>> x = Variable('x')
        >>> x.name
        'X'
        """
        self.name = name.upper()

    def __str__(self):
        """
        String representation to print

        >>> x = Variable('X')
        >>> str(x)
        'X'
        """
        return self.name

    def __eq__(self, other):
        return type(other) == type(self)

    def __hash__(self):
        return 0


def test():
    print('Testing')
    import doctest
    doctest.testmod()
    print('Done')

if __name__ == '__main__':
    test()
