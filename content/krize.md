# Řešení nestandartních situací

V případě výpadku systému se postupuje podle následujícího scénáře. 

## Kontaktní osoby
V případě výpadku systému postupujte přesně podle následujícího pořadí. V případě BUGu (špatného chování systému) přeskočte interní IT a začněte hlášení rovnou na helpdesk Anthill.

- **Interní IT (konektivita)** –> Jan Sysel; jan.sysel@expedis.cz; tel: +420 734 579 130
- **Podpora WMS** –> Helpdesk Anthill; helpdesk@anthill.cz; tel: +420 246 024 246
- **Podpora SAP** -> Tomáš Zajíc; tomas.zajic@t-mobile.cz; 
- **Klíčový užitavel WMS za PJ Expedis** -> František Sirůček; frantisek.sirucek@expedis.cz; +420 773 109 200

## Hlášení problému, které neohrožují provoz
- pokud narazíte na chybu v systému, která neohrožuje provoz. Ale způsobuje nějaké nepohodlí, využívejte hlášení na e-mail. Do kopie e-mailu dávejte vždy aktuálního klíčového uživatele WMS, který je zodpovědný na komunikaci s externí firmou a hledání řešení. 
- pokud si nebudete jistí, zda se jedná o problém, který je potřeba řešit akutně, kontaktujte klíčového uživatele. 
- hlášení o problému by mělo vždy obsahovat 
     - Co nefunguje
     - Jak to má správně fungovat
     - Konkrétní příklad toho co nefunguje
     - Jaké chybové hlášky se zobrazují.

---

## Hlášení akutních problému

### Předtím, než zavoláte na hotline

1. **Ověřte rozsah problému:**
   - Zjistěte, zda se problém týká jen vašeho zařízení/uživatele, nebo je systémový (zkuste se přihlásit z jiného terminálu, zeptejte se kolegů).

2. **Shromážděte nezbytné informace:**
   - **Kde je chyba:** název modulu nebo aplikace ve čtečce, která nefunguje, při jakém procesu nastala chyba, jaký uživatel byl přihlášený.
   - **Čas a datum:** Kdy se problém poprvé objevil? Kolikrát se zopakoval?
   - **Chybová hlášení nebo kódy:** Pokud systém zobrazuje chybové kódy, poznámky nebo hlášení, zapište si je.
   - **Kroky reprodukce problému:** Můžete poskytnout návod, jak problém vzniká (např. "Po přihlášení kliknu na modul příjem, zadám číslo dokladu a poté se zobrazí chyba.").
   - **Kontakt na Vás:** Jméno, pozice, telefonní číslo nebo email, případně jméno a kontakt na vedoucího směny.

3. **Kam volat jako první**
   - Výpadek připojení, selhádní HW ---> interní IT Podpora
   - Nestandartní chování systému, výpadek systému (WMS nebo jeho důležitá část nefunguje) ---> Helpdesk Anthill
   - Pokud není problém na straně WMS kontaktuje se podpora SAP z T-Mobile 
   - V případě, že si nejste jisti o jaký problém jde a kam volat jako prnví, kontaktujte vašeho klíčového uživatele.

### Během hovoru na hotline

1. **Identifikujte se:**
   - Uveďte své jméno, pozici (např. „Jsem vedoucí směny ve skladu XY…“), název firmy.

2. **Stručně popište problém:**
   - Představte problém srozumitelně a jasně, krátce shrňte, co a kdy přestalo fungovat.

3. **Poskytněte detailní informace:**
   - Uveďte všechny shromážděné údaje: čas výpadku, chybové kódy, kroky k reprodukci problému.
   - Dejte jim vědět, jak moc je situace urgentní (např. krátký výpadek, nebo kritické ohrožení provozu).

4. **Odpovídejte na otázky operátora hotline:**
   - Pokud se ptají na detaily, spolupracujte a poskytněte co nejpřesnější informace.
   - Buďte připraveni udělat základní úkony, jako je restart zařízení, ověření síťového připojení, pokud o to požádají.

