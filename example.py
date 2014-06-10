import upgma
import random
import matplotlib.pyplot as plt

# Example 1
datapoints = [(random.normalvariate(0, 1.5), random.normalvariate(0,1.5)) for i in xrange(100)] + \
				[(random.normalvariate(2, 0.75), random.normalvariate(2,0.75)) for i in xrange(100)]

nodes = upgma.upgma(datapoints, 2)
plt.plot([x[0] for x in nodes[0].points], [x[1] for x in nodes[0].points], 'b*')
plt.plot([x[0] for x in nodes[1].points], [x[1] for x in nodes[1].points], 'ro')
plt.show()
