import math

def euclideanDistance(point1, point2):
    """İki nokta arasındaki Öklid mesafesini hesaplar"""
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Test için örnek noktalar
points = [(0, 0), (1, 1), (2, 2), (3, 0), (0, 3)]
distances = []

# Her nokta çifti arasındaki mesafeyi hesapla
for i in range(len(points)):
    for j in range(i + 1, len(points)):  # i+1'den başlayarak tekrarları önlüyoruz
        distance = euclideanDistance(points[i], points[j])
        distances.append({
            'points': (points[i], points[j]),
            'distance': distance
        })

# Minimum mesafeyi bul
min_distance = min(distances, key=lambda x: x['distance'])

# Sonuçları yazdır
print("Hesaplanan tüm mesafeler:")
for d in distances:
    print(f"Noktalar {d['points']}: {d['distance']:.2f}")

print("\nEn kısa mesafe:")
print(f"Noktalar: {min_distance['points']}")
print(f"Mesafe: {min_distance['distance']:.2f}") 