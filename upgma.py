import math
import matplotlib.pyplot as plt

class Node:
	def __init__(self, p):
		self.points = p
		self.right = None
		self.left = None

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

def euclidistance(c1, c2):
	""" Calculate the distance between two cluster """
	dist = .0
	n1 = len(c1.points)
	n2 = len(c2.points)
	for i in xrange(n1):
		for j in xrange(n2):
			p1 = c1.points[i]
			p2 = c2.points[j]
			dim = len(p1)
			d = 0
			for k in xrange(dim):
				d = d + (p1[k]-p2[k])**2
			d = math.sqrt(d)
			dist = dist + d
	dist = dist / (n1*n2)

def upgma(points, k):
	""" Cluster based on distance matrix dist using Unweighted Pair Group Method with Arithmetic Mean algorithm up to k cluster"""

	# Initialize each cluster with one point
	nodes = []
	n = len(points)
	dim = len(points[0])
	for i in xrange(n):
		node = Node([points[i]])
		nodes = nodes + [node]

	# Iterate until the number of clusters is k
	nc = n
	while nc > k:
		# Calculate the pairwise distance of each cluster, while searching for pair with least distance
		c1 = 0; c2 = 0; i1 = 0; i2 = 0;
		sdis = 9999999999
		for i in xrange(nc):
			for j in xrange(i+1, nc):
				dis = euclidistance(nodes[i], nodes[j])
				if dis < sdis:
					sdis = dis
					c1 = nodes[i]; c2 = nodes[j];
					i1 = i; i2 = j;
		# Merge these two nodes into one new node
		node = Node(c1.points + c2.points)
		node.left = c1; node.right = c2;
		
		#Remove the previous nodes, and add the new node
		new_nodes = []
		for i in xrange(nc):
			if i != i1 or i != i2:
				new_nodes = new_nodes + [nodes[i]]
		new_nodes = new_nodes + [node]
		nc = nc - 1

	return nodes

points = [[0,0], [1,0], [0,1], [1,1], [3,2]]
# plt.plot(points, 'b.')
# plt.show()
# dist = to_dist_matrix(points)
# print dist

upgma(points, 2)
