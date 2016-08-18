#!/usr/bin/python
# -*- coding: utf8 -*-
"""This module contains the Constant class."""
from __future__ import unicode_literals


class Constant:
    """
    A logic constant is an abstraction of an object.

    Assertions or negations can be made of the constant's properties,
    which constitute a predicate.
    """

    def __init__(self, name):
        """
        Create a new constant with a given name.

        Constant names are all lower case.

        >>> a = Constant('a')
        >>> print(a.name)
        a
        """
        self.name = name.lower()

    def __str__(self):
        """
        String representation to print.

        >>> a = Constant('a')
        >>> print(a)
        a
        """
        return self.name

    def __eq__(self, other):
        """
        Compare two constants to check if they're equal.

        Two constants are equal when they have the same name.

        >>> c1 = Constant('c1')
        >>> c2 = Constant('c2')
        >>> c3 = Constant('c2')
        >>> c1 == c1
        True
        >>> c1 == c2
        False
        >>> c2 == c3
        True
        """
        return type(self) == type(self) and self.name == other.name

    def __hash__(self):
        """Get the hash of this constant."""
        return hash(self.name)


def test():
    """Test the module."""
    print('Testing')
    import doctest
    doctest.testmod()
    print('Done')

if __name__ == '__main__':
    test()
