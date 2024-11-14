ğitim Videoları Yorum Analizi
Bu proje, YouTube'daki eğitim videolarına gelen yorumları analiz eden bir duygu analiz uygulamasıdır. Kullanıcıların belirli bir eğitim konusundaki videoları aramasına, yorumları analiz etmesine ve yorumların olumlu, olumsuz veya nötr olup olmadığını görselleştirmesine olanak tanır.

Özellikler
Eğitim Konusu Arama: Kullanıcıların belirli bir eğitim konusunu girerek ilgili videoları bulmalarını sağlar.
Duygu Analizi: Yorumları pozitif, negatif veya nötr olarak sınıflandırır.
Kapsamlı Görselleştirme: Analiz edilen sonuçların grafikler ve tablolar ile sunulmasını sağlar.
Tema Seçimi: Kullanıcılar, uygulamanın temasını açık veya koyu mod olarak değiştirebilir.
Yeniden Analiz: Kullanıcılar mevcut analizi yenileyebilir ve yeni sonuçları görüntüleyebilir.
Kullanılan Teknolojiler ve Kütüphaneler
Python: Projenin ana programlama dili.
TensorFlow ve Keras: Duygu analizi modelini eğitmek için kullanılan yapay zeka kütüphaneleri.
Streamlit: Kullanıcı arayüzünü oluşturmak ve kullanıcı etkileşimlerini kolaylaştırmak için kullanıldı.
Matplotlib ve Pandas: Veri işleme ve sonuçları görselleştirme amacıyla kullanıldı.
Kurulum ve Çalıştırma
Gereksinimleri yükleyin:

bash
Kodu kopyala
pip install -r requirements.txt
Streamlit uygulamasını başlatın:

bash
Kodu kopyala
streamlit run main.py
Model ve Veri Dosyaları: Uygulamanın doğru çalışması için duygu analizi modeli (my_model.keras) ve yorum ön işleme aracı (tokenizer.joblib) proje klasöründe bulunmalıdır.

Proje Yapısı
main.py: Ana uygulama dosyası; Streamlit arayüzünü içerir.
utils.py: Yorumları temizlemek ve modeli yüklemek için yardımcı fonksiyonları içerir.
README.md: Proje hakkında bilgi sağlar.
requirements.txt: Proje için gerekli olan Python paketlerinin listesi.
Kullanım
Konu Girişi: Sol menüde, analiz etmek istediğiniz eğitim konusunu girin.
Analiz Sonuçları: Uygulama, yorumları analiz eder ve sonuçları tablo ve grafik olarak gösterir.
Tema Değiştirme: Koyu ve açık modlar arasında geçiş yaparak arayüzü özelleştirebilirsiniz.
Analizi Yenileme: Yeniden analiz yaparak güncel sonuçları görüntüleyebilirsiniz.
Örnek Sonuçlar
Yorum	Tahmin Edilen Duygu
"Bu video çok faydalıydı!"	Pozitif
"Hiçbir şey anlamadım."	Negatif
"Eğitici bir içerik."	Nötr
Geliştirme Hedefleri
YouTube API'sinden daha fazla veri çekerek analiz kapasitesini arttırmak.
Farklı duygu sınıflandırma algoritmaları ekleyerek analiz doğruluğunu artırmak.
Daha fazla grafik ve veri görselleştirme seçeneği eklemek.
