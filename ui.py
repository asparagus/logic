#!/usr/bin/python
# -*- coding: utf8 -*-
"""This module contains the ui methods for using the logic brain."""
# if __package__ is not None:
#     import sys
#     sys.path.append('./' + __package__.replace('.', '/'))

# import brain
# import expressions.parser


# def ask_input():
#     return input('>>> ').strip()


# def is_query(expr):
#     return len(expr) > 1 and expr[-1] == '?'


# def run():
#     ada = brain.Brain()
#     chomsky = expressions.parser.Parser()

#     command = ask_input()
#     while command is not "" and command != "quit":
#         if is_query(command):
#             expr = chomsky.parse(command[:-1])
#             print(ada.eval(expr))
#         else:
#             expr = chomsky.parse(command)
#             ada.learn(expr)

#         command = ask_input()


# if __name__ == '__main__':
#     run()
