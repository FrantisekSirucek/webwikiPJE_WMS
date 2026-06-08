### Replenish

## Obsah sekce

1. [Replenish](#replenish)
   - [Detail replenish jobu](#detail-replenish-jobu)
2. [Proces replenishmentu](#proces_replenishmentu)

<h2 id="replenish">Replenish</h2>
Replenishmen je proces automatizovaného doplňování zásob z lokací pro nadzásobu do lokací pro pickování.
Lokace pro nadzásbou je lokace, kam systém neposílá pickera pro zboží ale slouží k uložení zboží nad požadovanou zásobu. Jsou to lokace, které mají v nastavení zaškrtnutý parametr blokováno. Z pravidla jde o lokace ve vyšších patrech, kam se skladník nedostane jinak než s vysokozdvižnou manipulační technikou. Jinak také SWAP lokace.
Lokace pro pickování jsou lokace, kam tedy systém při běžném picku skladníka posílá, jde o lokace, které nejsou blokované a zpravidla jde o lokace u země. Kam skladník dosáhne rukama. 
Samozřejmě SWAPem můžou být i lokace vzdálené, v jiné budově a podobně dle provozních potřeb. 

Nastavení jaký stav na lokaci má systém hlídat se nastavuje v geo datech produktu v polích minimum pro replenish a maximum pro replenish
minumu znamená, že když zásoba na pickovacích lokacích klesne pod toto minimum tak se vygeneruje replenish
maximum je kolik maximálně ks lze ze SWAP lokace vzít

<a href="#inventury" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/inventury/inventury-radky.png')">
   <img src="/content/images/doklady/replenish/nastaveni_na_produktu.png" alt="nastaveni_na_produktu="900" />
</a>

Pro tento provoz bylo zvolené generování replenishmentu poloautomaticky, tedy na stisk tlačítka v modulu Replenishe. Ve chvíli kdy se stiskne tlačítko Vytvořit replenish joby.
Systém provede kontrolu skladové zásoby přes všechny produkty a lokace a pokud najde materiál s nedostatečnou zásobou na pickovací lokaci a zásobou na SWAP lokaci, tak vygeneruje job pro přeskladnění mezi těmito lokacemi. 
Joby se pak zpracovávají aplikací Replenish

<a href="#inventury" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/inventury/inventury-radky.png')">
   <img src="/content/images/doklady/replenish/modul_replenish.png" alt="modul_replenish="900" />
</a>

Sloupce:
- **Kód:** Unikátní identifikátor jobu (např. "RJ0000081833"). Po kliknutí na kód se zobrazí detailní informace daného jobu. S proklikem [na detail jobu](#detail-replenish-jobu)
- **Priorita:** priorita zpracování jobu, slouží pro řazené jobů v aplikaci
- **Účetní sklad:** účetní sklad pohybu (SAP účetní sklad)
- **Množství:**  počet kusů k přeskladnění ze SWAP na pick lokaci
- **P/N:** wms part number materiálu s proklikem na detail materiálu
- **Název:** Název materiálu s proklikem na detail materiálu
- **Zák. kód:** Part Nuber ze SAP
- **Výr.P/N:** Part number výrobce
- **Zdroj:** Zdrojová (SWAP) lokace
- **Cíl:** Cílová lokace
- **Vytvořeno:** Datum a čas, kdy byla příjemka vytvořena v systému.
- **Vytvořil:** Kdo joby vytvořil (klik na vytvořit)
- **Přiřazeno:** Kdo job zpracovává/al na čtečce
- **Dokončeno:** Datum a čas, kdy byl proces příjmu dokončen.
- **Zrušeno:** Datum a čas, kdy byl případně job stornován

<h3 id="detail-replenish-jobu">Detail replenish jobu</h3>
Obsahuje detailnější informace o pohybu. Jako je případně kontejner nebo číslo šarže a kód pro jedntolivé jobline. Pokud dojde například k rozdělení jobu při potvrzování a vrácení části jobu zpět na SWAP

<a href="#inventury" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/inventury/inventury-radky.png')">
   <img src="/content/images/doklady/replenish/detail_replenish_jobu.png" alt="detail_replenish_jobu="900" />
</a>


<h2 id="replenish">Proces replenishmentu</h2>
Odpovědná osoba jednou za den nechá vygenerovat replenish joby.
Dojde tak ke kontrole, zda je potřeba doplnit na nějaké lokace zásbou aby další dny nestál pick, kvůli nedostatečné zásobě na pick lokacích.
Skladník pak vezme čtečku a spustí dlaždici replenish
Systému mu bude postupně přidělovat vygenerované replenish joby a provede ho přeskladněním. 
Načtením zdrojové lokace a informace jaký produkt z lokace a v jakém množství má vzít
Posláním na cílovou lokaci, kterou načte a zadá kolik kusů produktu na ní reálně dal (vešlo se tam)
V případě, že se nevešlo vše lze zboží potvrdit na jinou libovolnou lokaci nebo zpět na SWAP lokaci. 
