1. [Inventury](#inventury)
    - [Doklady inventur](#doklady-inventur)
    - [Detail dokladu inventury a jeho zpracování](#detail-inventury)
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


<h2 id=detail-inventury>Detal dokladu inventury - zpracování inventury</h2>
U každé inventury je potřeba po fyzickém sečtené ještě provést kontrolu a schválení všech inventárních dokladů. Jedna inventarizovaná lokace = jeden inventární doklad. Každý doklad je po jeho dokončení v aplikace ještě potřeba zkontrolovat a schválit nebo odmítnuot. 

Doklad, který je připravený ke zpracování po svém otevření vypadá takto

V horní části jsou tlačítka pro <span style="background-color: green; color:white">Schválit</span> celý doklad nebo <span style="background-color: red; color:white">Odmítnout</span> celý doklad. Použitím jednoho z těchto tlačítek provedu akci nad všemi řádky dokladu. Pokud jsem si jistý, že doklad je v pořádku. Tak přesně pro tuto chvíli tlačítka slouží. 

Pod nimi je tabulka s obecnými informacemi o dokladu. Kde vidím v jaké stavu doklad je, kdy to bylo provedeno, kdo to provedl a na jaké lokaci byl doklad vytvořený.

To nejdůležitější je spodní tabulka, kde jsou jednotlivé řádky, které mi říkají jestli byl na lokaci nalezen nějaký rozdíl nebo ne. A zároveň na otevřeném dokladu mám možnost říct, co se má stát s jednotlivými řádky. 

<a href="#inventury" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/inventury/inventury-radky.png')">
   <img src="/content/images/doklady/inventury/inventura_detail_dokladu.png" alt="Řádky inventárních dokladů" width="900" />
</a>

Zde se tedy zastavíme a popíšemé si jednotlivé sloupce této části dokladu. 
- první 4 sloupce identifikují produkt. Tedy jeho PN, SAP PN, název a Výr PN (pokud je známé). Zároveň slouží jako proklik na kartu produktu. 
- **Batch** zobrazuje šarži produktu na lokačním záznamu. (obvykle "prázdné", NEW, USED a nebo nějaká číselná šarže)
  <span style="color: orange;">⚠️</span> pokud by produk byl na lokaci ve více šaržích, je pro každou šarži vlastní lokační záznam. 
- **Nalezeno** zobrazuje poček kusů, které zadal pracovník do aplikace pry fyzickém počítání
- **SN** - tbd
- **Očekáváno** zobrazuje počet kusů, které původně systém na lokaci očekával
- **Rozdíl** zobrazuje rozdíl mezi tím co bylo napočítáno a tím co původně systém očekával
- **Aktuální** zobrazuje počet kusů, které jsou na lokaci v tuto chvíli, kdy si prohlížím doklad. Obvykle bude stejný. Ale pokud by například mezi zpracování inventury a prohlížením dokladu došlo k nějakým pohybům. Pick nebo třeba schválení jiné inventury. Bude počet odlišný a může mi napovědět například to, jestli náhodou nebyla na lokaci provedena inventura 2x atp.
- **Opraveno** zobrazuje počet kusů, který bude na lokaci po schválení dokladu/řádku. <span style="color: red;">❗</span> pokud bude tento sloupec ukazovat zápornou hodnotu, nepůjde tento řádek schválit. Protože nelze mít záporný stav na lokaci. V takovém případě je vždy nutné nejdříve odmítnout tento řádek a pak teprve schválit doklad (bez této diference). Může to být důvod proč schválení celého dokladu končí chybou. Zároveň to může indikovat, že inventura nebyla provedena korektně nebo byla provedena duplicitní inventura. A admin by měl lokaci raději znovu přepočítat nebo nechat přepočítat. 
- **Akce** - umožňuje schválit nebo odmítnout konkrétní řádek. 

Jednotlivé řádky jsou pak také barevně odlišené pro rychlejší orientaci. Nulové diference jsou bez podbarvení. V případě kladné diference jsou podbarvené <span style="background-color: rgb(241, 174, 87); color:black">žlutě</span>. A záporné diference jsou podbarvené <span style="background-color: rgb(243, 101, 101); color:black">červně</span>

V případě, že otevřu doklad, který ještě nebyl v aplikaci dokončený bude horní část vypadat takto. Tlačítkem <span style="background-color: rgb(240, 217, 11); color:black">Dokončit doklad</span> mohu doklad dokončit. Ale měl bych to udělat jen v případě, kdy jsem si jistý, že už na něm pracovník nepracuje. V opačném případě mu spadne zpracování a bude potřeba inventuru udělat znova. 
<a href="#inventury" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/inventury/inventury-radky.png')">
   <img src="/content/images/doklady/inventury/inventura_rozpracovany_doklad.png" alt="Řádky inventárních dokladů" width="900" />
</a>

<h4>Scénář klasická inventura</h4>
Pokud schvaluji klasickou inventuru, obvykle schvaluji celé doklady a neřeším jednotlivé diference. I tak bych ale před samotným schválením měl na dokladu zkontrolovat, zda tam není záporný stav po opravě <span style="color: orange;">⚠️</span> v takovém případě stejně schválení skončí chybou <span style="color: orange;">⚠️</span>. V případě, že dělám inventuru při uzavřeném skladu, bych také měl zkontrolovat zda sloupce **Očekáváno** a **Aktuální** jsou stejné a zda náhodou nemám duplicitní doklad, který mi pracovník provádějící inventuru zapomněl nahlásit. 

<h4>Scénář opravy lokace<h4>
Pokud dělám inventuru z důvodu, že potřebuji upravit konkértní produkt (dohledaná diference, oprava šarže nebo účetního skladu atp...) je možné aplikací provést inventuru jen konkrétního produktu. 
Při schvalování pak najdu tento konkrétní řádek, který přijmu. Celý doklad pak ale odmítnu, protože ostatní neinventarizované produkty na lokaci budou mít záporné diference. 



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