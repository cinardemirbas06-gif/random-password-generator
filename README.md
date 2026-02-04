🔐 Güçlü Şifre Oluşturucu (CLI)

Python ile geliştirilmiş, özelleştirilebilir ve güvenli rastgele şifreler üreten komut satırı (CLI) tabanlı bir uygulamadır.
Kullanıcıdan alınan tercihlere göre şifre oluşturur ve isterse şifreleri dosyaya kaydeder.

🚀 Özellikler

🔢 Şifre Uzunluğu Seçimi
Kullanıcı istediği karakter uzunluğunu belirleyebilir.

🔠 Harf + Sayı + Sembol Desteği
Sayı ve sembol ekleme tamamen kullanıcı kontrolündedir.

🧠 Rastgele ve Güçlü Üretim
Python random ve string modülleri ile rastgele şifre oluşturur.

💾 Dosyaya Kaydetme
Oluşturulan şifreler tarih bilgisiyle birlikte sifrelerim.txt dosyasına eklenir.

🛡️ Hata Yönetimi
Geçersiz girişler ve dosya hatalarına karşı korumalıdır.

🚪 Güvenli Çıkış
Kullanıcı q yazarak programdan çıkabilir.

🛠️ Kullanılan Teknolojiler

Python 3.x

random – Rastgele seçimler için

string – Harf, sayı ve sembol kümeleri için

time – Tarih & saat bilgisi eklemek için

💻 Kurulum ve Çalıştırma
1️⃣ Projeyi İndirin
git clone (https://github.com/cinardemirbas06-gif/random-password-generator/blob/main/README.md)

2️⃣ Uygulamayı Başlatın
python sifre_olusturucu.py


📌 Ekstra bir kütüphane kurulumu gerekmez.

📝 Kullanım

Program çalıştığında sırasıyla şunları sorar:

Şifre uzunluğu

Sayı içersin mi? (e/h)

Sembol içersin mi? (e/h)

Oluşturulan şifre dosyaya kaydedilsin mi?

📌 Örnek Terminal Çıktısı
######################################
#   GÜÇLÜ ŞİFRE OLUŞTURUCU (CLI)     #
######################################

Şifre kaç haneli olsun? (Çıkış için 'q'): 12
İçinde SAYI olsun mu? (e/h): e
İçinde SEMBOL olsun mu? (e/h): e
------------------------------
OLUŞTURULAN ŞİFRE: A9@fK2!mQx#L
------------------------------
Bu şifreyi dosyaya kaydetmek ister misin? (e/h): e
Bu şifre ne için? (Örn: Instagram, Gmail): Gmail

>> BAŞARILI: Şifre 'sifrelerim.txt' dosyasına kaydedildi.

📂 Oluşan Dosya Yapısı
password-generator-cli/
│
├── sifre_olusturucu.py
├── sifrelerim.txt
└── README.md

🔐 Güvenlik Notu

Bu proje eğitim ve kişisel kullanım amaçlıdır.
Gerçek ve kritik hesaplar için şifre yöneticileri kullanmanız önerilir.

👨‍💻 Geliştirici

Geliştirici: ÇINAR DEMİRBAŞ
