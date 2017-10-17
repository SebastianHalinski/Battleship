class Square():
    status_empty = ' '
    status_hit = 'X'
    status_missed = 'O'
    status_ship = '@'

    def __init__(self, x, y, status=status_empty):
        self.x = x
        self.y = y
        self.status = status

    def __str__(self):
        return self.status

    # def get_location(self):
    #     pass
    # implementacja tego i iterowanie po wszystkich
    # elementach ocean?

    def change_status_to_hit(self):
        self.status = self.status_hit

    def change_status_to_missed(self):
        self.status = self.status_missed

    def get_status(self):
        return self.status

    # żeby inne klasy nie używały bezpośrednio atrybutów

    @classmethod
    def get_status_empty(cls):
        return cls.status_empty

    @classmethod
    def get_status_ship(cls):
        return cls.status_ship

    @classmethod
    def get_status_hit(cls):
        return cls. status_hit

# może zamiast status_ship to status_not_hit? albo coś takiego 

s = Square(1, 1)
print(s)
s.change_status_to_hit()
print(s)
s.change_status_to_missed()
print(s)