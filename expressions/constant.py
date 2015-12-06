class Constant:
    def __init__(self, name):
        """
        Creates a new constant with a given name

        >>> a = Constant('a')
        >>> a.name
        'a'
        """
        self.name = name

    def __str__(self):
        """
        String representation to print

        >>> a = Constant('a')
        >>> str(a)
        'a'
        """
        return self.name


def test():
    print('Testing')
    import doctest
    doctest.testmod()
    print('Done')

if __name__ == '__main__':
    test()
