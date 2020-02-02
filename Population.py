from Individual import Individual
import copy
import random
import constants as c

class Population:
    def __init__(self, pop_size):
      self.p = {}
      self.pop_size = pop_size
    
    def initialize(self):
       for i in range(0, self.pop_size):
          self.p[i] = Individual(i)
        
    def evaluate(self, envs, pb):
        for i in range(0, self.pop_size):
            self.p[i].fitness = 0
        for e in range(c.num_envs):
            for i in self.p:
                self.p[i].start_evaluation(envs[e], pb)
            for i in self.p:
                self.p[i].compute_fitness()
        for i in range(0, self.pop_size):
            self.p[i].fitness /= c.num_envs

    def evaluate_one(self, envs, pb):
        for e in range(c.num_envs):
            self.p[0].start_evaluation(envs[e], pb)
            self.p[0].compute_fitness()

    def mutate(self):
         for i in self.p:
            self.p[i].mutate()

    def replace_with(self, other):
        for i in self.p:
            if (self.p[i].fitness < other.p[i].fitness):
                self.p[i] = other.p[i]

    def fill_from(self, other):
        self.copy_best_from(other)
        self.collect_children_from(other)

    def copy_best_from(self, other):
        max_ind = 0
        for i in other.p:
            if other.p[i].fitness > other.p[max_ind].fitness:
                max_ind = i
        self.p[0] = copy.deepcopy(other.p[max_ind])

    # " tournament winner "
    def get_fittest(self, other):
        p1 = random.randint(0, self.pop_size-1)
        p2 = random.randint(0, self.pop_size-1)
        while p2 == p1:
            p2 = random.randint(0, self.pop_size-1)

        if other.p[p1].fitness > other.p[p2].fitness:
            return other.p[p1]
        return other.p[p2]
        

    def collect_children_from(self, other):
        for i in other.p:
            if i != 0:
                # lower chance of replacing individual
                chance = random.random()
                if chance > 0:
                    fittest = self.get_fittest(other)
                    fittest.mutate()
                    self.p[i] = copy.deepcopy(fittest)
                else:
                    other.p[i].mutate()
                    self.p[i] = copy.deepcopy(other.p[i])

                    
    def print_str(self):
        for i in self.p:
            self.p[i].print_str()
        print()