5. **Dohodněte se na dalším postupu:**
   - Získejte od hotline informace, kdy a jak budou problém řešit.
   - Ujistěte se, že máte kontaktní osobu, číslo incidentu nebo tiket, pod kterým je váš problém evidován.

### Po hovoru s hotline

1. **Zaznamenejte detaily o hovoru:**
   - Zapište si přidělené číslo incidentu, jméno operátora, čas hovoru a dohodnuté kroky.

2. **Informujte příslušné osoby interně:**
   - Oznamte vedoucímu, IT podpoře či vedení, že byl problém nahlášen a s jakým výsledkem.

3. **Sledujte další komunikaci:**
   - Pokud se situace nezlepší ve slíbeném čase, opět kontaktujte hotline s odkazem na číslo incidentu.
   - Udržujte odpovědné osoby interně informovány o vývoji.

---

## Výpadek systému

### Definice typů výpadků

1. **Krátký výpadek (např. do 2 minut):**
   - Systém je nedostupný jen krátce, po několika minutách opět naběhne.

2. **Dlouhý výpadek, který neohrožuje provoz (např. do 1 hodiny):**
   - Část procesů je omezená, ale lze je řešit náhradními manuálními postupy, provoz skladu nezkolabuje.  
   - Nebo časté opakování krátkých výpadků.

3. **Rozsáhlý výpadek, který ohrožuje provoz (výpadek nad 1 hodinu nebo kritické funkce mimo provoz):**
   - Systém je zcela nebo z významné části mimo provoz a způsobuje kritické omezení provozu, zpoždění expedic, příjmu zboží, inventur atd.  
   - Platí jak pro jeden konkrétní výpadek, tak pro souběh a opakování se kratších výpadků.

---

### 1. Krátký výpadek

**Postup:**
- Skladník zjistí, zda je problém lokální (na jednom zařízení) nebo obecný (ptá se kolegů, ověří na jiném terminálu).
- Pokud je problém obecný, informuje svého nadřízeného.
- Vedoucí směny nebo lokální IT podpora zkusí krátce zkontrolovat základní funkčnost (restart terminálu, ověření sítě).
- Pokud se systém během pár minut opět rozběhne, pokračují práce bez omezení.
- Není-li nutno zapojit další subjekty, incident se nepředává dál. Proběhne informovanost vedení, že se dělal výpadek.
- V případě pravidelného opakování se krátkých výpadků je potřeba začít hledat příčinu. V pořadí:
  1. Konektivita skladu (vnitřní síť -> komunikace s internetem) řeší s interním IT.
  2. Konektivita serverů WMS, kontaktuje se Helpdesk Anthill.
  3. Dotaz na konektivitu SAP.

---

### 2. Dlouhý výpadek, který neohrožuje provoz

**Postup:**
- Po zjištění, že výpadek trvá déle (např. nad 2 minuty a do 1 hodiny dle aktuálních provozních podmínek), vedení skladu kontaktuje hotline poskytovatele a předá co nejdetailnější info o problému.
- Spustí se náhradní (manuální) postupy, např. záznam zboží na papír, příprava expedice bez on-line potvrzení, dokud se systém nevrátí.
- IT podpora / WMS administrátor kontaktuje hotline dodavatele systému, pokud problém přetrvává déle než 30 minut.
- Pravidelně (např. co 20 minut) podává vedoucí směny informace o stavu svému nadřízenému (vedoucímu logistiky/oddělení), aby měl přehled.
- Po obnově systému je nutné provést kontrolu správnosti dat (doinformovat WMS o manuálně provedených krocích).

---

## Eskalační mapa (kdy koho informovat)

### Účastníci
- Skladník
- Vedoucí skladu
- IT podpora / WMS administrátor (interní)
- Dodavatel WMS (hotline Anthill)
- Vedení PJ Expedis

### Krátký výpadek (do 10 minut)
- **Skladník** → informuje **Vedoucího**  
- **Vedoucí** → případně informuje **IT podporu/WMS administrátora**, pokud se problém nevyřeší sám do několika minut.  
- Není-li potřeba, není eskalováno výš.

