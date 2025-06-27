## Obsah sekce

1. [Účetní sklady](#ucetni-sklady)
    - [Detail účetního skladu](#detail-ucetniho-skladu)
2. [Fyzické sklady](#fyzicke-sklady)
    - [Detail fyzického skladu](#detail-fyzickeho-skladu)
3. [Zóny](#zony)
    - [Editace zóny](#editace-zony)
    - [Detail zóny](#detail-zony)
4. [Lokace](#lokace)
    - [Detail lokace](#detail-lokace)
    - [Typy lokací](#typy-lokaci)
    - [Založení/Editace typu lokace](#zalozeni-editace-typu-lokace)

---

<h2 id="ucetni-sklady">Účetní sklady</h2>

[http://10.10.30.4:8080/modules/master-data/warehouses/](http://10.10.30.4:8080/modules/master-data/warehouses/)

Účetní sklady jsou systémové sklady, na které se ukládá zboží. V rámci tohoto provozu jsou zrcadlem účetních skladů ze systému SAP pro tento provoz.

Tato obrazovka zobrazuje přehled všech účetních skladů. Každý sklad je zde uveden se svým kódem, externím kódem a názvem.

- **Kód**: Unikátní identifikátor skladové položky.
- **Ext. kód**: Externí kód skladu, který může být použit pro komunikaci s jinými systémy.
- **Název**: Název účetního skladu, který může uživatel prokliknout pro zobrazení detailních informací.
- **Aktivní**: Označuje, zda je sklad aktivní.
- **Upravit**: Tlačítko pro editaci informací o skladu.
- **Nový účetní sklad**: Tlačítko v horní části obrazovky slouží k přidání nového skladu.
- **Další možnosti**: V dolní části je k dispozici nastavení počtu zobrazených položek na stránce (10, 50, 100).

<a href="#cisleniky" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/ciselniky/ucetni-sklady.png')">
    <img src="/content/images/ciselniky/ucetni-sklady.png" alt="Účetní sklady" width="900" />
</a>

<p><a href="#ciselniky" class="btn btn-link" onclick="window.scrollTo({ top: 0, behavior: 'smooth' });">Zpět nahoru</a></p>

---

<h2 id="detail-ucetniho-skladu">Detail účetního skladu</h2>

Po prokliku na jakýkoliv sklad z přehledu se zobrazí jeho detail.

- **Kód**: Zobrazuje unikátní kód skladu.
- **Název**: Název skladu.
- **Zákazník**: Pokud je relevantní, může být sklad spojen s konkrétním zákazníkem.
- **Externí kód**: Externí identifikátor skladu.
- **Upravit sklad**: Tlačítko pro přechod do editačního režimu pro úpravu detailů skladu.

<a href="#ciselniky" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/ciselniky/ucetni-sklady-detail.png')">
    <img src="/content/images/ciselniky/ucetni-sklady-detail.png" alt="Účetní sklady detail" width="900" />
</a>

Obrazovka editace účetního skladu:

<a href="#ciselniky" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/ciselniky/ucetni-sklady-editace.png')">
    <img src="/content/images/ciselniky/ucetni-sklady-editace.png" alt="Fyzické sklady" width="900" />
</a>

<p><a href="#ciselniky" class="btn btn-link" onclick="window.scrollTo({ top: 0, behavior: 'smooth' });">Zpět nahoru</a></p>

---

<h2 id="fyzicke-sklady">Fyzické sklady</h2>

[http://10.10.30.4:8080/modules/master-data/plants/](http://10.10.30.4:8080/modules/master-data/plants/)

Fyzický sklad představuje konkrétní fyzickou lokalitu, jako je plocha nebo hala, která slouží k uskladnění zboží.

- **Kód**: Unikátní identifikátor skladu.
- **Název**: Název fyzického skladu (např. "Plocha A", "Hala A").
- **Lokace**: Umístění skladu, může zahrnovat detailní informace o fyzické poloze.
- **Aktivní**: Indikace, zda je daný sklad aktivní.
- **Upravit**: Tlačítko pro přechod na obrazovku pro úpravu informací o konkrétním skladu.
- **Nový fyzický sklad**: Tlačítko v horní části obrazovky umožňuje přidání nového fyzického skladu.

<a href="#ciselniky" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/ciselniky/fyzicke-sklady.png')">
    <img src="/content/images/ciselniky/fyzicke-sklady.png" alt="Fyzické sklady" width="900" />
</a>

Obrazovka založení/editace

<a href="#ciselniky" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/ciselniky/fyzicke-sklady-editace.png')">
    <img src="/content/images/ciselniky/fyzicke-sklady-editace.png" alt="Fyzické sklady" width="900" />
</a>

<p><a href="#ciselniky" class="btn btn-link" onclick="window.scrollTo({ top: 0, behavior: 'smooth' });">Zpět nahoru</a></p>

---

<h2 id="detail-fyzickeho-skladu">Detail fyzického skladu</h2>

Po kliknutí na název skladu se zobrazí detailní informace o vybraném fyzickém skladu.

- **Kód**: Unikátní kód fyzického skladu.
- **Název**: Název skladu (např. "Plocha A").
- **Zákazník**: Pokud je relevantní, může být sklad přidělen konkrétnímu zákazníkovi.
- **Externí kód**: Kód používaný pro externí systémy.
- **Upravit**: Tlačítko pro přechod do režimu editace detailů skladu.

<a href="#ciselniky" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/ciselniky/fyzicke-sklady-detail.png')">
    <img src="/content/images/ciselniky/fyzicke-sklady-detail.png" alt="Fyzické sklady" width="900" />
</a>

<p><a href="#ciselniky" class="btn btn-link" onclick="window.scrollTo({ top: 0, behavior: 'smooth' });">Zpět nahoru</a></p>

---

<h2 id="zony">Zóny</h2>

[http://10.10.30.4:8080/modules/master-data/zones/](http://10.10.30.4:8080/modules/master-data/zones/)

Zóny jsou skupiny skladových lokací, které sdílejí společné vlastnosti nastavení.

<a href="#ciselniky" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/ciselniky/zony.png')">
    <img src="/content/images/ciselniky/zony.png" alt="Zóny" width="900" />
</a>

- **Kód**: Unikátní identifikátor zóny.
- **Název**: Jméno zóny (např. "ANTÉNY").
- **Fyzický sklad**: Název fyzického skladu, ke kterému je zóna přiřazena.
- **Účetní sklady**: Seznam účetních skladů, které jsou spojeny se zónou.
- **Typ zóny**: Určuje funkci zóny, např. "OUTGOING" (výstupní zóna).
- **Aktivní**: Checkbox označující, zda je zóna aktivní.
- **Upravit**: Tlačítko pro přechod na obrazovku pro úpravu detailů zóny.
- **Nová zóna**: Tlačítko v horní části obrazovky slouží k přidání nové zóny do systému.



<p><a href="#ciselniky" class="btn btn-link" onclick="window.scrollTo({ top: 0, behavior: 'smooth' });">Zpět nahoru</a></p>

---

<h2 id="editace-zony">Editace zóny</h2>

Tato obrazovka umožňuje upravit informace o zóně.

<a href="#ciselniky" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/ciselniky/zony-editace.png')">
    <img src="/content/images/ciselniky/zony-editace.png" alt="Zóny" width="900" />
</a>

- **Name**: Pole pro zadání nebo úpravu názvu zóny.
- **Code**: Unikátní kód zóny.
- **Plant**: Fyzický sklad, ke kterému je zóna přiřazena.
- **Warehouses**: Účetní sklady, které jsou k této zóně připojeny.
- **Active**: Checkbox označující, zda je zóna aktivní.
- **OK**: Tlačítko pro potvrzení změn.

<p><a href="#ciselniky" class="btn btn-link" onclick="window.scrollTo({ top: 0, behavior: 'smooth' });">Zpět nahoru</a></p>

---

<h2 id="detail-zony">Detail zóny</h2>

Po kliknutí na název zóny se zobrazí její detailní informace.

<a href="#ciselniky" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/ciselniky/zony-detail.png')">
    <img src="/content/images/ciselniky/zony-detail.png" alt="Zóny Detail" width="900" />
</a>

- **Kód**: Unikátní kód zóny.
- **Název**: Název zóny.
- **Fyzický sklad**: Fyzický sklad, ke kterému je zóna přiřazena.
- **Účetní sklady**: Seznam účetních skladů přidělených zóně.
- **Lokace**: Seznam skladových lokací, které se nacházejí v rámci této zóny. Zde se zobrazují kódy lokací, jejich názvy a třídy (např. "PAL-001").
- **Upravit**: Tlačítko pro přechod na obrazovku pro úpravu zóny.

### Funkčnost
Seznam zón umožňuje přehledně zobrazit a spravovat všechny zóny v systému, včetně přiřazení k fyzickým a účetním skladům.

Detail zóny poskytuje podrobné informace o konkrétní zóně, včetně skladových lokací, které jsou k ní přiřazeny.

Editace zóny umožňuje upravit veškeré údaje týkající se zóny, včetně přiřazených skladů a lokací. Lokace mohou být přidány, odebrány nebo upraveny, stejně tak lze aktualizovat stav zóny (aktivní/blokovaná).

<p><a href="#ciselniky" class="btn btn-link" onclick="window.scrollTo({ top: 0, behavior: 'smooth' });">Zpět nahoru</a></p>

---

<h2 id="lokace">Lokace</h2>

[http://10.10.30.4:8080/modules/master-data/locations/](http://10.10.30.4:8080/modules/master-data/locations/)

Tato obrazovka zobrazuje seznam všech skladových lokací. Lokace jsou fyzická místa ve skladech, kam se ukládá zboží, a jejich kódy jsou tisknuty na štítky a čárové kódy.

<a href="#ciselniky" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/ciselniky/lokace.png')">
    <img src="/content/images/ciselniky/lokace.png" alt="Lokace" width="900" />
</a>

- **Název**: Identifikátor lokace (např. "01-01-01").
- **Kód**: Unikátní kód lokace, který je zobrazen na štítcích a používán v systému.
- **Typ**: Určuje typ lokace (např. "PAL-001" pro paletové místo).
- **Zóna**: Zóna, do které lokace patří (např. "ZA-3007").
- **Účetní sklad**: Účetní sklad, k němuž je lokace přiřazena.
- **Aktivní**: Checkbox indikující, zda je lokace aktivní.
- **Blokovaná**: Určuje, zda je lokace blokována (např. pro příjem zboží).
- **Systémová**: Označuje, zda je lokace systémově spravována.
- **Upravit**: Tlačítko pro přechod na obrazovku pro úpravu lokace.
- **Nová lokace**: Tlačítko v horní části obrazovky slouží k přidání nové skladové lokace.

<a href="#ciselniky" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/ciselniky/lokace-editace.png')">
    <img src="/content/images/ciselniky/lokace-editace.png" alt="Lokace" width="900" />
</a>

Tato obrazovka umožňuje editaci parametrů konkrétní skladové lokace (v tomto případě "01-01-01").

- **Název**: Název lokace.
- **Kód**: Unikátní identifikátor lokace.
- **Zóna**: Zóna, do které lokace patří (např. "ZA-3007").
- **Typ**: Typ lokace (např. "PAL-001" pro paletové místo).
- **Aktivní**: Checkbox označující, zda je lokace aktivní.
- **Blokovaná**: Označuje, zda je lokace blokována.
- **Systémová**: Checkbox indikující, že lokace existuje pouze systémově, nikoliv fyzicky.
- **OK**: Tlačítko pro potvrzení provedených změn.


<p><a href="#ciselniky" class="btn btn-link" onclick="window.scrollTo({ top: 0, behavior: 'smooth' });">Zpět nahoru</a></p>

<h2 id="detail-lokace">Detail lokace</h2>

Tato obrazovka zobrazuje přehled materiálů, které jsou momentálně uloženy v konkrétní skladové lokaci (např. "01-01-01").

<a href="#ciselniky" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/ciselniky/lokace-edetail.png')">
    <img src="/content/images/ciselniky/lokace-detail.png" alt="Lokace detail" width="900" />
</a>

### Materiály:
- **Účetní sklad**: K jakému účetnímu skladu je materiál přiřazen.
- **P/N**: Identifikační číslo materiálu (např. "10101322").
- **Název**: Popis materiálu.
- **GTIN**: Globální identifikátor obchodní položky.
- **Množství**: Kolik jednotek daného materiálu je v lokaci.
- **Short-pick proveden**: Datum a čas, kdy byl proveden případný "short-pick" (krácení výběru).

**Kliknutím na modré texty se lze prokliknout na detail.**

### Kontejnery:
Pokud jsou v lokaci přítomné kontejnery, jsou zde uvedeny:

- **Kód**: Unikátní kód kontejneru.
- **Kontejner P/N**: Part Number produktu v kontejneru.
- **Materiál**: Název materiálu.

### Inventury:
Zobrazuje informace o inventurách, které byly provedeny pro tuto lokaci, včetně:

- **Kód**: Unikátní kód inventury.
- **Přijato**: Datum a čas, kdy byla inventura schválena, a kdo ji schválil.

**Kliknutím na modré texty se lze prokliknout na detail.**

<p><a href="#ciselniky" class="btn btn-link" onclick="window.scrollTo({ top: 0, behavior: 'smooth' });">Zpět nahoru</a></p>

---

<h2 id="typy-lokaci">Typy lokací</h2>

[http://10.10.30.4:8080/modules/master-data/location_types/](http://10.10.30.4:8080/modules/master-data/location_types/)

Tato obrazovka zobrazuje přehled všech typů skladových lokací. Typ lokace označuje vlastnosti, které jsou společné pro určité skupiny skladových lokací.

- **Název**: Název typu lokace (např. "PAL-001").
- **Kód**: Unikátní identifikátor typu lokace.
- **Šířka, Výška, Hloubka**: Rozměry lokace ve skladě (v centimetrech).
- **Nosnost**: Maximální zatížení (v kilogramech), které může být v lokaci uloženo.
- **Upravit**: Tlačítko pro přechod na obrazovku pro úpravu konkrétního typu lokace.
- **Nový typ lokace**: Tlačítko v horní části obrazovky slouží k přidání nového typu lokace.

<a href="#ciselniky" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/ciselniky/lokace-typy.png')">
    <img src="/content/images/ciselniky/lokace-typy.png" alt="Typy lokací" width="900" />
</a>

<p><a href="#ciselniky" class="btn btn-link" onclick="window.scrollTo({ top: 0, behavior: 'smooth' });">Zpět nahoru</a></p>

---

<h2 id="zalozeni-editace-typu-lokace">Založení/Editace typu lokace</h2>

Tato obrazovka umožňuje úpravu parametrů typu lokace.

<a href="#ciselniky" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/ciselniky/lokace-typy-editace.png')">
    <img src="/content/images/ciselniky/lokace-typy-editace.png" alt="Typy lokací" width="900" />
</a>

- **Name**: Pole pro zadání názvu typu lokace (např. "PAL-001").
- **Code**: Unikátní kód pro typ lokace.
- **Width, Height, Depth**: Rozměry lokace v centimetrech (šířka, výška, hloubka).
- **Load capacity**: Maximální nosnost lokace v kilogramech.
- **Equipment type**: Typ vybavení, které je spojeno s tímto typem lokace.
- **OK**: Tlačítko pro potvrzení změn.

<p><a href="#ciselniky" class="btn btn-link" onclick="window.scrollTo({ top: 0, behavior: 'smooth' });">Zpět nahoru</a></p>