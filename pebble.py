from lark import Lark 
import sys
from itertools import product, combinations
#from dataclasses import dataclass, field
from enum import Enum
from typing import *
from random import randint, choice

# grammar
with open("grammar.ebnf") as handle: grammar = ''.join(handle.readlines())
parser = Lark(grammar)

with open(sys.argv[1]) as file: program = ''.join(file.readlines())
tree = parser.parse(program)
print(tree.pretty())

