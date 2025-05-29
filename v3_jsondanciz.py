import json
import matplotlib.pyplot as plt

# --- Ayarlar ---
json_file_path = "api_get_20250514_094755.json"  # Aynı klasörde olmalı
real_width_cm = 107  # X yönündeki gerçek boy (Boy)
real_height_cm = 30  # Y yönündeki gerçek boy (En)

# --- JSON'dan Noktaları Yükle ---
with open(json_file_path, "r") as f:
    data = json.load(f)

shape_points = data[0]['points']

# Ham sınırlar (bounding box)
x_coords, y_coords = zip(*shape_points)
min_x, max_x = min(x_coords), max(x_coords)
min_y, max_y = min(y_coords), max(y_coords)

raw_width = max_x - min_x
raw_height = max_y - min_y

# Ölçek hesaplama
scale_x = real_width_cm / raw_width
scale_y = real_height_cm / raw_height

# Şekli ölçekleyerek çiz
x_vals = [x for x, _ in shape_points]
y_vals = [y for _, y in shape_points]
x_scaled = [(x - min_x) * scale_x for x in x_vals]
y_scaled = [(y - min_y) * scale_y for y in y_vals]

plt.figure(figsize=(10, 6))
plt.plot(x_scaled, y_scaled, color="black", linewidth=1.2, label="Şekil (cm)")

# Kutuyu çiz
box_x_scaled = [0, raw_width * scale_x, raw_width * scale_x, 0, 0]
box_y_scaled = [0, 0, raw_height * scale_y, raw_height * scale_y, 0]
plt.plot(box_x_scaled, box_y_scaled, linestyle="--", color="red", linewidth=1.2, label="Bounding Box (cm)")

# Etiket
cx_cm = (raw_width * scale_x) / 2
cy_cm = (raw_height * scale_y) / 2
plt.text(cx_cm, cy_cm, f"{real_width_cm} cm x {real_height_cm} cm", ha="center", va="center",
         bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3'), fontsize=9)

plt.title("Gerçek Ölçekli Şekil (cm)")
plt.xlabel("Boy (cm)")
plt.ylabel("En (cm)")
plt.axis('equal')
plt.grid(True, linestyle="--", alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()