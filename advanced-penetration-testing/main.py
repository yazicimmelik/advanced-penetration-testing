import socket
import json

def find_subdomains(domain):
    """
    Alt alan adlarını keşfetme simülasyonu. Bu liste statik olarak tanımlanır ancak,
    gerçek senaryolarda API çağrıları veya dosya tarama yapılabilir.
    """
    subdomains = [
        f"www.{domain}",
        f"mail.{domain}",
        f"blog.{domain}"
    ]
    return subdomains

def resolve_ips(subdomains):
    """
    Alt alan adları için IP adreslerini bulur. 
    Eğer IP çözümlenemiyorsa, 'Çözümlenemedi' bilgisi döner.
    """
    resolved = []
    for subdomain in subdomains:
        try:
            ip_address = socket.gethostbyname(subdomain)
            resolved.append({"subdomain": subdomain, "ip_address": ip_address})
        except socket.gaierror:
            resolved.append({"subdomain": subdomain, "ip_address": "Çözümlenemedi"})
    return resolved

def main():
    # Kullanıcıdan domain girişi al
    domain = input("Lütfen bir domain girin (ör: example.com): ").strip()
    
    if not domain:
        print(json.dumps({
            "status": "error",
            "error_message": "Domain alanı boş bırakılamaz!"
        }, indent=4))
        return

    try:
        # Alt alan adlarını bul
        subdomains = find_subdomains(domain)
        # Alt alan adlarının IP adreslerini çöz
        resolved = resolve_ips(subdomains)
        
        # JSON çıktısı üret
        result = {
            "status": "success",
            "data": {
                "domain": domain,
                "subdomains": resolved
            }
        }
        print(json.dumps(result, indent=4, ensure_ascii=False))

    except Exception as e:
        # Hata durumunda JSON formatında döndür
        result = {
            "status": "error",
            "error_message": str(e)
        }
        print(json.dumps(result, indent=4, ensure_ascii=False))

if __name__ == "__main__":
    main()
