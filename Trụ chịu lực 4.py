import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Hàm tạo trụ
def create_cylinder(radius, height, num_points=100):
    theta = np.linspace(0, 2 * np.pi, num_points)
    z = np.linspace(0, height, num_points)
    theta_grid, z_grid = np.meshgrid(theta, z)
    x_grid = radius * np.cos(theta_grid)
    y_grid = radius * np.sin(theta_grid)
    return x_grid, y_grid, z_grid

# Hàm vẽ mặt phẳng
def create_plane(length, width, height):
    x = np.array([[-length / 2, length / 2, length / 2, -length / 2]])
    y = np.array([[-width / 2, -width / 2, width / 2, width / 2]])
    z = np.array([[height, height, height, height]])
    return x, y, z

# Kích thước cột trụ
radius = 1
height = 5

# Kích thước mặt phẳng
length = 3
width = 3

# Tạo dữ liệu cho trụ
x_cyl, y_cyl, z_cyl = create_cylinder(radius, height)

# Tạo dữ liệu cho mặt phẳng
x_plane, y_plane, z_plane = create_plane(length, width, height)

# Vẽ trụ và mặt phẳng
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Vẽ trụ
ax.plot_surface(x_cyl, y_cyl, z_cyl, color='cyan', alpha=0.6)

# Vẽ mặt phẳng
verts = [list(zip(x_plane[0], y_plane[0], z_plane[0]))]
plane = Poly3DCollection(verts, color='red', alpha=0.7)
ax.add_collection3d(plane)

# Thiết lập hiển thị
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Thiết lập tỷ lệ
ax.set_box_aspect([1,1,1])

plt.show()
