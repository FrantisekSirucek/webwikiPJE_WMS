import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import xml.etree.ElementTree as ET

# Funkce pro získání všech odkazů na stránce
def get_links(base_url):
    try:
        response = requests.get(base_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        links = set()
        
        for a_tag in soup.find_all('a', href=True):
            url = urljoin(base_url, a_tag['href'])
            if base_url in url:
                links.add(url)
        return links
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {base_url}: {e}")
        return set()

# Vytvoření XML sitemap
def create_sitemap(base_url, urls):
    urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    
    for url in urls:
        url_elem = ET.SubElement(urlset, "url")
        loc_elem = ET.SubElement(url_elem, "loc")
        loc_elem.text = url
        changefreq_elem = ET.SubElement(url_elem, "changefreq")
        changefreq_elem.text = "daily"
        priority_elem = ET.SubElement(url_elem, "priority")
        priority_elem.text = "0.5"
    
    tree = ET.ElementTree(urlset)
    tree.write("sitemap.xml", encoding="utf-8", xml_declaration=True)
    print("Sitemap saved as sitemap.xml")

# Základní URL webu
base_url = "http://172.17.10.21:8080/"

# Získání všech odkazů
urls = get_links(base_url)

# Přidání základní URL do seznamu, pokud tam není
if base_url not in urls:
    urls.add(base_url)

# Vytvoření a uložení sitemap
create_sitemap(base_url, urls)
