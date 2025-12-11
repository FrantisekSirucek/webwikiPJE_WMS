# Stav skladu

Sekce systému související se stavem zboží na skladě.

## Obsah sekce

1. [Stav skladu](#stav-skladu-prehled)
  - [Popis sloupců](#popis-sloupcu)
  - [Funkce obrazovky](#funkce-obrazovky)


## Přehled stavů skladu

<h2 id="stav-skladu-prehled">Stav skladu</h2>

`http://10.10.30.4/modules/stock-state/`

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/stav-skladu/DODELAT.png')">
   <img src="/content/images/stav-skladu/DODELAT.png" alt="Stav skladu" width="900" />
</a>

Obrazovka "Stav skladu" poskytuje přehled o aktuálním množství materiálů na různých skladových lokacích v rámci celého skladu. Zobrazuje jednotlivé položky uskladněné na konkrétních lokacích spolu s jejich základními identifikačními údaji. Tento přehled slouží především pro kontrolu stavu zásob a pro plánování dalších operací ve skladu, jako je vyskladnění, doplnění zásob nebo inventura.

<h3 id="popis-sloupcu">Popis sloupců</h3>

- **Účetní sklad** – Označuje účetní sklad, do kterého daná lokace patří. To je důležité zejména pro oddělení skladových operací na úrovni účetnictví a fyzického skladu. Kliknutím se dostaneme na detail účetního skladu.
- **Lokace** – Zobrazuje konkrétní skladovou lokaci, na které je daný materiál uskladněn. Může se jednat o konkrétní regál, box nebo jiný fyzický prostor.
- **P/N (Part Number)** – Identifikační číslo produktu (výrobní číslo nebo katalogové číslo), které jednoznačně určuje konkrétní materiál.
- **Název** – Název produktu, což může být jeho obecný popis nebo technický název.
- **GTIN (Global Trade Item Number)** – Mezinárodní standard pro identifikaci obchodních položek. Slouží ke snadné a jednoznačné identifikaci položek napříč různými systémy. (zde obvykle EAN)
- **Množství** – Udává počet kusů daného materiálu, které se aktuálně nacházejí na uvedené lokaci.
- **Short-pick proveden** – Tento sloupec indikuje, zda byl na lokaci proveden short-pick. Pokud zde je datum, znamená to, že skladník nenalezl očekávané množství zboží, což bylo zaznamenáno jako short-pick.

<h3 id="funkce-obrazovky">Funkce obrazovky</h3>

Tato obrazovka umožňuje odpovědným pracovníkům přehledně sledovat aktuální stav zásob na různých lokacích a rychle identifikovat problémy, jako je například nedostatek zboží (short-pick). Zobrazené informace jsou důležité pro plánování vyskladňování a doplňování, stejně jako pro inventarizaci a správu zásob v reálném čase.

Stejně tak se lze prokliknutím na modrý text dostat na detail elementu.

