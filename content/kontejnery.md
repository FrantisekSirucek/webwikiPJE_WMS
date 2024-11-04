# Kontejnery

2. [Kontejnery (Master Obaly)](#kontejnery)
  - [Detail kontejneru](#detail-kontejneru)


<h2 id="kontejnery">Kontejnery (Master Obaly)</h2>

`http://10.10.30.4:8080/modules/stock-state/containers/`

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/stav-skladu/DODELAT.png')">
   <img src="/content/images/stav-skladu/DODELAT.png" alt="Kontejnery" width="900" />
</a>

Kontejnery jsou logickou jednotkou ve skladovém systému, která seskupuje určitý počet materiálů do jednoho celku s jedinečným identifikátorem. Tento identifikátor (obvykle ve formátu "HU + číslo") umožňuje jednoduše manipulovat s celou skupinou materiálů najednou. Zároveň sleduje polohu všech materiálů, které jsou v tomto kontejneru obsaženy.

Použití kontejnerů zjednodušuje procesy jako příjem, zaskladňování, vychystávání a expedici, protože místo manipulace s jednotlivými kusy materiálu se provádí operace na úrovni celého kontejneru.

Na této obrazovce je zobrazen seznam všech aktuálních kontejnerů v systému. Každý kontejner je identifikován svým kódem (HU kód), lokaci, kde se nachází, datem vytvoření a uživatelem, který kontejner vytvořil.

**Sloupce:**
- **Kód:** Tento sloupec obsahuje jedinečný identifikátor každého kontejneru. Kódy jsou ve formátu "HU" následovaném číslem, které představuje daný kontejner. Kliknutím na kód lze zobrazit detailní informace o kontejneru.
- **Lokace:** Zde se nachází kód lokace, kde je kontejner fyzicky uložen. Toto místo je důležité pro manipulaci a přehled o rozmístění materiálů ve skladu.
- **Vytvořeno:** Tento sloupec zobrazuje datum a čas, kdy byl kontejner vytvořen. To poskytuje přehled o tom, jak dlouho je kontejner ve skladu.
- **Vytvořil:** Uvádí uživatelské jméno nebo identifikátor osoby, která kontejner vytvořila, což je důležité pro sledování odpovědnosti a audity.
- **Účetní sklad:** Tento sloupec zobrazuje účetní sklad, pod který kontejner spadá. Je to důležité pro finanční a logistické sledování materiálů.

<h3 id="detail-kontejneru">Detail kontejneru</h3>

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/stav-skladu/DODELAT.png')">
   <img src="/content/images/stav-skladu/DODELAT.png" alt="Detail kontejneru" width="900" />
</a>

Tato obrazovka zobrazuje detail konkrétního kontejneru s kódem "HU0000010335". Struktura obrazovky je následující:

**Horní část obrazovky:**
- **Lokace:** Zobrazuje, kde je kontejner fyzicky uložen ve skladu. V tomto případě je to lokace "01-01-04".

**Sekce Materiály:**

Tato část obsahuje souhrn materiálů v kontejneru.
- **P/N (Part Number):** Unikátní identifikátor materiálu. Kliknutím na tento odkaz se zobrazí detailní informace o materiálu.
- **Název:** Popis nebo název daného materiálu. V tomto případě je to "BRU5000 Box".
- **GTIN:** Globální číslo obchodní položky, pokud je k dispozici. Tento sloupec je v tomto případě prázdný.
- **Množství:** Počet jednotek materiálu v kontejneru. Například, zde je 3 kusy "BRU5000 Box".
- **Short-pick proveden:** Indikuje, zda byl na této pozici proveden short-pick. Tento kontejner žádný short-pick nemá.

**Sekce Položky:**

Zde jsou uvedeny jednotlivé položky v rámci materiálů, které mají specifické identifikátory, jako jsou SN (Sériové číslo) a UID (Unikátní identifikátor).
- **P/N:** Opět identifikátor materiálu.
- **Název:** Popis materiálu.
- **Zák. P/N:** Zákaznický Part Number (pokud je vyžadován).
- **SN:** Sériové číslo jednotlivých položek. To umožňuje sledovat konkrétní kusy materiálu.
- **UIID:** Unikátní identifikátor, který pomáhá s identifikací specifických jednotek materiálu v rámci kontejneru.

Tato obrazovka poskytuje přehled o veškerých detailech týkajících se materiálu a jeho jednotlivých položek, které jsou uloženy v daném kontejneru.