import os
from PIL import Image
import shutil

def convert_bmp_to_jpg(folder_path):
    # Original klasörü oluştur
    original_folder = os.path.join(folder_path, "Original")
    if not os.path.exists(original_folder):
        os.makedirs(original_folder)

    # Klasördeki tüm dosyaları kontrol et
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        # Sadece .bmp dosyalarını işleme al
        if os.path.isfile(file_path) and file_name.lower().endswith(".bmp"):
            # Yeni dosya ismini belirle (jpg uzantılı)
            new_file_name = os.path.splitext(file_name)[0] + ".jpg"
            new_file_path = os.path.join(folder_path, new_file_name)

            # BMP dosyasını JPG'ye dönüştür
            with Image.open(file_path) as img:
                rgb_img = img.convert("RGB")
                rgb_img.save(new_file_path, "JPEG")

            # Orijinal dosyayı Original klasörüne taşı
            shutil.move(file_path, os.path.join(original_folder, file_name))

            print(f"{file_name} dönüştürüldü ve orijinal dosya taşındı.")

if __name__ == "__main__":
    folder_path = input("Lütfen BMP dosyalarının bulunduğu klasör yolunu girin: ").strip()

    if os.path.exists(folder_path) and os.path.isdir(folder_path):
        convert_bmp_to_jpg(folder_path)
        print("Tüm BMP dosyaları başarıyla dönüştürüldü!")
    else:
        print("Geçersiz klasör yolu. Lütfen doğru bir yol girin.")
