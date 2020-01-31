from Individual import Individual 
from Population import Population
from Environments import Environments
import pickle

f = open('data/robot.p','rb')
pop = pickle.load(f)
f.close()

envs = Environments()


pop.evaluate_one(envs.e, False)
pop.print_str()
