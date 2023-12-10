def menu():
    print("")
    print("╔════════════════════════╗")
    print("║ MESLEK REHBER PROGRAMI ║")
    print("╚════════════════════════╝")
    print("╔════════════════════════╗")
    print("║  1-Kayıt Ekle          ║")
    print("║  2-Kayıt Listele       ║")
    print("║  3-Kayıt Düzenle       ║")
    print("║  4-Kayıt Sil           ║") 
    print("║  5-Çıkış               ║")
    print("╚════════════════════════╝")
    print( "seçiminizi giriniz")
    secim = input()
    if secim == "1": 
        rehbereEkle() # rehbere yeni bir kayıt eklenebilir.
        listele()
        menu()
    if secim == "2": 
        listele() # dosya içindeki var olan kayıtları listeler.
        menu()
    if secim == "3": 
        kayitDuzenle()
        menu()
    if secim == "4": 
        kayitSil()
        menu()
    if secim == "5":
        print("Çıkış yapılıyor...")
    else:
        print("Geçersiz seçim! Tekrar deneyin.")
        menu()

def rehbereEkle():
    dosya = open("rehber.txt","a")
    ad = input("Ad:")
    soyad= input("Soyad:")
    numara = input("Numara:")
    bolum = input("Meslek:")
    sirket = input("Çalıştığınız kurum/şirket adı:")
    yazilacak = ad + "|" + soyad + "|"+ numara + "|" + bolum + "|" + sirket + "\n"
    dosya.write(yazilacak)
    dosya.close()
#listele()

def listele():
    try:
        dosya = open("rehber.txt","r")
        print("╔═══════════════════════╗")
        print("║     Kayıt Listesi     ║ ")
        print("╚═══════════════════════╝")
        a = 1
        for kayit in dosya.readlines():
            print(a,kayit)
            a += 1
    except:
        print("Dosya bulunamadı.")
        print("Devam etmek için entera basınız.")
        input()

def kayitDuzenle():
    try:
        dosya = open("rehber.txt", "r")
        kayitlar = dosya.readlines()
        dosya.close()

        print("Düzenlemek istediğiniz kaydın numarasını girin:")
        numara = int(input())

        if 1 <= numara <= len(kayitlar):
            duzenlenecek_kayit = kayitlar[numara - 1].split("|")
            print("Mevcut Bilgiler:")
            print(f"Ad: {duzenlenecek_kayit[0]} Soyad: {duzenlenecek_kayit[1]} Numara: {duzenlenecek_kayit[2]} Meslek: {duzenlenecek_kayit[3]} Şirket: {duzenlenecek_kayit[4]}")

            yeni_ad = input("Yeni Ad:")
            yeni_soyad = input("Yeni Soyad:")
            yeni_numara = input("Yeni Numara:")
            yeni_bolum = input("Yeni Meslek: ")
            yeni_sirket = input("Yeni iş yeriniz:")

            kayitlar[numara - 1] = f"{yeni_ad}|{yeni_soyad}|{yeni_numara}|{yeni_bolum}|{yeni_sirket} \n"

            dosya = open("rehber.txt", "w")
            dosya.writelines(kayitlar)
            dosya.close()

            print("Kayıt düzenleme başarılı.")
        else:
            print("Geçersiz kayıt numarası.")
    except Exception as e:
        print("Bir hata oluştu:", str(e))
        listele()

def kayitSil():
    try:
        dosya = open("rehber.txt", "r")
        kayitlar = dosya.readlines()
        dosya.close()

        print("Silmek istediğiniz kaydın numarasını girin:")
        numara = int(input())

        if 1 <= numara <= len(kayitlar):
            silinecek_kayit = kayitlar[numara - 1]
            del kayitlar[numara - 1]

            dosya = open("rehber.txt", "w")
            dosya.writelines(kayitlar)
            dosya.close()

            print(f"{silinecek_kayit.strip()} başarıyla silindi.")
        else:
            print("Geçersiz kayıt numarası.")
    except Exception as e:
        print("Bir hata oluştu:", str(e))
    listele()
menu()