kilo = float(input("Kilonuzu giriniz : "))
boy = float(input("Boyunuzu giriniz : "))

if boy > 3.0: # Eğer kullanıcı boyunu santimetre cinsinden girerse sistem bunu metreye çevirecektir.
    boy = boy / 100

vke = kilo / (boy*boy)

alt_sinir = (boy*boy) * 18.50

ust_sinir = (boy*boy) * 24.99


if vke < 18.50:
    print("Zayıfsınız. Normal olmak için kilo aralığınız en düşük {} en yüksek {} olmalıdır.".format(alt_sinir,ust_sinir))

elif 18.50 <= vke <= 24.99:
    print("Normal, sağlıklısınız.")

elif 25 < vke <= 29.99:
    print("Kilolusunuz. Normal olmak için kilo aralığınız en düşük {} en yüksek {} olmalıdır.".format(alt_sinir,ust_sinir))

elif vke > 30:
    print("Obezsiniz. Normal olmak için kilo aralığınız en düşük {} en yüksek {} olmalıdır.".format(alt_sinir,ust_sinir))