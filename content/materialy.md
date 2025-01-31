## Materiály

### Obsah sekce

1. [Přehled materiálů](#prehled-materialu)
2. [Detail materiálu](#detail-materialu)
    - [Obecné vlastnosti](#obecne-vlastnosti)
    - [Logistické vlastnosti / GEO data materiálu](#logisticke-vlastnosti)
    - [Vlastní pole](#vlastni-pole)
    - [Unikátní identifikátory](#unikatni-identifikatory)
3. [Editace obecných vlastností materiálu](#editace-obecnych-vlastnosti-materialu)
4. [Editace GEO dat](#editace-geo-dat)

---

<h3 id="prehled-materialu">Přehled materiálů</h3>

Tato obrazovka zobrazuje přehled všech materiálů spravovaných v systému. Každý materiál je detailně popsán několika parametry, které umožňují správu zásob ve skladech.

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/materialy/materialy.png')">
    <img src="/content/images/materialy/materialy.png" alt="Detail materiálu" class="img-fluid modal-thumbnail" />
</a>

- **PN (Part Number)**: Unikátní identifikátor materiálu (např. "1001001").
- **Zak. PN (Zákaznický PN)**: Identifikátor materiálu používaný zákazníkem.
- **Výr. PN (Výrobní PN)**: Identifikátor používaný výrobcem daného materiálu.
- **Název**: Popis materiálu (např. "32 port Asynchronous Module").
- **GTIN**: Globální identifikátor obchodní položky. (obvykle jde o EAN nebo UPC u spol Apple)
- **Fyz? (Fyzický)**: Checkbox, zda materiál existuje fyzicky v systému.
- **Skl?**: Checkbox označující, zda je materiál fyzický.
- **SN? (Sériové číslo)**: Checkbox, zda je materiál identifikován sériovým číslem.
- **Q (Kvalita)**: Checkbox indikující, zda materiál je po přijmu na kontrolu kvality.
- **Jednotka**: Jednotka materiálu.

**Funkčnost**: Seznam materiálů umožňuje přehlednou správu všech materiálů ve skladovém systému. Každý materiál je identifikován několika parametry, což usnadňuje jejich sledování a správu.

**Možnost filtrace**: Uživatel může filtrovat materiály podle klíčových atributů a efektivně tak spravovat velké množství materiálů v systému.

<p><a href="#" class="btn btn-link" onclick="window.scrollTo({ top: 0, behavior: 'smooth' });">Zpět nahoru</a></p>

---

<h3 id="detail-materialu">Detail materiálu</h3>

Tato obrazovka zobrazuje detailní informace o vybraném materiálu, rozdělené do několika sekcí pro přehlednost.

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/materialy/materialy-detail.png')">
    <img src="/content/images/materialy/materialy-detail.png" alt="Detail materiálu" class="img-fluid modal-thumbnail" />
</a>

<h4 id="obecne-vlastnosti">Obecné vlastnosti</h4>

- **PN (Part Number)**: Unikátní identifikátor materiálu (např. "1001018").
- **Výrobní PN**: Identifikátor materiálu používaný výrobcem (např. "NM-16ESW").
- **Zákaznický PN**: Identifikátor používaný zákazníkem.
- **Název**: Popis materiálu (např. "Cisco NM-16ESW").
- **GTIN**: Globální identifikátor obchodní položky.
- **Externí ID**: Externí identifikátor, pokud je materiál propojen s jinými systémy.
- **Poznámka**: Další informace nebo poznámky spojené s materiálem.
- **Barcodes**: Čárové kódy přidělené materiálu.
- **Upravit**: Tlačítko pro editaci obecné části vlastností materiálu.

<p><a href="#" class="btn btn-link" onclick="window.scrollTo({ top: 0, behavior: 'smooth' });">Zpět nahoru</a></p>

---

<h4 id="logisticke-vlastnosti">Logistické vlastnosti / GEO data materiálu</h4>

Zobrazuje logistické vlastnosti materiálu v systému:

- **Fyzický**: Indikace, zda materiál existuje fyzicky nebo pouze virtuálně (např. kupony).
- **Skladováno**: Zda je materiál fyzicky skladovatelný.
- **Serializováno**: Zda je materiál identifikován sériovým číslem.
- **Sledování položek na lokaci**: Zda je materiál sledován pomocí SN až na jednotlivé lokace.

<p><a href="#" class="btn btn-link" onclick="window.scrollTo({ top: 0, behavior: 'smooth' });">Zpět nahoru</a></p>

---

<h4 id="vlastni-pole">Vlastní pole</h4>

Tato sekce obsahuje specifická pole přizpůsobená pro potřeby firmy:

- **Detailní popisy materiálu**: Popisy v různých jazycích nebo specifické kódy.
- **Integrace**: Specifické kódy pro integraci s dalšími systémy. Data jsou synchronizována se systémem SAP.

<p><a href="#" class="btn btn-link" onclick="window.scrollTo({ top: 0, behavior: 'smooth' });">Zpět nahoru</a></p>

---

<h4 id="unikatni-identifikatory">Unikátní identifikátory</h4>

Seznam šablon spojených s materiálem, které mohou definovat různé aspekty jeho správy:

- **Typ**: Typ šablony (např. "SN").
- **Šablona**: REGEX kód pro kontrolu správnosti unikátního identifikátoru.

<p><a href="#" class="btn btn-link" onclick="window.scrollTo({ top: 0, behavior: 'smooth' });">Zpět nahoru</a></p>

---

<h3 id="editace-obecnych-vlastnosti-materialu">Editace obecných vlastností materiálu</h3>

Tato obrazovka umožňuje úpravu obecných vlastností konkrétního materiálu.

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/materialy/materialy-editace.png')">
    <img src="/content/images/materialy/materialy-editace.png" alt="Logistické vlastnosti materiálu" class="img-fluid modal-thumbnail" />
</a>

- **PN (Part Number)**: Unikátní identifikátor materiálu.
- **Výrobní PN**: Identifikátor používaný výrobcem.
- **Zákaznický PN**: Identifikátor používaný zákazníkem.
- **Název**: Popis materiálu.
- **GTIN**: Globální identifikátor obchodní položky.
- **Note**: Pole pro zadání poznámek k materiálu.
- **OK**: Tlačítko pro potvrzení a uložení změn.

<p><a href="#" class="btn btn-link" onclick="window.scrollTo({ top: 0, behavior: 'smooth' });">Zpět nahoru</a></p>

---

<h3 id="editace-geo-dat">Editace GEO dat</h3>

Tato obrazovka umožňuje správu a editaci logistických dat materiálu, která jsou klíčová pro skladovou správu a manipulaci s materiálem.

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/materialy/materialy-geo-data.png')">
    <img src="/content/images/materialy/materialy-geo-data.png" alt="Logistické vlastnosti materiálu" class="modal-thumbnail" />
</a>

- **Fyzický**: Checkbox označující, zda materiál existuje fyzicky ve skladu.
- **Uloženo**: Checkbox označující, zda je materiál uskladněn na lokaci.
- **Serializováno**: Checkbox pro označení, zda je materiál identifikován sériovým číslem.
- **Sledování položek na lokaci**: Označuje, zda je materiál sledován na konkrétních lokacích.
- **Váha netto**: Čistá hmotnost materi

<p><a href="#" class="btn btn-link" onclick="window.scrollTo({ top: 0, behavior: 'smooth' });">Zpět nahoru</a></p>
