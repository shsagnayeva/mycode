#!/usr/bin/env python3

"""
Author: Test

This program prints some things to the screen
"""

import crayons


def main():
    """Main program"""
    print(crayons.red('red string'))
    print(f"{crayons.red('red')} white {crayons.blue('blue')}") 
    crayons.disable()
    print(f"{crayons.red('red')} white {crayons.blue('blue')}")
    crayons.DISABLE_COLOR = False
    print(f"{crayons.red('red')} white {crayons.blue('blue')}")
    print(crayons.red('red string', bold=True))
    print(crayons.yellow('yellow string', bold=True))
    print(crayons.magenta('magenta string', bold=True))
    print(crayons.white('white string', bold=True))


if __name__ == main():
    main()
