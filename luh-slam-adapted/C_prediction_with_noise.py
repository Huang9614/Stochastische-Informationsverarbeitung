import matplotlib.pyplot as plt
from distribution import *

def convolve(a, b):
    
    dist_list = []
    offs = a.offset + b.offset
    for a_val in a.values:
        res = []
        for b_val in b.values:
           res.append(a_val*b_val)
           
        dist_list.append(Distribution(offs,res))
        offs += 1
        
    c = Distribution.sum(dist_list)
    return c  # Replace this by your own result.

'''
arena = (0,100)

# Move 3 times by 20.
moves = [20] * 3

# Start with a known position: probability 1.0 at position 10.
position = Distribution.triangle(10, 2)
plt.plot(position.plotlists(*arena)[0], position.plotlists(*arena)[1],
        linestyle='solid')

# Now move and plot.
for m in moves:
    move_distribution = Distribution.triangle(m, 2)
    position = convolve(position, move_distribution)
    plt.plot(position.plotlists(*arena)[0], position.plotlists(*arena)[1],
            linestyle='solid')

plt.ylim(0.0, 1.1)
plt.savefig("move with noise")
plt.show()

'''
