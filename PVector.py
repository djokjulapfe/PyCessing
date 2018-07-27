"""

<LINK>

Abstract:


"""

import random
from PConstants import *
from math import sin, cos


class DVector:

    def __init__(self, x=0.0, y=0.0, z=0.0):
        """
        Initializes vector's coordinates.

        Args:
            x (float): Initial x coordinate.
            y (float): Initial y coordinate.
            z (float): Initial z coordinate.
        """

        self.x = x
        self.y = y
        self.z = z

    def set(self, x, y, z=None):
        """
        Changes vector's coordinates.
        Args:
            x (new): Initial x coordinate.
            y (new): Initial y coordinate.
            z (new): Initial z coordinate.
        """

        self.x = x
        self.y = y
        self.z = z if z is not None else self.z

    @staticmethod
    def random2D(r=1):
        """

        Args:
            r ():

        Returns:

        """

        phi = random.uniform(0, 2 * PI)
        x, y = r * cos(phi), r * sin(phi)
        return DVector(x, y)
