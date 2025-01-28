<h1 align="center">🌐 Subdomain Keşif Aracı v2.0</h1>
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.7%2B-blue" alt="Python Version">
  <img src="https://img.shields.io/badge/License-MIT-green" alt="License">
  <img src="https://img.shields.io/badge/Version-2.0-red" alt="Version">
</p>
<h2>📝 Proje Açıklaması</h2>
<p>Gelişmiş Python tabanlı subdomain keşif aracı. Hedef domain üzerindeki alt alan adlarını (subdomain) tespit eder, IP adreslerini çözümler ve çeşitli DNS kayıtlarını kontrol eder.</p>
<h2>✨ Özellikler</h2>
<ul>
  <li>🔍 Kapsamlı subdomain taraması (24 yaygın subdomain)</li>
  <li>🚀 Paralel tarama ile hızlı sonuç</li>
  <li>🌐 IP adresi çözümleme</li>
  <li>📊 DNS kayıt analizi (A, MX, TXT, CNAME)</li>
  <li>🌍 HTTP durum kontrolü</li>
  <li>📋 JSON ve CSV formatında raporlama</li>
  <li>⚡ Çoklu thread desteği</li>
  <li>🛡️ Gelişmiş hata yönetimi</li>
</ul>
<h2>🛠 Gereksinimler</h2>
<ul>
  <li>Python 3.7+</li>
  <li>dns.resolver</li>
  <li>requests</li>
  <li>concurrent.futures</li>
  <li>csv</li>
  <li>json</li>
  <li>datetime</li>
  <li>os</li>
  <li>typing</li>
</ul>
<h2>🚀 Kurulum</h2>

Projeyi klonlayın:

bashCopygit clone https://github.com/kullaniciadi/subdomain-scanner.git
cd subdomain-scanner

Gerekli paketleri yükleyin:

bashCopypip install -r requirements.txt
<h2>💻 Kullanım</h2>

Programı çalıştırın:

bashCopypython main.py

İstenildiğinde domain adını girin:

CopyDomain adını girin (örn: example.com): example.com
<h2>📋 Çıktı Formatları</h2>
<h3>JSON Çıktı Örneği:</h3>
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
<h3>CSV Çıktı Örneği:</h3>
csvCopySubdomain,IP Addresses,HTTP Status,DNS Records
www.example.com,93.184.216.34,200,{"MX":["10 mail.example.com"]}
<h2>🔧 Konfigürasyon</h2>
config.json dosyasını düzenleyerek ayarları özelleştirebilirsiniz:
jsonCopy{
    "default_domain": "example.com",
    "timeout": 10,
    "max_threads": 10,
    "output_dir": "results"
}
<h2>🚧 Geliştirilecek Özellikler</h2>
<ul>
  <li>🔒 SSL sertifika kontrolü</li>
  <li>🌐 Web arayüzü</li>
  <li>🔌 API desteği</li>
  <li>🚪 Port tarama özelliği</li>
  <li>📸 Screenshot alma özelliği</li>
  <li>📧 E-posta bildirim sistemi</li>
</ul>
<h2>🤝 Katkıda Bulunma</h2>
<ol>
  <li>Projeyi fork edin</li>
  <li>Yeni bir branch oluşturun (<code>git checkout -b yeni-ozellik</code>)</li>
  <li>Değişikliklerinizi commit edin (<code>git commit -am 'Yeni özellik: X'</code>)</li>
  <li>Branch'inizi push edin (<code>git push origin yeni-ozellik</code>)</li>
  <li>Pull Request oluşturun</li>
</ol>
<h2>📄 Lisans</h2>
<p>Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için <code>LICENSE</code> dosyasını inceleyebilirsiniz.</p>
<h2>📬 İletişim</h2>
<ul>
  <li>GitHub: <a href="https://github.com/kullaniciadi">@kullaniciadi</a></li>
  <li>E-posta: ornek@email.com</li>
</ul>
<h2>⚠️ Yasal Uyarı</h2>
<p>Bu araç, yalnızca yasal ve etik kullanım için tasarlanmıştır. Yetkisiz sistem taraması yasal değildir.</p>
