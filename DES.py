from diffie import k1
# Hexadecimal den binary e dönüştürme

#Bu işlem, sozluk adlı bir sözlük (dictionary) kullanılarak gerçekleştirilir. Her bir hexadecimal karakter, sözlükteki karşılığı olan ikili sayı ile değiştirilir ve sonuç olarak bir ikili sayı stringi elde edilir.

def hex2bin(s):#hex2bin fonksiyonu: Hexadecimal (onaltılık) sayıyı ikili (binary) sayıya dönüştürür. Örnek: 'A' -> '1010'
	sozluk = {'0': "0000",
		'1': "0001",
		'2': "0010",
		'3': "0011",
		'4': "0100",
		'5': "0101",
		'6': "0110",
		'7': "0111",
		'8': "1000",
		'9': "1001",
		'A': "1010",
		'B': "1011",
		'C': "1100",
		'D': "1101",
		'E': "1110",
		'F': "1111"}
	binString = ""  # Boş bir string (ikili sayının tutulacağı değişken) oluşturuluyor.
	for i in range(len(s)): # hexadecimal string üzerinde döngü
		binString = binString + sozluk[s[i]] # Her bir karakterin karşılığı olan ikili sayı, ikili sayı stringine ekleniyor.
	return binString # Sonuç olarak elde edilen ikili sayı stringi döndürülüyor.


# Binary den hexadecimal e dönüştürme


def bin2hex(s):#bin2hex fonksiyonu: İkili sayıyı hexadecimal sayıya dönüştürür.
	sozluk = {"0000": '0',
		"0001": '1',
		"0010": '2',
		"0011": '3',
		"0100": '4',
		"0101": '5',
		"0110": '6',
		"0111": '7',
		"1000": '8',
		"1001": '9',
		"1010": 'A',
		"1011": 'B',
		"1100": 'C',
		"1101": 'D',
		"1110": 'E',
		"1111": 'F'}
	hex = ""
	for i in range(0, len(s), 4):  #s adlı bir dize (string) üzerinde döngü oluşturuluyor. 
		ch = ""						#Bu döngü, s dizisinin her 4 karakterlik dilimleri üzerinde gezinmeyi saglar.
		ch = ch + s[i]				#Boş bir dize olan ch oluşturuluyor. Bu dize, her döngü adımında 4 karakterlik bir dilim içerecek.
		ch = ch + s[i + 1]			#ch adlı dize, her seferinde s dizisinin farklı indekslerindeki karakterlerle güncelleniyor. 
		ch = ch + s[i + 2]			#Bu sayede her adımda ch, s dizisinin o anki 4 karakterlik dilimini temsil eder.
		ch = ch + s[i + 3]
		hex = hex + sozluk[ch]			# mp nin içinde, ch dizesine karşılık gelen bir değer alınır ve bu değer,hex adlı bir dize ile birleştirilir.
									# Bu işlem, döngü boyunca her 4 karakterlik dilimi işleyerek bir hexadecimal (onaltılık) değer elde etmeyi amaçlar.
	return hex



# Binary den decimal e dönüştürme

def bin2dec(binary):#bin2dec fonksiyonu: İkili sayıyı ondalık sayıya dönüştürür.
# binary: ikili sayıyı temsil eden bir tam sayı
	binary1 = binary# İkili sayının orijinal değerini sakla
	decimal, i, n = 0, 0, 0 # Ondalık sayı, üs değeri ve ikili sayının basamak sayısını tutan değişkenler
	while(binary != 0):# İkili sayı sıfır olana kadar döngüyü devam ettir
		dec = binary % 10 # İkili sayının en sagdaki basamağını al
		decimal = decimal + dec * pow(2, i)# İkili sayıdaki basamağı ondalık sayıya dönüştür ve toplama ekle
		binary = binary//10 # İkili sayının en sagdaki basamağını at
		i += 1 # Üs değerini bir arttır
	return decimal



