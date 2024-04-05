import matplotlib.pyplot as plt
from distribution import *

def multiply(a, b):
    """Multiply two distributions and return the resulting distribution."""

    # --->>> Put your code here.
    start = min([a.start(),b.start()])
    stop = max([a.stop(),b.stop()])
    multi_dist = []
    
    for i in range(start,stop):
        a_val = a.value(i)
        b_val = b.value(i)
        multi_dist.append(a_val * b_val)
    
    d = Distribution(start,multi_dist)
    Distribution.normalize(d)
    
    return d  # Modify this to return your result.

'''
arena = (0,1000)

# Here is our assumed position. Plotted in blue.
position_value = 400
position_error = 100
position = Distribution.triangle(position_value, position_error)
plt.plot(position.plotlists(*arena)[0], position.plotlists(*arena)[1],
        color='b', linestyle='-')

# Here is our measurement. Plotted in green.
# That is what we read from the instrument.
measured_value = 410
measurement_error = 200
measurement = Distribution.triangle(measured_value, measurement_error)
plt.plot(measurement.plotlists(*arena)[0], measurement.plotlists(*arena)[1],
        color='g', linestyle='-')

# Now, we integrate our sensor measurement. Result is plotted in red.
position_after_measurement = multiply(position, measurement)
plt.plot(position_after_measurement.plotlists(*arena)[0],
        position_after_measurement.plotlists(*arena)[1],
        color='r', linestyle='-')

plt.show()


'''

