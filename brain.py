if __package__ is not None:
    import sys
    sys.path.append('./' + __package__.replace('.', '/'))

import expressions.predicate
import expressions.constant
import expressions.atomic
import expressions.negation
import expressions.conjunction
import expressions.parser


class Brain:
    def __init__(self):
        """
        Creates a new brain with zero knowledge

        >>> a = Brain()
        >>> a.knowledge
        set()
        """
        self.parser = expressions.parser.Parser()
        self.knowledge = set()
        self.rules = {}
        self.memory = {}

    def eval(self, e):
        """
        Evaluates a given expression according to the brain's knowledge

        >>> p = expressions.predicate.Predicate('P')
        >>> q = expressions.predicate.Predicate('Q')
        >>> c = expressions.constant.Constant('c')
        >>> d = expressions.constant.Constant('d')
        >>> b = Brain()
        >>> p = expressions.atomic.Atomic(p, c)
        >>> b.knowledge = {p}
        >>> b.eval(p)
        True
        >>> q = expressions.atomic.Atomic(q, d)
        >>> b.eval(q)
        False
        """
        result = e.eval(self.knowledge)
        # print('%s => %s' % (e, result))
        return result

    def add_rule(self, antecedent, consequent):
        """
        Adds a give antecedent -> consequent rule to the brain
        """
        if antecedent not in self.rules:
            self.rules[antecedent] = set()

        self.rules[antecedent].add(consequent)

        if self.eval(antecedent):
            if consequent not in self.knowledge:
                self.learn(consequent)

    def add_atomic(self, expr):
        """
        Adds a given expression to the knowledge base
        """
        self.knowledge.add(expr)

        if expr in self.memory:
            memory = self.memory[expr]
            if memory in self.knowledge:
                if memory in self.rules:
                    for consequent in self.rules[memory]:
                        self.learn(consequent)

        if expr in self.rules:
            for consequent in self.rules[expr]:
                self.learn(consequent)

    def add_memory(self, memory, reminder):
        self.memory[reminder] = memory

    def learn(self, e):
        """
        Adds a given expression to the knowledge base

        >>> p = expressions.predicate.Predicate('P')
        >>> x = expressions.constant.Constant('x')
        >>> a = expressions.atomic.Atomic(p, x)
        >>> b = Brain()
        >>> b.learn(a)
        >>> b.eval(a)
        True
        """
        # print('Brain <- %s' % str(e))
        if e.type() == 'Conjunction':
            self.learn(e.expr1)
            self.learn(e.expr2)

        elif e.type() == 'Atomic':
            self.add_atomic(e)

        elif e.type() == 'Implication':
            self.add_rule(e.expr1, e.expr2)

        elif e.type() == 'Disjunction':
            self.add_rule(expressions.negation.Negation(e.expr1), e.expr2)
            self.add_rule(expressions.negation.Negation(e.expr2), e.expr1)

        else:
            print('None')


def test():
    print('Testing')
    import doctest
    doctest.testmod()
    print('Done')

if __name__ == '__main__':
    test()
