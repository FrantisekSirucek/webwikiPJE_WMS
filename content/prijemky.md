# Příjemky

## Obsah sekce

1. [Příjem](#prijem)
   - [Příjemky](#prijemky)
   - [Detail příjemky](#detail-prijemky)
    - [Přehled Řádky příjemky](#prehled-radky-prijemky)
    - [Přehled příjmových jobů](#prehled-prijmovych-jobu)
    - [Detail příjemky](#detail-prijemky-detail)
    - [Dokončená příjemka](#dokoncena-prijemka)
    - [Import příjemky ze SAP](#import-prijemky-ze-sap)
    - [Založení interní příjemky mimo SAP](#zalozeni-interni-prijemky-mimo-sap)
2. [Proces příjmu dokladu](#proces_dokladu_prijemka)
3. [Další informace a řešení problémů](#reseni-problemu)

<h2 id="prijem">Příjem</h2>

Příjem zboží je jedním z klíčových procesů skladového hospodářství. Při příjmu zboží do skladu je potřeba zajistit, aby veškeré doručené zboží bylo řádně evidováno a uloženo na správné lokace. Tento proces obvykle začíná vytvořením **příjemky**, která slouží jako doklad potvrzující přijetí zboží. Příjemka obsahuje informace o dodaném zboží, jeho množství, původu a datu přijetí. V našem provozu příjemky importujeme ze systému SAP pomocí čísla příjemky v tomto systému.

Příjemky vytvořené ve WMS využijeme pouze ve specifických případech jako testování, nebo korekce stavu po nějakém výpadku. Nebo na evidenci materiálu, který není v systému SAP.

**Hlavní kroky příjmu zboží:**

1. **Příjem zboží**: Fyzické převzetí zboží ve skladu. Ověřuje se množství a kvalita doručeného zboží.
2. **Vytvoření (import) příjemky**: Záznam přijatého zboží do systému, kde je každý příjem zboží evidován prostřednictvím příjemky.
3. **Kontrola a zaúčtování**: Srovnání údajů z příjemky s dodacím listem a následné zaúčtování příjmu.
4. **Uložení zboží**: Po zpracování příjemky je zboží uloženo na specifické lokace ve skladu.

Příjemka tak hraje zásadní roli při evidenci skladových zásob, sledování toku materiálů a zajišťuje správný přehled o zásobách ve skladu.

<h3 id="prijemky">Doklady (Příjemky)</h3>

`http://10.10.30.4:8080/modules/documents/goods-receipt/index`

<a href="" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/images/doklady/prijemky/doklady-prijemky.png" alt="Příjem" width="900" />
</a>


Na této obrazovce je zobrazen seznam všech příjmových dokladů (příjemek), které byly vytvořeny v systému.

Sloupce:
- **Kód:** Unikátní identifikátor příjemky (např. "PZ00001774"). Po kliknutí na kód příjemky se zobrazí detailní informace o daném příjmu. S proklikem [na detail příjemky](#detail-prijemky)
- **Externí číslo:** Externí referenční číslo přijatého zboží, které může pocházet z dodacího listu nebo jiného systému. S proklikem [na detail příjemky](#detail-prijemky)
- **Vytvořeno:** Datum a čas, kdy byla příjemka vytvořena v systému.
- **Dokončeno:** Datum a čas, kdy byl proces příjmu dokončen.

Funkce:
1. Importovat ze SAPu: Tlačítko pro import příjmových dokladů ze systému SAP.
2. Vyrobit: [Tlačítko pro manuální vytvoření nové příjemky](#zalozeni-interni-prijemky-mimo-sap).
3. Ouška:
  a. Doklady, Řádky, Joby: Přepínání mezi různými částmi procesu příjmu (doklady, řádky a jednotlivé úkoly spojené s příjmem).

<h3 id="prehled-radky-prijemky">Přehled Řádky příjemky</h3>

`http://10.10.30.4:8080/modules/documents/goods-receipt/lines`

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/radky-prijemky.png')">
   <img src="/content/images/doklady/prijemky/radky-prijemky.png" alt="Řádky příjemky" width="900" />
</a>

Tato obrazovka zobrazuje podrobný přehled jednotlivých řádků příjmových dokladů. Každý řádek reprezentuje konkrétní položku nebo materiál, který byl přijat do skladu.

Sloupce:
- **Kód:** Unikátní identifikátor příjemky v rámci systému WMS, ke které daný řádek patří.
- **Externí číslo:** Externí referenční číslo (SAP) vztahující se k příjemce nebo objednávce.
- **Účetní sklad:** Účetní sklad, do kterého je zboží přijímáno (např. "3007").
- **PN (Part Number):** Unikátní identifikátor materiálu (např. "1001512").
- **Název:** Popis materiálu (např. "WS-C3524-XL-EN").
- **Zák. PN:** Zákaznické číslo materiálu (SAP kod), pokud je relevantní.
- **Očekáváno:** Počet kusů nebo množství, které bylo očekáváno na příjem.
- **Obdrženo:** Skutečně přijaté množství zboží.
- **S/N (Sériové číslo):** Proklik na seznam přijatých SN na řádku příjemky.
- **SN?:** Zda se daná položka bude přijímat na SN.
- **UIID?:** Zda se daná položka bude přijímat na UIID.

Možnosti zobrazení:
Ve spodní části obrazovky je možné zvolit, kolik položek se zobrazí na jedné stránce (10, 50, 100).

<h3 id="prehled-prijmovych-jobu">Přehled příjmových jobů</h3>

`http://10.10.30.4:8080/modules/documents/goods-receipt/store-on-location`

<a href="" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/prijemky/prijem-joby-radky.png')">
   <img src="/content/images/doklady/prijemky/prijem-joby-radky.png" alt="Přehled příjmových jobů" width="900" />
</a>


Tato obrazovka zobrazuje přehled všech úkolů (jobů) spojených s příjmem zboží ve skladu. Každý **job** představuje konkrétní úkol nebo operaci, která byla vytvořena v rámci procesu příjmu a musí být splněna, aby byl příjem zboží dokončen.

Sloupce:
- **Kód:** Unikátní identifikátor jobu (např. "JS0000000048"). Kliknutím na kód lze zobrazit podrobné informace o jobu.
- **Objednávka:** Číslo objednávky, ke které se job vztahuje.
- **Externí číslo:** Externí referenční číslo objednávky, často zadané dodavatelem.
- **Vytvořeno:** Datum a čas vytvoření jobu v systému.
- **Přiřazeno:** Zobrazuje, zda byl úkol přiřazen ke konkrétní osobě nebo procesu.
- **Přiřazeno k:** Konkrétní osoba nebo oddělení, kterému byl job přiřazen.
- **Dokončeno:** Datum a čas, kdy byl job úspěšně dokončen.
- **Dokončil:** Jméno osoby, která úkol dokončila.
- **Zrušeno:** Datum a čas, kdy byl job zrušen, pokud k tomu došlo.
- **Zrušil:** Jméno osoby, která úkol zrušila.

<h3 id="detail-prijemky-detail">Detail příjemky</h3>

Příjemka, která se teprve bude zpracovávat:

<a href="" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/prijemky/prijemky-detail.png')">
    <img src="/content/images/doklady/prijemky/prijemky-detail.png" alt="Detail příjemky" width="900" />
</a>

Tato obrazovka zobrazuje detailní informace o příjmovém dokladu, který zatím nebyl plně zpracován. Příjemka čeká na přijetí zboží a její stav a další podrobnosti lze sledovat na této obrazovce.

Obecné vlastnosti:
- **Kód:** Unikátní identifikátor příjmového dokladu (např. "RZ00000375").
- **Externí kód:** Externí referenční číslo vztahující se k příjemce (není vyplněno, tedy "None").
- **Zdrojový systém:** Informace o systému, odkud byl příjemka importována (není uvedeno, "None").
- **Vytvořeno:** Datum a čas vytvoření příjemky v systému (např. "2024-10-14 16:21:08").
- **Vytvořil:** Uživatel, který příjemku vytvořil (např. "František Sirůček").
- **Aktivováno:** Stav aktivace příjemky (není zatím aktivováno).
- **Dokončeno:** Datum a čas, kdy byla příjemka dokončena (není vyplněno, příjem ještě neproběhl).
- **Zrušeno:** Pokud by byla příjemka zrušena, zde by se zobrazilo datum a čas zrušení.
- **Exportováno:** Indikace, zda byl doklad exportován do externího systému, u nás SAP.
- **Účetní sklad:** Sklad, do kterého má být zboží přijato (např. "3007").
- **Poznámka:** Případná poznámka k příjemce.

Řádky:
Zobrazuje jednotlivé položky spojené s příjmovým dokladem:
- **Účetní sklad:** Sklad, do kterého se daný materiál přijímá (např. "3007").
- **PN:** Unikátní identifikátor materiálu (např. "100614").
- **Název:** Popis materiálu (např. "AGF_E006C4XK2").
- **Zák. PN:** SAP PN.
- **Očekáváno:** Počet kusů, které jsou očekávány (např. "5").
- **Obdrženo:** Počet kusů, které byly skutečně přijaty (zatím 0, protože příjemka ještě není dokončena).
- **S/N:** Proklik na seznam SN přijatých na řádku dokladu
- **SN?:** Položka vyžaduje SN.
- **UIID?:** Položka vyžaduje UIID.


Skladové joby:
Zobrazuje úkoly spojené s příjmem tohoto materiálu:
- **Kód:** Unikátní identifikátor jobu (úkolu).
- **Vytvořeno:** Datum a čas vytvoření jobu.
- **Kontejner:** Kontejner, ve kterém je materiál přijímán (pokud je relevantní).
- **PN:** Unikátní identifikátor materiálu ve WMS.
- **Název:** Popis materiálu.
- **Zák. PN:** SAP PN.
- **Množství:** Počet kusů, které jsou v jobu řešeny.
- **Přiřazeno:** Osoba nebo oddělení, kterému je job přiřazen.
- **Dokončeno:** Datum a čas dokončení jobu (zatím nevyplněno, protože příjem ještě neproběhl).
- **Zrušeno:** Datum a čas zrušení jobu, pokud byl job zrušen.



<h3 id="dokoncena-prijemka">Dokončená příjemka</h3>

<a href="" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/prijemky/dokoncena-prijemka.png')">
   <img src="/content/images/doklady/prijemky/dokoncena-prijemka.png" alt="Dokončená příjemka" width="900" />
</a>

<a href="" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/prijemky/dokoncena-prijemka-2.png')">
   <img src="/content/images/doklady/prijemky/dokoncena-prijemka-2.png" alt="Dokončená příjemka detail" width="900" />
</a>

Rozdíly mezi dokončenou a nedokončenou příjemkou:

1. **Obecné vlastnosti**
- **Dokončeno:** U dokončené příjemky je vyplněn datum a čas, kdy byl proces příjmu zboží dokončen (např. "2024-10-03 19:09:37"). Tento údaj v předchozí nezpracované příjemce nebyl přítomen.
- **Dokončil:** Jméno uživatele, který příjemku dokončil (např. "Jana Kreckova"). V nezpracované příjemce nebyl tento údaj uveden.

2. **Řádky**
- **Obdrženo:** U dokončené příjemky je v poli "Obdrženo" zaznamenáno množství skutečně přijatého zboží (např. 5 kusů, 100 kusů, atd.). U nezpracované příjemky bylo toto pole prázdné nebo mělo hodnotu 0, což znamenalo, že zboží ještě nebylo přijato.

3. **Skladové joby**
U dokončené příjemky je zobrazen seznam skladových jobů, které byly zpracovány během procesu příjmu. Tyto joby ukazují, kdy a jak byl příjem realizován, včetně informací o kontejneru, množství a přidělených osobách. U nezpracované příjemky nebyly joby ještě vygenerovány, protože příjem nebyl dokončen.

<h3 id="import-prijemky-ze-sap">Import příjemky ze SAP</h3>

<a href="" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/prijemky/import-prijemky.png')">
   <img src="/content/images/doklady/prijemky/import-prijemky.png" alt="Import příjemky ze SAP" width="900" />
</a>

Zvolím typ zda importuji Příjem nového (Purchase order) nebo *(bude doplněno po dokončení Demontáží)*

Do ID zkopíruji všechna SAP ID příjemek, které chci importovat.

A kliknu na modré Import. Červené Zrušit mě naopak vrátí zpět na seznam příjemek a vše co jsem vyplnil bude nenávratně zahozeno.


<h3 id="zalozeni-interni-prijemky-mimo-sap">Založení interní příjemky mimo SAP</h3>

<a href="" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/prijemky/zalozeni-interni-prijemky.png')">
   <img src="/content/images/doklady/prijemky/zalozeni-interni-prijemky.png" alt="Založení interní příjemky" width="900" />
</a>

Tata obrazovka slouží k vytvoření nové interní WMS příjemky. **Tyto příjemky jsou určeny především k testovacím účelům nebo pro příjem materiálu, který se neeviduje v systému SAP. Interní WMS příjemky mohou obsahovat pouze jeden řádek, a jejich použití je omezeno na specifické situace.**

Pole pro vytvoření příjemky:
- **Warehouse (Sklad)**: Výběr skladu, do kterého bude materiál přijat (např. "2005 B2B voice oper").
- **Material (Materiál):** Pole pro zadání materiálu, který bude přijat.
- **Quantity (Množství):** Pole pro zadání množství přijímaného materiálu.

Tlačítka:
- **Vytvořit:** Tlačítko pro vytvoření nové interní příjemky.
- **Zrušit:** Tlačítko pro zrušení operace a návrat na předchozí obrazovku.

**Omezení a pravidla:**

Interní WMS příjemky by měly být používány výhradně pro příjem materiálu, který není evidován v SAP. Příjem materiálu, který je součástí systému SAP, pomocí této funkce je zakázán, protože by to vedlo k nekonzistenci dat mezi systémy WMS a SAP.

Interní příjemky jsou často využívány pro testování, zpracování neformálního příjmu materiálu nebo pro evidenci materiálu, který není součástí hlavního systému ERP. Případně k doskladnění materiálu, který je v SAP a nelze tedy do SAP přijmout opakovaně

> **Důležité upozornění:** Jakýkoliv pokus o přijetí materiálu, který je zároveň spravován v SAPu, způsobí závažné problémy s datovou konzistencí a správností skladových zásob mezi systémy!

---
<h2 id="proces_dokladu_prijemka">Proces příjmu v systému</h2>

1. Pomocí čísla dokladu si importuji příjemku
2. V Modulu Příjem se založí nový doklad RZ a Externím číslem = SAP číslo dokladu
3. Proces přijmu pak standartně probíhá přes aplikaci Příjem viz Čtečky -> Příjem <a href="#Terminal/T_Prijem">ZDE</a>
4. Pokud chci provést příjem pomocí lotfile. Tak kliknu na tlačítko <span style="color: #0dcaf0;">Importovat SN</span> a na další obrazovce vyberu soubor s SN a nahraju
   - ⚠️ soubor musí být ve správném formátu (xlsx), kdy první sloupec je záhlavý a sloupce jsou přesně  v pořadí 
      - Mat ID (Barcodes);SN;UIID;KS;MasterObal;SAP batch nr;Sarze cislena
   - nahrávání přes import také kontrolue správnost zadaných dat, jako masky SN, zda existuje Material ID atp a případně zobrazí chybu
5. V případě, že potřebuji vytisknout příjmový doklad, jdu od detailu příjemky a stisknu tlačítko 📝 **PDF** otevře se mi nová záložka s příjemkou a tu si mohu stáhnout nebo vytisknout
6. Pokud je doklad špatně zpracován, lze pomocí tlačítka <span style="background-color: red; color: white">Vrátit</span>
   - ❌ pouze ale pokud už nejsou potvrzené skladové joby na lokace. 
   - vrácením příjmu se zruší všechny dosud vytvořené skladové joby a odskladní SN v dokladu
7. V případě, že Příjemku nebudu vůbec zpracovávat tak aby nesvítila mezi nedokončenými přijmy tak použiji tlačítko <span style="background-color: red; color: white">Zrušit</span>

---

<h2 id="reseni-problemu">Další informace a Řešení Problémů</h2>

**Opakované přijímání na stejný již dokončený doklad**
Pokud se potřebuji vrátit k Příjemkce, kterou jsem již z WMS odeslal do SAP. Tak jediný správný způsobej je doklad znovu naimportovat

**Oprava nascanovaného SN** 
Pokud jsem načetl špatně SN z produktu, mohu ho ještě **před dokončením příjemky** změnit. A to přes detail dokladu.
1. Otevřu si detail příjemky, kde potřebuji změnit SN

obrazek

2. kliknu na text **SN** na příšlušném řádku materiálu

obrazek

3. Otevře se mi seznam všech přijatých SN. Najdu to které potřebuji opravit a kliknu na něj. Otevře se mi nové okno, kde mohu SN přepsat a uložit. Tím se SN změní a do SAP bude odesláno to opravené. 

obrazek

**Vrácení příjmu**
V případě velké chyby při přijmu lze doklad vrátit do původního stavu. Pomocí tlačítaka vrátit příjem se smažou všechna přijatá data a příjemka lze zpracovat znovu a správně. 
Vrátit příjem nelze, pokud už na dokladu došlo k potvrzení nějakého jobu. 

---
