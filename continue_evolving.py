from Individual import Individual 
from Population import Population
import pickle

f = open('data/robot.p','rb')
parents = pickle.load(f)
f.close()

parents.evaluate(True)

g = 100000

for i in range(1, g+1):
    children = Population(parents.pop_size)
    children.fill_from(parents)
    children.evaluate(True)
    print(str(i), end=' ')
    children.print_str()
    parents = children

    f = open('data/robot.p','wb')
    pickle.dump(parents, f)
