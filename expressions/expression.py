class Expression:
    def __init__(self):
        pass

    def eval(self, knowledge={}):
        return False

    def __str__(self):
        return 'Expression'

    def type(self):
        return 'Expression'

    def __eq__(self, other):
        return False

    def __hash__(self):
        return 0


class Contradiction(Expression):
    def __init__(self):
        """
        Creates a new Contradiction expression, which always evaluates to false
        """
        pass

    def eval(self, knowledge={}):
        """
        Evaluates the Contradiction, returns false

        >>> a = Contradiction()
        >>> a.eval()
        False
        """
        return False

    def __str__(self):
        return 'F'

    def type(self):
        return 'Contradiction'


class Tautology(Expression):
    def __init__(self):
        """
        Creates a new Tautology expression, which always evaluates to true
        """
        pass

    def eval(self, knowledge={}):
        """
        Evaluates the Tautology, returns true

        >>> a = Tautology()
        >>> a.eval()
        True
        """
        return True

    def __str__(self):
        return 'T'

    def type(self):
        return 'Tautology'


def test():
    print('Testing')
    import doctest
    doctest.testmod()
    print('Done')

if __name__ == '__main__':
    test()
