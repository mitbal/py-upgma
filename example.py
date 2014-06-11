import upgma
import random
import matplotlib.pyplot as plt
import math

# Example 1
datapoints = [(random.normalvariate(2.5, 1.0), random.normalvariate(1.5,1.0)) for i in xrange(100)] + \
				[(random.normalvariate(-1, 0.5), random.normalvariate(3,0.5)) for i in xrange(100)]

# Plot datapoints before clustering
plt.plot([x for (x,y) in datapoints], [y for (x,y) in datapoints], 'k^')
plt.show()

# Cluster the data
nodes = upgma.upgma(datapoints, 2)
plt.plot([x[0] for x in nodes[0].points], [x[1] for x in nodes[0].points], 'b*')
plt.plot([x[0] for x in nodes[1].points], [x[1] for x in nodes[1].points], 'ro')
plt.show()

# Example 2
# Load and convert data
f = open('faithful.dat.txt', 'r')
lines = f.readlines()
f.close()

datapoints = []
for line in lines:
	tokens = line.split()
	datapoints += [(float(tokens[1]), float(tokens[2]))]

# Normalize the data
avg1 = sum([x for (x,y) in datapoints])
avg2 = sum([y for (x,y) in datapoints])
centered_datapoints = map(lambda (x,y): (x-avg1, y-avg2), datapoints)
std1 = math.sqrt(sum(map(lambda x: x*x, [x for (x,y) in centered_datapoints])))
std2 = math.sqrt(sum(map(lambda x: x*x, [y for (x,y) in centered_datapoints])))
normalized_datapoints = map(lambda (x,y): (x/std1, y/std2), centered_datapoints)

# Before clustering
plt.plot([x for (x,y) in normalized_datapoints], [y for (x,y) in normalized_datapoints], 'k^')
plt.show()

# Cluster the data
nodes = upgma.upgma(normalized_datapoints, 2)
plt.plot([x[0] for x in nodes[0].points], [x[1] for x in nodes[0].points], 'b*')
plt.plot([x[0] for x in nodes[1].points], [x[1] for x in nodes[1].points], 'ro')
plt.show()
