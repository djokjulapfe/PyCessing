"""

<https://github.com/djokjulapfe/PyCessing>

Abstract:
    A Vector with Descarte's coordinates. Enables simple storage of vectors and common linear algebra operations such
    as adding, dot product, cross product, rotation...

# TODO: This class is under construction.

"""

import random
from PConstants import *
from math import sin, cos, sqrt


class PVector:

    def __init__(self, x=0.0, y=0.0, z=0.0):
        """ Initializes vector's coordinates.

        Args:
            x (float): Initial x coordinate.
            y (float): Initial y coordinate.
            z (float): Initial z coordinate.

        """

        self.x = x
        self.y = y
        self.z = z

    def set(self, x, y, z=None):
        """ Changes vector's coordinates.

        Args:
            x (new): Initial x coordinate.
            y (new): Initial y coordinate.
            z (new): Initial z coordinate.

        """

        self.x = x
        self.y = y
        self.z = z if z is not None else self.z

    def __add__(self, other):
        """ Adds two vectors together.

        Args:
            other (PVector): The rhs operand.

        Returns:
            PVector: Vectors added together

        """
        return PVector(self.x + other.x, self.y + other.y, self.z + other.z)

    @staticmethod
    def random2D(r=1.0):
        """ Creates a vector of magnitude r with a random direction on the xy plane.

        Args:
            r (float): Magnitude of the vector.

        Returns:
            PVector: A random vector as described, with it's z coordinate set to 0.

        """

        phi = random.uniform(0, 2 * PI)
        x, y = r * cos(phi), r * sin(phi)
        return PVector(x, y)

    @staticmethod
    def random3D(r=1.0):
        """ Creates a vector of magnitude r with a random direction.
        # TODO: Direction should be uniformly distributed on the sphere with size r.

        Args:
            r (float): Magnitude of the vector.

        Returns:
            PVector: A random vector as described.

        """

        return None

    @staticmethod
    def fromAngle(phi, r=1.0):
        """ Creates a vector who's angle from the x coordinate is phi.

        Args:
            phi (float): Angle of the new vector.
            r (float): Magnitude of the new vector.

        Returns:
            PVector: A 2D vector with angle phi

        """
        return PVector(r * cos(phi), r * sin(phi))

    def magSq(self):
        """ Calculates the magnitude squared of the vector, or the distance from the point the vector is pointing to,
        to the origin using the Pitagora's theorem. This is much faster since it doesn't include square rooting.

        Returns:
            float: Vector's magnitude squared.

        """
        return self.x ** 2 + self.y ** 2 + self.z ** 2

    def mag(self):
        """ Calculates the magnitude of the vector, or the distance from the point the vector is pointing to, to the
        origin using the Pitagora's theorem.
        # TODO: Add options to use a different metric (manhattan or any other).

        Returns:
            float: Vector's magnitude.

        """
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def add(self, other):
        """ Adds one vector to the current one.

        Args:
            other (PVector): Vector that should get added.

        """
        self.x += other.x
        self.y += other.y
        self.z += other.z

    def sub(self, other):
        """ Subtracts one vector from the current one.

        Args:
            other (PVector): Vector that should be subtracted.

        """
        self.x -= other.x
        self.y -= other.y
        self.z -= other.z

    def mult(self, scalar):
        """ Multiplies the vector with a scalar.

        Args:
            scalar (float): Scaling factor.

        """
        self.x *= scalar
        self.y *= scalar
        self.z *= scalar

    @staticmethod
    def dist(A, B):
        """ Calculates the distance between two points.

        Args:
            A (PVector): First point
            B (PVector): Second point

        Returns:
            float: The value |A - B|

        """
        R = PVector()
        R.add(A)
        R.sub(B)
        return R.mag()

    def dot(self, other):
        """ Calculates the dot product of two vectors

        Args:
            other (PVector):

        Returns:

        """
        pass
