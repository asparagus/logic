if __package__ is not None:
    import sys
    sys.path.append('./' + __package__.replace('.', '/'))

import expression


class Conjunction(expression.Expression):
    def __init__(self, expr1, expr2):
        """
        Creates a new Conjunction off expressions 1 and 2

        >>> e = Conjunction(1, 2)
        >>> e.expr1
        1
        >>> e.expr2 == 2
        True
        """
        self.expr1 = expr1
        self.expr2 = expr2

    def eval(self, knowledge={}):
        """
        Evaluates the Conjunction expression
        Returns true if both expressions are true

        >>> t = expression.Tautology()
        >>> f = expression.Contradiction()
        >>> a = Conjunction(t, f)
        >>> a.eval()
        False
        >>> a = Conjunction(t, t)
        >>> a.eval()
        True
        >>> a = Conjunction(f, f)
        >>> a.eval()
        False
        """
        return (self.expr1.eval(knowledge) and self.expr2.eval(knowledge))

    def __str__(self):
        """
        String representation to print

        >>> t = expression.Tautology()
        >>> f = expression.Contradiction()
        >>> a = Conjunction(t, f)
        >>> str(a)
        '(T & F)'
        """
        return '(%s & %s)' % (self.expr1, self.expr2)

    def type(self):
        """
        Returns the type of this expression
        """
        return 'Conjunction'

    def __eq__(self, other):
        """
        Compares two expressions to check if they're equal

        >>> import constant
        >>> import predicate
        >>> import atomic
        >>> p = predicate.Predicate('P')
        >>> c = constant.Constant('c')
        >>> d = constant.Constant('d')
        >>> e = constant.Constant('e')
        >>> P_c = atomic.Atomic(p, c)
        >>> P_d = atomic.Atomic(p, d)
        >>> P_e = atomic.Atomic(p, e)
        >>> conj1 = Conjunction(P_c, P_d)
        >>> conj2 = Conjunction(P_c, P_d)
        >>> conj1 == conj2
        True
        >>> conj3 = Conjunction(P_c, P_e)
        >>> conj1 == conj3
        False
        """
        return type(self) == type(other) and\
            self.expr1 == other.expr1 and\
            self.expr2 == other.expr2

    def __hash__(self):
        """
        Gets the hash of this conjunction
        """
        return hash((type(self), self.expr1, self.expr2))


def test():
    print('Testing')
    import doctest
    doctest.testmod()
    print('Done')

if __name__ == '__main__':
    test()
