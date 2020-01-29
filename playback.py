from Individual import Individual 
from Population import Population
import pickle

f = open('data/robot.p','rb')
pop = pickle.load(f)
f.close()

pop.evaluate_one(False)
pop.print_str()
