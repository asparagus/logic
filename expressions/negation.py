if __package__ is not None:
    import sys
    sys.path.append('./' + __package__.replace('.', '/'))

import expression


class Negation(expression.Expression):
    def __init__(self, expr):
        """
        Creates a new Negation off expression expr

        >>> e = Negation(1)
        >>> e.expr
        1
        """
        self.expr = expr

    def eval(self, knowledge={}):
        """
        Evaluates the negative of the inner expression

        >>> t = expression.Tautology()
        >>> f = expression.Contradiction()
        >>> a = Negation(t)
        >>> a.eval()
        False
        >>> a = Negation(f)
        >>> a.eval()
        True
        """
        return not self.expr.eval(knowledge)

    def __str__(self):
        """
        String representation to print

        >>> a = Negation(expression.Tautology())
        >>> str(a)
        '(¬T)'
        """
        return '(¬%s)' % str(self.expr)

    def type(self):
        return 'Negation'


def test():
    print('Testing')
    import doctest
    doctest.testmod()
    print('Done')

if __name__ == '__main__':
    test()
