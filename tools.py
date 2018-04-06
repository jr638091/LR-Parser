epsilon = '@'
EOF = "$"

class Node:
    def __init__(self, * args):
        if len(args) < 2:
            self.next = None
            self.last = None
            if len(args) == 0:
                self.value = None
            else:
                self.value = args[0]
        else:
            self.value = args[0]
            self.next = args[1]
            self.last = args[2]


class Linked_list:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.count = 0

    def append(self, value):
        if self.count == 0:
            self.head = self.tail = Node(value)
        else:
            self.tail.next = Node(value, self.tail, None)
        self.count += 1

    def __getitem__(self, key):
        r = self.head
        while key > 0:
            r = self.head.next
        return r


class Firsts:
    def __init__(self):
        self.keys = []
        self.firsts = []

    def __setitem__(self, key, Values):
        if key in self.keys:
            i = 0
            for i in range(0, len(self.keys)):
                if key == self.keys[i]:
                    break
            for j in Values:
                if not j in self.firsts[i]:
                    self.firsts[i].append(j)
        else:
            self.keys.append(key)
            self.firsts.append(Values.copy())

    def insert_one_first(self, key, value):
        if key in self.keys:
            values = self[key]
            if not value in values:
                values.append(value)
                self[key] = values
                return True
            return False
        else:
            self.keys.append(key)
            self.firsts.append([value])

    def insert_various_firsts(self, key, Values):
        if key in self.keys:
            values = self[key]
            r = False
            for i in Values:
                if not i in values:
                    values.append(i)
                    r = True
            self[key] = values
            return r
        else:
            self.keys.append(key)
            self.firsts.append(Values)
            return True

    def __getitem__(self, key):
        if not key in self.keys:
            return[]
        i = 0
        for i in range(0, len(self.keys)):
            if key == self.keys[i]:
                break
        return self.firsts[i].copy()

    def remove_value(self, key, value):
        i = 0
        for i in range(0, len(self.keys)):
            if key == self.keys[i]:
                break
        if key in self.firsts[i]:
            self.firsts.remove(key)

    def __str__(self):
        result = ""
        for i in range(0, len(self.keys)):
            result += str(self.keys[i]) + ":" + str(self.firsts[i])+"\n"
        return result


class Follow:
    def __init__(self):
        self.keys = []
        self.follow = []

    def __setitem__(self, key, Values):
        if key in self.keys:
            i = 0
            for i in range(0, len(self.keys)):
                if key == self.keys[i]:
                    break
            for j in Values:
                if not j in self.follow[i]:
                    self.follow[i].append(j)
        else:
            self.keys.append(key)
            self.follow.append(Values.copy())

    def insert_one_first(self, key, value):
        if key in self.keys:
            values = self[key]
            if not value in values:
                values.append(value)
                self[key] = values
                return True
            return False
        else:
            self.keys.append(key)
            self.follow.append([value])

    def insert_various_follow(self, key, Values):
        if key in self.keys:
            values = self[key]
            r = False
            for i in Values:
                if not i in values:
                    values.append(i)
                    r = True
            self[key] = values
            return r
        else:
            self.keys.append(key)
            self.follow.append(Values)
            return True

    def __getitem__(self, key):
        if not key in self.keys:
            return[]
        i = 0
        for i in range(0, len(self.keys)):
            if key == self.keys[i]:
                break
        return self.follow[i].copy()

    def remove_value(self, key, value):
        i = 0
        for i in range(0, len(self.keys)):
            if key == self.keys[i]:
                break
        if key in self.follow[i]:
            self.follow.remove(key)

    def __str__(self):
        result = ""
        for i in range(0, len(self.keys)):
            result += str(self.keys[i]) + ":" + str(self.follow[i])+"\n"
        return result

def first(G):
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


def first_special(list,f):
    result = []
    for i in list:
        for j in f[i]:
            if not j in result and j != epsilon:
                result.append(j)
        if not epsilon in f[i]:
            return result, False
    return result, True


def follow(G,f):
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
                    right_part[index + 1:len(right_part)],f)
                if follows.insert_various_follow(right_part[index], first):
                    has_been_modified = True
                if all_epsilon:
                    if follows.insert_various_follow(right_part[index], follows[left_part]):
                        has_been_modified = True
        if not has_been_modified:
            break
    return follows