# Decimal den binary e dönüştürme

# sayi: ondalık sayıyı temsil eden bir tam sayı
def dec2bin(sayi):#dec2bin fonksiyonu: Ondalık sayıyı ikili sayıya dönüştürür.
	res = bin(sayi).replace("0b", "")# Ondalık sayıyı ikili sayıya dönüştür ve "0b" ön ekini kaldır
	if(len(res) % 4 != 0): # Elde edilen ikili sayının uzunluğu 4'ün katı değilse (4 bit grupları olacak şekilde düzenlenir)
		div = len(res) / 4
		div = int(div)
		sayac = (4 * (div + 1)) - len(res)# Eksik olan sıfırları eklemek için gereken sayıyı hesapla
		for i in range(0, sayac):
			res = '0' + res# Eksik sıfırları başa ekle
	return res

a=dec2bin(4)
print(f"şifre: {a}")



# bitleri yeniden düzenlemek için permütasyon fonksiyonu

def permutasyonFonk(k, arr, n):#permutasyonFonk fonksiyonu: Verilen sıralama tablosuna göre bitleri yeniden düzenler.
	permutasyon = ""
	for i in range(0, n):  # Sıralama tablosu üzerinde döngü
		permutasyon = permutasyon + k[arr[i] - 1] #Giriş bit dizisinden sıralama tablosuna göre bitleri alıp yeni bir sıralama oluştur
	return permutasyon
 	# k: giriş bit dizisi
    # arr: sıralama tablosu (permutasyon tablosu)
    # n: sıralama tablosunun uzunluğu




# bitleri n'inci kaydırma kadar sola kaydırmak

	# k: giriş bit dizisi
    # nth_shifts: sola kaydırılacak bit sayısı
def shift_sol(k, nth_shifts):#shift_sol fonksiyonu: Belirtilen sayıda biti sola kaydırır.
	s = ""# Yardımcı bir dize
	for i in range(nth_shifts):# Belirtilen sayıda sola doğru kaydırma işlemi
		for j in range(1, len(k)):# Giriş bit dizisindeki her bir biti bir sola kaydırarak yeni bir dize oluştur
			s = s + k[j]
		s = s + k[0]# En sonda kalan ilk biti, yeni oluşturulan dizinin sonuna ekle
		k = s# Oluşturulan yeni diziyi, giriş dizisi olarak güncelle
		s = ""# Yardımcı diziyi sıfırla
	return k


# a ve b binary(ikili sayılarından oluşan iki dizinin xor'unun hesaplanması)
# a ve b: ikili sayıları temsil eden diziler
def xor(a, b):#xor fonksiyonu: İki ikili sayının XOR (exclusive OR) işlemi sonucunu döndürür.
	ans = ""# XOR işlemi sonucunu tutacak olan dize
	for i in range(len(a)):# Her bir biti karşılaştır ve XOR işlemi uygula
		if a[i] == b[i]:
			ans = ans + "0"# İki bit değeri eşitse, XOR sonucu 0 olur
		else:
			ans = ans + "1"# İki bit değeri farklıysa, XOR sonucu 1 olur
	return ans


# Table of Position of 64 bits at initial level: Initial permutasyon Table
initial_perm = [58, 50, 42, 34, 26, 18, 10, 2,#initial_perm ve diğer sabitler: DES algoritması için kullanılacak olan sabit sıralama tablolarını içerir.
				60, 52, 44, 36, 28, 20, 12, 4,
				62, 54, 46, 38, 30, 22, 14, 6,
				64, 56, 48, 40, 32, 24, 16, 8,
				57, 49, 41, 33, 25, 17, 9, 1,
				59, 51, 43, 35, 27, 19, 11, 3,
				61, 53, 45, 37, 29, 21, 13, 5,
				63, 55, 47, 39, 31, 23, 15, 7]

