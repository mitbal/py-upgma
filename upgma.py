import math
import matplotlib.pyplot as plt

def to_dist_matrix(points):
	""" Convert a set of points into a distance matrix based on a certain distance measure """

	n = len(points)
	dim = len(points[0])
	dist = [[0 for x in xrange(n)] for y in xrange(n)]

	for i in xrange(n):
		for j in xrange(n):
			d = 0
			p1 = points[i]
			p2 = points[j]
			for k in xrange(dim):
				d = d + (p1[k]-p2[k])**2
			dist[i][j] = math.sqrt(d)

	return dist


points = [[0,0], [1,0], [0,1], [1,1], [3,2]]
# plt.plot(points, 'b.')
# plt.show()
dist = to_dist_matrix(points)
print dist
