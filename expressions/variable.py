#!/usr/bin/python
# -*- coding: utf8 -*-
"""This module contains the Variable class."""
from __future__ import unicode_literals


class Variable:
    """A variable represents some indeterminate abstract object."""

    def __init__(self, name):
        """
        Create a new variable with a given name.

        Constant names are all upper case.

        >>> x = Variable('x')
        >>> print(x.name)
        X
        """
        self.name = name.upper()

    def __str__(self):
        """
        String representation to print.

        >>> x = Variable('X')
        >>> print(x)
        X
        """
        return self.name

    def __eq__(self, other):
        """
        Compare two variables to check if they're equal.

        Two variables are equal when they have the same name.
        """
        return self.name == other.name

    def __hash__(self):
        """
        Get the hash of this variable.

        All variables have the same hash.
        """
        return 0


def test():
    """Test the module."""
    print('Testing')
    import doctest
    doctest.testmod()
    print('Done')

if __name__ == '__main__':
    test()
