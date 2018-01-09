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
# Dependency: Python 3.X

(lambda width: print('{tree}\n{root}\n\n{message}\n'.format(tree='\n'.join('{}'.format(('★' * stars).center(width, '.')) for stars in range(1, width, 2)), root='▓'.center(width), message=input("What's your christmas message? ").center(width))))(2 * int(input('How big is your tree?(E.g. 5) '))) # noqa:E501
