"""

<https://github.com/djokjulapfe/PyCessing>

Abstract:
    Main facade class that generates the window, settings, and everything.

# TODO: This class is under construction.

"""

import pygame as pg


class PApplet:

    def __init__(self):
        """ Sets up all parameters and initializes pygame """

        pg.init()
        pg.display.set_caption('sketch')

        # template dp functions
        self.setup = None
        self.draw = None
        self.user_event = None

        # main drawing area
        self.canvas = None

        # helper color palette
        self.fill_color = [255, 255, 255]
        self.stroke_color = [0, 0, 0]
        self.stroke_weight = 1

    def set_setup(self, setup):
        self.setup = setup

    def set_draw(self, draw):
        self.draw = draw

    def set_user_event(self, user_event):
        self.user_event = user_event

    def run_sketch(self):
        """ Runs the sketch by initalizing everything and creating the main loop """

        clk = pg.time.Clock()
        if self.setup is not None:
            self.setup()
        end_loop = False

        while not end_loop:

            for e in pg.event.get():
                if e.type == pg.QUIT:
                    end_loop = True
                if e.type == pg.KEYUP:
                    if e.key == 27:
                        end_loop = True
                    print(e.key)
                if self.user_event is not None:
                    self.user_event(e)

            if self.draw is not None:
                self.draw()

            pg.display.update()
            clk.tick(30)

        pg.quit()


dApplet = PApplet()


def size(w, h):
    """ Set the width and height of the window.

    Args:
        w (int): Width of the screen.
        h (int): Height of the screen.

    """
    dApplet.canvas = pg.display.set_mode((w, h))
    dApplet.canvas.fill([0, 0, 0])


# TODO: add multiple argumets
def background(r, g=None, b=None):
    """ Fills the canvas with a single color.

    Args:
        r (float): Red component of the color if g and b are given, or the gray value if they are None.
        g (float): Green component of the color (only if b is also not None).
        b (float): Blue component of the color (onli if g is also not None).

    """
    if g is None or b is None:
        dApplet.canvas.fill([r, r, r])
    else:
        dApplet.canvas.fill([r, g, b])


def line(x1, y1, x2, y2):
    """ Draws a line from point (x1, y1) to (x2, y2).
    # TODO: Use x1 and y1 as PVector as an option.

    Args:
        x1 (float): x coordinate of the first point.
        y1 (float): y coordinate of the first point.
        x2 (float): x coordinate of the second point.
        y2 (float): y coordinate of the second point.

    """
    pg.draw.line(dApplet.canvas,
                 dApplet.stroke_color,
                 (x1, y1),
                 (x2, y2),
                 dApplet.stroke_weight)


def ellipse(x, y, w, h):
    """ Draws an ellipse with the center at (x, y), width of w and height of h.

    Args:
        x (float): x coordinate for the center of an ellipse.
        y (float): y coordinate for the center of an ellipse.
        w (float): width of the ellipse.
        h (float): height of the ellipse.

    """

    pg.draw.ellipse(dApplet.canvas,
                    dApplet.fill_color,
                    (x - w/2, y - h/2, w, h),
                    dApplet.stroke_weight)