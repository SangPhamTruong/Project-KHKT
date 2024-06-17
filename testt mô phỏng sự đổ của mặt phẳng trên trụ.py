import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Các thông số của cột trụ và bề mặt phẳng
radius = 0.15  # bán kính của cột trụ (m)
height = 3  # chiều cao của cột trụ (m)
f_c = 25 * 10**6  # cường độ chịu nén của vật liệu (N/m^2)
q = 5000  # tải trọng phân bố đều (N/m^2)

# Trọng lượng của vật nặng
weight_mass = 100000  # khối lượng của vật nặng (kg)
g = 9.81  # gia tốc trọng trường (m/s^2)
weight = weight_mass * g  # trọng lượng của vật nặng (N)

# Tính diện tích mặt cắt ngang của cột trụ
A = np.pi * radius**2

# Tính cường độ chịu nén của cột trụ
P_total = A * f_c

# Tính diện tích tối đa của bề mặt phẳng bao gồm cả tải trọng của vật nặng
A_surface_max = (P_total - weight) / q
side_length = np.sqrt(A_surface_max)  # giả sử bề mặt phẳng là hình vuông

# Hàm tạo trụ
def create_cylinder(radius, height, num_points=100):
    theta = np.linspace(0, 2 * np.pi, num_points)
    z = np.linspace(0, height, num_points)
    theta_grid, z_grid = np.meshgrid(theta, z)
    x_grid = radius * np.cos(theta_grid)
    y_grid = radius * np.sin(theta_grid)
    return x_grid, y_grid, z_grid

# Hàm vẽ mặt phẳng
def create_plane(length, width, height, tilt_angle=0):
    x = np.array([[-length / 2, length / 2, length / 2, -length / 2]])
    y = np.array([[-width / 2, -width / 2, width / 2, width / 2]])
    z = np.array([[height, height, height, height]], dtype=np.float64)  # Chuyển đổi sang kiểu float64

    # Tính toán độ nghiêng của mặt phẳng
    z_tilt = np.tan(np.radians(tilt_angle)) * x
    z += z_tilt
    return x, y, z

# Tạo dữ liệu cho trụ
x_cyl, y_cyl, z_cyl = create_cylinder(radius, height)

# Tính toán độ nghiêng của mặt phẳng
# Giả sử vị trí đặt vật nặng là (length/2, width/2)
# Mô-men tạo ra bởi vật nặng quanh tâm của mặt phẳng
moment = weight * (side_length / 2)  # N.m
# Giả sử cột trụ có mô-men quán tính (đơn giản hóa)
I = (1/12) * (side_length**2)  # m^4 (giả sử)
# Tính góc nghiêng (đơn giản hóa)
tilt_angle = np.degrees(moment / (P_total * I))

# Tạo dữ liệu cho mặt phẳng nghiêng
x_plane, y_plane, z_plane = create_plane(side_length, side_length, height, tilt_angle)

# Tạo dữ liệu cho mặt đất
ground_length = 10  # chiều dài của mặt đất
ground_width = 10   # chiều rộng của mặt đất
x_ground, y_ground, z_ground = create_plane(ground_length, ground_width, 0)

# Vẽ trụ, mặt phẳng và mặt đất
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Vẽ trụ
ax.plot_surface(x_cyl, y_cyl, z_cyl, color='cyan', alpha=0.6)

# Vẽ mặt phẳng
verts_plane = [list(zip(x_plane[0], y_plane[0], z_plane[0]))]
plane = Poly3DCollection(verts_plane, color='red', alpha=0.7)
ax.add_collection3d(plane)

# Vẽ mặt đất
verts_ground = [list(zip(x_ground[0], y_ground[0], z_ground[0]))]
ground = Poly3DCollection(verts_ground, color='green', alpha=0.5)
ax.add_collection3d(ground)

# Vẽ vật nặng
weight_pos_x = side_length / 2  # Vị trí x của vật nặng
weight_pos_y = side_length / 2  # Vị trí y của vật nặng
weight_height = height + np.tan(np.radians(tilt_angle)) * (side_length / 2)  # Vị trí z của vật nặng

ax.scatter([weight_pos_x], [weight_pos_y], [weight_height], color='blue', s=100, label='Vật nặng (1 tấn)')

# Thiết lập hiển thị
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Thiết lập tỷ lệ và phạm vi trục
ax.set_box_aspect([1, 1, 0.3])  # Tỷ lệ khung hình
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_zlim(0, 5)

# Thêm chú thích
ax.legend()

plt.show()

# In kết quả tính toán
print(f"Sức chịu tải của cột trụ: {P_total / 10**6:.2f} MN")
print(f"Diện tích tối đa của bề mặt phẳng: {A_surface_max:.2f} m²")
print(f"Chiều dài cạnh của bề mặt phẳng hình vuông: {side_length:.2f} m")
print(f"Góc nghiêng của mặt phẳng: {tilt_angle:.2f} độ")