# Expansion D-box Table
geniletmeTablosu = [32, 1, 2, 3, 4, 5, 4, 5, #GENİŞLETME PERMÜTASYONU
		6, 7, 8, 9, 8, 9, 10, 11,
		12, 13, 12, 13, 14, 15, 16, 17,
		16, 17, 18, 19, 20, 21, 20, 21,
		22, 23, 24, 25, 24, 25, 26, 27,
		28, 29, 28, 29, 30, 31, 32, 1]

# Straight permutasyon Table
per = [16, 7, 20, 21, #P-KUTUSU PERMÜTASYONU
	29, 12, 28, 17,
	1, 15, 23, 26,
	5, 18, 31, 10,
	2, 8, 24, 14,
	32, 27, 3, 9,
	19, 13, 30, 6,
	22, 11, 4, 25]

# S-box Table
sbox = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],#sbox sabiti: S-box tablosunu içerir, DES algoritmasında kullanılan bir substitüsyon işlemi için gerekli olan kutuları temsil eder.
		[0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
		[4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
		[15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

		[[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
		[3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
		[0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
		[13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

		[[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
		[13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
		[13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
		[1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

		[[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
		[13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
		[10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
		[3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

		[[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
		[14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
		[4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
		[11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

		[[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
		[10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
		[9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
		[4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

		[[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
		[13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
		[1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
		[6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

		[[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
		[1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
		[7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
		[2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]

# Final permutasyon Table
final_perm = [40, 8, 48, 16, 56, 24, 64, 32, #SONUÇ PERMÜTASYONU:başlangıç permütasyonunun tersi
			39, 7, 47, 15, 55, 23, 63, 31,
			38, 6, 46, 14, 54, 22, 62, 30,
			37, 5, 45, 13, 53, 21, 61, 29,
			36, 4, 44, 12, 52, 20, 60, 28,
			35, 3, 43, 11, 51, 19, 59, 27,
			34, 2, 42, 10, 50, 18, 58, 26,
			33, 1, 41, 9, 49, 17, 57, 25]





	# pt: şifrelenecek metin
    # yaa: yuvarlama alt anahtarları (round subkeys)
    # ya: yuvarlama anahtarları (round keys)
def sifrele(pt, yaa, ya):#sifrele fonksiyonu: Metni şifrelemek için DES algoritmasını kullanır. İlk olarak, metni başlangıç permütasyonu (initial permutasyon) ile işler, ardından 16 turda (round) saga kaydırma, XOR, S-box işlemleri ve permütasyon işlemleri gerçekleştirir. Son olarak, final permütasyonu ile sonuç elde edilir.
	pt = hex2bin(pt)# Hexadecimal metni ikili sayıya dönüştür

	# Initial permutasyon:BAŞLANGIÇ PERMÜTASYONU
	pt = permutasyonFonk(pt, initial_perm, 64)
	print("Baslangic permutasyonundan sonra", bin2hex(pt))

	# Metni iki parçaya bölme
	sol = pt[0:32]
	sag = pt[32:64]
	for i in range(0, 16):
		# Expansion D-box(GENİŞLETME PERMÜTASYONU):32 bit veriyi 48 bit'e genişletme
		sag_expanded = permutasyonFonk(sag, geniletmeTablosu, 48)

		# XOR RoundKey[i] and sag_expanded
		xor_x = xor(sag_expanded, yaa[i])

		# S-boxex: satır ve sütunu hesaplayarak s-box tablosundaki değerin değiştirilmesi
		sbox_str = ""
		for j in range(0, 8):
			row = bin2dec(int(xor_x[j * 6] + xor_x[j * 6 + 5]))
			col = bin2dec(
				int(xor_x[j * 6 + 1] + xor_x[j * 6 + 2] + xor_x[j * 6 + 3] + xor_x[j * 6 + 4]))
			val = sbox[j][row][col]
			sbox_str = sbox_str + dec2bin(val)

		# Straight D-box: Bitleri yeniden düzenledikten sonra
		sbox_str = permutasyonFonk(sbox_str, per, 32)

		# XOR sol and sbox_str
		sonuc = xor(sol, sbox_str)
		sol = sonuc

		# Swapper
		if(i != 15):
			sol, sag = sag, sol
		print(" ", i + 1, " ", bin2hex(sol),
			" ", bin2hex(sag), " ", ya[i])

	# Combination:BİRLEŞTİRME
	combine = sol + sag

	# Final permutasyon: Son bit düzenlemesiyle şifreleme sonucunu elde etme
	cipher_text = permutasyonFonk(combine, final_perm, 64)
	return cipher_text


pt = "123456ABCD132536" #PLAİN TEXT:şifrelenecek metin
#key = "AABB09182736CCDD" #ŞİFRELEME ANAHTARI
#diffie hellman'da bulunan ortak gizli anahtar
key="1234567890ABCDEF"
# ANAHTAR ÜRETİMİ
# --hex to binary

key = hex2bin(key)

# --parity bit drop table
keyp = [57, 49, 41, 33, 25, 17, 9,#ANAHTAR PERMÜTASYONU
		1, 58, 50, 42, 34, 26, 18,
		10, 2, 59, 51, 43, 35, 27,
		19, 11, 3, 60, 52, 44, 36,
		63, 55, 47, 39, 31, 23, 15,
		7, 62, 54, 46, 38, 30, 22,
		14, 6, 61, 53, 45, 37, 29,
		21, 13, 5, 28, 20, 12, 4]

# parity bitlerini kullanarak 64 bitten 56 bit anahtar alma
key = permutasyonFonk(key, keyp, 56)

# Bit kaydırma sayısı
shift_table = [1, 1, 2, 2, #HER DÖNGÜDE KAYDIRILACAK BİT SAYISI
			2, 2, 2, 2,
			1, 2, 2, 2,
			2, 2, 2, 1]

# Key- Compression Table(Anahtar sıkıştırma tablosu):Anahtarın 56 bitten 48 bit'e sıkıştırılması
anahtarCompressionTablosu = [14, 17, 11, 24, 1, 5, #SIKIŞTIRMA PERMÜTASYONU
			3, 28, 15, 6, 21, 10,
			23, 19, 12, 4, 26, 8,
			16, 7, 27, 20, 13, 2,
			41, 52, 31, 37, 47, 55,
			30, 40, 51, 45, 33, 48,
			44, 49, 39, 56, 34, 53,
			46, 42, 50, 36, 29, 32]

# Anahtarın iki parçaya bölünmesi
sol = key[0:28] # rkb (RoundKeys in binary) için sol yarısı
sag = key[28:56] # rk (RoundKeys in hexadecimal) için sag yarısı

yaa = [] # Yuvarlama alt anahtarları (round subkeys)
ya = [] # Yuvarlama anahtarları (round keys)
# 16 tur için alt anahtarların oluşturulması
for i in range(0, 16):
	# Bitleri shift_table'dan alınan değerlere göre kaydırma
	sol = shift_sol(sol, shift_table[i])
	sag = shift_sol(sag, shift_table[i])

	# Sol ve sag dizeyi birleştirme
	str_birlestir = sol + sag

	# Anahtarın sıkıştırılması (56 bit'ten 48 bit'e)
	round_key = permutasyonFonk(str_birlestir, anahtarCompressionTablosu, 48)

	yaa.append(round_key)
	ya.append(bin2hex(round_key))

print("Sifreleme")
sifreli_metin = bin2hex(sifrele(pt, yaa, ya))
print("Cipher Text(Sifreli Metin) : ", sifreli_metin)

print("Desifreleme")
# Alt anahtarların ters sırayla alınması
yaa_ters = yaa[::-1]
ya_ters = ya[::-1]
metin = bin2hex(sifrele(sifreli_metin, yaa_ters, ya_ters))
print("Plain Text(Orijinal Metin) : ", metin)


