class Constant:
    def __init__(self, name):
        """
        Creates a new constant with a given name
        Constant names are all lower case

        >>> a = Constant('a')
        >>> a.name
        'a'
        """
        self.name = name.lower()

    def __str__(self):
        """
        String representation to print

        >>> a = Constant('a')
        >>> str(a)
        'a'
        """
        return self.name

    def __eq__(self, other):
        """
        Compares two constants to check if they're equal
        Two constants are equal when they have the same name

        >>> c1 = Constant('c1')
        >>> c2 = Constant('c2')
        >>> c3 = Constant('c2')
        >>> c1 == c1
        True
        >>> c1 == c2
        False
        >>> c2 == c3
        True
        """
        return type(self) == type(self) and self.name == other.name

    def __hash__(self):
        """
        Gets the hash of this constant
        """
        return hash(self.name)


def test():
    print('Testing')
    import doctest
    doctest.testmod()
    print('Done')

if __name__ == '__main__':
    test()
