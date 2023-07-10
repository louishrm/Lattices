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
        margin_x = 0.2 * (max(vertices_x) - min(vertices_x))
        margin_y = 0.2 * (max(vertices_y) - min(vertices_y))
        ax.set_xlim(min(vertices_x) - margin_x, max(vertices_x) + margin_x)
        ax.set_ylim(min(vertices_y) - margin_y, max(vertices_y) + margin_y)

        ax.add_patch(patches.Polygon(xy=list(zip(vertices_x,vertices_y)), fill=False))