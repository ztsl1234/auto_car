from datetime import datetime
import logging

from field import Field
from car import Car

from utils import utils
from validation_error import ValidationError

logger = logging.getLogger(__name__)

class Simulation:
    def __init__(self, width, height):
        """
        Constructor

        Args:
            width (_type_): width of Field
            height (_type_): height of Field

        Raises:
            ValidationError: _description_
        """
        if width <= 0 or height <= 0:
            raise ValidationError("Width and Height must be positive integers.")
                
        #create field
        self.field = Field(width, height)
        self.cars = []
        self.car_positions = {}  # pos-list of cars 

    def add_car(self, name, x, y, direction, commands):
        """
        Function to Add car to the Field

        Args:
            name (_type_): name of car
            x (_type_): x position of car
            y (_type_): y position of car
            direction (_type_): direction of car
            commands (_type_): commands to apply to car

        Raises:
            ValidationError: Postion already occupied by another car
            ValidationError: Car outside the Field
            ValidationError: Invalid direction
            ValidationError: Invalid command
        """

        if (x, y) in self.car_positions:
            raise ValidationError(f"Position ({x},{y}) is already occupied by another car.")
        
        if not self.field.is_within_bounds(x, y):
            raise ValidationError(f"Position ({x},{y}) is outside the field boundaries.")
        
        if direction not in Car.available_directions:
            raise ValidationError(f"Invalid direction. Must be one of these values {Car.available_directions}.")
        
        if not all(cmd in Car.available_commands for cmd in commands):
            raise ValidationError(f"Invalid commands. Only these commands {Car.available_commands} are allowed.")
        
        car = Car(name, x, y, direction, commands, self.field)
        self.cars.append(car)
        self.car_positions[(x, y)] = car

    def run_simulation(self):
        """
        This function runs the simulation of the cars moving
        """
        step = 1
        # Find cars that can still move - those not collided and still have commands left
        moving_cars = [car for car in self.cars if not car.has_collided and car.commands]

        # no more moving cars => exit loop
        while moving_cars:
            # Execute one command(1 step) for each moving car
            for car in moving_cars:
                command = car.commands.pop(0)
                car.execute_command(command)
            
            # Check for collisions
            position_to_cars = {}
            for car in self.cars:
                pos = (car.x, car.y)
                if pos not in position_to_cars:
                    position_to_cars[pos] = []
                position_to_cars[pos].append(car)
            
            # Mark collisions
            for pos, cars_at_pos in position_to_cars.items():
                #more than 1 car at same position => collision
                if len(cars_at_pos) > 1:
                    for car in cars_at_pos:
                        if not car.has_collided:
                            car.has_collided = True
                            car.collision_step = step
                            car.collision_position = pos
                            car.collision_with = [c.name for c in cars_at_pos if c != car]

            # for next loop:
            # Find cars that can still move - those not collided and still have commands left
            moving_cars = [car for car in self.cars if not car.has_collided and car.commands]
            step += 1
            
        # Print results at the end of simulation
        for car in self.cars:
            if car.has_collided:
                collided_with = ', '.join(car.collision_with)
                pos_str = f"({car.collision_position[0]},{car.collision_position[1]})"
                print(f"- {car.name}, collides with {collided_with} at {pos_str} at step {car.collision_step}")
            else:
                print(f"- {car.name}, ({car.x},{car.y}) {car.direction}")   