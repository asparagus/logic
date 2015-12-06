if __package__ is not None:
    import sys
    sys.path.append('./' + __package__.replace('.', '/'))

import expressions.predicate
import expressions.constant
import expressions.atomic
import expressions.negation
import expressions.conjunction


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

        >>> p = expressions.predicate.Predicate('P')
        >>> q = expressions.predicate.Predicate('Q')
        >>> c = expressions.constant.Constant('c')
        >>> d = expressions.constant.Constant('d')
        >>> b = Brain()
        >>> b.knowledge = {'P': {('c',): True}}
        >>> p = expressions.atomic.Atomic(p, c)
        >>> b.eval(p)
        True
        >>> q = expressions.atomic.Atomic(q, d)
        >>> b.eval(q)
        False
        """
        return e.eval(self.knowledge)

    def learn(self, e):
        """
        Adds a given expression to the knowledge base

        >>> p = expressions.predicate.Predicate('P')
        >>> c = expressions.constant.Constant('c')
        >>> a = expressions.atomic.Atomic(p, c)
        >>> b = Brain()
        >>> b.learn(a)
        >>> b.eval(a)
        True
        """
        if type(e) is expressions.conjunction.Conjunction:
            self.learn(e.expr1)
            self.learn(e.expr2)

        elif type(e) is expressions.atomic.Atomic:
            p = e.predicate.name
            if p not in self.knowledge:
                self.knowledge[p] = {}

            self.knowledge[p][tuple(x.name for x in e.arguments)] = True


def test():
    print('Testing')
    import doctest
    doctest.testmod()
    print('Done')

if __name__ == '__main__':
    test()
