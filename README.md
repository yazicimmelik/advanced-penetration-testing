🌐 Subdomain Keşif Aracı
📝 Proje Açıklaması
Basit bir Python subdomain keşif aracı. Domain üzerindeki alt alan adlarını (subdomainleri) keşfeder ve IP adreslerini çözer.
✨ Özellikler

🔍 Statik subdomain keşfi
🌐 IP adresi çözümleme
📋 JSON formatında çıktı
🛡️ Hata yönetimi

🛠 Gereksinimler

Python 3.7+
socket kütüphanesi
json kütüphanesi

🚀 Kurulum
# Gerekli kütüphaneleri yükle
pip install -r requirements.txt
💻 Kullanım

🔧 Fonksiyonlar

find_subdomains(domain): Statik subdomain listesi oluşturur
resolve_ips(subdomains): Subdomainlerin IP adreslerini bulur
main(): Ana çalıştırma fonksiyonu

<h2>📋 Çıktı Formatı <h2>

jsonCopy{
    "status": "success",
    "data": {
        "domain": "example.com",
        "subdomains": [
            {
                "subdomain": "www.example.com",
                "ip_address": "192.168.1.1"
            }
        ]
    }
}
<br>
🚧 Geliştirilecek Özellikler
<br>
1 - )Dinamik subdomain keşfi <br>
2 - )Çoklu thread desteği <br>
3 - )Daha kapsamlı IP çözümleme <br>
<br>
🤝 Katkıda Bulunma <br>

a.Fork yapın <br>
b.Yeni branch oluşturun <br>
c.Değişikliklerinizi commit edin <br>
d.Pull request gönderin <br>































































## Lisans
Bu proje [MIT Lisansı](LICENSE) altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasını inceleyebilirsiniz.



