import os
from PIL import Image

def resim_bozuk_mu(dosya_yolu):
    """Bir resim dosyasının bozuk olup olmadığını kontrol eder."""
    try:
        with Image.open(dosya_yolu) as img:
            img.verify()  # Resmin geçerli olup olmadığını doğrular
        return False  # Bozuk değil
    except Exception:
        return True  # Bozuk

def bozuk_resimleri_bul(dizin):
    """Verilen dizindeki tüm bozuk resim dosyalarını bulur."""
    bozuk_dosyalar = []
    for kok, _, dosyalar in os.walk(dizin):
        for dosya in dosyalar:
            if dosya.lower().endswith(('.jpg', '.jpeg', '.bmp')):
                dosya_yolu = os.path.join(kok, dosya)
                if resim_bozuk_mu(dosya_yolu):
                    bozuk_dosyalar.append(dosya_yolu)
    return bozuk_dosyalar

def dosyalari_sil(dosya_listesi):
    """Belirtilen dosyaları dosya sisteminden siler."""
    for dosya_yolu in dosya_listesi:
        try:
            os.remove(dosya_yolu)
            print(f"Silindi: {dosya_yolu}")
        except Exception as e:
            print(f"{dosya_yolu} silinirken hata oluştu: {e}")

def ana():
    dizin = input("Resimleri içeren dizinin yolunu girin: ").strip()

    if not os.path.isdir(dizin):
        print("Geçersiz dizin yolu.")
        return

    print("Bozuk resimler taranıyor...")
    bozuk_dosyalar = bozuk_resimleri_bul(dizin)

    if bozuk_dosyalar:
        print("Aşağıdaki bozuk dosyalar bulundu:")
        for dosya in bozuk_dosyalar:
            print(dosya)

        onay = input("Bu dosyaları silmek istiyor musunuz? (evet/hayır): ").strip().lower()
        if onay in ("evet", "e"):
            dosyalari_sil(bozuk_dosyalar)
            print("Tüm bozuk dosyalar silindi.")
        else:
            print("Hiçbir dosya silinmedi.")
    else:
        print("Bozuk dosya bulunamadı.")

if __name__ == "__main__":
    ana()
