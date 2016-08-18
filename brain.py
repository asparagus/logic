#!/usr/bin/python
# -*- coding: utf8 -*-
"""This module contains the Brain class for logical processing."""
import expressions.predicate
import expressions.constant
import expressions.atomic
import expressions.negation
import expressions.conjunction
import expressions.parser


class Brain:
    """Class modelling a logic brain."""

    def __init__(self):
        """
        Create a new brain with zero knowledge.

        >>> a = Brain()
        >>> len(a.knowledge)
        0
        """
        self.parser = expressions.parser.Parser()
        self.knowledge = set()
        self.rules = {}
        self.memory = {}

    def eval(self, e):
        """
        Evaluate a given expression according to the brain's knowledge.

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
        return result

    def add_rule(self, antecedent, consequent):
        """Add a give antecedent -> consequent rule to the brain."""
        if antecedent not in self.rules:
            self.rules[antecedent] = set()

        self.rules[antecedent].add(consequent)

        if self.eval(antecedent):
            if consequent not in self.knowledge:
                self.learn(consequent)

    def add_atomic(self, expr):
        """Add a given expression to the knowledge base."""
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
        """Add a new memory to the brain."""
        self.memory[reminder] = memory

    def learn(self, e):
        """Add a given expression to the knowledge base.

        >>> p = expressions.predicate.Predicate('P')
        >>> x = expressions.constant.Constant('x')
        >>> a = expressions.atomic.Atomic(p, x)
        >>> b = Brain()
        >>> b.learn(a)
        >>> b.eval(a)
        True
        """
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

    def __str__(self):
        """String representation of a brain's knowledge."""
        knowledge_str = str({str(e) for e in self.knowledge})
        rule_str = str({str(p): [str(q) for q in self.rules[p]]
                        for p in self.rules})
        reminder_str = str({str(p): self.memory[p] for p in self.memory})

        result_str = "Knowledge:\n%s\n\nRules:\n%s\n\nReminders:\n%s\n\n" %\
                     (knowledge_str, rule_str, reminder_str)

        return result_str


def test():
    """Test the module."""
    print('Testing')
    import doctest
    doctest.testmod()
    print('Done')

if __name__ == '__main__':
    test()
