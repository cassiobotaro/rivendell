#!/usr/bin/env python3
# One line python code to wish merry christmas with height and
# custom message.
#
#     *
#    ***
#   *****
#  *******
# *********
#     |
#
# Merry christmas!
# Usage: python tree.py
# Dependency: Python 3.12+
# fmt: off
print(f'{'' *  (width := 2 * int(input('How big is your tree?(E.g. 5) ')))}{'\n'.join(f"{'★' * stars:.^{width}}" for stars in range(1, width, 2))}\n{'▓':^{width}}\n\n{input("What's your christmas message? "):^{width}}')
