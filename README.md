# FastAPI Projesi 🚀

Bu proje, FastAPI kullanılarak geliştirilmiş bir örnek API uygulamasıdır.

## Özellikler 📝
- Dinamik ve ölçeklenebilir API geliştirme.
- FastAPI framework'ü ile hızlı geliştirme.
- Asenkron fonksiyonlarla yüksek performans.

## Gereksinimler 📋
Bu projeyi çalıştırmak için aşağıdaki bileşenlere ihtiyacınız var:
- Python 3.8 veya üstü
- `pip`

## Kurulum 🔧

Projeyi çalıştırmak için şu adımları izleyin:

1. **Projeyi Kopyalayın:**

   ```bash
   git clone https://github.com/kullaniciadi/proje-adi.git
   cd proje-adi
   ```

2. **Virtualenv Oluşturun:**
   Virtualenv, projenizin bağımlılıklarını izole etmek için kullanılır:
   ```bash
   python -m venv venv
   source venv/bin/activate       # macOS/Linux
   venv\Scripts\activate          # Windows
   ```

3. **Bağımlılıkları Yükleyin:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Uygulamayı Çalıştırın:**

   ```bash
   uvicorn main:app --reload
   ```

5. **API'yi Kullanın:**
   Tarayıcınızda [http://127.0.0.1:8000](http://127.0.0.1:8000) adresini ziyaret edin.

## Kullanım 📖
### Örnek API Endpoints:
- **Ana Sayfa:** `GET /`
    - Mesaj döndürür: `"Hello World"`
- **Kişiye Merhaba De:** `GET /hello/{name}`
    - Bir kişiye isme özel mesaj döndürür.

### Örnek:
```bash
curl http://127.0.0.1:8000/hello/John
```

Dönen sonucu:
```json
{
    "message": "Hello John"
}
```

## Katkıda Bulunma 🤝

1. Bu projeyi forklayın
2. Bir özellik dalına geçin: `git checkout -b yeni-ozellik`
3. Değişikliklerinizi yapın ve commitleyin: `git commit -m 'Yeni özellik eklendi'`
4. Dalınızı gönderin: `git push origin yeni-ozellik`
5. Pull Request oluşturun.

## Lisans 📝
Bu proje [MIT Lisansı](LICENSE) ile lisanslanmıştır.

## İletişim 📬
Eğer daha fazla bilgiye ihtiyaç duyarsanız, lütfen [email@example.com](mailto:email@example.com) ile iletişime geçin!