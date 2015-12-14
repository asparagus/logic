import brain
import expressions.parser


class Agent:
    def __init__(self):
        self.brain = brain.Brain()
        self.parser = expressions.parser.Parser()

        self.learn('Say(ariel,hello)>Say(self,hello)')

    def learn(self, rule_str):
        self.brain.learn(self.parser.parse(rule_str))

    def interact(self):
        speaker = input("What is your name?: ")
        print(self.brain)
        while(True):
            speech = input()
            expression = self.parser.parse('Say(%s, %s)' % (speaker, speech))

            if expression in self.brain.rules:
                responses = self.brain.rules[expression]
                for response in responses:
                    if response.type() == 'Atomic':
                        if response.predicate.name == 'Say':
                            if response.arguments[0].name == 'self':
                                for argument in response.arguments[1:]:
                                    print(argument.name)


if __name__ == '__main__':
    a = Agent()
    a.interact()
