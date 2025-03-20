import logging

logger = logging.getLogger(__name__)

class Car:
    def __init__(self, name, x, y, direction, commands, field):
        self.name = name

        #initial position
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
        """
        change the direction of the car

        e.g. N rotate left becomes W
        
        """
        self.direction_index = (self.direction_index - 1) % 4

    def rotate_right(self):
        """
        change the direction of the car

        e.g. N rotate right becomes E
        
        """
        self.direction_index = (self.direction_index + 1) % 4

    def move_forward(self):
        """
        Move forward 1 step depending on the direction
        and check if still within the field
        """

        dx, dy = [(0, 1), (1, 0), (0, -1), (-1, 0)][self.direction_index]

        new_x = self.x + dx
        new_y = self.y + dy

        #check if still within field
        if self.field.is_within_bounds(new_x, new_y):
            self.x = new_x
            self.y = new_y

    def execute_command(self, command):
        """
        execute command for 1 step

        Args:
            command (_type_): L,R,F
        """
        if command == 'L':
            self.rotate_left()
        elif command == 'R':
            self.rotate_right()
        elif command == 'F':
            self.move_forward()

