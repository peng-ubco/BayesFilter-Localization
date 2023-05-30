from plot import plot
import numpy as np


class Robot1D:
    def __init__(self, pos):
        self.pos = pos   # robot initialized position

    def move(self):
        self.pos += 1

    def pole_detected(self, poles):
        if self.pos + 1 in poles:
            return True
        else:
            return False


def bayes(PBA, PA, PB):
    """your code here"""
    '''****************'''
    # This function compute the Bayes rule and returns the posterior probability
    PAB = PBA*PA / PB
    '''****************'''
    return PAB


def shift_prior(P_loc_i):
    """your code here"""
    '''****************'''
    # Shift all probabilities to the right by one.
    for i in range(len(P_loc_i)-1, 0, -1):
        P_loc_i[i] = P_loc_i[i-1]
    P_loc_i[0] = 0
    '''****************'''


def update_loc_posteri():
    """your code here"""
    '''****************'''
    # Perform Bayes Rule on each location.
    for i in range(distance):
        if robot.pole_detected(poles):
            P_loc_i_posteri[i] = bayes(
                P_D_given_loc_i[i],
                P_loc_i_prior[i],
                P_D
            )
        else:
            P_loc_i_posteri[i] = bayes(
                P_not_D_given_loc_i[i],
                P_loc_i_prior[i],
                P_not_D
            )
    '''****************'''


distance = 40

robot = Robot1D(pos=2)
poles = [5, 9, 13]

# Initalize variables (generally you do not need to do this in python,
# but I did this so you can see if the variable is a vector or a scalar.)
# Initalize bayes probabilities. Create as many probabilities or beliefs as
# the same number of discrete locations the robot can occupy.
P_loc_i_prior = np.zeros(distance)  # P(Li) - Prior belief of being in location i.
P_loc_i_posteri = np.zeros(distance)  # posterior belief of being in location i, updated by performing Bayes Rule.
P_D = 0.   # P(D) -- Probability of Detecting a Pole.
P_not_D = 0.   # P(!D) -- Probability of Not Detecting Pole.
P_D_given_loc_i = np.zeros(distance)  # P(D|Li) - Probability of detecting a pole, given at location i.
P_not_D_given_loc_i = np.zeros(distance)  # P(!D|Li) - Probability of not detecting a pole, given at location i.

"""your code here"""
'''****************'''
# Set the prior assuming the robot has equal probability to be at each location.
P_loc_i_prior += 1 / distance
# Set probabilities of detecting a pole or not.
P_D = len(poles) / distance
P_not_D = 1 - P_D
# Sensor model (Observation model):
# Set the probabilities for a pole being detected or not detected for each location i.
# Assuming the sensor can 100% accurately detect the pole only at one-unit before the pole
for i in range(distance):
    if i+1 in poles:
        P_D_given_loc_i[i] = 1.0
    else:
        P_D_given_loc_i[i] = 0.
P_not_D_given_loc_i = 1.0 - P_D_given_loc_i
'''****************'''


# Setup done, run the first calculation for the probabilities of robots location.
update_loc_posteri()
plot(distance, poles, P_loc_i_posteri, robot, block=True)

# Begin Moving
for j in range(13):
    robot.move()
    # Shift the priors to follow the robot moving.
    shift_prior(P_loc_i_posteri)
    # Set prior using the previous posterior, so we can start the iteration over again.
    P_loc_i_prior = P_loc_i_posteri
    # Perform Bayes Rule using new measurement about whether the robot sensor detected a pole.
    update_loc_posteri()
    plot(distance, poles, P_loc_i_posteri, robot)

plot(distance, poles, P_loc_i_posteri, robot, block=True, pause_time=1)
