import constants as c
import random

class Environment:
    def __init__(self, ID):
        self.ID = ID
        self.l = c.L
        self.w = c.L
        self.h = c.L
        self.x = 0
        self.y = 0
        self.z = c.L/2

        if ID == 0:
            self.send_light("front")
        elif ID == 1:
            self.send_light("right")
        elif ID == 2:
            self.send_light("back")
        elif ID == 3:
            self.send_light("left")

    def send_light(self, dir):
        if dir == "front":
            self.x = c.L * 30
        if dir == "right":
            self.x = c.L * -30
        if dir == "back":
            self.y = c.L * 30
        if dir == "left":
            self.y = c.L * -30

    def randomize(self):
        pass
    '''
        rand = random.randint(0, 3)
        #rand = 0
        if rand == 0:
            self.y = c.L * 30
            self.x = 0
        elif rand == 1:
            self.x = c.L * 30
            self.y = 0
        elif rand == 2:
            self.y = c.L * -30
            self.x = 0
        elif rand == 3:
            self.x = c.L * -30
            self.y = 0
            '''
    def send_to(self, sim):
        # body
        self.light_source = sim.send_box(x=self.x, y=self.y, z=self.z, length=self.l, width=self.w, height=self.h, r=0.5,
                               g=0.5, b=0.5)

        sim.send_light_source(body_id=self.light_source)


