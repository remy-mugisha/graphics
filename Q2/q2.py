import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Create a figure and a 3D axis
fig = plt.figure()
axis = fig.add_subplot(111, projection='3d')

# Define pyramid vertices
vertices = np.array([
    [0, 0, 0],  
    [1, -1, -1], 
    [-1, -1, -1],
    [-1, 1, -1], 
    [1, 1, -1],  
])

# Define faces using vertex indices
faces = [
    [vertices[0], vertices[1], vertices[2]], 
    [vertices[0], vertices[2], vertices[3]], 
    [vertices[0], vertices[3], vertices[4]], 
    [vertices[0], vertices[4], vertices[1]], 
    [vertices[1], vertices[2], vertices[3], vertices[4]]
]

# Create a Poly3DCollection from the faces
pyramid = Poly3DCollection(faces, facecolors='green', edgecolors='black', alpha=0.5)
axis.add_collection3d(pyramid)

# Set plot limits and labels
axis.set_xlim([-2, 2])
axis.set_ylim([-2, 2])
axis.set_zlim([0, 2])
axis.set_xlabel('X')
axis.set_ylabel('Y')
axis.set_zlabel('Z')
axis.set_title('3D Pyramid Plot')

# Show the plot
plt.show()
