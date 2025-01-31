# Objednávky

1. [Průběh procesu objednávek](#prubeh-procesu-objednavek)
2. [Dokumenty, řádky a joby](#dokumenty-radky-a-joby)
3. [Dokumenty](#dokumenty)
4. [Import objednávky](#import-objednavky)
5. [Aktivace objednávky](#aktivace-objednavky)
    - [Hromadná aktivace](#aktivace-objednavky)
    - [Aktivace jedné objednávky tlačítkem](#aktivace-objednavky)
6. [Vytvoření objednávky](#vytvoreni-objednavky)
7. [Řádky objednávky](#radky-objednavky)
8. [Detail objednávky](#detail-objednavky)
    - [Skladová výdejka](detail-objednavky)
    - [Tlačítka v detailu](detail-objednavky)
9. [Pick Joby](#pick-joby)
10. [Detail jobu](#detail-jobu)


<h2 id="objednavky">Objednávky</h2>

Ve skladu se proces objednávek řídí jasně definovanými postupy, které zahrnují příjem objednávek ze systému SAP, vychystávání (picking) zboží pomocí mobilních terminálů a zpětnou komunikaci vychystaného zboží zpět do SAPu.

<h3 id="prubeh-procesu-objednavek">Průběh procesu objednávek</h3>

**Import objednávek z SAPu:** Všechny objednávky jsou do systému WMS automaticky importovány ze systému SAP. Každá objednávka je reprezentována jako dokument. Každý dokument obsahuje řádky, přičemž každý řádek představuje jednu položku, která má být vychystána.

**Vychystávání zboží (picking):**

Ve skladu existují dvě hlavní metody vychystávání zboží:
- **Single pick** (Jednoobjednávkové vychystávání): Skladník vychystává zboží pro jednu objednávku najednou. Tento proces je vhodný pro objednávky, které jsou časově citlivé nebo specifické.
- **Multipick** (Vychystávání více objednávek najednou): Skladník vychystává zboží pro více objednávek současně. Tento proces optimalizuje cestu skladníka, který může vychystat zboží pro více objednávek při jedné návštěvě lokací ve skladu.

**Použití mobilního terminálu (čtečky):**
- Skladník obdrží seznam položek k vychystání, který se zobrazuje na jeho mobilním terminálu (čtečce). Systém ho provádí skladovými lokacemi, kde má vychystávat produkty.
- Skladník se přesouvá od jedné lokace k druhé a ověřuje produkty, které po něm chce systém vychystat, aby byla zajištěna správnost vychystaného zboží.
- Jakmile jsou všechny produkty vychystány, skladník je odloží do expedičního prostoru, kde je zboží připraveno k odeslání.

**Zpětná komunikace do SAPu:**
Po dokončení vychystání je stav objednávky odeslán zpět do SAPu, kde je aktualizována informace o tom, co bylo vychystáno a připraveno k expedici.

<h3 id="dokumenty-radky-a-joby">Dokumenty, řádky a joby</h3>

- **Dokument:** Každá objednávka je reprezentována jako dokument v systému WMS. Tento dokument obsahuje řádky s jednotlivými položkami objednávky.
- **Řádky dokumentu:** Každý řádek dokumentu reprezentuje jednu objednanou položku. Například objednávka s pěti různými produkty bude mít pět řádků.
- **Joby a joblines:** Každý dokument je přiřazen ke konkrétnímu systémovému jobu, který řídí celý proces vychystání. Každý řádek objednávky je pak přiřazen k jobline (řádka jobu), což umožňuje detailní sledování práce skladníka při vychystávání.

<h3 id="dokumenty">Dokumenty</h3>

`http://10.10.30.4:8080/modules/documents/orders/index`

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/objednavky/doklady-objednavky.png')">
   <img src="/content/images/doklady/objednavky/doklady-objednavky.png" alt="Dokumenty" width="900" />
</a>

Tato obrazovka poskytuje přehled všech dokumentů objednávek v systému WMS. Každý dokument představuje konkrétní objednávku, kterou je potřeba ve skladu zpracovat. Obrazovka zobrazuje důležité informace o jednotlivých dokumentech, včetně jejich stavu a průběhu zpracování.

Sloupce:
- **Kód:** Unikátní identifikátor dokumentu objednávky (např. "OZ000000014"). Kliknutím na tento kód se uživatel dostane k detailním informacím o objednávce.
- **Ext. číslo:** Externí číslo objednávky, které je přiřazeno v SAPu (např. "081321072670"). Toto číslo je často referenční číslo objednávky v ERP systému, a slouží k propojení mezi WMS a SAPem.
- **Vytvořeno:** Datum a čas, kdy byl dokument objednávky vytvořen v systému WMS.
- **Aktivováno:** Datum a čas, kdy byla objednávka aktivována pro vychystávání. Pokud je objednávka aktivní, skladníci mohou začít s vychystáváním zboží.
- **Poznámka:** Volné textové pole pro poznámky nebo dodatečné informace k objednávce.
- **Dokončeno:** Datum a čas, kdy byla objednávka plně zpracována a vychystána.
- **Aktivovatelné?:** Indikátor, zda lze objednávku aktivovat. Zobrazuje se buď jako červený křížek (nelze aktivovat), nebo zelený indikátor (lze aktivovat). Posuzuje se podle počtu kusů skladem.

**Funkce:**
- **Importovat ze SAPu:** Tlačítko pro manuální import nových objednávek ze SAPu.
- **Vytvořit:** Tlačítko pro manuální vytvoření nové objednávky přímo v systému WMS, pokud je to potřeba.
- **Aktivovat aktivovatelné objednávky:** Tlačítko pro hromadnou aktivaci všech objednávek, které jsou připraveny k aktivaci (objednávky, které mají zelený indikátor v kolonce „Aktivovatelné?").

**Funkčnost:**  
Tato obrazovka slouží k přehledné správě všech objednávek ve skladu. Uživatel zde může sledovat stav jednotlivých objednávek, ověřovat, kdy byly vytvořeny, zda jsou aktivní a zda již byly dokončeny.

Pomocí tlačítka Importovat ze SAPu lze načítat nové objednávky z ERP systému. Po dokončení vychystávání je stav objednávky zaslán zpět do SAPu.


<h3 id="import-objednavky">Import objednávky</h3>

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/objednavky/import-objednavky.png')">
   <img src="/content/images/doklady/objednavky/import-objednavky.png" alt="Import objednávky" width="900" />
</a>

Tato obrazovka slouží k manuálnímu importu objednávek ze systému SAP do systému WMS. Tento import zajišťuje, že objednávky z ERP systému (SAP) jsou k dispozici ve skladu pro další zpracování a vychystávání.

**Pole pro import objednávky:**
- **Typ:** Výběr typu objednávky, která bude importována. V tomto případě je zvolen typ CSOrder / Delivery (typ objednávky v SAPu). Importovat lze vždy jen jeden typ objednávek
- **ID:** Unikátní identifikátor objednávky ze SAPu, který je třeba zadat pro manuální import. Toto ID je číslo objednávky v SAPu. Lze zadat více objednávek, ale odpovídajícího typu
- **Poznámka:** Volitelné pole, kam uživatel může zapsat doplňující poznámky k importované objednávce.
- **Aktivovat:** Zaškrtávací pole, které umožňuje ihned po importu objednávku automaticky aktivovat pro vychystávání.

**Tlačítka:**
- **Importovat:** Tlačítko pro spuštění procesu importu objednávky ze SAPu do WMS.
- **Zrušit:** Tlačítko pro zrušení procesu a návrat na předchozí obrazovku bez provedení jakýchkoli změn.

**Funkčnost:**
Tato obrazovka slouží ke manuálnímu načtení objednávek ze SAPu do systému WMS, což je důležité pro případy, kdy je potřeba zadat objednávku do WMS rychle a mimo standardní automatizovaný proces.
Po importu lze objednávku okamžitě aktivovat pro vychystávání, pokud je zaškrtnuto pole Aktivovat.
Importované objednávky jsou následně zpracovány stejně jako ostatní objednávky a po vychystání je stav objednávky vrácen zpět do SAPu.


<h3 id="aktivace-objednavky">Aktivace objednávky</h3>

Aktivace se provádí dvěma způsoby. Tlačítkem „Aktivovat aktivovatelné objednávky" – to způsobí, že všechny objednávky, které mají zelenou fajfku ve sloupci „Aktivovatelné?" se aktivují. Aktivací se k dokumentům vygenerují skladové joby.

**Hromadná aktivace**

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/objednavky/hromadna-aktivace.png')">
   <img src="/content/images/doklady/objednavky/hromadna-aktivace.png" alt="Hromadná aktivace" width="900" />
</a>

Tato obrazovka zobrazuje dialog pro **aktivaci objednávek**, které jsou připraveny k vychystávání ve skladu. Aktivací objednávky se umožní skladníkům začít s jejím vychystáváním na základě pokynů zadaných systémem.

Pole pro aktivaci objednávek:
- **Priorita:** Pole pro zadání priority objednávky. Čím vyšší číslo, tím vyšší prioritu bude mít objednávka při zpracování. Standardně je nastaveno na "0", což je neutrální priorita. Omezení pole je celé kladné číslo.
- **Počet:** Počet objednávek, které mají být aktivovány. Toto pole umožňuje zvolit, kolik objednávek se má současně aktivovat (např. 10).
- **Poznámka:** Volitelné pole pro vložení poznámky, která se vztahuje k procesu aktivace. Může být použito pro interní poznámky nebo komunikaci mezi pracovníky skladu.

Tlačítka:
-	**Aktivovat:** Tlačítko pro spuštění procesu aktivace objednávek. Po kliknutí na toto tlačítko systém aktivuje zadaný počet objednávek a připraví je k vychystávání.
-	**Zrušit:** Tlačítko pro zrušení akce a návrat na předchozí obrazovku bez provedení změn.

**Funkčnost:**
Aktivace objednávek je klíčovým krokem před zahájením vychystávacího procesu. Jakmile jsou objednávky aktivovány, skladníci mohou začít s jejich zpracováním pomocí mobilních terminálů.
Pole Priorita umožňuje správu důležitosti jednotlivých objednávek, což je užitečné pro řízení provozu ve skladu, kde některé objednávky mohou mít vyšší prioritu z důvodu termínů expedice nebo zákaznických požadavků.
Po aktivaci jsou objednávky připraveny k vychystání, což znamená, že systém začne skladníkům přiřazovat konkrétní úkoly související s vychystáním produktů.

**Aktivace jedné objednávky tlačítkem**

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/objednavky/aktivace-tlacitkem.png')">
   <img src="/content/images/doklady/objednavky/aktivace-tlacitkem.png" alt="Vytvoření objednávky" width="900" />
</a>

Na detailu objednávky stisknu tlačítko aktivovat

<h3 id="vytvoreni-objednavky">Vytvoření objednávky</h3>

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/objednavky/vytvoreni-interni-objednavky.png')">
   <img src="/content/images/doklady/objednavky/vytvoreni-interni-objednavky.png" alt="Vytvoření objednávky" width="900" />
</a>

Tato obrazovka slouží k manuálnímu vytvoření objednávky přímo v systému WMS. Funkce manuálního vytváření objednávek by měla být použita pouze ve specifických případech, například pro testovací účely nebo pro výdej materiálu, který není evidován v systému SAP.

**Pole pro vytvoření objednávky:**
- **Warehouse (Sklad):** Výběr skladu, ze kterého bude materiál vydáván. Uživatel může zvolit příslušný sklad z dostupné nabídky (např. "3007 RN výstavba").
- **Material (Materiál):** Pole pro zadání konkrétního materiálu, který má být vydán. Materiál je zadáván pomocí unikátního čísla (např. "000000000004975631").
- **Quantity (Množství):** Počet kusů daného materiálu, který bude zahrnut v objednávce.
- **Note (Poznámka):** Volitelné pole, kam lze zadat dodatečné informace nebo poznámky (např. "testovací").

**Tlačítka:**
- **Vytvořit:** Tlačítko, které spustí proces vytvoření objednávky.
- **Zrušit:** Tlačítko, které slouží k přerušení procesu a návratu na předchozí obrazovku bez uložení objednávky.

**Omezení:**
Stejně jako u ručního vytváření příjemek, i zde platí pravidlo, že **manuální vytváření objednávek** je určeno pouze pro:
- **Testovací účely:** Vytváření testovacích objednávek pro potřeby kontroly funkčnosti systému.
- **Výdej materiálu, který není v SAP:** Materiál, který není evidován v SAPu, ale přesto je potřeba ho vydat ze skladu.

> **Důležité:** Zakázáno je vytvářet objednávky pro materiál, který je součástí systému SAP, protože to může způsobit nekonzistenci dat mezi WMS a SAPem. Všechny objednávky, které jsou součástí SAPu, musí být importovány prostřednictvím standardního procesu, nikoliv vytvořeny ručně.


<h3 id="radky-objednavky">Řádky objednávky</h3>

`http://10.10.30.4:8080/modules/documents/orders/lines` 

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/objednavky/objednavky-radky.png')">
   <img src="/content/images/doklady/objednavky/objednavky-radky.png" alt="Vytvoření objednávky" width="900" />
</a>

Tato obrazovka poskytuje detailní přehled jednotlivých řádků objednávek (lines), které byly importovány nebo vytvořeny v systému WMS. Každý řádek představuje jednu položku objednávky a obsahuje informace o počtu objednaných, dostupných a odeslaných kusů.

**Seznam sloupců na obrazovce:**
- **Kód:** Unikátní identifikátor objednávky (např. "OZ000000015"). Každá objednávka může obsahovat více řádků.
- **Externí číslo:** Externí číslo objednávky přidělené v SAPu, které propojuje objednávku mezi systémy SAP a WMS.
- **Účetní sklad:** Kód skladu, ze kterého bude zboží vychystáváno (např. "3007").
- **P/N (Part Number):** Unikátní číslo produktu (např. "1001144"). Je to identifikátor jednotlivé položky ve skladu, který se používá pro jednoznačné rozpoznání materiálu.
- **Název:** Název materiálu nebo produktu, který je uveden na řádku objednávky (např. "Antena exter. 3Mfgs Conel").
- **Zák. P/N:** Zákaznický part number (P/N) – číslo dílu, které používá zákazník pro identifikaci produktu.
- **Objednáno:** Počet jednotek daného materiálu, které byly objednány.
- **Odesláno:** Počet jednotek, které již byly odeslány zákazníkovi. Pokud je hodnota 0, znamená to, že žádné jednotky ještě nebyly odeslány.
- **Dostupné:** Počet jednotek, které jsou dostupné ve skladu a mohou být vychystány.
- **SN7 (Sériové číslo):** Sloupec indikuje, zda je pro tuto položku vyžadováno sériové číslo (SN). Pokud je symbol zelený, sériová čísla jsou povinná.
- **UID7 (Unique ID):** Sloupec indikuje, zda je u dané položky povinný unikátní identifikátor (UID).

**Funkce obrazovky:**
- **Filtrace:** Uživatel může filtrovat objednávky podle různých kritérií, jako jsou kódy objednávek nebo stav odeslání.
- **Detailní kontrola:** Pomocí této obrazovky může uživatel kontrolovat, které položky jsou již odeslané, kolik z nich je stále dostupných, a zda mají přidělená sériová čísla či unikátní identifikátory.

<h3 id="detail-objednavky">Detail objednávky</h3>

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/objednavky/detail-objednavky.png')">
   <img src="/content/images/doklady/objednavky/detail-objednavky.png" alt="Vytvoření objednávky" width="900" />
</a>

Tato obrazovka zobrazuje detailní informace o konkrétní objednávce v systému WMS. V tomto případě se jedná o dokončenou objednávku, jejíž stav je plně zpracován a veškeré položky byly vychystány a odeslány.

**Tlačítko PDF:**  
V pravém horním rohu je tlačítko **PDF**, které umožňuje tisknout **skladovou výdejku** pro tuto objednávku. Výdejka obsahuje souhrnné informace o objednávce, které slouží jako doklad o vychystání zboží ze skladu.

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/objednavky/vydejka-pdf.png')">
   <img src="/content/images/doklady/objednavky/vydejka-pdf.png" alt="Vytvoření objednávky" width="900" />
</a>

**Obecné vlastnosti:**
- **Kód:** Unikátní identifikátor objednávky (např. "OZ00000328").
- **Externí kód:** Externí číslo objednávky přiřazené systémem SAP (např. "7000246921").
- **Zdrojový systém:** Informace o tom, odkud byla objednávka importována (např. "SAP Delivery").
- **Vytvořeno:** Datum a čas, kdy byla objednávka vytvořena v systému (např. "2024-09-17 14:51:00").
- **Aktivováno:** Datum a čas, kdy byla objednávka aktivována (např. "2024-09-17 15:16:33").
- **Dokončeno:** Datum a čas, kdy byla objednávka dokončena, tedy veškeré položky byly vychystány a odeslány (např. "2024-09-17 15:20:33").
- **Přiřazeno:** Jméno pracovníka, který byl zodpovědný za dokončení objednávky (např. "Jana Kreckova").
- **Poznámka:** Volné pole pro poznámky, v tomto případě se jedná o poznámku "test SAP", která může označovat typ objednávky nebo testovací charakter.

**Řádky objednávky:**  
Zde jsou uvedeny jednotlivé položky objednávky, které byly zahrnuty ve vychystávání:
- **Účetní sklad:** Kód skladu, kde je daná položka uskladněna (např. "3007").
- **P/N:** Unikátní identifikátor produktu (např. "1000129").
- **Název:** Popis položky nebo materiálu (např. "BUS/500 Box").
- **Zák. P/N:** Zákaznický part number (např. "0000000000035611922").
- **Objednáno:** Počet kusů, které byly objednány (např. "2").
- **Vychystáno:** Počet kusů, které byly vychystány ze skladu a připraveny k expedici (např. "2").
- **Odesláno:** Počet kusů, které byly odeslány zákazníkovi (např. "2").
- **Dostupné:** Počet kusů, které byly ještě dostupné v daném skladu (např. "17").
- **Všechny sklady:** Celkový počet dostupných kusů ve všech skladech.
- **Zóna:** Zóna, ve které je daný materiál umístěn (např. "ZA-3007").
- **SN:** proklik na seznam vypickovaných SN na řádku
- **SN?** a **UIID?:** Sloupce indikují, zda je potřeba zadat sériová čísla nebo unikátní identifikátory pro daný produkt.

**Skladové joby:**  
Tato sekce ukazuje, jaké skladové joby byly v rámci objednávky vytvořeny a zpracovány:
- **Kód:** Kód jobu (např. "JPO000000634").
- **Vytvořeno:** Datum a čas vytvoření jobu.
- **Přiřazeno:** Datum a čas, kdy byl job přiřazen pracovníkovi.
- **Dokončeno:** Datum a čas dokončení jobu.
- **Dokončil:** Jméno pracovníka, který job dokončil (např. "Jana Kreckova").
- **Zrušeno a Zrušil:** Informace o případném zrušení jobu, pokud by k tomu došlo.

**Význam obrazovky:**  
Tato obrazovka poskytuje uživateli přehled o všech důležitých informacích týkajících se konkrétní objednávky. Je užitečná zejména pro kontrolu stavu objednávky, potvrzení, že všechny položky byly vychystány a odeslány, a pro následné vygenerování výdejky ve formě PDF, která může být přiložena k fyzickému zboží při expedici.

V případě neaktivované objednávky vypadá horní lišta takto a objednávka lze aktivovat za splnění podmínek k aktivaci. Viz zde

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/objednavky/aktivace-tlacitkem.png')">
   <img src="/content/images/doklady/objednavky/aktivace-tlacitkem.png" alt="Vytvoření objednávky" width="900" />
</a>

Aktivovaná ale nedokončená objednávka má pak tyto možnosti

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/objednavky/lista-aktivovana-objednavka.png')">
   <img src="/content/images/doklady/objednavky/lista-aktivovana-objednavka.png" alt="Vytvoření objednávky" width="900" />
</a>

**Zrušit (Červené tlačítko):**  
- Toto tlačítko umožňuje zrušit celou objednávku. Po jeho stisknutí nebude objednávka dále zpracovávána, a tím pádem se žádná data neodešlou do systému SAP. Toto tlačítko by mělo být používáno opatrně, protože zrušená objednávka nelze znovu aktivovat.

**Dokončit (Zelené tlačítko):**  
- Toto tlačítko umožňuje dokončení objednávky. Dokončením se myslí odeslání informací o vychystání zboží zpět do systému SAP. Je možné dokončit objednávku i v případě, že nebyly všechny položky plně uspokojeny (např. nedostatek zásob na skladě). Před samotným dokončením se zobrazí potvrzovací dialog (viz druhý obrázek), kde se uživatel musí rozhodnout, zda skutečně chce objednávku dokončit.

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/objednavky/dialog-dokoncit-objednavku.png')">
   <img src="/content/images/doklady/objednavky/dialog-dokoncit-objednavku.png" alt="Vytvoření objednávky" width="900" />
</a>

**PDF:**
-	Stisknutím tohoto tlačítka lze vygenerovat a stáhnout skladovou výdejku ve formátu PDF, která obsahuje detailní informace o objednávce, vychystaném zboží, a dalších logistických údajích. Tento dokument může být přiložen k zásilce nebo použit pro interní evidenci.

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/objednavky/vydejka-pdf.png')">
   <img src="/content/images/doklady/objednavky/vydejka-pdf.png" alt="Vytvoření objednávky" width="900" />
</a>


<h3 id="pick-joby">Pick Joby</h3>

`http://10.10.30.4:8080/modules/documents/orders/pick-jobs`

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/objednavky/pick_joby.png')">
   <img src="/content/images/doklady/objednavky/pick_joby.png" alt="Vytvoření objednávky" width="900" />
</a>

Tato obrazovka poskytuje přehled o **pickovacích jobech** (vychystávacích úkolech), které byly vytvořeny v rámci objednávek ve WMS systému. Každý pickovací job představuje soubor úkolů, které skladníci vykonávají při vychystávání objednávek.

**Seznam sloupců na obrazovce:**
- **Kód:** Unikátní identifikátor pickovacího jobu (např. "JPO000000462"). Každý job je jednoznačně identifikován tímto kódem a propojen s objednávkou.
- **Priorita:** Prioritní úroveň přiřazená danému jobu. Čím nižší číslo, tím vyšší prioritu má job. V tomto případě je většina jobů nastavena na "0.0", což indikuje neutrální prioritu.
- **Objednávka:** Odkaz na příslušnou objednávku, ke které je job přiřazen (např. "OZ00000376").
- **Externí číslo:** Externí číslo objednávky ze SAPu, které propojuje objednávku mezi SAP a WMS.
- **Vytvořeno:** Datum a čas, kdy byl pickovací job vytvořen.
- **Přiřazeno:** Datum a čas, kdy byl pickovací job přiřazen konkrétnímu skladníkovi, který jej má vychystat.
- **Přiřazeno k:** Jméno pracovníka, kterému byl job přidělen k vychystávání (např. "František Sirůček").
- **Dokončeno:** Datum a čas, kdy byl pickovací job úspěšně dokončen.
- **Dokončil:** Jméno pracovníka, který úspěšně dokončil pickovací job (např. "Jana Kreckova").
- **Zrušeno:** Zobrazuje, zda byl pickovací job zrušen (např. v případě, že objednávka byla zrušena).
- **Zrušil:** Pokud byl job zrušen, zobrazuje jméno osoby, která job zrušila.

**Funkce obrazovky:**
- **Přehled stavu jobů:** Tato obrazovka umožňuje uživatelům vidět aktuální stav jednotlivých pickovacích jobů – jaké byly vytvořeny, přiřazeny, dokončeny nebo případně zrušeny.
- **Monitoring pracovníků:** Obrazovka také slouží k monitorování výkonu pracovníků, protože ukazuje, komu byly joby přiřazeny, kdy byly dokončeny, a kdo je dokončil. Případně jak dlouho trvalo jejich dokončení.

<h3 id="detail-jobu">Detail jobu</h3>

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/objednavky/job-detail.png')">
   <img src="/content/images/doklady/objednavky/job-detail.png" alt="Detail jobu" width="900" />
</a>

Obrazovka detailu pickovacího jobu poskytuje přehled o konkrétním jobu a jeho řádcích.

**Sekce "Obecné vlastnosti":**
V této sekci jsou uvedeny základní informace o jobu:
- **Kód:** Unikátní identifikátor jobu, v tomto případě JP0000000469.
- **Priorita:** Nastavená priorita pro tento job (v tomto případě 0.0, což značí, že priorita nebyla speciálně nastavena).
- **Vytvořeno:** Datum a čas, kdy byl job vygenerován, spolu s informací o uživateli, který job vytvořil.
- **Přiděleno:** Zde by se zobrazilo, kterému skladníkovi nebo skupině byl job přidělen.
- **Dokončeno:** Informace o tom, kdy a kým byl job dokončen.
- **Zrušeno:** Pokud by byl job zrušen, byla by zde uvedena informace o zrušení.

**Sekce "Řádky":**  
Tato část zobrazuje jednotlivé řádky pickovacího jobu. Každý řádek odpovídá jedné položce, kterou je nutné vychystat v rámci objednávky:
- **Kód:** Unikátní identifikátor jobové řádky (v tomto případě LM0000000465).
- **Typ:** Určuje typ řádky, zde je uvedeno "JobMaterialLine", což znamená, že se jedná o řádek materiálu k vychystání.
- **P/N:** Part Number materiálu, v tomto případě 1020414.
- **Název:** Název materiálu, zde "ULEUB".
- **Zák. P/N:** Zákaznické Part Number, což je zákazníkův identifikační kód pro materiál (zde 000000000004975611).
- **Kontejner:** Pokud by materiál byl v kontejneru, byl by zde uveden jeho kód. V tomto případě je tato informace prázdná.
- **Zdroj:** Označuje, odkud je materiál vychystáván. Zde není vyplněno.
- **Cíl:** Cílové místo, kam bude materiál přemístěn po vychystání.
- **Očekáváno:** Počet kusů očekávaných k vychystání (zde 1).
- **Dokončeno:** Počet kusů, které byly skutečně vychystány (zde 0, protože job zatím nebyl dokončen).

**Tlačítka:**
- **PDF:** Toto tlačítko umožňuje stáhnout nebo vytisknout souhrnnou dokumentaci k tomuto jobu ve formátu PDF.

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/objednavky/job-pdf.png')">
   <img src="/content/images/doklady/objednavky/job-pdf.png" alt="Vytvoření objednávky" width="900" />
</a>