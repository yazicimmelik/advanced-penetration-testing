<h1>🌐 Subdomain Keşif Aracı</h1>

<h2>📝 Proje Açıklaması</h2>
<p>Basit bir Python subdomain keşif aracı. Domain üzerindeki alt alan adlarını (subdomainleri) keşfeder ve IP adreslerini çözer.</p>

<h2>✨ Özellikler</h2>
<ul>
    <li>🔍 Statik subdomain keşfi</li>
    <li>🌐 IP adresi çözümleme</li>
    <li>📋 JSON formatında çıktı</li>
    <li>🛡️ Hata yönetimi</li>
</ul>

<h2>🛠 Gereksinimler</h2>
<ul>
    <li>Python 3.7+</li>
    <li>socket kütüphanesi</li>
    <li>json kütüphanesi</li>
</ul>

<h2>🚀 Kurulum</h2>
<pre><code>pip install -r requirements.txt</code></pre>

<h2>💻 Kullanım</h2>
<pre><code>python main.py</code></pre>

<h2>🔧 Fonksiyonlar</h2>
<ul>
    <li><code>find_subdomains(domain)</code>: Statik subdomain listesi oluşturur</li>
    <li><code>resolve_ips(subdomains)</code>: Subdomainlerin IP adreslerini bulur</li>
    <li><code>main()</code>: Ana çalıştırma fonksiyonu</li>
</ul>

<h2>📋 Çıktı Formatı</h2>
<pre><code>{
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
}</code></pre>

<h2>🚧 Geliştirilecek Özellikler</h2>
<ul>
    <li>Dinamik subdomain keşfi</li>
    <li>Çoklu thread desteği</li>
    <li>Daha kapsamlı IP çözümleme</li>
</ul>

<h2>🤝 Katkıda Bulunma</h2>
<ol>
    <li>Fork yapın</li>
    <li>Yeni branch oluşturun</li>
    <li>Değişikliklerinizi commit edin</li>
    <li>Pull request gönderin</li>
</ol>

<h2>📄 Lisans</h2>
































































## Lisans
Bu proje [MIT Lisansı](LICENSE) altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasını inceleyebilirsiniz.



