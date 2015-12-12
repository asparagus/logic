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
        """
        Compares two variables to check if they're equal
        Two variables are equal when they have the same name
        """
        return self.name == other.name

    def __hash__(self):
        """
        Gets the hash of this variable
        All variables have the same hash
        """
        return 0


def test():
    print('Testing')
    import doctest
    doctest.testmod()
    print('Done')

if __name__ == '__main__':
    test()
