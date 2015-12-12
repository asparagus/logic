if __package__ is not None:
    import sys
    sys.path.append('./' + __package__.replace('.', '/'))

import expression


class Atomic(expression.Expression):
    def __init__(self, p, *x):
        """
        Creates a new atomic expression with given predicate and arguments

        >>> import variable
        >>> import predicate
        >>> p = predicate.Predicate('P')
        >>> x = variable.Variable('X')
        >>> a = Atomic(p, x)
        >>> a.predicate.name
        'P'
        >>> len(a.arguments)
        1
        >>> a.arguments[0].name
        'X'
        """
        self.predicate = p
        self.arguments = x

    def eval(self, knowledge={}):
        """
        Evaluates an atomic expression on a given knowledge base

        >>> import constant
        >>> import predicate
        >>> p = predicate.Predicate('P')
        >>> c = constant.Constant('c')
        >>> a = Atomic(p, c)
        >>> k = {a}
        >>> a.eval(k)
        True
        >>> a.eval()
        False
        >>> b = Atomic(p, c)
        >>> b.eval(k)
        True
        """
        return self in knowledge

    def __str__(self):
        """
        String representation to print

        >>> import variable
        >>> import predicate
        >>> p = predicate.Predicate('P')
        >>> x = variable.Variable('X')
        >>> y = variable.Variable('Y')
        >>> z = variable.Variable('Z')
        >>> a = Atomic(p, x, y, z)
        >>> str(a)
        'P(X, Y, Z)'
        """
        return '%s(%s)' % (self.predicate, ', '.join([str(x)
                                                      for x in self.arguments]
                                                     ))

    def type(self):
        """
        Returns the type of this expression
        """
        return 'Atomic'

    def __eq__(self, other):
        """
        Compares two expressions to check if they're equal

        >>> import constant
        >>> import predicate
        >>> p = predicate.Predicate('P')
        >>> c = constant.Constant('c')
        >>> a = Atomic(p, c)
        >>> b = Atomic(p, c)
        >>> a == b
        True
        """
        if other.type() == self.type():
            return self.predicate == other.predicate and\
                self.arguments == other.arguments
        return False

    def __hash__(self):
        """
        Gets the hash of this atomic expression
        """
        return hash((type(self), self.predicate, self.arguments))


def test():
    print('Testing')
    import doctest
    doctest.testmod()
    print('Done')

if __name__ == '__main__':
    test()
