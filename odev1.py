import random

def siralama(sayilar):
    n = len(sayilar)
    for i in range(n):
        enbuyuki = i
        for j in range(i + 1, n):
            if sayilar[j] > sayilar[enbuyuki]:
                enbuyuki = j
        sayilar[i], sayilar[enbuyuki] = sayilar[enbuyuki], sayilar[i]
    return sayilar

def ortalama(sayilar):
    return sum(sayilar) / len(sayilar)

def medyanke(sirali_sayilar):
    n = len(sirali_sayilar)
    orta = n // 2
    return (sirali_sayilar[orta - 1] + sirali_sayilar[orta]) / 2 if n % 2 == 0 else sirali_sayilar[orta]

def modke(sayilar):
    frekans = {}
    for sayi in sayilar:
        frekans[sayi] = frekans.get(sayi, 0) + 1
    
    en_yuksek = max(frekans.values())
    mod = max(s for s, f in frekans.items() if f == en_yuksek)
    return mod, en_yuksek

#random.seed(31)
sayilar = [random.randint(1, 1000) for _ in range(100)]

print(f"Toplam: {sum(sayilar)}")
print(f"Ortalama: {ortalama(sayilar):.2f}")

sirali_sayilar = siralama(sayilar.copy())
print(f"Minimum: {sirali_sayilar[0]}")
print(f"Maksimum: {sirali_sayilar[-1]}")
print(f"Medyan: {medyanke(sirali_sayilar)}")

mod_degeri, mod_frekansi = modke(sayilar)
print(f"Mod: {mod_degeri} (frekans: {mod_frekansi})")

print("Sayılar ama sıralı:")
print(*sirali_sayilar[:20] + "...")