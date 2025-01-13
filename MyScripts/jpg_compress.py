import os
from PIL import Image
import shutil

def convert_and_compress_jpg(folder_path, quality=70):
    # Original klasörü oluştur
    original_folder = os.path.join(folder_path, "Original")
    if not os.path.exists(original_folder):
        os.makedirs(original_folder)

    # Klasördeki tüm dosyaları kontrol et
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        # Sadece .jpg dosyalarını işleme al
        if os.path.isfile(file_path) and file_name.lower().endswith(".jpg"):
            # Yeni dosya ismini belirle (aynı isim, sadece sıkıştırma işlemi yapılacak)
            new_file_path = os.path.join(folder_path, file_name)

            # JPG dosyasını sıkıştır
            with Image.open(file_path) as img:
                rgb_img = img.convert("RGB")
                rgb_img.save(new_file_path, "JPEG", quality=quality)

            # Orijinal dosyayı Original klasörüne taşı
            shutil.move(file_path, os.path.join(original_folder, file_name))

            print(f"{file_name} sıkıştırıldı ve orijinal dosya taşındı.")

if __name__ == "__main__":
    folder_path = input("Lütfen JPG dosyalarının bulunduğu klasör yolunu girin: ").strip()
    compression_quality = int(input("Lütfen sıkıştırma kalitesini (ör: 70) girin: ").strip())

    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        convert_and_compress_jpg(folder_path, quality=compression_quality)
        print("Tüm JPG dosyaları başarıyla sıkıştırıldı!")
    else:
        print("Geçersiz klasör yolu. Lütfen doğru bir yol girin.")
