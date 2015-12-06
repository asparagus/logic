if __package__ is not None:
    import sys
    sys.path.append('./' + __package__.replace('.', '/'))

import brain
import expressions.parser

if __name__ == '__main__':
    b = brain.Brain()
    p = expressions.parser.Parser()

    command = input()
    while command is not "" and command is not "quit":
        e = p.parse(command)
        print(e)
        command = input()
