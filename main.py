from grammar import Grammar
from tools import Firsts, Follow

productions = "E   -> T X \n X ->  + E\n X -> @ \n    T     ->     int    Y \nT-> ( E )\nY-> * T\nY-> @"

epsilon = '@'
EOF = '$'


def first():
    firsts = Firsts()

    for i in G.terminals:
        firsts[i] = [i]

    while True:
        has_been_modified = False
        for i in G.productions:
            left_part = i.left
            right_part = i.right
            if i.to_epsilon():
                has_been_modified = firsts.insert_one_first(left_part, epsilon)
            else:
                all_epsilon = True
                for j in right_part:
                    firsts.insert_various_firsts(left_part, firsts[j])
                    if not epsilon in firsts[j]:
                        all_epsilon = False
                        break
                if all_epsilon:
                    firsts.insert_one_first(left_part, epsilon)

        if not has_been_modified:
            break

    return firsts


def first_special(list):
    result = []
    for i in list:
        for j in f[i]:
            if not j in result and j != epsilon:
                result.append(j)
        if not epsilon in f[i]:
            return result, False
    return result, True


def follow():
    follows = Follow()
    follows[G.distinguished] = [EOF]
    while True:
        has_been_modified = False
        for i in G.productions:
            left_part = i.get_Left()
            right_part = i.get_Right()
            for index in range(0, len(right_part)):
                if right_part[index] in G.terminals:
                    continue
                first, all_epsilon = first_special(
                    right_part[index + 1:len(right_part)])
                if follows.insert_various_follow(right_part[index], first):
                    has_been_modified = True
                if all_epsilon:
                    if follows.insert_various_follow(right_part[index], follows[left_part]):
                        has_been_modified = True
        if not has_been_modified:
            break
    return follows


G = Grammar(productions, 'E')
print(G)
# print(G.terminals, G.not_terminals)
f = first()
print(f)
fo = follow()
print(fo)
