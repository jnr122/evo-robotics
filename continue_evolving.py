from Individual import Individual 
from Population import Population
from Environments import Environments
import pickle
import constants as c

f = open('data/robot.p','rb')
parents = pickle.load(f)
f.close()

envs = Environments()


parents.evaluate(envs.e, True)

for i in range(1, c.num_conts+1):
    children = Population(parents.pop_size)
    children.fill_from(parents)
    children.evaluate(envs.e, True)
    print(str(i), end=' ')
    children.print_str()

    if children.p[0].fitness > parents.p[0].fitness:
        
        f = open('data/robot.p','wb')
        pickle.dump(children, f)
    
    parents = children
