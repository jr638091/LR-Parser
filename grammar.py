from productions import Production


class Grammar:
    def __init__(self, productions, distinguished):
        self.distinguished = distinguished
        self.productions = []
        for i in productions.split('\n'):
            self.productions.append(Production(i))
        self.not_terminals = []
        self.terminals = []
        self.taking_not_terminals()
        self.taking_terminals()
        self.epsilon = "@"
        self.EOF = "$"

    def taking_not_terminals(self):
        for i in self.productions:
            if not i.left in self.not_terminals:
                self.not_terminals.append(i.left)

    def taking_terminals(self):
        for i in self.productions:
            for j in i.get_Right():
                if not j in self.terminals and not j in self.not_terminals:
                    self.terminals.append(j)

    def __str__(self):
        result = ""
        for i in self.productions:
            result += str(i) + '\n'
        return result[0:-1]

