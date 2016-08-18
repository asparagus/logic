#!/usr/bin/python
# -*- coding: utf8 -*-
"""This module contains the Atomic expression class."""
from __future__ import unicode_literals
import expression


class Atomic(expression.Expression):
    """Atomic expression class. Represents a simple statement."""

    def __init__(self, p, *x):
        """
        Create a new atomic expression with given predicate and arguments.

        >>> import variable
        >>> import predicate
        >>> p = predicate.Predicate('P')
        >>> x = variable.Variable('X')
        >>> a = Atomic(p, x)
        >>> print(a.predicate.name)
        P
        >>> len(a.arguments)
        1
        >>> print(a.arguments[0].name)
        X
        """
        self.predicate = p
        self.arguments = x

    def eval(self, knowledge={}):
        """
        Evaluate an atomic expression on a given knowledge base.

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
        String representation to print.

        >>> import variable
        >>> import predicate
        >>> p = predicate.Predicate('P')
        >>> x = variable.Variable('X')
        >>> y = variable.Variable('Y')
        >>> z = variable.Variable('Z')
        >>> a = Atomic(p, x, y, z)
        >>> print(a)
        P(X, Y, Z)
        """
        return '%s(%s)' % (self.predicate, ', '.join([str(x)
                                                      for x in self.arguments]
                                                     ))

    def type(self):
        """Return the type of this expression."""
        return 'Atomic'

    def __eq__(self, other):
        """Compare two expressions to check if they're equal.

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
        """Get the hash of this atomic expression."""
        return hash((type(self), self.predicate, self.arguments))


def test():
    """Test the module."""
    print('Testing')
    import doctest
    doctest.testmod()
    print('Done')

if __name__ == '__main__':
    test()
