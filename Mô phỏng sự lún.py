from vpython import canvas, box, color, vector, rate

def mo_phong_lun_dan_hoi():
    # Tạo khung cảnh 3D
    scene = canvas(title='Mô phỏng lún đàn hồi 3D', width=1200, height=800, center=vector(0, 0, 0), background=color.white)

    # Thông số ngôi nhà
    house_width = 10
    house_length = 20
    house_height = 10
    house_mass = 100000  # Khối lượng của ngôi nhà (giả sử)

    # Thông số khối đất
    soil_width = 60
    soil_length = 80
    soil_height = 20  # Chiều cao tổng của khối đất
    depth_of_settlement = 5  # Chiều sâu của lớp đất bị lún
    E = 30000000  # Mô đun đàn hồi của đất
    nu = 0.3  # Hệ số Poisson của đất

    # Trọng lượng của vật nặng
    weight_mass = 100000  # khối lượng của vật nặng (kg)
    g = 9.81  # gia tốc trọng trường (m/s^2)
    weight = weight_mass * g  # trọng lượng của vật nặng (N)

    # Tạo mô hình khối đất
    soil = box(pos=vector(0, -soil_height/2, 0), size=vector(soil_width, soil_height, soil_length), color=color.green, opacity=0.5)

    # Tạo mô hình ngôi nhà
    house = box(pos=vector(0, soil_height/2 + house_height/2, 0), size=vector(house_width, house_height, house_length), color=color.blue)

    # Tính độ lún đàn hồi (sơ bộ)
    P = (house_mass + weight_mass) * g  # Tải trọng tác dụng lên móng (trọng lực tổng cộng)
    q = P / (house_width * house_length)  # Áp lực phân bố đều
    delta = (q * (1 - nu**2)) / E  # Độ lún đàn hồi tại mỗi điểm

    # Tính tổng độ lún trong phạm vi độ sâu giới hạn
    total_settlement = delta * depth_of_settlement * 1000  # Nhân thêm hệ số để rõ ràng hơn trong mô phỏng

    # Thông số lún không đều
    uneven_settlement_factor = 0.5  # Hệ số lún không đều

    # Mô phỏng ngôi nhà đè xuống khối đất
    steps = 100
    for i in range(steps):
        rate(50)  # Tốc độ mô phỏng
        # Tính độ lún không đều
        left_settlement = total_settlement * (1 + uneven_settlement_factor)
        right_settlement = total_settlement * (1 - uneven_settlement_factor)

        # Tính độ lún trung bình
        average_settlement = (left_settlement + right_settlement) / 2

        # Tính momen lực dựa trên sự chênh lệch độ lún
        torque = (left_settlement - right_settlement) / house_width

        # Cập nhật vị trí ngôi nhà
        house.pos.y -= average_settlement / steps

        # Xoay ngôi nhà dựa trên momen lực
        house.rotate(angle=torque / steps, axis=vector(0, 0, 1), origin=house.pos)

    # Vòng lặp giữ cho cửa sổ mở
    while True:
        rate(10)

# Gọi hàm mô phỏng
mo_phong_lun_dan_hoi()
