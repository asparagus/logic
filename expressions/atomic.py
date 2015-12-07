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

        >>> import variable
        >>> import predicate
        >>> p = predicate.Predicate('P')
        >>> x = variable.Variable('X')
        >>> a = Atomic(p, x)
        >>> k = {'P': {('X',): True}}
        >>> a.eval(k)
        True
        >>> a.eval()
        False
        """
        pred = self.predicate.name
        args = tuple(arg.name for arg in self.arguments)
        if pred in knowledge:
            if args in knowledge[pred]:
                return True

        return False

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
        return 'Atomic'


def test():
    print('Testing')
    import doctest
    doctest.testmod()
    print('Done')

if __name__ == '__main__':
    test()
