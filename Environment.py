import constants as c

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
            self.send_light_front()

        print(self.y)

    def send_light_front(self):
        self.y = c.L * 30

    def send_to(self, sim):
        # body
        self.box = sim.send_box(x=self.x, y=self.y, z=self.z, length=self.l, width=self.w, height=self.h, r=0.5,
                               g=0.5, b=0.5)
