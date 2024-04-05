import matplotlib.pyplot as plt 
from distribution import *

def move(distribution, delta):
    return Distribution(distribution.offset + delta, distribution.values)

'''
moves = [20] *3

position = Distribution.triangle(10,2)
plt.plot(position.plotlists(0,100)[0], position.plotlists(0,100)[1], linestyle='-')

for m in moves:
    position = move(position, m)
    plt.plot(position.plotlists(0,100)[0], position.plotlists(0,100)[1],
             linestyle='-')
    
plt.ylim(0.0, 1.1)
plt.savefig("pure move")
plt.show()


'''

