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
