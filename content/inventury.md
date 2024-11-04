1. [Inventury](#inventury)
    - [Doklady inventur](#doklady-inventur)
    - [Řádky inventárních dokladů](#radky-inventarnich-dokladu)
2. [Short picky](#short-picky)

<h2 id="inventury">Inventury</h2>

Inventura je klíčovým procesem pro ověření fyzického stavu skladových zásob a jejich porovnání se záznamy v systému. Ve skladu, který používá tento systém, probíhá inventura pomocí mobilního terminálu (čtečky). Skladník nascanuje lokace a poté materiály umístěné v těchto lokacích, přičemž zadá buď počet materiálů, nebo nascanuje všechna sériová čísla (SN) na dané lokaci. V případě, že systém zaznamená rozdíly mezi očekávaným a naskenovaným stavem (diference), je tato diference zaznamenána a poté projde schvalovacím procesem.

Po schválení diferencí je stav na lokaci aktualizován v systému a změny jsou zaúčtovány. Pokud je diference odmítnuta, nedojde k žádným úpravám zásob. Tento proces je důležitý pro udržení přesného přehledu o skladových zásobách a minimalizaci chyb v evidenci materiálů.

<h3 id="doklady-inventur">Doklady inventur</h3>

`http://10.10.30.4:8080/modules/documents/inventory-check/`

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/inventury/doklady-inventury.png')">
   <img src="/content/images/doklady/inventury/doklady-inventury.png" alt="Doklady inventur" width="900" />
</a>

Tato obrazovka poskytuje přehled o všech inventurních dokladech a jejich aktuálním stavu. Každý inventurní doklad odpovídá jedné lokaci, která byla inventarizována.

Jsou zde sloupce:
- **Kód:** Unikátní identifikátor inventurního dokladu.
- **Lokace:** Lokace, na které probíhá inventura.
- **Vytvořeno:** Datum a čas vytvoření inventurního dokladu, spolu s informací o uživateli, který inventuru provedl.
- **Dokončeno:** Datum a čas, kdy byla inventura dokončena.
- **Shoduje se:** Informace o tom, zda se inventura shoduje se systémovým stavem (zelená značka) nebo zda byly nalezeny diference (červená značka).
- **Přijato:** Datum a čas, kdy byl stav materiálů potvrzen.
- **Zamítnuto:** Datum a čas, kdy byla diference zamítnuta, pokud byla v průběhu inventury identifikována a následně neschválena.

<h3 id="radky-inventarnich-dokladu">Řádky inventárních dokladů</h3>

`http://10.10.30.4:8080/modules/documents/inventory-check/lines`

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/inventury/inventury-radky.png')">
   <img src="/content/images/doklady/inventury/inventury-radky.png" alt="Řádky inventárních dokladů" width="900" />
</a>

Tato obrazovka zobrazuje jednotlivé řádky inventurních dokladů, které odpovídají konkrétním materiálům na různých lokacích, jež byly zahrnuty do inventury. Každý řádek obsahuje detaily o výsledku inventury pro daný materiál.

Sloupce:
- **CheckLine:** Pořadové číslo řádky v rámci inventury.
- **Doklad:** Odkaz na inventurní doklad, který odpovídá dané lokaci.
- **Vytvořeno:** Datum a čas vytvoření inventurního dokladu.
- **P/N:** Part Number materiálu, který byl kontrolován.
- **Název:** Název materiálu.
- **Zák. P/N:** Zákaznický part number, pokud je k dispozici.
- **Nalezeno:** Počet kusů nalezených na dané lokaci při inventuře.
- **Očekáváno:** Počet kusů očekávaných podle systému WMS.
- **Rozdíl:** Rozdíl mezi nalezeným a očekávaným počtem kusů (pozitivní hodnota značí nadbytek, negativní nedostatek).
- **Aktuální:** Počet, který je aktuálně potvrzený nebo opravený po inventuře.
- **Opraveno:** Informace o tom, kolik jednotek bylo opraveno (pokud byl nalezen rozdíl, který byl následně opraven).

<h2 id="short-picky">Short picky</h2>

`http://10.10.30.4:8080/modules/documents/inventory-check/shortpick`

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/inventury/short-pick.png')">
   <img src="/content/images/doklady/inventury/short-pick.png" alt="Short picky" width="900" />
</a>

**Shortpick** je situace, která nastane, když skladník během pickování nenajde na lokaci očekávané množství zboží nebo zboží nenajde vůbec. V praxi to znamená, že když systém přiřadí skladníkovi úkol vychystat určité množství materiálu z konkrétní lokace, a skladník na této lokaci najde méně než požadované množství nebo nenajde žádné zboží, je to zaznamenáno jako shortpick.

Tento proces slouží k identifikaci nesouladu mezi evidovaným stavem zboží ve skladu a skutečným fyzickým stavem na dané lokaci. Shortpick může být způsoben různými důvody, jako je chybně zadaná inventura, špatně provedený přesun materiálu nebo jiné logistické problémy.

Tato obrazovka poskytuje přehled o všech lokacích, kde byl shortpick zjištěn. Slouží jako upozornění pro odpovědného pracovníka, který má za úkol zkontrolovat dané lokace, provést inventuru nebo najít chybějící zboží.

**Popis sloupců:**
- **Datum:** Zaznamenává čas, kdy byl shortpick proveden.
- **Lokace:** Odkaz na lokaci, kde byl shortpick zjištěn, kliknutím na tento odkaz lze přejít na detail lokace.
- **P/N:** Part Number materiálu, který byl z lokace vychystáván.
- **Název:** Název materiálu, který chyběl nebo byl nedostatečně nalezen.
- **Zák. P/N:** Zákaznický part number, pokud existuje.
- **Množství:** Počet kusů, které byly vychystány (v případě shortpicku je tento počet obvykle nižší než očekávané množství).