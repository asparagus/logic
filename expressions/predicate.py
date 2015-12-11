class Predicate:
    def __init__(self, name):
        """
        Creates a new predicate with a given name

        >>> p = Predicate('P')
        >>> p.name
        'P'
        """
        self.name = name

    def __str__(self):
        """
        String representation to print

        >>> p = Predicate('P')
        >>> str(p)
        'P'
        """
        return self.name

    def __eq__(self, other):
        return type(self) == type(other) and self.name == other.name

    def __hash__(self):
        return hash(self.name)


def test():
    print('Testing')
    import doctest
    doctest.testmod()
    print('Done')

if __name__ == '__main__':
    test()
