**file: input.txt **
 
PLACE 1,2,EAST
MOVE
MOVE
LEFT
MOVE
REPORT

Method 1 - Command line

python toy_robot.py input.txt

or 

python -m toy_robot input.txt

Method 2 - Loading Module

from toy_robot import ToyRobot
run = ToyRobot()
run.simulate('input.txt')
