import random
import string
import time


def sifre_uret(uzunluk, sayi_olsun_mu, sembol_olsun_mu):
    """
    Belirtilen kurallara göre rastgele şifre üretir.
    """
    # 1. Temel harfler (a-z ve A-Z)
    karakterler = string.ascii_letters

    # 2. İsteğe bağlı karakterleri havuza ekle
    if sayi_olsun_mu:
        karakterler += string.digits  # 0123456789 ekle

    if sembol_olsun_mu:
        karakterler += string.punctuation  # !@#$ ekle

    # 3. Rastgele seçim yap
    sifre = ""
    for _ in range(uzunluk):
        sifre += random.choice(karakterler)

    return sifre


def dosyaya_kaydet(uygulama_adi, sifre):
    """
    Şifreyi 'sifrelerim.txt' dosyasına ekler.
    """
    try:
        with open("sifrelerim.txt", "a", encoding="utf-8") as dosya:
            tarih = time.strftime("%d.%m.%Y %H:%M")
            dosya.write(f"[{tarih}] {uygulama_adi} -> {sifre}\n")
        print(f">> BAŞARILI: Şifre 'sifrelerim.txt' dosyasına kaydedildi.")
    except Exception as e:
        print(f">> HATA: Dosyaya yazılamadı. Sebep: {e}")


# --- ANA PROGRAM DÖNGÜSÜ ---
def main():
    print("######################################")
    print("#   GÜÇLÜ ŞİFRE OLUŞTURUCU (CLI)     #")
    print("######################################")

    while True:
        try:
            # 1. Kullanıcıdan Uzunluk İste
            uzunluk_giris = input("\nŞifre kaç haneli olsun? (Çıkış için 'q'): ")

            if uzunluk_giris.lower() == 'q':
                print("Programdan çıkılıyor...")
                break

            uzunluk = int(uzunluk_giris)

            if uzunluk < 4:
                print(">> UYARI: Şifre en az 4 karakter olmalıdır!")
                continue

            # 2. Seçenekleri Sor (E/H)
            sayi_soru = input("İçinde SAYI olsun mu? (e/h): ").lower()
            sembol_soru = input("İçinde SEMBOL olsun mu? (e/h): ").lower()

            sayi_var = True if sayi_soru == 'e' else False
            sembol_var = True if sembol_soru == 'e' else False

            # 3. Şifreyi Oluştur
            yeni_sifre = sifre_uret(uzunluk, sayi_var, sembol_var)

            print("-" * 30)
            print(f"OLUŞTURULAN ŞİFRE: {yeni_sifre}")
            print("-" * 30)

            # 4. Kaydetmek ister mi?
            kayit_soru = input("Bu şifreyi dosyaya kaydetmek ister misin? (e/h): ").lower()

            if kayit_soru == 'e':
                uygulama = input("Bu şifre ne için? (Örn: Instagram, Gmail): ")
                dosyaya_kaydet(uygulama, yeni_sifre)

        except ValueError:
            print(">> HATA: Lütfen geçerli bir sayı giriniz!")


if __name__ == "__main__":
    main()