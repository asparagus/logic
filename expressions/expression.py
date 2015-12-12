class Expression:
    def __init__(self):
        """
        Initializes the expression
        """
        raise Exception('Non-subclass expressions cannot be initialized')

    def eval(self, knowledge={}):
        """
        Evaluates the expression
        """
        raise Exception('Non-subclass expressions cannot be evaluated')

    def __str__(self):
        """
        String representation to print
        """
        raise Exception('Non-subclass expressions cannot be parsed')

    def type(self):
        """
        Returns the type of this expression
        """
        raise Exception('Non-subclass expressions do not have a type')

    def __eq__(self, other):
        """
        Compares two expressions to check if they're equal
        """
        raise Exception('Non-subclass expressions cannot be compared')

    def __hash__(self):
        """
        Gets the hash of this expression
        """
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
        """
        String representation to print
        """
        return 'F'

    def type(self):
        """
        Returns the type of this expression
        """
        return 'Contradiction'

    def __eq__(self, other):
        """
        Compares two expressions to check if they're equal
        """
        return type(self) == type(other)

    def __hash__(self):
        """
        Gets the hash of this expression
        """
        return hash('F')


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
        """
        String representation to print
        """
        return 'T'

    def type(self):
        """
        Returns the type of this expression
        """
        return 'Tautology'

    def __eq__(self, other):
        """
        Compares two expressions to check if they're equal
        """
        return type(self) == type(other)

    def __hash__(self):
        """
        Gets the hash of this expression
        """
        return hash('T')


def test():
    print('Testing')
    import doctest
    doctest.testmod()
    print('Done')

if __name__ == '__main__':
    test()
