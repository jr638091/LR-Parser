class Production:

    epsilon = "@"

    def __init__(self, text):
        left = text.split('->')[0]
        right = text.split('->')[1]
        left = left.split()
        while'' in left:
            left.remove('')
        left = left[0]
        right = right.split()
        while'' in right:
            right.remove('')
        self.left = left
        self.right = right

    def to_epsilon(self):
        if self.epsilon in self.right and len(self.right) == 1:
            return True
        return False

    def __str__(self):
        result = self.left + " -> "
        for i in self.right:
            result += i + ' '
        return result

    def get_Left(self):
        return self.left

    def get_Right(self):
        return self.right

    def __eq__(self, production):
        if self.left != production.left:
            return False
        if len(self.right) != len(production.right):
            return False
        a = self.right.copy()
        b = self.right.copy()
        a.sort()
        b.sort()
        for i in range(0, len(self.right)):
            if a[i] != b[i]:
                return False
        return True
