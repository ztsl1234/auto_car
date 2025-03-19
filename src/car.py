import logging

logger = logging.getLogger(__name__)

class Car:
    def __init__(self, name, x, y, direction, commands, field):
        self.name = name
        self.x = x
        self.y = y
        self.direction_index = ['N', 'E', 'S', 'W'].index(direction)
        self.commands = list(commands)
        self.field = field
        self.has_collided = False
        self.collision_step = None
        self.collision_position = None
        self.collision_with = []

    @property
    def direction(self):
        return ['N', 'E', 'S', 'W'][self.direction_index]

    def rotate_left(self):
        self.direction_index = (self.direction_index - 1) % 4

    def rotate_right(self):
        self.direction_index = (self.direction_index + 1) % 4

    def move_forward(self):
        dx, dy = [(0, 1), (1, 0), (0, -1), (-1, 0)][self.direction_index]
        new_x = self.x + dx
        new_y = self.y + dy
        if self.field.is_within_bounds(new_x, new_y):
            self.x = new_x
            self.y = new_y

    def execute_command(self, command):
        if command == 'L':
            self.rotate_left()
        elif command == 'R':
            self.rotate_right()
        elif command == 'F':
            self.move_forward()

