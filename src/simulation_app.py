import logging

from utils import utils
from simulation import Simulation
from validation_error import ValidationError

logger = logging.getLogger(__name__)

class SimulationApp:
    #????
    #def __init__(self):
        

    def run(self):
        
        while True:            
            print("\nWelcome to Auto Driving Car Simulation!")
            loop_flag1=True
            while loop_flag1:
                #Setup Field
                try:
                    width, height = map(int, input("\nPlease enter the width and height of the simulation field in x y format: ").split())
                    self.sim = Simulation(width, height)
                    print(f"\nYou have created a field of {width} x {height}.")
                    loop_flag1=False #exit this loop
                except ValueError:
                    print("Please enter two integers separated by a space.")
                except (ValidationError) as e:
                    print(f"{str(e)}")                    

            #main menu
            loop_flag2=True
            while loop_flag2:                
                print("\nPlease choose from the following options:")
                print("[1] Add a car to field")
                print("[2] Run simulation")
        
                choice = input()

                if choice == '1':
                    self.add_car()
                elif choice == '2':
                    if not self.run_simulation():
                        return #exit program
                    else:
                        loop_flag2=False #exit this loop
                else:
                    print("Invalid choice.")

    def add_car(self):
        """
        This function will handle the Add Car function in the Simulation
        """
        name = input("\nPlease enter the name of the car: ")

        loop_flag=True
        while loop_flag:
            try:
                pos_dir = input(f"\nPlease enter initial position of car {name} in x y Direction format: ").split()
                x, y, direction = int(pos_dir[0]), int(pos_dir[1]), pos_dir[2].upper()
                
                commands = input(f"\nPlease enter the commands for car {name}: ").upper()
            
                self.sim.add_car(name, x, y, direction, commands)

                print("\nYour current list of cars are:")
                for car in self.sim.cars:
                    print(f"- {car.name}, ({car.x},{car.y}) {car.direction}, {''.join(car.commands)}")

                loop_flag=False #no error exit loop                            
            except (ValueError, IndexError):
                print("Please enter two integers and a direction (N, S, W, E) separated by spaces.")
            except (ValidationError) as e:
                print(f"{str(e)}")                    

    def run_simulation(self):
        """
        This function allows user to run the simulation 
        """
        
        print("\nYour current list of cars are:")
        for car in self.sim.cars:
            print(f"- {car.name}, ({car.x},{car.y}) {car.direction}, {''.join(car.commands)}")
            print("\nAfter simulation, the result is:")
            self.sim.run_simulation()
            
        loop_flag=True
        while loop_flag:
            print("\nPlease choose from the following options:")
            print("[1] Start over")
            print("[2] Exit")

            post_choice = input()
            
            if post_choice == '1':
                return True
            elif post_choice == '2':
                print("Thank you for running the simulation. Goodbye!")
                return False
            else:
                print("Invalid choice.")
     