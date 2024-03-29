#!/usr/bin/env python
# coding: utf-8

# In[1]:


#############################################
#  Readify Coding Challenge - Toy Robot Simulation
#  Simulation of a toy robot moving on a 5 x 5 square tabletop
#  Aakash Deep
##############################################
class ToyRobot:
    '''
        N
    W       E
        S


    04 14 24 34 44
    03 13 23 33 43
    02 12 22 32 42
    01 11 21 31 41
    00 10 20 30 40


    north -> x = x , y + 1
    south -> x = x, y - 1
    east -> x = x + 1, y = y
    west -> x = x - 1, y = y
    '''

    # initialising location, direction, table values
    def __init__(self):
        self.dim = 6        # iteration 1
        self.pointer_x = 0
        self.pointer_y = 0
        self.saved_direction = 'EAST'
        self.dirs = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'NORTH EAST', 'SOUTH EAST', 'NORTH WEST', 'SOUTH WEST']
        self.table = {}
        self.intialise()

    # initialising table entries, 0 means 'no visit', 1 means 'visit'
    def intialise(self):
        for i in range(self.dim):
            for j in range(self.dim):
                self.table[i, j] = 0

    # checking whether location values lie within the range
    def validation(self, num):
        if num >= 0 and num < self.dim:
            return True
        else:
            return False

    def obstruction(self, xx, yy):
        x = int(xx)
        y = int(yy)

        if self.table[x, y] == 2:
            return False        # obstruction
        else:
            return True         # no obstruction

    # placing robot at x, y position, and setting the direction and discarded if obstruction is encountered
    def set_place(self, xx, yy, direction):
        x = int(xx)
        y = int(yy)

        if self.validation(x) and self.validation(y) and self.obstruction(x, y) is True:
            self.table[x, y] = 1
            self.pointer_x = x
            self.pointer_y = y
            self.saved_direction = direction

    # placing robot at x, y position, and setting the direction and discarded if obstruction is encountered
    def set_place_without_direction(self, xx, yy):
        x = int(xx)
        y = int(yy)

        if self.validation(x) and self.validation(y):
            self.table[x, y] = 1
            #self.pointer_x = x
            #self.pointer_y = y


    # avoiding robot due to obstruction on the table
    def set_avoid(self, xx, yy):
        x = int(xx)
        y = int(yy)

        # if coordinates are valid, specify obstruction(2)
        if self.validation(x) and self.validation(y) and (self.pointer_x != x or self.pointer_y != y):
            self.table[x, y] = 2


    # moving robot one unit ahead, along the previous saved direction
    def set_move(self):
        # if direction is NORTH and modifying location value doesn't cause robot to fall outside the table
        if self.dirs[0] == self.saved_direction and self.validation(self.pointer_y + 1) and self.obstruction(self.pointer_x, self.pointer_y+1) is True:  # NORTH
            self.table[self.pointer_x, self.pointer_y + 1] = 1
            self.pointer_x = self.pointer_x
            self.pointer_y = self.pointer_y + 1

        # if direction is SOUTH and modifying location value doesn't cause robot to fall outside the table
        if self.dirs[1] == self.saved_direction and self.validation(self.pointer_y - 1) and self.obstruction(self.pointer_x, self.pointer_y-1) is True:  # SOUTH
            self.table[self.pointer_x, self.pointer_y - 1] = 1
            self.pointer_x = self.pointer_x
            self.pointer_y = self.pointer_y - 1

        # if direction is EAST and modifying location value doesn't cause robot to fall outside the table
        if self.dirs[2] == self.saved_direction and self.validation(self.pointer_x + 1) and self.obstruction(self.pointer_x+1, self.pointer_y) is True:  # EAST
            self.table[self.pointer_x + 1, self.pointer_y] = 1
            self.pointer_x = self.pointer_x + 1
            self.pointer_y = self.pointer_y

        # if direction is WEST and modifying location value doesn't cause robot to fall outside the table
        if self.dirs[3] == self.saved_direction and self.validation(self.pointer_x - 1) and self.obstruction(self.pointer_x-1, self.pointer_y) is True:  # WEST
            self.table[self.pointer_x - 1, self.pointer_y] = 1
            self.pointer_x = self.pointer_x - 1
            self.pointer_y = self.pointer_y

        # if direction is NORTH WEST and modifying location value doesn't cause robot to fall outside the table
        if self.dirs[6] == self.saved_direction and self.validation(self.pointer_x - 1) and self.validation(self.pointer_y + 1) and self.obstruction(
                self.pointer_x - 1, self.pointer_y + 1) is True:  # NORTH WEST
            self.table[self.pointer_x - 1, self.pointer_y + 1] = 1
            self.pointer_x = self.pointer_x - 1
            self.pointer_y = self.pointer_y + 1

            # if direction is NORTH EAST and modifying location value doesn't cause robot to fall outside the table
        if self.dirs[4] == self.saved_direction and self.validation(self.pointer_x + 1) and self.validation(self.pointer_y + 1) and self.obstruction(
                self.pointer_x + 1, self.pointer_y + 1) is True:  # NORTH EAST
            self.table[self.pointer_x + 1, self.pointer_y + 1] = 1
            self.pointer_x = self.pointer_x + 1
            self.pointer_y = self.pointer_y + 1

            # if direction is SOUTH WEST and modifying location value doesn't cause robot to fall outside the table
        if self.dirs[7] == self.saved_direction and self.validation(self.pointer_x - 1) and self.validation(self.pointer_y - 1) and self.obstruction(
                self.pointer_x - 1, self.pointer_y - 1) is True:  # SOUTH WEST
            self.table[self.pointer_x - 1, self.pointer_y - 1] = 1
            self.pointer_x = self.pointer_x - 1
            self.pointer_y = self.pointer_y - 1

            # if direction is SOUTH EAST and modifying location value doesn't cause robot to fall outside the table
        if self.dirs[5] == self.saved_direction and self.validation(self.pointer_x + 1) and self.validation(self.pointer_y - 1) and self.obstruction(
                self.pointer_x + 1, self.pointer_y - 1) is True:  # SOUTH EAST
            self.table[self.pointer_x + 1, self.pointer_y - 1] = 1
            self.pointer_x = self.pointer_x + 1
            self.pointer_y = self.pointer_y - 1

    # Rotate 90 degrees to left and set new direction
    def set_left(self):
        # 0 - NORTH, 1 - SOUTH, 2 - EAST, 3 - WEST
        if self.saved_direction == self.dirs[0]:  # NORTH
            self.saved_direction = self.dirs[6]  # NORTH WEST
        elif self.saved_direction == self.dirs[1]:  # SOUTH
            self.saved_direction = self.dirs[5]  # SOUTH EAST
        elif self.saved_direction == self.dirs[2]:  # EAST
            self.saved_direction = self.dirs[4]  # NORTH EAST
        elif self.saved_direction == self.dirs[3]:  # WEST
            self.saved_direction = self.dirs[7]  # SOUTH WEST
        # 4 - NORTH EAST, 5 - SOUTH EAST, 6 - NORTH WEST, 7 - SOUTH WEST
        elif self.saved_direction == self.dirs[4]:  # NORTH EAST
            self.saved_direction = self.dirs[0]  # NORTH
        elif self.saved_direction == self.dirs[7]:  # SOUTH WEST
            self.saved_direction = self.dirs[1]  # SOUTH
        elif self.saved_direction == self.dirs[6]:  # NORTH WEST
            self.saved_direction = self.dirs[3]  # WEST
        elif self.saved_direction == self.dirs[5]:  # SOUTH EAST
            self.saved_direction = self.dirs[2]  # EAST

    # Rotate 90 degrees to right and set new direction
    def set_right(self):
        # 0 - NORTH, 1 - SOUTH, 2 - EAST, 3 - WEST
        if self.saved_direction == self.dirs[0]:  # NORTH
            self.saved_direction = self.dirs[4]  # NORTH EAST
        elif self.saved_direction == self.dirs[1]:  # SOUTH
            self.saved_direction = self.dirs[7]  # SOUTH WEST
        elif self.saved_direction == self.dirs[2]:  # EAST
            self.saved_direction = self.dirs[5]  # SOUTH EAST
        elif self.saved_direction == self.dirs[3]:  # WEST
            self.saved_direction = self.dirs[6]  # NORTH WEST
        # 4 - NORTH EAST, 5 - SOUTH EAST, 6 - NORTH WEST, 7 - SOUTH WEST
        elif self.saved_direction == self.dirs[4]:  # NORTH EAST
            self.saved_direction = self.dirs[2]  # EAST
        elif self.saved_direction == self.dirs[7]:  # SOUTH WEST
            self.saved_direction = self.dirs[3]  # WEST
        elif self.saved_direction == self.dirs[6]:  # NORTH WEST
            self.saved_direction = self.dirs[0]  # NORTH
        elif self.saved_direction == self.dirs[5]:  # SOUTH EAST
            self.saved_direction = self.dirs[1]  # SOUTH

    # print location and direction values
    def set_report(self):
        print('Output: ' + str(self.pointer_x) + ", " + str(self.pointer_y) + ", " + self.saved_direction)

    # read input file
    def simulate(self, filename):

        # open file
        file = open(filename, "r")

        # read file line by line
        for name in file:
            line = name.strip()
            print(line)

            # split line into tokens
            tokens = line.split(" ")

            # if token is PLACE
            if tokens[0] == 'PLACE':
                nxtpart = tokens[1]
                nxtparttokens = nxtpart.split(",")
                x = nxtparttokens[0]  # get location x
                y = nxtparttokens[1]  # get location y
                if len(nxtparttokens) == 3:
                    direction = nxtparttokens[2]  # get direction

                    # if coordinates are valid, place the robot at the x,y location
                    if self.validation(int(x)) and self.validation(int(y)):
                        self.set_place(x, y, direction)

                else:
                    # if coordinates are valid, place the robot at the x,y location
                    if self.validation(int(x)) and self.validation(int(y)):
                        self.set_place_without_direction(x, y)


            # if token is MOVE and robot has visited atleast one location
            if tokens[0] == 'MOVE' and 1 in self.table.values():
                self.set_move()

            # if token is LEFT and robot has visited atleast one location
            if tokens[0] == 'LEFT' and 1 in self.table.values():
                self.set_left()

            # token is RIGHT and robot has visited atleast one location
            if tokens[0] == 'RIGHT' and 1 in self.table.values():
                self.set_right()

            # if token is REPORT and robot has visited atleast one location
            if tokens[0] == 'REPORT' and 1 in self.table.values():
                self.set_report()

            # if token is AVOID and robot has visited atleast one location
            if tokens[0] == 'AVOID' and 1 in self.table.values():
                nxtpart = tokens[1]
                nxtparttokens = nxtpart.split(",")
                x = nxtparttokens[0]  # get location x
                y = nxtparttokens[1]  # get location y

                # if coordinates are valid, place the robot at the x,y location
                if self.validation(int(x)) and self.validation(int(y)):
                    self.set_avoid(x, y)

            #print(self.pointer_x, self.pointer_y, self.saved_direction)

        # close file
        file.close()

        #print(self.table)


# In[2]:

#make ToyRobot object
toy_robot = ToyRobot()

if __name__ == '__main__':
    import sys
    
    #perform simulation
    toy_robot.simulate(sys.argv[1])   

