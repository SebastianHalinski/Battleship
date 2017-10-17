class Square():

    SQUARE_STATES = {'empty': ' ',
                     'ship': '@',
                     'hit': 'X',
                     'missed': 'O'}

    def __init__(self, x, y, status):
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
        self.status = self.SQUARE_STATES['hit']

    def change_status_to_missed(self):
        self.status = self.SQUARE_STATES['missed']

    def get_status(self):
        return self.status

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    @classmethod
    def get_status_empty(cls):
        return cls.SQUARE_STATES['empty']

    @classmethod
    def get_status_ship(cls):
        return cls.SQUARE_STATES['ship']

    @classmethod
    def get_status_hit(cls):
        return cls.SQUARE_STATES['hit']

