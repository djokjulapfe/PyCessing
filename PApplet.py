import pygame as pg


class PApplet:

    def __init__(self):
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

    def run_scetch(self):
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
    dApplet.canvas = pg.display.set_mode((w, h))
    dApplet.canvas.fill([0, 0, 0])


# TODO: add multiple argumets
def background(r, g=None, b=None):
    if g is None or b is None:
        dApplet.canvas.fill(r)
    else:
        dApplet.canvas.fill([r, g, b])


def line(x1, y1, x2, y2):
    pg.draw.line(dApplet.canvas,
                 dApplet.stroke_color,
                 (x1, y1),
                 (x2, y2),
                 dApplet.stroke_weight)
