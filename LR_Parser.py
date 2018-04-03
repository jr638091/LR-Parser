from productions import Production


class item_SLR:
    def __init__(self, text):
        self.production = Production(text)
        self.point_position = 0

    def shift(self):
        if self.point_position < len(self.production.get_Right) - 1:
            self.point_position += 1

    def reduce(self):
        if self.point_position > 0:
            self.point_position -= 1

    def __eq__(self, item):
        if self.production == item.production and self.point_position == item.point_position:
            return True
        return False


class estado_SLR:
    def __init__(self, items):
        self.items = items
        pass
