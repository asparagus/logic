#!/usr/bin/python
# -*- coding: utf8 -*-
"""This module contains the Implication expression class."""
from __future__ import unicode_literals
import expression


class Implication(expression.Expression):
    """
    An implication expression.

    Represents the logical implication between two sub-expressions.
    Evaluates to true as long as it's not the case that the first
    expression evaluates to true and the second doesn't.
    """

    def __init__(self, expr1, expr2):
        """
        Create a new Implication off expressions 1 and 2.

        >>> e = Implication(1, 2)
        >>> e.expr1
        1
        >>> e.expr2 == 2
        True
        """
        self.expr1 = expr1
        self.expr2 = expr2

    def eval(self, knowledge={}):
        """
        Evaluate the Implication expression.

        Evaluates to true as long as it's not the case that the first
        expression evaluates to true and the second doesn't.

        >>> t = expression.Tautology()
        >>> f = expression.Contradiction()
        >>> a = Implication(t, f)
        >>> a.eval()
        False
        >>> a = Implication(t, t)
        >>> a.eval()
        True
        >>> a = Implication(f, f)
        >>> a.eval()
        True
        """
        return (not self.expr1.eval(knowledge) or self.expr2.eval(knowledge))

    def __str__(self):
        """
        String representation to print.

        >>> t = expression.Tautology()
        >>> f = expression.Contradiction()
        >>> a = Implication(t, f)
        >>> print(a)
        (T > F)
        """
        return '(%s > %s)' % (self.expr1, self.expr2)

    def type(self):
        """Return the type of this expression."""
        return 'Implication'

    def __eq__(self, other):
        """Compare two expressions to check if they're equal.

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
        >>> imp1 = Implication(P_c, P_d)
        >>> imp2 = Implication(P_c, P_d)
        >>> imp1 == imp2
        True
        >>> imp3 = Implication(P_c, P_e)
        >>> imp1 == imp3
        False
        """
        return type(self) == type(other) and\
            self.expr1 == other.expr1 and\
            self.expr2 == other.expr2

    def __hash__(self):
        """Get the hash of this implication."""
        return hash((type(self), self.expr1, self.expr2))


def test():
    """Test the module."""
    print('Testing')
    import doctest
    doctest.testmod()
    print('Done')

if __name__ == '__main__':
    test()
