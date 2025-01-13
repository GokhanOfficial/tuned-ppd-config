import os
import subprocess

# Sağlam olmayan dosyaların tutulacağı dosya
output_file = "hatalar.txt"

# Hedef klasör
mp_folder = input("MP3 ve MP4 klasör yolunu girin: ")

# Klasör kontrolü
if not os.path.isdir(mp_folder):
    print("Geçersiz klasör yolu.")
    exit(1)

# Sağlam olmayan dosyaların listeleneceği dosya
with open(output_file, 'w') as out_file:
    # Klasördeki tüm mp3 ve mp4 dosyalarını kontrol et
    for root, dirs, files in os.walk(mp_folder):
        for file in files:
            if file.endswith((".mp3", ".mp4")):  # Hem mp3 hem de mp4 dosyalarını kontrol et
                file_path = os.path.join(root, file)
                #print(f"Kontrol ediliyor: {file_path}")

                # Dosya yolundaki boşlukları düzgün şekilde işle
                result = subprocess.run(
                    ['ffmpeg', '-v', 'error', '-i', file_path, '-f', 'null', '-'],
                    stderr=subprocess.PIPE
                )

                # ffmpeg hata durumunda, dosyayı hatalı olarak kaydet
                if result.returncode != 0:
                    print(f"Hatalı: {file_path}")
                    out_file.write(f"{file_path}\n")

print(f"Kontrol tamamlandı. Hatalı dosyalar {output_file} içinde listelendi.")

# Hatalı dosyaları silme işlemi
with open(output_file, 'r') as out_file:
    hatali_dosyalar = out_file.readlines()

if hatali_dosyalar:
    # Kullanıcıya dosyaların silinmesi için onay soralım
    onay = input(f"{len(hatali_dosyalar)} hatalı dosya bulundu. Bu dosyaları silmek ister misiniz? (E/H): ").strip().lower()

    if onay == 'e':
        for dosya in hatali_dosyalar:
            dosya = dosya.strip()  # Satır sonu boşluklarını temizle
            if os.path.exists(dosya):
                try:
                    os.remove(dosya)
                    print(f"Silindi: {dosya}")
                except Exception as e:
                    print(f"Dosya silinemedi: {dosya}. Hata: {e}")
            else:
                print(f"Dosya bulunamadı: {dosya}")
    else:
        print("Silme işlemi iptal edildi.")
else:
    print("Hiçbir hatalı dosya bulunamadı.")
