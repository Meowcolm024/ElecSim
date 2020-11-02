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

    return (left_dir, right_dir, motor)