import time

mesaj = input("Lütfen Mesajınızı Giriniz: ")
print("MESAJINIZ ŞİFRELENİYOR...")
time.sleep(2)

sifreli_mesaj=""
for x in range(0,len(mesaj)):
    sifreli_mesaj += (chr(ord(mesaj[x])+1))
print("Şifreli Mesaj: " + sifreli_mesaj)

coz = input("Hadi Mesaj Çözelim: ")
print("MESAJINIZ ÇÖZÜLÜYOR...")
time.sleep(2)

cozumlu_mesaj=""
for x in range(0,len(coz)):
    cozumlu_mesaj += (chr(ord(coz[x])-1))
print("Şifresi Çözülen Mesaj: " + cozumlu_mesaj)