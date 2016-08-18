#!/usr/bin/python
# -*- coding: utf8 -*-
"""
This module contains the classes Expression, Contradiction and Tautology.

The Expression class is the base for all logic expressions.
Contradiction and Tautology are just constant examples.
"""
from __future__ import unicode_literals


class Expression:
    """
    This class is the parent for all logic expressions.

    Provides the method signature for all methods expected from an expression:
    eval, str, type, eq, hash
    """

    def __init__(self):
        """Initialize the expression."""
        raise Exception('Non-subclass expressions cannot be initialized')

    def eval(self, knowledge={}):
        """Evaluate the expression."""
        raise Exception('Non-subclass expressions cannot be evaluated')

    def __str__(self):
        """String representation to print."""
        raise Exception('Non-subclass expressions cannot be parsed')

    def type(self):
        """Return the type of this expression."""
        raise Exception('Non-subclass expressions do not have a type')

    def __eq__(self, other):
        """Compare two expressions to check if they're equal."""
        raise Exception('Non-subclass expressions cannot be compared')

    def __hash__(self):
        """Get the hash of this expression."""
        return 0


class Contradiction(Expression):
    """A constant expression. Contradiction is always False."""

    def __init__(self):
        """
        Create a new Contradiction instance.

        It always evaluates to false.
        """
        pass

    def eval(self, knowledge={}):
        """
        Evaluate the Contradiction, returns false.

        >>> a = Contradiction()
        >>> a.eval()
        False
        """
        return False

    def __str__(self):
        """String representation to print."""
        return 'F'

    def type(self):
        """Return the type of this expression."""
        return 'Contradiction'

    def __eq__(self, other):
        """Compare two expressions to check if they're equal."""
        return type(self) == type(other)

    def __hash__(self):
        """Get the hash of this expression.

        >>> c = Contradiction()
        >>> hash(c) == hash('F')
        True
        """
        return hash(str(self))


class Tautology(Expression):
    """A constant expression. Tautology is always True."""

    def __init__(self):
        """
        Create a new Tautology expression.

        It always evaluates to true.
        """
        pass

    def eval(self, knowledge={}):
        """
        Evaluate the Tautology, returns true.

        >>> a = Tautology()
        >>> a.eval()
        True
        """
        return True

    def __str__(self):
        """String representation to print."""
        return 'T'

    def type(self):
        """Return the type of this expression."""
        return 'Tautology'

    def __eq__(self, other):
        """Compare two expressions to check if they're equal."""
        return type(self) == type(other)

    def __hash__(self):
        """
        Get the hash of this expression.

        >>> t = Tautology()
        >>> hash(t) == hash('T')
        True
        """
        return hash(str(self))


def test():
    """Test the module."""
    print('Testing')
    import doctest
    doctest.testmod()
    print('Done')

if __name__ == '__main__':
    test()
