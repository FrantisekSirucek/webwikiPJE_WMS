<h1> Postup picku aplikací pro čtečky k WMS </h2>

1. [Přeskladnění mezi lokacemi v rámci WMS](#preskladneni)
2. [Přeskladnění mezi účetními sklady](#SAP_restorage)

Pro přeskladnění v rámci skladu (baráku) se používají tyto dvě aplikace. Pro čistě přesouvání zboží mezi lokacemi v rámci skladu a účetního skladu stačí aplikace přeskladnění. Poku je potřeba zboží v rámci baráku přeskladnit na jiný účetní sklad a tuto změnu poslat do SAP. Tak pak je potřeba použít SAP Přeskladnění (SAP Restorage), která slouží k tomuto účelu. 

<h2 id="preskladneni">Přeskladnění mezi lokacemi v rámci WMS</h2>

Aplikace pro jednoduché přesunutí produktu mezi dvěma lokacemi. Spouští se touto dlaždicí.

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Preskladneni/preskladneni_dlazdice.png" alt="Pick" width="900" />
</a>

Po spuštění se zobrazí následující obrazovka, která mě vyzve k načtení lokace, ze které zboží přesouvám. (zdrojová lokace). Místo lokace lze také načíst kontejner, ze kterého budu zboží odebírat.

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Preskladneni/preskladneni_scan_zdroj.png" alt="Pick" width="900" />
</a>

Po nascanování platné lokace se zobrazí seznam všeho co na lokaci (v kontejneru) je. Výběr produktu provedu scanem PN, nebo kliknutím na řádek na displeji, nebo zapsaním pomocí klávesnice.

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Preskladneni/preskladneni_obsah_zdroje.png" alt="Pick" width="900" />
</a>

Po výběru produktu (který se na lokaci nachází) jsem vyzván k zadání počtu kusů, které chci přesunout. 

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Preskladneni/preskladneni__zadej_ks.png" alt="Pick" width="900" />
</a>

Po zadání počtu ks, které chci přesunout (samozžřejmě nelze zadat větší počet, než který na lokaci je. Platné zadání ja 0 až počet na zdrojové lokaci). Jsem vyzván k načtení lokace na kterou chci materiál přesunout. Dojdu tedy k této loakci, vložím do ní produkty a nascanuji její čárový kód. Lokace musí být ve stejném účetním skladě jako zdrojová, jinak systém odmítne operaci provést. 

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Preskladneni/preskladneni_dlazdice.png" alt="Pick" width="900" />
</a>

A pokud jsem udělal všchno správně dostanu zelené potvrzení a je hotovo

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Preskladneni/OK.png" alt="Pick" width="900" />
</a>

---


<h2 id="SAP_restorage">Přeskladnění mezi účetními sklady v SAP a WMS</h2>

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Preskladneni/SAPrestorage_dlazdice.png" alt="Pick" width="900" />
</a>


**To be done**

