from datetime import datetime
import logging

from field import Field
from car import Car

from utils import utils
from validation_error import ValidationError

logger = logging.getLogger(__name__)

class Simulation:
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValidationError("Width and height must be positive integers.")
                
        self.field = Field(width, height)
        self.cars = []
        self.car_positions = {}  # To check initial position conflicts

    def add_car(self, name, x, y, direction, commands):

        if (x, y) in self.car_positions:
            raise ValidationError(f"Position ({x},{y}) is already occupied by another car.")
        
        if not self.field.is_within_bounds(x, y):
            raise ValidationError(f"Position ({x},{y}) is outside the field boundaries.")
        
        if direction not in ['N', 'S', 'W', 'E']:
            raise ValidationError("Invalid direction. Must be N, S, W, or E.")
        
        if not all(cmd in ['L', 'R', 'F'] for cmd in commands):
            raise ValidationError("Invalid commands. Only L, R, F are allowed.")
        
        car = Car(name, x, y, direction, commands, self.field)
        self.cars.append(car)
        self.car_positions[(x, y)] = car
        print(f"Car {name} added successfully.")

    def run_simulation(self):
        step = 0
        while True:
            # Find cars that can move: not collided and have commands left
            moving_cars = [car for car in self.cars if not car.has_collided and car.commands]
            if not moving_cars:
                break
            step += 1
            # Execute one command for each moving car
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
                if len(cars_at_pos) > 1:
                    for car in cars_at_pos:
                        if not car.has_collided:
                            car.has_collided = True
                            car.collision_step = step
                            car.collision_position = pos
                            car.collision_with = [c.name for c in cars_at_pos if c != car]
        # Print results
        for car in self.cars:
            if car.has_collided:
                collided_with = ', '.join(car.collision_with)
                pos_str = f"({car.collision_position[0]},{car.collision_position[1]})"
                print(f"- {car.name}, collides with {collided_with} at {pos_str} at step {car.collision_step}")
            else:
                print(f"- {car.name}, ({car.x},{car.y}) {car.direction}")

