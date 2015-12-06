if __package__ is not None:
    import sys
    sys.path.append('./' + __package__.replace('.', '/'))

import expression


class Atomic(expression.Expression):
    def __init__(self, p, x):
        """
        Creates a new atomic expression with given predicate and elements

        >>> a = Atomic('P', 'x')
        >>> a.predicate
        'P'
        >>> a.element
        'x'
        """
        self.predicate = p
        self.element = x

    def eval(self, knowledge={}):
        """
        Evaluates an atomic expression on a given knowledge base

        >>> a = Atomic('P', 'x')
        >>> k = {'P': {'x': True}}
        >>> a.eval(k)
        True
        >>> a.eval()
        False
        """
        if self.predicate in knowledge:
            if self.element in knowledge[self.predicate]:
                return True

        return False

    def __str__(self):
        """
        String representation to print

        >>> a = Atomic('P', ('x', 'y', 'z'))
        >>> str(a)
        'P(x, y, z)'
        """
        return '%s(%s)' % (self.predicate, ', '.join([str(x)
                                                      for x in self.element]))


def test():
    print('Testing')
    import doctest
    doctest.testmod()
    print('Done')

if __name__ == '__main__':
    test()
