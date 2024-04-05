import matplotlib.pyplot as plt
from distribution import *
from C_prediction_with_noise import convolve
from C_filter_with_noise import multiply


arena = (0,300)

# Start position. Exactly known - a unit pulse.
start_position = 10
position = Distribution.triangle(start_position,5)

plt.plot(position.plotlists(*arena)[0], position.plotlists(*arena)[1], color = "g", linestyle='-')

# Movement data.
controls  =   [ 30 ] * 10

# Measurement data. Assume (for now) that the measurement data
# is correct. - This code just builds a cumulative list of the controls,
# plus the start position.
p = start_position
measurements = []
for c in controls:
    p += c
    measurements.append(p)

# This is the filter loop.
for i in range(len(controls)):
    # Move, by convolution. Also termed "prediction".
    control = Distribution.triangle(controls[i], 10)
    position = convolve(position, control)
    plt.plot(position.plotlists(*arena)[0], position.plotlists(*arena)[1], color='b', linestyle='-')

    # Measure, by multiplication. Also termed "correction".
    measurement = Distribution.triangle(measurements[i], 10)
    position = multiply(position, measurement)
    plt.plot(position.plotlists(*arena)[0], position.plotlists(*arena)[1],color='r', linestyle='-')

plt.savefig("Wonham Filter")
plt.show()