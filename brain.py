class Brain:
    def __init__(self):
        """
        Creates a new brain with zero knowledge

        >>> a = Brain()
        >>> a.knowledge
        {}
        """
        self.knowledge = {}

    def eval(self, e):
        """
        Evaluates a given expression according to the brain's knowledge

        >>> import expressions.atomic as atomic
        >>> b = Brain()
        >>> b.knowledge = {'P': {'x': True}}
        >>> p = atomic.Atomic('P', 'x')
        >>> b.eval(p)
        True
        >>> q = atomic.Atomic('Q', 'x')
        >>> b.eval(q)
        False
        """
        return e.eval(self.knowledge)


def test():
    print('Testing')
    import doctest
    doctest.testmod()
    print('Done')

if __name__ == '__main__':
    test()
