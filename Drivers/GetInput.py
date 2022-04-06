#from Drivers.Connect import gyro
from random import randrange

class gyro_data:
    #data = gyro()
    current_traj = []
    MAX_X = 20 # Change on max angle 
    MAX_Y = 20 # Change on max angle
    MAX_Z = 20 # Change on max angle
    def __init__(self):
        self.current_traj = [0,0,0]


    def set_data(self, x, y, z):
        self.current_traj = [x, y, z]

    

class output:
    MAX_SENSITIVITY = 1
    up = 0 # The angle at which the controller is up. Farther pressed the faster the object moves
    side = 0 # The angle to the side it is. Farther the faster to the side it moves.
    def __init__(self):
        self.up = 0
        self.side = 0
        self.data = gyro_data()

    # Gets data from the gyroscope or test_data
    def get_data(self):
        #Call accelerometer/gyro data or test data
        x = (randrange(3)- 1)/4
        y = 0
        z = 0
        self.data.set_data(x, y, z)
    # Sets the direction and the magnitude of the direction
    def set_output(self):
        if self.data.current_traj[0] < 0:
            self.up = int(self.data.current_traj[0]/self.data.MAX_X) - (self.data.current_traj[0] % self.data.MAX_X > 0)
        else:
            self.up = int(self.data.current_traj[0] / self.data.MAX_X) + (
                        self.data.current_traj[0] % self.data.MAX_X > 0)
        if self.data.current_traj[1] < 0:
            self.side = int(self.data.current_traj[1]/self.data.MAX_Y) - (self.data.current_traj[1] % self.data.MAX_Y > 0)
        else:
            self.side = int(self.data.current_traj[1] / self.data.MAX_Y) + (
                        self.data.current_traj[1] % self.data.MAX_Y > 0)

    def update(self):
        self.get_data()
        self.set_output()

