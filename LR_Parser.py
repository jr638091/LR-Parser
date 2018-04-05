from productions import Production
from queue import Queue
from grammar import Grammar

G = None

class SLR_item:
    def __init__(self, text, point_position):
        self.production = Production(text)
        self.point_position = point_position

    def shift(self):
        if self.point_position < len(self.production.get_Right()):
            self.point_position += 1
            return True
        return False

    def get_next_token(self):
        if self.point_position == len(self.production.get_Right()): return '$'
        else: return self.production.get_Right()[self.point_position]

    def reduce(self):
        if self.point_position > 0:
            self.point_position -= 1

    def __eq__(self, item):
        if self.production == item.production and self.point_position == item.point_position:
            return True
        return False

    def __str__(self):
        r = self.production.get_Left() + " -> "
        for i in range(0,len(self.production.get_Right())):
            if i == self.point_position:
                r+='.'
            r += self.production.get_Right()[i]
        if self.point_position == len(self.production.get_Right()):
            r+='.'
        return r

class SLR_state:
    def __init__(self, productions,state_number):
        self.items = []
        for i in productions:
            i = SLR_item(str(i),0)
            if not i.production.to_epsilon():
                self.items.append(i)
        self.state_number = state_number
        
    def expand(self,items,G):
        for i in items:
            if i.get_next_token() in G.not_terminals:
                for j in G.productions:
                    if not j.to_epsilon() and j.get_Left() == i.get_next_token():
                        temp_item = SLR_item(str(j),0)
                        if not temp_item in items:
                            items.append(temp_item)     

    def __eq__(self,state):
        if len(self.items) != len(state.items):
            return False
        for i in self.items:
            if not i in state.items:
                return False
        for i in state.items:
            if not i in self.items:
                return False
        return True

    def move(self, token,grammar):
        items = []
        for i in self.items:
            if i.get_next_token() == token:
                item_2 = SLR_item(str(i.production),i.point_position)
                if item_2.shift():
                    items.append(SLR_item(str(item_2.production),item_2.point_position))
                else: return None
        self.expand(items,grammar)
        return items

    def __str__(self):
        r = ""
        for i in self.items:
            r+= str(i) + '\n'
        return r

    def token_to_analize(self):
        tokens = []
        for i in self.items:
            if not i.get_next_token in tokens:
                tokens.append(i.get_next_token())
        return tokens


class SLR_automata:
    def __init__(self, grammar):
        self.G = grammar
        self.states = []
        production_prim = Production("S_prim -> " + grammar.distinguished)
        self.insert_state(SLR_state([production_prim],0))
        self.states[0].expand(self.states[0].items, self.G)
        self.goto = {}
        self.queue = Queue()
        self.queue.put(self.states[0])

    def insert_state(self, state):
        for i in range(0, len(self.states)):
            if self.states[i] == state:
                return i
        else:
            self.states.append(state)
            return state.state_number

    def move_action(self):
        while not self.queue.empty():
            state_to_analize = self.queue.get()
            token = state_to_analize.token_to_analize()
            for i in token:
                temp_state = SLR_state([],0)
                temp_state.items = state_to_analize.move(i,self.G)
                temp_state.state_number = len(self.states)
                if temp_state.items != None:
                    number_st = self.insert_state(temp_state)
                    if (state_to_analize.state_number,i) in self.goto.keys():
                        self.goto[(state_to_analize.state_number,i)].append(number_st)
                    else:
                        self.goto[(state_to_analize.state_number,i)] = [number_st]
                    if temp_state.state_number == self.states[-1].state_number:
                        self.queue.put(temp_state)
                    
            

    def __str__(self):
        r = ''
        for i in self.states:
            r += "q "+str(i.state_number) +":\n" + str(i) + '\n'
        return r