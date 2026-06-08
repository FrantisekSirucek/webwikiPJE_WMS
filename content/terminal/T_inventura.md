<h1 id="main"> Postup pro inventarizaci zásob </h1>

1. [Kusová inventura](#inventura)
1. [Inventura seriových čísel](#inventuraSN)


Aplikace pro inventury slouží primárně k inventarizaci zásob po lokacích. Proces obou inventur je shodný. Uživatel přijde k lokaci, kterou chce inventarizovat a načte její kód. Následně oscanuje a sečte počty všech produktů na lokaci a potvrdí. Tím vytvoří inventurní doklad, který je potřeba následně schválit v modulu [Inventury](#/inventury). 
Dokud nedojde ke schválení inventury, tak opakované načtení lokace bude pořád ukazovat původní stavy produktů.
Rozdíl mezi kusovou inventurou a inventurou sériových čísel je, že při druhé zmiňované budu sečtení serializovaných produktů provádět pomocí scanování jejich SN/UID. Jde o delší proces, který je určen zejména pro velké roční inventury, kde se pak scan SN exportuje a porovnává se systémem SAP. 

<span style="color: #0d6efd;">ℹ️</span>  To ze využít například, pokud jsem udělal inventuru špatně a chci ji předělat ale v takovém případě musím <span style="color: red;">❗</span> nahlásit vedoucím, který doklad nemá schvalovat <span style="color: red;">❗</span>

<span style="color: #0d6efd;">ℹ️</span> Inventura (zejména kusová) lze také využívat k cílené opravě stavu zásob. Lze tak změnit účetní sklad zboží na lokaci nebo šarže. Vždy je ale potřeba nejdříve daný produkt inventárně vydat - tedy udělat inventuru na 0ks a schválit ji. Následně pak udělat inventuru znovu, kde se zadá správný sklad a šarže produktu.
<span style="color: orange;">⚠️</span> Pokud chci opravit jen jeden produkt a nalokaci je produktů více, musím si dát pozor na to co schvaluji. V takovém případě bych měl buď u ostatních produktů zadat při obou inventurách počet ks bez diferencí. Nebo na detailu dokladu nejprve schválím jen řádek s produktem. A následně celý doklad (tedy ostatní neschválené řádky) dám <span style="color: red;">❗</span> <span style="background-color: red; color:black">Odmítnout</span>


<h2 id="inventura">Kusová inventura</h2>

Kusovou inventuru otevřeme pomocí dlaždice Inventury
<a href="#terminal/T_inventura" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Inventura/inventura_dlazdice.png" alt="Inventura" width="900" />
</a>

Po spuštění aplikace se zobrazí obrazovka, která nás vyzve k načtení lokace, kde chceme inventuru provést. 
<a href="#terminal/T_inventura" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Inventura/inventura_lokace.png" alt="Inventura" width="900" />
</a>

Po načtení lokace se zobrazí seznam produktů, které jsou na lokaci. Vidíme zde název materiálu, SAP PN, Batch, Účetní sklad, Q = počet kusů, které jsme již spočítali, E - očekáváný stav, který by měl na lokaci být. Sečtení konkétního produktu provede jeho scanem nebo výběrem přímo na obrazovce. 
<a href="#terminal/T_inventura" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Inventura/inventura_obsah_lokace.png" alt="Inventura" width="900" />
</a>

Pro příklad jsem oscanoval produkt 40350255. Tím se otevře obrazovka, kam zadám počet kusů, které jsem napočítal. 
<a href="#terminal/T_inventura" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Inventura/inventura_pocet.png" alt="Inventura" width="900" />
</a>

Po zadání počtu kusů a potvrzením klikem na OK se vrátíme zpět na obsah lokace, ale zde již vidíme, že ve sloupci Q je počet 156ks a tedy, že zadání bylo úspěšné, zároveň na materiálu není rozdíl. <span style="color: red;">❗</span> Pozor při opakovném zadání, se nově zadaný počet ks přičtě. Je to tak nastavené z důvodu, že máme na skladě spoustu hodně namixovaných lokací a často není možné napočítat materiál na poprvé. Můžu tedy nejdříve zadat například 100ks a pak 56ks. I v takovém případě nakonec budu mít v napočítaném množství 156ks
<a href="#terminal/T_inventura" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Inventura/inventura_obsah_lokace2.png" alt="Inventura" width="900" />
</a>

Tímto způsobem pokračuji, dokud nemám spočítané všechny produkty na lokaci. Ve chvíli kdy, jsem hotový tak stisknu tlačítko <span style="background-color: green; color:white">Hotovo</span>. Tím inventuru ukončím a Inventární doklad bude připraven ke schválení. [Inventury](#/inventury)

<span style="color: #0d6efd;">ℹ️</span> Zároveň ale můžu narazit na případ, kdy je fyzicky na lokaci produkt, který aplikace na lokaci nezobrazuje. V takovém případě je potřeba produkt na lokaci přidat. To provedu tak, že na obrazovce s obsahem lokace tento produkt načtu. A zobrazí se mi obrazovka přidání nového produktu na lokaci. Zde je potřeba vyplnit batch(šarži), může zůstat i prázdné. A účetní sklad na který produkt patří. Účetní sklady jsou na výběr po rozkliknutí a jen pro sklady, které jsou na dané lokaci povoleny.

<a href="#terminal/T_inventura" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Inventura/inventura_pridat_produkt.png" alt="Inventura" width="900" />
</a>

Poté již následuje standartní zadání počtu kusů a materiál se objeví na obsahu lokace. Poznáme ho tak, že v Q je počet, který jsme zadali a v E je 0 (protože nebyl očekáván)

<a href="#terminal/T_inventura" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Inventura/inventura_obsah_lokace3.png" alt="Inventura" width="900" />
</a>

<span style="color: #0d6efd;">ℹ️</span> Je také možné, že se při zadávání počtu ks přepočítám nebo přepíši. Jako se stalo zde, kdy místo 59ks jsem zadal 159ks. 

<a href="#terminal/T_inventura" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Inventura/inventura_spatny_pocet.png" alt="Inventura" width="900" />
</a>

Zde mohu využít toho, že pole pro počet kusů každé nové zadání přičte k původnímu. A zároveň mi povolí zadat záporné množství. Zadám tedy -100ks. 

<a href="#terminal/T_inventura" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Inventura/inventura_zaporny_pocet.png" alt="Inventura" width="900" />
</a>

A po potvrzení už uvidím, že celkový počet klesl o 100ks a již ukazuje správně 56ks. 

<a href="#terminal/T_inventura" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Inventura/inventura_opraveny_pocet.png" alt="Inventura" width="900" />
</a>



---
[Zpět na začátek](#main)

---

<h2 id="inventuraSN">Inventura seriových čísel</h2>
Proces inventury SN od předchozího se odlišuje pouze u materiálů, které evidujeme pomocí seriových čísel nebo UID. V případě, že v aplikaci Inventura SN narazím na produkt, který není serializovaný, tak je proces uplně stejný jeko obyčejná inventura. 
Proces u serializovaných produktů je popsán níže. Aplikace akceptuje načtení jak Manufacturer SN, tak CZUID tak GENUID (V SAPu stejné pole UID) pro účely WMS říkám CZUID přiřazenému UID, které začíná CZTM a GENUID (temporary UIID) je to UID co si SAP generuje složenín CZUI+ManSN+SAPPN

Inventuru SN otevřeme pomocí dlaždice Inventury SB
<a href="#terminal/T_inventura" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/Inventura_SN_dlazdice.png')">
    <img src="/content/terminal/images/Inventura/inventura_SN_dlazdice.png" alt="InventuraSN" width="900" />
</a>

Po spuštění aplikace se zobrazí obrazovka, která nás vyzve k načtení lokace, kde chceme inventuru provést. 
<a href="#terminal/T_inventura" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Inventura/inventura_lokace.png" alt="Inventura" width="900" />
</a>

Po načtení lokace se zobrazí seznam produktů, které jsou na lokaci. Vidíme zde název materiálu, SAP PN, Batch, Účetní sklad, Q = počet kusů, které jsme již spočítali, E - očekáváný stav, který by měl na lokaci být. Sečtení konkétního produktu provede jeho scanem nebo výběrem přímo na obrazovce. A účetní sklady, které na lokaci patří. Načteme tedy materiál z lokace
<a href="#terminal/T_inventura" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/inventuraSN_obsah_lokace.png')">
    <img src="/content/terminal/images/Inventura/inventuraSN_obsah_lokace.png" alt="Inventura" width="900" />
</a>

Pokud je produkt na SN vyzve nás aplikace k načítání SN, které na lokaci jsou.
<a href="#terminal/T_inventura" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/inventuraSN_obsah_lokace.png')">
    <img src="/content/terminal/images/Inventura/inventuraSN_nactinSN.png" alt="Inventura" width="900" />
</a>

Po načtení správného SN, tedy toho co patří k materiálu dostaneme zelené potvrzení a můžeme pokračovat scanem dalšího kusu nebo se vrátit na obrazvku obsah lokace a přejít na další materiál
Pokud je produkt na SN vyzve nás aplikace k načítání SN, které na lokaci jsou.
<a href="#terminal/T_inventura" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/inventuraSN_obsah_lokace.png')">
    <img src="/content/terminal/images/Inventura/inventuraSN_nactinSN2.png" alt="Inventura" width="900" />
</a>

Tento proces se používá, pokud chci mít jistotu, že načítám jen SN počítaného kusu. Pokud bych načetl SN jiného produktu, čtečka mě zastaví. 

Alternativně lze použít rychlejíš proces. A to pokud je na lokaci více různých položek mohu načítat kus po kusu, bez ohledu na materiál. Tedy na obrazovce obsah lokace nebudu načítat PN materiálu ale rovnou SN ze všech kusů co najdu na lokaci. A každé načtené SN se přiřadí ke správnému materiálu a já na obrazovace sledují pouze jestli jsem dostal zelenou hlášku a jak se mnění počty u jednotlivých materiálů ve sloupci Q.

<span style="color: red;">❗</span> Pozor u zrychleného procesu, ManufacturerSN není v systému unikátní skrz materiály. Jedno stejné ManufacturerSN může být o více různých Materiálů. Z toho důvodu je doporučeno zrychlený proces načítání provádět pouze skrz UID, které je globálně unikatní <span style="color: red;">❗</span>

<a href="#terminal/T_inventura" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/inventuraSN_obsah_lokace.png')">
    <img src="/content/terminal/images/Inventura/inventuraSN_obsah_lokace2.png" alt="Inventura" width="900" />
</a>

Tímto způsobem pokračuji, dokud nemám spočítané všechny produkty na lokaci. Ve chvíli kdy, jsem hotový tak stisknu tlačítko <span style="background-color: green; color:white">Hotovo</span>. Tím inventuru ukončím a Inventární doklad bude připraven ke schválení. [Inventury](#/inventury)

<span style="color: #0d6efd;">ℹ️</span> Zároveň ale můžu narazit na případ, kdy je fyzicky na lokaci produkt, který aplikace na lokaci nezobrazuje. V takovém případě je potřeba produkt na lokaci přidat. To provedu tak, že na obrazovce s obsahem lokace tento produkt načtu. A zobrazí se mi obrazovka přidání nového produktu na lokaci. Zde je potřeba vyplnit batch(šarži), může zůstat i prázdné. A účetní sklad na který produkt patří. Účetní sklady jsou na výběr po rozkliknutí a jen pro sklady, které jsou na dané lokaci povoleny.

---
[Zpět na začátek](#main)

---


**To be done**