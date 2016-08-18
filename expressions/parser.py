#!/usr/bin/python
# -*- coding: utf8 -*-
"""This module contains the Parser class."""
from __future__ import unicode_literals
import re

import conjunction
import disjunction
import implication
import negation
import atomic

import predicate
import variable
import constant


class Parser:
    """Parser class. Parses expressions from strings."""

    def __init__(self):
        """Initialize an instance of Parser."""
        pass

    def unbox(self, str_expression):
        """Remove unnecessary parenthesis.

        >>> p = Parser()
        >>> p.unbox('((hey,))') == 'hey,'
        True
        """
        while str_expression[0] == '(' and\
                self.closure(str_expression) == len(str_expression) - 1:
            str_expression = str_expression[1:-1].strip()

        return str_expression

    def parse(self, str_expression):
        """Parse a given expression."""
        str_expression = self.unbox(str_expression.strip())

        atomic = self.try_parse_atomic(str_expression)
        if atomic is not None:
            return atomic

        negation = self.try_parse_negation(str_expression)
        if negation is not None:
            return negation

        binary = self.try_parse_binary(str_expression)
        if binary is not None:
            return binary

    def try_parse_atomic(self, str_expression):
        """
        Parse an atomic expression.

        If the expression does not match, returns None.

        >>> p = Parser()
        >>> expr = 'P(x, y)'
        >>> atomic = p.try_parse_atomic(expr)
        >>> tuple(arg.name for arg in atomic.arguments) == ('x', 'y')
        True

        >>> expr = 'P(x, y) & Q(z)'
        >>> p.try_parse_atomic(expr)

        """
        pattern = '^\w+\(\s*\w*(,\s*\w+\s*)*\)$'
        match = re.match(pattern, str_expression)
        if match:
            opening_parenthesis_idx = str_expression.index('(')
            closing_parenthesis_idx = str_expression.index(')')

            predicate_name = str_expression[:opening_parenthesis_idx].strip()
            variable_names = [x.strip() for x in
                              str_expression[
                              opening_parenthesis_idx + 1:
                              closing_parenthesis_idx].
                              split(',')
                              if x]

            p = predicate.Predicate(predicate_name)
            args = tuple(variable.Variable(x) if x[0].isupper()
                         else constant.Constant(x) for x in variable_names)

            return atomic.Atomic(p, *args)

    def try_parse_negation(self, str_expression):
        """
        Parse a negation expression.

        If the expression does not match, returns None.

        >>> p = Parser()
        >>> expr = '¬P(a, Y)'
        >>> negation = p.try_parse_negation(expr)
        >>> atomic = negation.expr
        >>> atomic.predicate.name
        u'P'
        >>> tuple(arg.name for arg in atomic.arguments) == ('a', 'Y')
        True

        >>> expr = 'P(x, y) & Q(z)'
        >>> p.try_parse_negation(expr)

        """
        if str_expression[0] == '¬':
            str_inner_expression = str_expression[1:]
            expr = self.parse(str_inner_expression)

            if expr:
                return negation.Negation(expr)

    def try_parse_binary(self, str_expression):
        """
        Parse either a conjunction or disjunction.

        >>> p = Parser()
        >>> expr = 'P(X) & P(Y)'
        >>> res = p.try_parse_binary(expr)
        >>> print(res.type())
        Conjunction
        >>> print(res.expr1.predicate.name)
        P
        >>> tuple(x.name for x in res.expr1.arguments) == ('X',)
        True

        >>> expr = 'P(X) | Q(Y)'
        >>> res = p.try_parse_binary(expr)
        >>> print(res.type())
        Disjunction
        >>> print(res.expr1.predicate.name)
        P
        >>> tuple(x.name for x in res.expr2.arguments) == ('Y',)
        True

        >>> expr = 'P(x) & P(y) & P(z)'
        >>> res = p.try_parse_binary(expr)
        >>> print(res.type())
        Conjunction

        >>> print(res.expr2.predicate.name)
        P
        >>> tuple(x.name for x in res.expr2.arguments) == ('z',)
        True
        """
        str_last_expression = self.grab_last_expression(str_expression)

        if str_last_expression:
            remainder = str_expression[:-len(str_last_expression)].strip()
            if len(remainder) > 0:
                operator = remainder[-1]

                if operator in ('&', '|', '>'):
                    str_first_expression = remainder[:-1]
                    # self.grab_first_expression(remainder[1:])

                    if str_first_expression:
                        expr1 = self.parse(str_first_expression)
                        expr2 = self.parse(str_last_expression)

                        if expr1 and expr2:
                            if operator == '&':
                                return conjunction.Conjunction(expr1, expr2)
                            elif operator == '|':
                                return disjunction.Disjunction(expr1, expr2)
                            elif operator == '>':
                                return implication.Implication(expr1, expr2)

    def grab_last_expression(self, str_expression):
        """
        Grab the last section that could be an expression from a string.

        >>> p = Parser()
        >>> print(p.grab_last_expression('P(x) & P(y)'))
        P(y)

        >>> p.grab_last_expression('abc(def()), asd')

        """
        if len(str_expression) > 0 and str_expression[-1] == ')':
            start = self.backwards_closure(str_expression)
            if start:
                idx = start - 1
                while idx >= -len(str_expression):
                    c = str_expression[idx]
                    if c not in ['_.-'] and not c.isalnum():
                        return str_expression[idx + 1:]

                    idx -= 1

    def backwards_closure(self, str_expression, end=-1):
        """
        Get the index at which parenthesis are balanced.

        >>> p = Parser()
        >>> p.backwards_closure('(((,))()),()')
        -2
        """
        idx = end - 1
        stack = 1

        while idx >= -len(str_expression):
            if str_expression[idx] == ')':
                stack += 1
            elif str_expression[idx] == '(':
                stack -= 1

            if stack == 0:
                return idx

            idx -= 1

    def closure(self, str_expression, start=0):
        """
        Get the index at which parenthesis are balanced.

        >>> p = Parser()
        >>> p.closure('(((,))()),()')
        8

        >>> p.closure('(((')

        """
        stack = 1
        for idx in range(start + 1, len(str_expression)):
            if str_expression[idx] == '(':
                stack += 1
            elif str_expression[idx] == ')':
                stack -= 1

            if stack == 0:
                return idx


def test():
    """Test the module."""
    print('Testing')
    import doctest
    doctest.testmod()
    print('Done')

if __name__ == '__main__':
    test()
