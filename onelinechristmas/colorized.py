#!/usr/bin/env python3
# One line python code to wish merry christmas with custom height and
# message.
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

(lambda width: print('\033[0;32;40m{tree}\n{root}\n\n\033[5;31;40m{message}\n'.format(tree='\n'.join('{}'.format(('★' * stars).center(width, '.')) for stars in range(1, width, 2)), root='▓'.center(width), message=input("What's your christmas message? ").center(width))))(2 * int(input('How big is your tree?(E.g. 5) '))) # noqa:E501
