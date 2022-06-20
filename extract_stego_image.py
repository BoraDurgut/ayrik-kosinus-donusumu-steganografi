'''
Author: BORAPC

'''
#------ Kütüphane ------#
import cv2
import struct
import bitstring
import numpy  as np
import zigzag as zz
#================================#
#---------- Kaynak  --------#
import data_embedding as stego
import run_stego_algorithm as src
import image_preparation   as img
#================================#

# ============================================================================= #
# ============================================================================= #
# =========================== BAŞLA =========================================== #
# ============================================================================= #
# ============================================================================= #

stego_image     = cv2.imread(src.STEGO_IMAGE_FILEPATH, flags=cv2.IMREAD_COLOR)
stego_image_f32 = np.float32(stego_image)
stego_image_YCC = img.YCC_Image(cv2.cvtColor(stego_image_f32, cv2.COLOR_BGR2YCrCb))

# İLERİ DCT AŞAMASI
dct_blocks = [cv2.dct(block) for block in stego_image_YCC.channels[0]]  # Only care about Luminance layer

# NİCELEME AŞAMASI
dct_quants = [np.around(np.divide(item, img.JPEG_STD_LUM_QUANT_TABLE)) for item in dct_blocks]

# DCT katsayılarını frekansa göre sırala
sorted_coefficients = [zz.zigzag(block) for block in dct_quants]

# VERİ ÇIKARMA AŞAMASI
recovered_data = stego.extract_encoded_data_from_DCT(sorted_coefficients)

# Gizli iletinin uzunluğunu belirleme
data_len = int(recovered_data.read('uint:32') / 8)

# DCT katsayılarından gizli mesaj çıkarma
extracted_data = bytes()
for _ in range(data_len): extracted_data += struct.pack('>B', recovered_data.read('uint:8'))

# Gizli iletiyi kullanıcıya geri yazdır
print(extracted_data.decode('ascii'))