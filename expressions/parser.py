if __package__ is not None:
    import sys
    sys.path.append('./' + __package__.replace('.', '/'))

import expression
import conjunction
import disjunction
import negation
import atomic

import predicate
import variable
import constant

import re


class Parser:
    def __init__(self):
        """
        Initializes an instance of Parser
        """
        pass

    def parse(self, str_expression):
        atomic = self.try_parse_atomic(str_expression)
        if atomic is not None:
            return atomic

        negation = self.try_parse_negation(str_expression)
        if negation is not None:
            return negation

        binary = self.try_parse_binary(str_expression)
        if binary is not None:
            return binary

        return None

    def try_parse_atomic(self, str_expression):
        """
        Parses an atomic expression
        If the expression does not match, returns None

        >>> p = Parser()
        >>> expr = 'P(x, y)'
        >>> atomic = p.try_parse_atomic(expr)
        >>> tuple(element.name for element in atomic.element)
        ('x', 'y')

        >>> expr = 'P(x, y) & Q(z)'
        >>> p.try_parse_atomic(expr)

        """
        str_expression = str_expression.strip()
        pattern = '^\w\(\s*\w*(,\s*\w+\s*)*\)$'
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
            v = tuple(variable.Variable(v) for v in variable_names)

            return atomic.Atomic(p, v)
        else:
            return None

    def try_parse_negation(self, str_expression):
        """
        Parses a negation expression
        If the expression does not match, returns None

        >>> p = Parser()
        >>> expr = '¬(P(x, y))'
        >>> negation = p.try_parse_negation(expr)
        >>> atomic = negation.expr
        >>> atomic.predicate.name
        'P'
        >>> tuple(element.name for element in atomic.element)
        ('x', 'y')

        >>> expr = 'P(x, y) & Q(z)'
        >>> p.try_parse_negation(expr)

        """
        str_expression = str_expression.strip()
        pattern = '^¬\(.*\)$'
        match = re.match(pattern, str_expression)
        if match:
            opening_parenthesis_idx = str_expression.index('(')
            closing_parenthesis_idx = str_expression.rindex(')')

            str_inner_expression = str_expression[opening_parenthesis_idx + 1:
                                                  closing_parenthesis_idx]

            expr = self.parse(str_inner_expression)
            if expr:
                return negation.Negation(expr)

        return None

    def find_closing_parenthesis(self, text):
        """
        Gets the first closing parenthesis of a text
        First output is the parenthesis, second is a tuple with indices

        >>> p = Parser()
        >>> p.find_closing_parenthesis('(Hey()),())')
        ('(Hey())', (0, 6))

        >>> p.find_closing_parenthesis('Hey(((')

        """
        start = -1
        stack = 0
        for index in range(len(text)):
            if text[index] == '(':
                if start < 0:
                    start = index
                stack += 1
            if text[index] == ')':
                stack -= 1
            if stack == 0 and start >= 0:
                break

        if stack == 0 and start >= 0:
                return (text[start:index + 1], (start, index))
        else:
            return None

    def try_parse_binary(self, str_expression):
        """
        Parses either a conjunction or disjunction

        >>> p = Parser()
        >>> expr = '(P(x)) & (P(y))'
        >>> res = p.try_parse_binary(expr)
        >>> type(res) == conjunction.Conjunction
        True
        >>> res.expr1.predicate.name
        'P'
        >>> tuple(x.name for x in res.expr2.element)
        ('y',)

        >>> expr = '(P(x)) | (Q(x))'
        >>> res = p.try_parse_binary(expr)
        >>> type(res) == disjunction.Disjunction
        True
        >>> res.expr1.predicate.name
        'P'
        >>> tuple(x.name for x in res.expr2.element)
        ('x',)
        """
        str_expression = str_expression.strip()
        result = self.find_closing_parenthesis(str_expression)

        if result:
            (parenthesis, indices) = result
            if indices[0] == 0:
                remainder = str_expression[indices[1] + 1:]
                result2 = self.find_closing_parenthesis(remainder)

                if result2:
                    operator = remainder[:result2[1][0]].strip()
                    str_first_expression = result[0][1: -1]
                    str_second_expression = result2[0][1: -1]

                    if operator in ('&', '|'):
                        expr1 = self.parse(str_first_expression)
                        expr2 = self.parse(str_second_expression)

                        if expr1 and expr2:
                            if operator is '&':
                                return conjunction.Conjunction(expr1, expr2)
                            elif operator is '|':
                                return disjunction.Disjunction(expr1, expr2)

        return None


def test():
    print('Testing')
    import doctest
    doctest.testmod()
    print('Done')

if __name__ == '__main__':
    test()
