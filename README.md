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

📋 Çıktı Formatı

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

🚧 Geliştirilecek Özellikler

1 - )Dinamik subdomain keşfi <br>
2 - )Çoklu thread desteği <br>
3 - )Daha kapsamlı IP çözümleme <br>

🤝 Katkıda Bulunma

a.Fork yapın
b.Yeni branch oluşturun
c.Değişikliklerinizi commit edin
d.Pull request gönderin































































## Lisans
Bu proje [MIT Lisansı](LICENSE) altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasını inceleyebilirsiniz.



