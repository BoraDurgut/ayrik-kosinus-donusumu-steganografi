# Zigzag scan of a matrix
# Argüman, kesinlikle bir kare değil
# herhangi bir boyutta iki boyutlu bir matristir.
# İşlev, 1'e (m * n) bir dizi döndürür; burada m ve n,
# burada m ve n, bir zikzak yöntemiyle taranan öğelerinden oluşan,
# bir giriş matrisinin boyutlarıdır.



import numpy as np

def zigzag(input):
	#değişkenleri başlat
	#----------------------------------
	h = 0
	v = 0

	vmin = 0
	hmin = 0

	vmax = input.shape[0]
	hmax = input.shape[1]

	#print(vmax ,hmax )

	i = 0

	output = np.zeros(( vmax * hmax))
	#----------------------------------

	while ((v < vmax) and (h < hmax)):

		if ((h + v) % 2) == 0:                 # yukarı çık

			if (v == vmin):
				#print(1)
				output[i] = input[v, h]        # eğer ilk satıra ulaşırsak

				if (h == hmax):
					v = v + 1
				else:
					h = h + 1

				i = i + 1

			elif ((h == hmax -1 ) and (v < vmax)):   # eğer son sütuna ulaşırsak
				#print(2)
				output[i] = input[v, h]
				v = v + 1
				i = i + 1

			elif ((v > vmin) and (h < hmax -1 )):    # diğer tüm durumlar için
				#print(3)
				output[i] = input[v, h]
				v = v - 1
				h = h + 1
				i = i + 1


		else:                                    # aşağı in

			if ((v == vmax -1) and (h <= hmax -1)):       # eğer son satıra ulaşırsak
				#print(4)
				output[i] = input[v, h]
				h = h + 1
				i = i + 1

			elif (h == hmin):                  # eğer ilk sütuna ulaşırsak
				#print(5)
				output[i] = input[v, h]

				if (v == vmax -1):
					h = h + 1
				else:
					v = v + 1

				i = i + 1

			elif ((v < vmax -1) and (h > hmin)):     # diğer tüm durumlar
				#print(6)
				output[i] = input[v, h]
				v = v + 1
				h = h - 1
				i = i + 1




		if ((v == vmax-1) and (h == hmax-1)):          # sağ alt öğe
			#print(7)
			output[i] = input[v, h]
			break

	#print ('v:',v,', h:',h,', i:',i)
	return output




# Bir matrisin ters zikzak taraması
# Bağımsız değişkenler şunlardır: m & n'nin bir çıktı matrisinin dikey
# ve yatay boyutları olduğu 1'e m * n dizisi.
# Fonksiyon, zikzak yöntemiyle toplanan girdi dizisi öğelerinden oluşan
# tanımlanmış boyutlarda iki boyutlu bir matris döndürür.



def inverse_zigzag(input, vmax, hmax):

	#print input.shape

	# değişkenleri başlatma
	#----------------------------------
	h = 0
	v = 0

	vmin = 0
	hmin = 0

	output = np.zeros((vmax, hmax))

	i = 0
	#----------------------------------

	while ((v < vmax) and (h < hmax)):
		#print ('v:',v,', h:',h,', i:',i)
		if ((h + v) % 2) == 0:                 # going up

			if (v == vmin):
				#print(1)

				output[v, h] = input[i]        # if we got to the first line

				if (h == hmax):
					v = v + 1
				else:
					h = h + 1

				i = i + 1

			elif ((h == hmax -1 ) and (v < vmax)):   # if we got to the last column
				#print(2)
				output[v, h] = input[i]
				v = v + 1
				i = i + 1

			elif ((v > vmin) and (h < hmax -1 )):    # all other cases
				#print(3)
				output[v, h] = input[i]
				v = v - 1
				h = h + 1
				i = i + 1


		else:                                    # going down

			if ((v == vmax -1) and (h <= hmax -1)):       # if we got to the last line
				#print(4)
				output[v, h] = input[i]
				h = h + 1
				i = i + 1

			elif (h == hmin):                  # if we got to the first column
				#print(5)
				output[v, h] = input[i]
				if (v == vmax -1):
					h = h + 1
				else:
					v = v + 1
				i = i + 1

			elif((v < vmax -1) and (h > hmin)):     # all other cases
				output[v, h] = input[i]
				v = v + 1
				h = h - 1
				i = i + 1




		if ((v == vmax-1) and (h == hmax-1)):          # bottom right element
			#print(7)
			output[v, h] = input[i]
			break


	return output
