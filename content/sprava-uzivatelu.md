# Správa uživatelů

## Obsah sekce

1. [Přehled správy uživatelů](#sprava-uzivatelu-prehled)
2. [Detail Uživatele](#detail-uzivatele)
  - [Obecné vlastnosti](#obecne-vlastnosti)
  - [Seznam skupin](#seznam-skupin)
  - [Přehled přiřazených práv](#prehled-prirarenych-prav)
3. [Detail Skupiny](#detail-skupiny)
  - [Obecné vlastnosti skupiny](#obecne-vlastnosti-skupiny)
  - [Práva přiřazená k roli](#prava-prirazena-k-roli)
  - [Členové skupiny](#clenove-skupiny)
  - [Skupiny](#skupiny)
  - [Přiřazená práva](#prirazena-prava)
  - [Popis práv](#Popis-prav)

<h2 id="sprava-uzivatelu-prehled">Přehled správy uživatelů</h2>

`http://10.10.30.4:8080/modules/users/`

<a href="" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/sprava-uzivatelu/seznam-uzivatelu.png')">
   <img src="/content/images/sprava-uzivatelu/seznam-uzivatelu.png" alt="Seznam uživatelů" width="900" />
</a>

Správa probíhá v tomto modulu. Vytváří se zde jak noví uživatelé, tak nové skupiny uživatelů. Zde vidíme jak tabulku se seznamem uživatelů, tak pro skupiny. Kdy kliknutím na položku lze daný řádek dále editovat.

Skupiny uživatelů se tvoří pro jednodušší přiřazování oprávnění. Logika oprávnění probíhá tak, že jednotlivá oprávnění se přidávají skupinám a do skupin se pak přiřazují uživatelé.

<h2 id="detail-uzivatele">Detail Uživatele</h2>

<a href="" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/sprava-uzivatelu/detail-uzivatele.png')">
   <img src="/content/images/sprava-uzivatelu/detail-uzivatele.png" alt="Detail uživatele" width="900" />
</a>


<h3 id="obecne-vlastnosti">Obecné vlastnosti</h3>

Zde je zobrazen název uživatele, uživatelské jméno a stav uživatele (aktivní/neaktivní).
- **Název:** Zpravidla zobrazuje celé jméno uživatele (v tomto případě "František Sirůček").
- **Uživatelské jméno:** Unikátní identifikátor uživatele (zde "fsirucek").
- **Aktivní:** Checkbox určuje, zda je účet aktivní.
- **Upravit:** Tlačítko pro úpravu uživatelských údajů.

<a href="" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/sprava-uzivatelu/editace-uzivatele.png')">
   <img src="/content/images/sprava-uzivatelu/editace-uzivatele.png" alt="Úprava uživatele" width="900" />
</a>

<h3 id="seznam-skupin">Seznam skupin</h3>

Pod Obecné vlastnosti se nachází seznam skupin ve kterých je uživatel přidaný:
- **Název:** Název skupiny (zde "Administrators").
- **Description:** Popis skupiny (není vyplněn).
- **Active:** Checkbox indikující, zda je skupina aktivní.
- **Odstranit:** Tlačítko pro odstranění uživatele ze skupiny.
- **Add group to role:** Možnost přiřazení uživatele do nové skupiny zadáním jejího názvu (např. "sklad") a kliknutím na tlačítko Přidat.

<h3 id="prehled-prirarenych-prav">Přehled přiřazených práv</h3>

Na levé straně okna se nachází přehledy přiřazených práv.

**Přímá práva uživatele:**  
Vrchní tabulka jsou práva, která jsou přiřazena napřímo tomuto uživateli. A je možnost tady takto na přímo přidat další právo. Přiřazení práva tímto způsobem tedy neovlivní žádného dalšího uživatele. A hodí se to v situacích, kde je potřeba něco řízené otestovat nebo je potřeba mít jednoho uživatele se specifickým oprávněním. V tomto použití systému je Role a Uživatel jedna entita.
- **Kód:** Kód přiřazeného oprávnění (zde "ADMIN").
- **Přidat oprávnění:** Dropdown pro výběr dalšího oprávnění (např. "CONTAINERS - Správa příjmů").
- **Přidat:** Tlačítko pro přidání zvoleného oprávnění.

**Práva uživatele dle skupin:**  
Ve spodní tabulce jsou pak vidět všechna práva, které daný uživatel má. A to rozdělené tak aby bylo vidět, na základě jaké skupiny:
- **Typ:** Určuje, zda se jedná o roli přiřazenou přímo uživateli nebo skupině.
- **Název role:** Název role nebo skupiny, ke které se oprávnění váže.
- **Název:** Jméno uživatele nebo skupiny.
- **Kód a Popis:** Zobrazuje kód a popis přiřazeného oprávnění (např. "ADMIN – Administrátor - obchází všechna práva").

<h2 id="detail-skupiny">Detail Skupiny</h2>

<a href="" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/sprava-uzivatelu/detail-skupiny.png')">
   <img src="/content/images/sprava-uzivatelu/detail-skupiny.png" alt="Detail skupiny" width="900" />
</a>

Tato obrazovka zobrazuje správu skupiny "Administrators" ve webové aplikaci pro správu uživatelských oprávnění. Slouží k zobrazení detailů o skupině, správě jejích členů a přiřazení oprávnění.

<h3 id="obecne-vlastnosti-skupiny">1. Obecné vlastnosti</h3>

Zde jsou zobrazeny informace o skupině:
- **Název:** Název skupiny (zde "Administrators").
- **Popis:** Popis skupiny (není uveden).
- **Aktivní:** Checkbox označuje, zda je skupina aktivní.
- **Upravit:** Tlačítko pro úpravu základních informací o skupině. Upravovat lze jen popis skupiny a nebo ji deaktivovat

<a href="" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/sprava-uzivatelu/editace-skupiny.png')">
   <img src="/content/images/sprava-uzivatelu/editace-skupiny.png" alt="Úprava skupiny" width="900" />
</a>

Lze změnit jméno a popis skupiny a zadané hodnoty se uloží tlačítkem OK. Zrušení zadávání se provede tlačítkem zpět ve webovém prohlížeči.

<h3 id="prava-prirazena-k-roli">2. Práva přiřazená k roli</h3>

V této sekci lze přiřazovat oprávnění roli (skupině) a zobrazovat již přiřazená oprávnění:
- **Kód:** Zobrazuje kód oprávnění, které je aktuálně přiřazeno skupině (zde "ADMIN").
- **Odstranit:** Tlačítko pro odebrání přiřazeného oprávnění.
- **Přidat oprávnění:** Dropdown, ve kterém lze vybrat další oprávnění k přiřazení (např. "CONTAINERS - Správa příjmů").
- **Přidat:** Tlačítko pro přidání zvoleného oprávnění.

<h3 id="clenove-skupiny">3. Členové skupiny</h3>

Zobrazuje seznam uživatelů, kteří jsou členy této skupiny, spolu s možností jejich odstranění:
- **Typ:** Označuje, že se jedná o uživatele.
- **Název role:** Uživatelské jméno člena skupiny.
- **Název:** Celé jméno člena skupiny.
- **Odstranit:** Tlačítko pro odstranění uživatele ze skupiny.

**Přidání nového člena skupiny:**
- Vstupní pole umožňuje zadat uživatelské jméno dalšího uživatele, který má být přidán do skupiny (např. "jdradzansky").
- Přidat: Tlačítko pro přidání vybraného uživatele do skupiny.

<h3 id="skupiny">4. Skupiny</h3>

Zobrazuje seznam skupin, do kterých tato skupina může být přidána, včetně možnosti odstranit skupiny. Systém umožňuje vkládání skupin do skupiny. V praxi provozu výstavby toto nedoporučuji.

- **Název:** Název skupiny.
- **Popis:** Popis skupiny (není uveden).
- **Aktivní:** Checkbox označuje, zda je skupina aktivní.
- **Odstranit:** Tlačítko pro odstranění skupiny.

**Přidání nové skupiny:**
- Vstupní pole umožňuje zadat název nové skupiny, do které má být přidána skupina "Administrators" (např. "sklad").
- Přidat: Tlačítko pro přidání skupiny.

<h3 id="prirazena-prava">5. Přiřazená práva</h3>

Seznam všech oprávnění, která jsou přiřazena této skupině:
- **Typ:** Označuje, že se jedná o skupinu.
- **Název role:** Název skupiny (zde "Administrators").
- **Kód a Popis:** Kód a popis přiřazeného oprávnění (zde "ADMIN – Administrátor - obchází všechna práva").

**Funkčnost:**  
Tato obrazovka umožňuje správu členů skupiny a jejich oprávnění. Administrátoři mohou přidávat nebo odebírat členy skupiny a také spravovat oprávnění, která jsou této skupině přidělena. Skupiny mohou být také vkládány do jiných skupin, což umožňuje flexibilní správu přístupových práv.

<h3 id="Popis-prav">5. Popis práv</h3>

Seznam všech oprávnění:
<h4 id="Popis-wms">Popis práv ve WMS</h4>

- **ADMIN** : Udělí práva univerzálně na cokoliv
- **USERS_AND_ROLES** : právo na modul Uživatelé a role a jejich administraci
- **CONTAINERS** : práva na modul kontejnery a jejich prohlížení
- **CUSTOMERS** : práva na modul a správu zákazníků
- **GOODS_RECEIPT** : práva na modul Příjmy a import příjemky ze SAP
- **GOODS_RECEIPT_CREATE** : právo vytvořit interní příjemku
- **GOODS_RECEIPT_MISMATCH** : chybné doklady prohlížení
- **INVENTORY_CHECK** : práva na inventurní modul a schvalování dokladů
- **location_types** : práva na modul typy lokací a jejich správu
- **locations** : práva na modul lokace a jejich správu
- **MATERIALS** : právo na modul materiály, detail materiálu a jejich editaci
- **MATERIALS_ITEM_CHANGE_WAREHOUSE** : právo na tvrdou změnu účetního skladu SN/UID v rámci WMS, nefunguje bez předchozího práva na správu materiálů
- **ORDERS** : právo na modul Objednávky, detail objednávky, import ze SAP, aktivaci
- **ORDERS_CREATE** : právo na vytvoření interní obejednávky
- **ORDERS_CREATE_TRANSFER** : právo na vytvoření dokladu na dvoukrokové přeskladnění
- **ORDERS_DELIVERY2_REFRESH** : právo na refresh Delivery
- **ORDERS_EXPORT** : právo na ruční export do SAP, pozor je nutné mít také právo na detail jobu **STORE_JOBS**
- **PLANTS** : právo na moful Plants, fyzické sklady, a jejich editaci
- **REPLENISH** : právo na modul Replenish a vytváření replenishů
- **SAP_DOCUMENTS** : právo na modul SAP dokumenty
- **SAP_ERRORS** : právo na modul Chyby
- **STOCK_STATE** : právo na modul Stav zásob
- **STORE_JOBS** : právo na prohlížení modulu skladové joby a detail skladového jobu
- **STORE_JOBS_CANCEL** : právo na stornování jobu
- **WAREHOUSES** : právo na modul Účetní sklady a jejich správu
- **ZONES** : právo na modul Zóny a jejich správu

<h4 id="Popis-apky">Popis práv na Aplikace</h4>

- **MT_CABLE_CUTTING** : aplikace na stříhání kabelů
- **MT_GOODS_ISSUE** : aplikace na výdej (vyskladněných Order/Delivery)
- **MT_GOODS_RECEIPT** : aplikace na příjem zboží a inventuru SN
- **MT_INVENTORY_CHECK** : aplikace na inventury
- **MT_MULTI_PICK** : aplikace na výdej pomocí multipicku
- **MT_PACKAGING** : aplikace balení / třízení
- **MT_PICK** : aplikace na pickování / vyskladnění
- **MT_PICK_SKIP_SCAN** : umožňuje volbu, že se nebude číst čárový kód u pickování
- **MT_RESTORAGE** : aplikace přeskladnění mezi lokacemi
- **MT_RESTORAGE_SAP** : aplikace přeskladnění mezi účetními sklady - jednokrokové přeskladnění i do SAP
- **MT_STORE_ON_LOCATION** : aplikace potvrzování
- **MT_REPLENISH** : aplikace na zpracování replensihů
- **MT_REPLENISH_SKIP_SCAN** : umožňuje volbu, že se nebude číst čárový kód u pickování replenishů
- **MT_UNIQUE_ITEM_ID** : přířazení/změna UID na materiálu
- **MT_BARCODE_INFO** : právo na aplikaci BarcodeInfo
- **MT_DEBUG_BARCODE_DECODER** : rozklíčování barcode (debug apka)
- **MT_TERMINAL_DEBUG** : debugovací apka 

