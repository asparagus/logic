#!/usr/bin/python
# -*- coding: utf8 -*-
"""This module contains the Negation expression."""
from __future__ import unicode_literals
import expression


class Negation(expression.Expression):
    """
    A negation expression.

    Represents the logical NOT of a sub-expression.
    """

    def __init__(self, expr):
        """
        Create a new Negation off expression expr.

        >>> e = Negation(1)
        >>> e.expr
        1
        """
        self.expr = expr

    def eval(self, knowledge={}):
        """
        Evaluate the negative of the inner expression.

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
        String representation to print.

        >>> a = Negation(expression.Tautology())
        >>> print(a)
        (^T)
        """
        return '(^%s)' % str(self.expr)

    def type(self):
        """Return the type of this expression."""
        return 'Negation'

    def __eq__(self, other):
        """
        Compare two expressions to check if they're equal.

        >>> import constant
        >>> import predicate
        >>> import atomic
        >>> p = predicate.Predicate('P')
        >>> c = constant.Constant('c')
        >>> d = constant.Constant('d')
        >>> a = atomic.Atomic(p, c)
        >>> b = atomic.Atomic(p, d)
        >>> na = Negation(a)
        >>> nb = Negation(b)
        >>> na == nb
        False
        >>> na == Negation(a)
        True
        """
        return self.type() == other.type() and self.expr == other.expr

    def __hash__(self):
        """Get the hash of this implication."""
        return hash((type(self), self.expr))


def test():
    """Test the module."""
    print('Testing')
    import doctest
    doctest.testmod()
    print('Done')

if __name__ == '__main__':
    test()
