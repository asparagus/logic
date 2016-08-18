#!/usr/bin/python
# -*- coding: utf8 -*-
"""This module contains the Predicate class."""
from __future__ import unicode_literals


class Predicate:
    """An assertion over a variable or constant."""

    def __init__(self, name):
        """
        Create a new predicate with a given name.

        >>> p = Predicate('P')
        >>> print(p.name)
        P
        """
        self.name = name

    def __str__(self):
        """
        String representation to print.

        >>> p = Predicate('P')
        >>> print(p)
        P
        """
        return self.name

    def __eq__(self, other):
        """
        Compare two predicates to check if they're equal.

        Two predicates are equal when they have the same name.
        """
        return type(self) == type(other) and self.name == other.name

    def __hash__(self):
        """Get the hash of this predicate."""
        return hash(self.name)


def test():
    """Test the module."""
    print('Testing')
    import doctest
    doctest.testmod()
    print('Done')

if __name__ == '__main__':
    test()
