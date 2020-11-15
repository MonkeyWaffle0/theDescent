from data.scripts.level_generator.config import EMPTY, TAKEN, ROOM


class Grid:
    def __init__(self):
        self.tile = 1024
        self.width = 9
        self.height = 9
        self.grid = [[0 for _ in range(10)] for _ in range(10)]

    def get_room(self, pos):
        return self.grid[pos[0]][pos[1]]

    def check_top(self, point):
        if point[0] == 0:
            return None
        else:
            return self.get_top(point)

    def check_bottom(self, point):
        if point[0] == self.height:
            return None
        else:
            return self.get_bottom(point)

    def check_left(self, point):
        if point[1] == 0:
            return None
        else:
            return self.get_left(point)

    def check_right(self, point):
        if point[1] == self.width:
            return None
        else:
            return self.get_right(point)

    def check_bottom_right(self, point):
        return point[0] == self.height or point[1] == self.width or self.get_grid_right(self.get_bottom(point)) != EMPTY

    def check_around(self, point):
        return {'top': self.check_top(point), 'bottom': self.check_bottom(point), 'left': self.check_left(point),
                'right': self.check_right(point)}

    def get_grid_top(self, point):
        return self.grid[point[0] - 1][point[1]]

    def get_grid_bottom(self, point):
        return self.grid[point[0] + 1][point[1]]

    def get_grid_left(self, point):
        return self.grid[point[0]][point[1] - 1]

    def get_grid_right(self, point):
        return self.grid[point[0]][point[1] + 1]

    def get_top(self, point):
        return point[0] - 1, point[1]

    def get_bottom(self, point):
        return point[0] + 1, point[1]

    def get_left(self, point):
        return point[0], point[1] - 1

    def get_right(self, point):
        return point[0], point[1] + 1

    def take(self, pos):
        room = dict(ROOM)
        room['pos'] = pos
        self.grid[pos[0]][pos[1]] = room

    def place_room(self, room, pos):
        self.take(pos)
        if room['shape']['letter'] == 'I':
            if self.check_bottom(pos):
                return False
            else:
                self.take(self.get_bottom(pos))
        elif room['shape']['letter'] == '_':
            if self.check_right(pos):
                return False
            else:
                self.take(self.get_right(pos))
        elif room['shape']['letter'] == 'O':
            if self.check_right(pos) or self.check_bottom(pos) or self.check_bottom_right(pos):
                return False
            else:
                self.take(self.get_right(pos))
                self.take(self.get_bottom(pos))
                self.take(self.get_bottom(self.get_right(pos)))
        return True

    def __iter__(self):
        for row in self.grid:
            for room in row:
                yield room

    def __str__(self):
        string = ''
        for row in self.grid:
            for char in row:
                string += str(char)
            string += '\n'
        return string

