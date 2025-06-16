# 2/ Příjem

## Obsah sekce "Příjem"
1. [Příjem produktu na SN (+ UIID)](#prijem-produktu-na-sn--uiid)  
2. [Příjem položky bez SN (UIID)](#prijem-polozky-bez-sn-uiid)  
3. [Dokončení příjmu](#dokonceni-prijmu)  
4. [Vytváření kontejnerů (Master Obalů)](#vytvareni-kontejneru-master-obalu)
5. [Řešení problémů](#reseni-problemu) 

---

V hlavním menu čtečky vybereme dlaždici **Příjem**.

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/terminal/images/prijem_dlazdice.png')"> 
    <img src="/content/terminal/images/prijem_dlazdice.png" alt="Hlavní menu aplikace" width="900" /> 
</a>

Po zvolení dlaždice **Příjem** na hlavní obrazovce aplikace se uživatel dostane na obrazovku, kde je zobrazen přehled všech dostupných příjemek. Uživatel má možnost prokliku na konkrétní příjemku podle kódu a dokladu. Kliknutím na příjemku se otevře její detail.

- **Kód**: Unikátní identifikátor příjemky.  
- **Doklad**: Číslo dokladu spojeného s příjemkou.

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/terminal/images/prijem_seznam_prijemek.png')"> 
    <img src="/content/terminal/images/prijem_seznam_prijemek.png" alt="Hlavní menu aplikace" width="900" /> 
</a>

Po výběru příjemky je uživatel přesměrován na obrazovku, kde vidí jednotlivé řádky příjemky. Zde nascanuje nebo vybere produkt, který bude přijímat.

- **Materiál**: Kód a popis přijímaného materiálu.  
- **Q**: Množství přijímaného zboží.  
- **CQ**: Počet zboží z kontrolní kvality.  
- **SN?**: Indikátor, zda produkt vyžaduje sériové číslo.  
- **UIID?**: Indikátor, zda produkt vyžaduje UIID.

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/terminal/images/prijem_prijemka_produktyek.png')"> 
    <img src="/content/terminal/images/prijem_prijemka_produkty.png" alt="Hlavní menu aplikace" width="900" /> 
</a>

---

<h3 id="prijem-produktu-na-sn--uiid">Příjem produktu na SN (+ UIID)</h3>

Pokud je produkt označen jako vyžadující UIID, systém se uživatele zeptá, zda chce UIID přiřadit již při příjmu.

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/terminal/images/prijem_dotaz_UIID_priradit.png')"> 
    <img src="/content/terminal/images/prijem_dotaz_UIID_priradit.png" alt="Hlavní menu aplikace" width="900" /> 
</a>

Uživatel má možnost volby:
- **Ano**: UIID bude přiřazeno ihned během procesu přijmu.
- **Ne**: UIID nebude přiřazeno.
- **Zrušit**: Uživatel může zrušit celý proces.

Po potvrzení, že bude přiřazováno UIID, systém vyzve uživatele k načtení sériového čísla (SN) daného produktu:

- **Kód**: Sériové číslo produktu (SN).  
- **Název**: Popis produktu.  
- **Hodnota**: Pole pro zadání sériového čísla.
<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/terminal/images/prijem_prijemka_SNaUIID.png')"> 
    <img src="/content/terminal/images/prijem_prijemka_SNaUIID.png" alt="Hlavní menu aplikace" width="900" /> 
</a>



Pokud se produkt eviduje pouze na SN nebo uživatel v předchozí obrazovce zvolil **Ne** na přiřazení UIID, pokračuje načtením všech požadovaných sériových čísel.  
V případě, že se přiřazuje UIID, scanuje se SN a poté následuje další obrazovka pro scan UIID. Poté opět SN + UIID, a takto dokola, dokud nejsou ověřeny všechny kusy.


Po načtení SN je uživatel vyzván k zadání UIID pro produkt:
- **Kód**: Unikátní identifikátor (UIID).  
- **Název**: Popis produktu.  
- **Hodnota**: Pole pro zadání UIID.
<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/terminal/images/prijem_prijemka_SNaUIID_UIID.png')"> 
    <img src="/content/terminal/images/prijem_prijemka_SNaUIID_UIID.png" alt="Hlavní menu aplikace" width="900" /> 
</a>

Pokud během načítání dojde k chybě (např. nesprávný formát sériového čísla), systém zobrazí červené varování v horní části obrazovky. Uživatel je informován o typu chyby a může opravit zadání.
---

<h3 id="prijem-polozky-bez-sn-uiid">Příjem položky bez SN</h3>

V případě, že materiál **není** evidovaný na SN, tak místo obrazovek na načítání SN (UIID) se zobrazí pouze obrazovka, kam se zadá počet ks k přijetí.

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/terminal/images/prijem_prijemka_produkty_kusovky.png')"> 
    <img src="/content/terminal/images/prijem_prijemka_produkty_kusovky.png" alt="Obrazovka na zadání počtu ks" width="900" /> 
</a>

Lze přijmout část množství, poté příjemka vypadá následovně:

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/terminal/images/prijem_prijemka_produkty_kusovky_castecny.png')"> 
    <img src="/content/terminal/images/prijem_prijemka_produkty_kusovky_castecny.png" alt="Příjemka po částečném příjmu" width="900" /> 
</a>

A nebo celé množství. **Nikdy nejde přijmout víc**, než je na řádku položky.

---

<h3 id="dokonceni-prijmu">Dokončení příjmu</h3>

Po dokončení příjmu řádky se zobrazí potvrzovací obrazovka a výzva k načtení tiskárny pro vytištění potvrzovacího lístku. Nebo je zde možnost tisk vynechat.

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/terminal/images/prijem_prijemka_dokonceno.png')"> 
    <img src="/content/terminal/images/prijem_prijemka_dokonceno.png" alt="Potvrzovací obrazovka" width="900" /> 
</a>

Následně se vrátím na Příjemku, kde vidím, které řádky jsou **přijaté** a případně **nepřijaté**.

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/terminal/images/prijem_prijemka_dokonceno_seznam.png')"> 
    <img src="/content/terminal/images/prijem_prijemka_dokonceno_seznam.png" alt="Zobrazení stavu příjemky" width="900" /> 
</a>

Kliknutím na **Hotovo** dokončím práci a zobrazí se mi tento dialog. Zde zvolím, zda chci:

1. **Data o příjmu odeslat do SAPu** (Dokončit a odeslat doklad).  
2. Pouze **Odejít** ze zpracování příjemky, data do SAP **nebudou** zatím odeslána. (Tato volba se používá např. pokud se budu k příjmu ještě vracet a přijímat další řádky.)  
3. Nebo se **vrátit zpět** na předchozí obrazovku volbou **Zrušit**.

---

<h3 id="vytvareni-kontejneru-master-obalu">Vytváření kontejnerů (Master Obalů)</h3>

V případě, že chci už při **příjmu** vytvořit kontejner, tak zvolím tlačítko (na obrazovce zadání počtu nebo skenování SN).

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/terminal/images/prijem_prijemka_kontejner_button.png')"> 
    <img src="/content/terminal/images/prijem_prijemka_kontejner_button.png" alt="Vytvoření kontejneru" width="900" /> 
</a>

Následně po mě bude aplikace chtít načíst tiskárnu, aby se vytiskl štítek s ID kontejneru, který se na něj nalepí.

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/terminal/images/prijem_prijemka_kontejner_tisky.png')"> 
    <img src="/content/terminal/images/prijem_prijemka_kontejner_tisky.png" alt="Scan tiskárny" width="900" /> 
</a>

Po načtení tiskárny se vytiskne štítek a aplikace si vyžádá vložení kusů do kontejneru.  
Buď **počtem** (produkty bez SN), nebo nascanováním **SN** (plus případně UIID).

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/terminal/images/prijem_prijemka_kontejner_zadani_kusu.png')"> 
    <img src="/content/terminal/images/prijem_prijemka_kontejner_zadani_kusu.png" alt="Vložení ks do kontejneru" width="900" /> 
</a>
<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/terminal/images/prijem_prijemka_kontejner_prijemka.png')"> 
    <img src="/content/terminal/images/prijem_prijemka_kontejner_prijemka.png" alt="Vložení ks do kontejneru" width="900" /> 
</a>

<h3 id="reseni-problemu">Řešení Problémů</h3>

---

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