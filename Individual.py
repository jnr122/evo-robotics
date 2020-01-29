import random
from pyrosim import pyrosim
from Robot import Robot
import math
import numpy

class Individual:

      def __init__(self, ID):
          self.genome = numpy.random.random((4,8)) * 2 - 1
          self.fitness = 0
          self.ID = ID

      def start_evaluation(self, pb):
          # define simulation
          self.sim = pyrosim.Simulator(play_paused=True, eval_time=10000, play_blind=pb)
          self.robot = Robot(self.sim, self.genome)

          # run sim
          self.sim.start()
          
      def compute_fitness(self):
          self.sim.wait_to_finish()
          
          x = self.sim.get_sensor_data(sensor_id=self.robot.P4, svi=0)
          y = self.sim.get_sensor_data(sensor_id=self.robot.P4, svi=1)
          z = self.sim.get_sensor_data(sensor_id=self.robot.P4, svi=2)

          self.fitness = y[-1]
          del self.sim
          
      def mutate(self):
          r = random.randint(0,3)
          c = random.randint(0,7)

          mutate_val = random.random()
          mutate_val = random.gauss(self.genome[r][c], math.fabs(self.genome[r][c]))
          if mutate_val > 1:
                mutate_val = 1
          elif mutate_val < -1:
                mutate_val = -1
          
          self.genome[r][c] = mutate_val

      def print_str(self):
          print('[' + str(self.ID) + ' ' + str(self.fitness) + ']', end=' ')