### Dlouhý výpadek (nad 10 min a do 1 hod)
- **Skladník** → **Vedoucí**  
- **Vedoucí** → **IT podpora/WMS helpdesk**  
- Po 30 minutách **IT podpora/WMS helpdesk** → **Vedení firmy**  
- Vedoucí směny průběžně informuje Vedení o průběhu řešení a přijímaných opatřeních (u dlouhých a rozsáhlých výpadků)

### Rozsáhlý výpadek (nad 1 hod nebo kritické funkce mimo provoz - ihned)
- **Skladník** → **Vedoucí**  
- **Vedoucí směny** → **IT podpora/WMS helpdesk**  
- **Vedoucí** → **Vedení firmy**  
- Vedoucí směny průběžně informuje Vedení o průběhu řešení a přijímaných opatřeních (u dlouhých a rozsáhlých výpadků).  
- Pokud předpokládané řešení přesáhne čas, kdy je možné nezpozdit kritickou expedici (výpadek trvá déle jak 4 hodiny), nastupuje rozhodování o tom, které procesy se dokončí rovnou v systému SAP. Aktivuje se krizové řízení.

---

## Krizové řízení

1. **Dojde k určení krizového manažera pro tuto situaci.**

2. **Rozhodnutí o prioritních procesech**
   - Krizový manažer určí, které procesy je nutno bezodkladně dokončit v SAP (např. urgentní expedice, příjem kritických komponent).
   - Tyto procesy se provedou v SAP i přes riziko dočasné nekonzistence s WMS.

3. **Důsledná evidence manuálních a SAP-only pohybů**
   - Každý pohyb materiálu či zboží, který je proveden mimo WMS, musí být zaznamenán:
     - Číslo dokladu SAP, čas a datum provedení.
     - Množství a druh zboží.
     - Související skladová lokace (fyzická nebo plánovaná).
   - Záznamy vedou zodpovědní pracovníci (např. skladník pověřený krizovým manažerem, vedoucí směny) podle předem stanoveného formátu.

4. **Dočasné zajištění provozu a minimalizace chyb**
   - Omezte na minimum další operace, které nejsou nezbytně nutné.
   - Používejte standardizované papírové formuláře pro evidenci pohybů zboží.
   - Snažte se držet fyzickou organizaci skladu tak, aby co nejvíce odpovídala pozdější korekci v systému.

5. **Konzultace a příprava na narovnání dat**
   - Jakmile je známo, že se blíží obnova WMS, kontaktujte klíčového uživatele WMS a dodavatele WMS.
   - Společně prodiskutujte plán, jak provést nápravné inventární pohyby v WMS.
   - Ověřte doporučené postupy, skripty či nástroje, které WMS nabízí pro hromadnou úpravu dat a inventární korekce.

6. **Obnova provozu WMS a narovnání dat**
   - Po obnovení WMS zkontrolujte, zda jsou základní funkce v provozu.
   - Na základě zaznamenaných papírových a SAP-only transakcí proveďte inventární korekce v WMS:
     - Porovnejte skutečný fyzický stav zásob s evidencí SAP i se záznamy o provedených mimo-systémových operacích.
     - Vytvořte inventární dokumenty a proveďte opravy stavů v WMS podle instrukcí schválených klíčovým uživatelem a ve spolupráci s dodavatelem WMS.

7. **Kontrola a ověření konzistence**
   - Po provedení korekcí proveďte kontrolu, zda WMS nyní souhlasí se SAP.
   - Zkontrolujte kritické položky, u kterých byla prováděna ruční evidence a manuální zásahy.

8. **Zpětná vazba a dokumentace celého procesu**
   - Zaznamenejte, jak dlouho trvala odstávka, jaké kroky byly provedeny, jaký byl rozsah manuálních operací a korekcí.
   - Vypracujte report pro vedení, ve kterém uvedete zjištění, doporučení pro zlepšení a případné návrhy na preventivní opatření (např. lepší záložní řešení, rychlejší eskalační proces).
   - Diskutujte s klíčovými uživateli a dodavatelem WMS možnosti, jak zlepšit proces obnovy a minimalizovat vliv podobných výpadků v budoucnu.
