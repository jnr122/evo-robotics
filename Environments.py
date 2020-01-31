from Environment import Environment
import constants as c

class Environments:
    def __init__(self):
      self.e = {}

      for e in range(c.num_envs):
          self.e[e] = Environment(e)
