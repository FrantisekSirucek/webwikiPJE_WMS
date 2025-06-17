<h1 id="main"> Postup pro přeskladnění přes aplikaci ve čtečce </h1>

1. [Přeskladnění mezi lokacemi v rámci WMS](#preskladneni)
2. [Přeskladnění mezi účetními sklady](#SAP_restorage)

Pro přeskladnění v rámci skladu (baráku) se používají tyto dvě aplikace. Pro čisté přesouvání zboží mezi lokacemi v rámci skladu a účetního skladu stačí aplikace Přeskladnění. 

Pokud je potřeba zboží v rámci baráku přeskladnit na jiný účetní sklad a tuto změnu poslat do SAP, je nutné použít SAP Přeskladnění (SAP Restorage). Tato aplikace slouží právě k tomuto účelu.

<h2 id="preskladneni">Přeskladnění mezi lokacemi v rámci WMS</h2>

Aplikace pro jednoduché přesunutí produktu mezi dvěma lokacemi. Spouští se touto dlaždicí.

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Preskladneni/preskladneni_dlazdice.png" alt="Přeskladnění" width="900" />
</a>

Po spuštění se zobrazí následující obrazovka, která mě vyzve k načtení lokace, ze které zboží přesouvám. (zdrojová lokace). Místo lokace lze také načíst kontejner, ze kterého budu zboží odebírat.

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Preskladneni/preskladneni_scan_zdroj.png" alt="Přeskladnění" width="900" />
</a>

Po nascanování platné lokace se zobrazí seznam všeho co na lokaci (v kontejneru) je. Výběr produktu provedu scanem PN, nebo kliknutím na řádek na displeji, nebo zapsaním pomocí klávesnice.

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Preskladneni/preskladneni_obsah_zdroje.png" alt="Přeskladnění" width="900" />
</a>

Po výběru produktu (který se na lokaci nachází) jsem vyzván k zadání počtu kusů, které chci přesunout. 
> **Poznámka:** Nelze zadat větší počet, než který je na lokaci. Platné zadání je 0 až počet na zdrojové lokaci.

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Preskladneni/preskladneni_zadej_ks.png" alt="Přeskladnění" width="900" />
</a>


Dojdu tedy k této lokaci, vložím do ní produkty a nascanuji její čárový kód. Lokace musí být ve stejném účetním skladě jako zdrojová, jinak systém odmítne operaci provést.
Lze také načíst jiný kontejner, do kterého produkt přesouvám. Nebo načíst tiskárnu a tím se vytvoří nový kontejner. 

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Preskladneni/preskladneni_scan_cil.png" alt="Přeskladnění" width="900" />
</a>

A pokud jsem udělal všechno správně dostanu zelené potvrzení a je hotovo

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Preskladneni/OK.png" alt="Přeskladnění" width="900" />
</a>

[Zpět na začátek](#main)

---


<h2 id="SAP_restorage">Přeskladnění mezi účetními sklady v SAP a WMS</h2>

Aplikace, které slouží pro přesun produktu z jednoho účetního skladu na druhý a tuto změnu provede i v systému SAP. Postup je podobný jako u obyčejného přeskladnění. Ale zde se očekává, že bude cílová lokace (kam přeskladňuji) mít jiný účetní sklad než lokace zdrojová. Zároveň je také v tomto procesu nutné scanovat jednotlivá SN, které přesouvám. To je důležité k tomu aby oba systémy věděli, které konkrétní díly se mají přesunout na jiný účetní sklad. 

Aplikaci zapnu pomocí této dlaždice. 

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Preskladneni/SAPrestorage_dlazdice.png" alt="Přeskladnění" width="900" />
</a>


Po spuštění uvidím, stejně jako u obyčejného přeskladnění, obrazovku, která po mě chce načíst zdrojovou lokaci. 

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Preskladneni/preskladneni_scan_zdroj.png" alt="Přeskladnění" width="900" />
</a>

Po načtení lokace, se také zobrazí seznam všech produktů na lokaci. Pro vzorový přesun jsem vybral lokaci 02-02-02 na účetním skladě 3009. Vyberu tedy položku, která je na lokaci a kterou chci přesunout. (scan, klik na obrazovce).


<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Preskladneni/SAPrestorage_obsah_zdroje.png" alt="Přeskladnění" width="900" />
</a>

A Zobrazí se mi výzva abych zadal počet ks, který budu přesouvat. Zadám v tomto případě například 2ks

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Preskladneni/SAPrestorage_pocet_ks.png" alt="Přeskladnění" width="900" />
</a>

Následně načtu lokaci, kam produkty přesouvám. Lokace by měla být na účetním skladě, kam je chci přesunout. Zde si vyberu třeba lokaci ze 4015

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Preskladneni/SAPrestorage_scan_cil.png" alt="Přeskladnění" width="900" />
</a>

Pokud by lokace, na kterou přesouvám produkty měla možnost více účetních skladů, zobrazí se mi po jejím načtení obrazovka, kde budou vypsané všechny povolené sklady a já vyberu na který chci dané produkty naskladnit.

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Preskladneni/SAPrestorage_sklady.png" alt="Přeskladnění" width="900" />
</a>

A poté bude potřeba nascanovat všechna SN, která jsem vzal a chci přesunout (u kusovek to samozřejmě SN chtít nebude a tento krok bude přeskočen)

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Preskladneni/SAPrestorage_scan_SN.png" alt="Přeskladnění" width="900" />
</a>


A pokud jsem udělal všechno správně dostanu zelené potvrzení a je hotovo

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Preskladneni/OK.png" alt="Přeskladnění" width="900" />
</a>


[Zpět na začátek](#main)


