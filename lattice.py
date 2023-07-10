import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class lattice:
    
    def __init__(self, a1, a2):
        """Initializes the lattice with the vectors a1 and a2 of the parallelogram"""
        a1, a2 = np.array(a1), np.array(a2)
        self.a1, self. a2 = a1, a2
        self.area = np.abs(a1.dot(a2))
        self.angle = np.arccos(a1.dot(a2)/(np.linalg.norm(a1)*np.linalg.norm(a2)))
    
    def plot_unit(self):
        """Plots the unit cell of the lattice"""
        vertices_x = [0, self.a1[0], (self.a1+self.a2)[0], self.a2[0]]
        vertices_y = [0, self.a1[1], (self.a1+self.a2)[1], self.a2[1]]

        fig = plt.figure()
        ax = fig.add_subplot(111, aspect='equal')

        #Defining the margin manually to ensure entire plot is visible
        margin_x = 0.1 * (max(vertices_x) - min(vertices_x))
        margin_y = 0.1 * (max(vertices_y) - min(vertices_y))
        ax.set_xlim(min(vertices_x) - margin_x, max(vertices_x) + margin_x)
        ax.set_ylim(min(vertices_y) - margin_y, max(vertices_y) + margin_y)

        ax.add_patch(patches.Polygon(xy=list(zip(vertices_x,vertices_y)), fill=False))
        plt.title('Plot of the [' + str(self.a1) + str(self.a2) + '] unit cell')

    def plot_lattice(self, n, m):
        """Plots the unit cell of the lattice"""
        vertices_x = [0, self.a1[0], (self.a1+self.a2)[0], self.a2[0]]
        vertices_y = [0, self.a1[1], (self.a1+self.a2)[1], self.a2[1]]

        fig = plt.figure()
        ax = fig.add_subplot(111, aspect='equal')

        #Defining the margin manually to ensure entire plot is visible
        margin = 0.1 * min(n, m) * (max(vertices_x) - min(vertices_x))
        ax.set_xlim(min(vertices_x) - margin, n * self.a1[0] + m * self.a2[0] + margin)
        ax.set_ylim(min(vertices_y) - margin, n * self.a1[1] + m * self.a2[1] + margin)

        #Printing the cells one by one in both directions
        for i in range(0, n):
            for j in range (0, m):
                cell_x = vertices_x + i*self.a1[0] + j*self.a2[0]
                cell_y = vertices_y + i*self.a1[1] + j*self.a2[1]
                ax.add_patch(patches.Polygon(xy=list(zip(cell_x, cell_y)), fill=False))

        plt.title('Plot of the ' + str(n) + 'x' + str(m) + ' lattice of [' + str(self.a1) + str(self.a2) + ']')
