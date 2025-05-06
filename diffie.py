# Diffie-Hellman Code

G=93796485345547
P=80515489873454
x1=2
x2=3

# Açık anahtarları Hesapla ve Paylaş
y1, y2 = pow(G, x1) % P, pow(G, x2) % P

# Gizli Anahtarlari Oluştur
k1, k2 = pow(y2, x1) % P, pow(y1, x2) % P

print(f"\n1. Kullanici İçin Gizli Anahtar: {k1}\n2. Kullanici İçin Gizli Anahtar: {k2}\n")


if k1 == k2:
	print("Anahtarlar Başariyla Değiştirildi.")
else:
	print("Anahtarlar Başariyla Değiştirilemedi.")
 

hexadecimal = hex(k1)
print(f"{k1} sayisinin hexadecimal karşiligi: {hexadecimal}")