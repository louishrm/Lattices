import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

class lattice:
    
    def __init__(self, a1, a2):
        """Initializes the lattice with the vectors a1 and a2 of the parallelogram"""
        a1, a2 = np.array(a1), np.array(a2)
        self.a1, self.a2 = a1, a2
        self.amat = np.array([a1, a2])
        self.area = np.abs(a1.dot(a2))
        self.angle = np.arccos(a1.dot(a2)/(np.linalg.norm(a1)*np.linalg.norm(a2)))

        #reciprocal lattice vectors 
        factor = 2*np.pi/(a1[0]*a2[1] - a1[1]*a2[0])
        self.b1 = factor*np.array([a2[1], -a1[1]])
        self.b2 = factor*np.array([-a2[0], a1[0]])
    
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

        plt.title('Plot of the ' + str(n) + 'x' + str(m) + ' lattice of ' + str(self.amat))

    def plot_supercell(self, n, n_, m, m_):
        """Plots a supercell of the lattice"""
        tmat = np.array([[n, n_], [m, m_]])
        #Calculating the coordinates of the vertices of the supercell
        super_x, super_y = np.array([[0, 0], tmat[0], tmat[0]+tmat[1], tmat[1]]).dot(self.amat.T).T

        fig = plt.figure()
        ax = fig.add_subplot(111, aspect='equal')
        ax.add_patch(patches.Polygon(xy=list(zip(super_x, super_y)), fill=False))

        #Defining the margin manually to ensure entire plot is visible
        margin = min(max(super_x) - min(super_x), max(super_y) - min(super_y))
        ax.set_xlim(min(super_x) - margin, max(super_x) + margin)
        ax.set_ylim(min(super_y) - margin, max(super_y) + margin)

        plt.title('Plot of the ' + str(tmat) + ' supercell of ' + str(self.amat))

        site_x, site_y = [], []

        for i in range(-(abs(n) + abs(m)), abs(n) + abs(m)):
            for j in range(-(abs(n_) + abs(m_)), abs(n_) + abs(m_)):
                #Checking if the site is inside the supercell
                spvec = np.linalg.inv(tmat.T).dot(np.array([i, j]).T)
                if 0 <= spvec[0] < 1 and 0 <= spvec[1] < 1:
                    #Calculating the real coordinates of the site
                    x, y = self.amat.dot(np.array([i, j])).T
                    site_x.append(x)
                    site_y.append(y)

        ax.scatter(site_x, site_y, color='r')