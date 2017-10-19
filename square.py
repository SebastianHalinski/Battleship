class Square():

    SQUARE_STATES = {'empty': ' ',
                     'ship': '#',
                     'hit': 'X',
                     'missed': 'O'}

    def __init__(self, x, y, status):
        self.x = x
        self.y = y
        self.status = status

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def __str__(self):
        return self.status

    def get_status(self):
        return self.status

    def set_status(self, new_status):
        self.status = self.SQUARE_STATES[new_status]
