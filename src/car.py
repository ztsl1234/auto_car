import logging

logger = logging.getLogger(__name__)

class Car:
    
    available_directions=['N', 'E', 'S', 'W'] #index 0,1,2,3
    available_commands=['L', 'R', 'F']
    available_moves=[(0, 1), (1, 0), (0, -1), (-1, 0)] 

    def __init__(self, name, x, y, direction, commands, field):
        self.name = name

        #initial position
        self.x = x
        self.y = y

        #index of the direction in the list
        self.direction_index = self.available_directions.index(direction)
        
        self.commands = list(commands)

        self.field = field

        self.has_collided = False

        self.collision_step = None
        self.collision_position = None
        self.collision_with = []

    @property
    def direction(self):
        return self.available_directions[self.direction_index]

    def rotate_left(self):
        """
        Turn car to the left

        e.g. N rotate left becomes W (index 0 -1 => -1%4 = -1 => last element => W)
        W rotate left becomes S (index 3 - 1 => 2%4 = 2 => S)
        S rotate left becomes E (index 2 - 1 => 1%4 = 1 => E)
        E rotate left becomes N (index 1 - 1 => 0%4 = 0 => N)
        """
        self.direction_index = (self.direction_index - 1) % len(self.available_directions)

    def rotate_right(self):
        """
        Turn car to the right

        e.g. N rotate right becomes E (index 0 + 1 => 1%4 =1 => E)
        E rotate right becomes S (index 1 + 1 => 2%4 = 2=> S)
        S rotate right becomes W (index 2 + 1 => 3%4 = 3 => W)
        W rotate right becomes N (index 3 + 1 = 4%4 =0 => => N)
        """
        self.direction_index = (self.direction_index + 1) % len(self.available_directions)

    def move_forward(self):
        """
        Move forward 1 step depending on the direction
        and check if still within the field
        """

        #to move forward 1 step for each direction
        dx, dy = self.available_moves[self.direction_index]

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