# Library App
## Basit bir kütüphane veri tabanı uygulaması.
Farazi bir kütüphane için oluşturduğum mySql veri tabanında kitaplar, üyeler ve kiralanan kitaplar için üç ayrı tablo oluşturdum. <br>
### Kitaplar (books) tablosu:
Kitap bilgilerini tuttuğum tabloda "id", "name", "author" ve kitabın mevcut olup olmadığını gösteren "isAvailable" bilgileri mevcut. <br>
Uygulama kısmında "books" tablosuna yeni bir kitap ekleyebilirim, bir kitabın bilgilerini düzenleyebilirim, tablodaki kitapları listeleyebilirim ve bir kitabı veri tabanından silebilirim.
### Üyeler (members) tablosu:
Üye bilgilerini tuttuğum tabloda "id", "name", "surname" ve "email" bilgileri mevcut. <br>
Uygulama kısmında "members" tablosuna yeni bir üye ekleyebilirim, üye bilgilerini düzenler ve üyeyi veri tabanından silebilirim.
### Ödünç Verilenler (loans) tablosu:
Ödünç verilen kitapların bilgilerini tuttuğum tabloda "memberId", "bookId", "loanDate" ve "returnDate" bilgileri mevcut. <br>
Anlaşıldığı üzere "memberId" bilgisini "members" tablosundaki "id" bilgisinden, "bookId" bilgisini de "books" tablosundaki "id" bilgisinden alıyorum. Bunun için foreign key tanımlıyorum. <br>
Böylece ilişkisel veri tabanları yöntemini kullanmış oluyorum. <br>
Kitap ödünç alma işlemini yaparken bizden önce "bookId" ve "memberId" bilgilerini girmemiz isteniyor. Ardından kitabın mevcut olup olmadığı kontrol ediliyor eğer mevcut ise kitap veriliyor. Teslim tarihi otomatik hesaplanıp işlemin yapıldığı tarih bilgisiyle beraber veri tabanımıza ("loans" tablosuna) kaydediliyor. 

## Lisans

Bu proje [MIT Lisansı](LICENSE) ile lisanslanmıştır.

