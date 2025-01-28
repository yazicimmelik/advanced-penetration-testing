🌐 Subdomain Keşif Aracı v2.0
📝 Proje Açıklaması
Gelişmiş Python tabanlı subdomain keşif aracı. Hedef domain üzerindeki alt alan adlarını (subdomain) tespit eder, IP adreslerini çözümler ve çeşitli DNS kayıtlarını kontrol eder.
✨ Özellikler

🔍 Kapsamlı subdomain taraması (24 yaygın subdomain)
🚀 Paralel tarama ile hızlı sonuç
🌐 IP adresi çözümleme
📊 DNS kayıt analizi (A, MX, TXT, CNAME)
🌍 HTTP durum kontrolü
📋 JSON ve CSV formatında raporlama
⚡ Çoklu thread desteği
🛡️ Gelişmiş hata yönetimi

🛠 Gereksinimler

Python 3.7+
dns.resolver
requests
concurrent.futures
csv
json
datetime
os
typing

🚀 Kurulum

Projeyi klonlayın:

bashCopygit clone https://github.com/kullaniciadi/subdomain-scanner.git
cd subdomain-scanner

Gerekli paketleri yükleyin:

bashCopypip install -r requirements.txt
💻 Kullanım

Programı çalıştırın:

bashCopypython main.py

İstenildiğinde domain adını girin:

CopyDomain adını girin (örn: example.com): example.com
📋 Çıktı Formatları
JSON Çıktı Örneği:
jsonCopy{
    "scan_info": {
        "domain": "example.com",
        "scan_date": "2025-01-28T14:30:00",
        "total_subdomains_checked": 24,
        "found_subdomains": 3
    },
    "findings": [
        {
            "subdomain": "www.example.com",
            "ip_addresses": ["93.184.216.34"],
            "http_status": 200,
            "dns_records": {
                "MX": ["10 mail.example.com"],
                "TXT": ["v=spf1 include:_spf.example.com ~all"]
            }
        }
    ]
}
CSV Çıktı Örneği:
csvCopySubdomain,IP Addresses,HTTP Status,DNS Records
www.example.com,93.184.216.34,200,{"MX":["10 mail.example.com"]}
🔧 Konfigürasyon
config.json dosyasını düzenleyerek ayarları özelleştirebilirsiniz:
jsonCopy{
    "default_domain": "example.com",
    "timeout": 10,
    "max_threads": 10,
    "output_dir": "results"
}
🚧 Geliştirilecek Özellikler

🔒 SSL sertifika kontrolü
🌐 Web arayüzü
🔌 API desteği
🚪 Port tarama özelliği
📸 Screenshot alma özelliği
📧 E-posta bildirim sistemi

🤝 Katkıda Bulunma

Projeyi fork edin
Yeni bir branch oluşturun (git checkout -b yeni-ozellik)
Değişikliklerinizi commit edin (git commit -am 'Yeni özellik: X')
Branch'inizi push edin (git push origin yeni-ozellik)
Pull Request oluşturun

📄 Lisans
Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için LICENSE dosyasını inceleyebilirsiniz.
📬 İletişim

GitHub: @yazicimmelik
E-posta: yedekmelik80@gmail.com

⚠️ Yasal Uyarı
Bu araç, yalnızca yasal ve etik kullanım için tasarlanmıştır. Yetkisiz sistem taraması yasal değildir.
