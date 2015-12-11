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
        return type(self) == type(self) and self.name == other.name

    def __hash__(self):
        return hash(self.name)


def test():
    print('Testing')
    import doctest
    doctest.testmod()
    print('Done')

if __name__ == '__main__':
    test()
