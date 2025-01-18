# Öklid Mesafe Hesaplayıcı

Bu Python projesi, 2 boyutlu uzayda verilen noktalar arasındaki Öklid mesafesini hesaplayan ve en kısa mesafeyi bulan bir programdır.

## 🚀 Özellikler

- İki nokta arasındaki Öklid mesafesini hesaplama
- Verilen nokta kümesindeki tüm nokta çiftleri arasındaki mesafeleri hesaplama
- En kısa mesafeyi bulma ve gösterme
- Sonuçları okunaklı bir formatta görüntüleme

## 💻 Kurulum

1. Bu repository'yi klonlayın:
```bash
git clone https://github.com/KULLANICI_ADINIZ/euclidean-distance-calculator.git
```

2. Proje dizinine gidin:
```bash
cd euclidean-distance-calculator
```

3. Programı çalıştırın:
```bash
python euclidean_distance.py
```

## 📝 Kullanım

Program varsayılan olarak şu noktalarla çalışır:
```python
points = [(0, 0), (1, 1), (2, 2), (3, 0), (0, 3)]
```

Farklı noktalar kullanmak için `euclidean_distance.py` dosyasındaki `points` listesini değiştirebilirsiniz.

## 📊 Örnek Çıktı

```
Hesaplanan tüm mesafeler:
Noktalar ((0, 0), (1, 1)): 1.41
Noktalar ((0, 0), (2, 2)): 2.83
Noktalar ((0, 0), (3, 0)): 3.00
Noktalar ((0, 0), (0, 3)): 3.00
...

En kısa mesafe:
Noktalar: ((0, 0), (1, 1))
Mesafe: 1.41
```

## 🧮 Matematiksel Formül

Program, iki nokta arasındaki Öklid mesafesini şu formüle göre hesaplar:

d = √[(x₂-x₁)² + (y₂-y₁)²]

Burada:
- (x₁,y₁) ilk noktanın koordinatları
- (x₂,y₂) ikinci noktanın koordinatları

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır.