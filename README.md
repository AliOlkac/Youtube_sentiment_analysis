# _**Eğitim Videoları Yorum Analizi**_

Bu proje, YouTube'daki eğitim videolarına gelen yorumları analiz eden bir duygu analiz uygulamasıdır. Kullanıcıların belirli bir eğitim konusundaki videoları aramasına, yorumları analiz etmesine ve yorumların olumlu, olumsuz veya nötr olup olmadığını görselleştirmesine olanak tanır.

## **Özellikler**
*  Eğitim Konusu Arama: Kullanıcıların belirli bir eğitim konusunu girerek ilgili videoları bulmalarını sağlar.
*  Duygu Analizi: Yorumları pozitif, negatif veya nötr olarak sınıflandırır.
*  Kapsamlı Görselleştirme: Analiz edilen sonuçların grafikler ve tablolar ile sunulmasını sağlar.
*  Tema Seçimi: Kullanıcılar, uygulamanın temasını açık veya koyu mod olarak değiştirebilir.
*  Yeniden Analiz: Kullanıcılar mevcut analizi yenileyebilir ve yeni sonuçları görüntüleyebilir.
*  Kullanılan Teknolojiler ve Kütüphaneler
*  Python: Projenin ana programlama dili.
*  TensorFlow ve Keras: Duygu analizi modelini eğitmek için kullanılan yapay zeka kütüphaneleri.
*  Streamlit: Kullanıcı arayüzünü oluşturmak ve kullanıcı etkileşimlerini kolaylaştırmak için kullanıldı.
*  Matplotlib ve Pandas: Veri işleme ve sonuçları görselleştirme amacıyla kullanıldı.


### **Kullanılan Teknolojiler ve Kütüphaneler**
*  Python: Projenin ana programlama dili.
*  TensorFlow ve Keras: Duygu analizi modelini eğitmek için kullanılan yapay zeka kütüphaneleri.
*  Streamlit: Kullanıcı arayüzünü oluşturmak ve kullanıcı etkileşimlerini kolaylaştırmak için kullanıldı.
*  Matplotlib ve Pandas: Veri işleme ve sonuçları görselleştirme amacıyla kullanıldı.


**Kurulum ve Çalıştırma**

```python
pip install -r requirements.txt
streamlit run main.py
```
## **Proje Yapısı**
*  main.py: Ana uygulama dosyası; Streamlit arayüzünü içerir.
*  README.md: Proje hakkında bilgi sağlar.
*  requirements.txt: Proje için gerekli olan Python paketlerinin listesi.

### **Kullanım**
*  Konu Girişi: Sol menüde, analiz etmek istediğiniz eğitim konusunu girin.
*  Tema Değiştirme: Koyu ve açık modlar arasında geçiş yaparak arayüzü özelleştirebilirsiniz.

![image](https://github.com/user-attachments/assets/508faddb-d0bb-4b3d-b0a0-a76d4c45ab45)

*  Analiz Sonuçları: Uygulama, yorumları analiz eder ve sonuçları tablo ve grafik olarak gösterir.

![image](https://github.com/user-attachments/assets/292c79d5-1756-41d1-9505-43334a9ca469)




## **Örnek Sonuçlar**
![image](https://github.com/user-attachments/assets/672e382e-d2d9-449b-b163-d3ad0c88e9cb)


# **Geliştirme Hedefleri**
*  YouTube API'sinden daha fazla veri çekerek analiz kapasitesini arttırmak.
*  Farklı duygu sınıflandırma algoritmaları ekleyerek analiz doğruluğunu artırmak.
*  Daha fazla grafik ve veri görselleştirme seçeneği eklemek.
