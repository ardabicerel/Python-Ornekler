from random import randint

kolon_sayisi = int(input("Oynanacak kolon sayısını giriniz : "))

sansliSayi = []
sansliSayi_onay = int(input("Şanslı sayınız var ise 1 yoksa 0 giriniz : "))

if sansliSayi_onay == 1:
    sansliSayi = int(input("Şanslı sayınızı giriniz : "))
elif sansliSayi_onay == 0:
    sansliSayi is None


kotuSayi = []
kotuSayi_onay = int(input("Kötü sayınız var ise 1 yoksa 0 yazınız : "))

if kotuSayi_onay == 1:
    kotuSayi = int(input("Kötü sayınızı giriniz : "))
elif kotuSayi_onay == 0:
    kotuSayi is None


for sayi in range(kolon_sayisi):
    kolon = []
    if sansliSayi:
        kolon.append(sansliSayi)
    for kolonUzunluk in range(6):
        ic_sayi = randint(1,90)
        if ic_sayi != kotuSayi:
            kolon.append(ic_sayi)
    print(f"Kolon {sayi+1}: {sorted(kolon)}")


