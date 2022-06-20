# AYRIK KOSİNÜS DÖNÜŞÜMÜ KULLANAN GÖRÜNTÜ STEGANOGRAFISI 
 Bu proje, bir görüntüyü DCT kullanarak frekans alanına dönüştürmeyi ve ardından gizlenmesi gereken gizli bir metin parçası eklemeyi amaçlamaktadır. Yöntem DCT steganografisi çeşidini kullanır. DCT steganografi mesajı görüntüye gizler. Görüntü sıkıştırma için yaygın olarak kullanılan ve sağlam bir yöntemdir. DFT ve LSB'den kesinlikle üstün olan yüksek oranda ilişkili veriler için mükemmel bir sıkıştırma oranına sahiptir. Sonuç olarak, işlevsel dönüşüm kodlamasının sisteminin çoğunluğu makul bir veri paketleme kapasitesi ve hesaplama karmaşıklığı dengesi sunan DCT'ye dayanmaktadır. Ayrıca, doğruluğu tahmin etmek ve verimlilik hakkında kısa bir fikir edinmek için Ortalama Kare Hatası ve Tepe Sinyali Gürültü oranı gibi veri kaybı ölçümlerini hesaplanmıştır. 

İki boyutlu ayrık kosinüs dönüşümü (2D-DCT) şu şekilde tanımlanır: 

![adsasd](https://user-images.githubusercontent.com/70798901/174661256-4d9677de-f5f1-458d-a765-ce979e6f2a8e.png)


Karşılık gelen ters dönüşüm ((2DIDCT olsun) olarak tanımlarsak:

![qqq](https://user-images.githubusercontent.com/70798901/174661298-efe78201-9dee-452c-8a70-131cc4494b03.png)

2D-DCT, orijinal görüntünün ana bilgilerini yalnızca en küçük düşük frekans katsayısına yoğunlaştırmakla kalmaz, aynı zamanda görüntü engelleme etkisinin en küçük olmasına neden olabilir, bu da bilgi merkezileştirme ile bilgi işlem komplikasyonu arasındaki iyi uzlaşmayı gerçekleştirebilir. Böylece sıkıştırma kodlamasında geniş yayılan uygulamayı elde eder. 


Embedding/Veri Gömme: 


![q](https://user-images.githubusercontent.com/70798901/174661439-5047c5d1-7db8-4d9f-952d-dcf571a2201e.png)


Ayıklama: 


![r](https://user-images.githubusercontent.com/70798901/174661498-3dbbb2c6-f901-4da3-88f0-269a5ba251f6.png)


Metin gömme: 

![t1](https://user-images.githubusercontent.com/70798901/174661554-554efbe2-6cdb-480f-a521-cf0b25da7278.png)


Gömülü metin ayıklanması: 

![t2](https://user-images.githubusercontent.com/70798901/174661573-750af804-cc34-4c0a-90f7-d7729fe84a34.png)


PSNR: 


![gq](https://user-images.githubusercontent.com/70798901/174661614-3c63482e-95f5-4eed-9fbc-ead4f98bfdf3.png)


SONUÇ:

![bb](https://user-images.githubusercontent.com/70798901/174661638-3a3e7ef3-514d-496a-84fe-af6004142ae5.png)


