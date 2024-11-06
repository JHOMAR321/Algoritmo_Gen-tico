import robot
import support_functions
import random

maze = [
        [0,0,0,0,0,0,1],
        [0,0,0,1,0,0,0],
        [0,0,1,0,0,0,0],
        [1,0,0,0,0,0,0],
        [0,1,1,0,0,0,0],
        [1,0,0,0,0,0,0]
        ]

robot = robot.Robot((0,0),maze)

for i in range(8):
    limit_max_random = support_functions.max_number_gen_cromosome(robot.position,(6,6))
    print(limit_max_random)
    random_value=random.randint(1,4)
    print(f"{random_value} : {support_functions.selection_move(random_value)}")
    robot.move(support_functions.selection_move(random_value))


