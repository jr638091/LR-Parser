from grammar import Grammar
from tools import first, follow
from LR_Parser import SLR_automata, G

productions = "E   -> T X \n X ->  + E\n X -> @ \n    T     ->     int    Y \nT-> ( E )\nY-> * T\nY-> @"

epsilon = '@'
EOF = '$'

G = Grammar(productions, 'E')
print(G)
print(G.terminals, G.not_terminals)
SLR_a = SLR_automata(G)
print(SLR_a.firsts)
print(SLR_a.follows)
print(SLR_a)
