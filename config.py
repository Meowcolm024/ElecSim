# Copyright (c) 2020 Malcolm Law
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

def logic(lights: (int, int), bump: int) -> (int, int, bool):
    """ logic
    
    Parameters
    ----------
        light : (int, int)
    left and right light sensor

        bump : int
    bump sensor

    Returns
    -------
        (int, int, bool)
    left motor dir and right motor dir and motor status
    """
    left_dir = 0    # left dir output
    right_dir = 0   # right dir output
    motor = False   # motor status
    LOW = 0
    HIGH = 1

    # print(lights)

    leftSensor = lights[0]
    rightSensor = lights[1]

    # if not leftSensor:
    #     left_dir = LOW
    #     right_dir = HIGH
    # else:
    #     left_dir = HIGH
    #     if rightSensor:
    #         right_dir = HIGH
    #     else:
    #         right_dir = LOW

    left_dir = leftSensor//255
    right_dir = rightSensor//255
    
    motor = True

    return (left_dir, right_dir, motor)
