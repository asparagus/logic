#!/usr/bin/python
# -*- coding: utf8 -*-
"""This module contains the Agent class."""
# import brain
# import expressions.parser


# class Agent:
#     """An Agent is an class capable of using logic."""

#     def __init__(self):
#         """Initialize an agent with an empty brain."""
#         self.brain = brain.Brain()
#         self.parser = expressions.parser.Parser()

#         self.learn('Say(ariel,hello)>Say(self,hello)')

#     def learn(self, rule_str):
#         """Learn a new rule."""
#         self.brain.learn(self.parser.parse(rule_str))

#     def interact(self):
#         """Interact with a brain
#         speaker = input("What is your name?: ")
#         print(self.brain)
#         while(True):
#             speech = input()
#             expression = self.parser.parse('Say(%s, %s)' % (speaker, speech))

#             if expression in self.brain.rules:
#                 responses = self.brain.rules[expression]
#                 for response in responses:
#                     if response.type() == 'Atomic':
#                         if response.predicate.name == 'Say':
#                             if response.arguments[0].name == 'self':
#                                 for argument in response.arguments[1:]:
#                                     print(argument.name)


# if __name__ == '__main__':
#     a = Agent()
#     a.interact()
