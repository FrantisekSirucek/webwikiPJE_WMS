<h1 id="main"> Postup pro zaskladnění nového zboží do lokace </h1>

1. [Zaskladnění do lokace](#zaskladneni)

<h2 id="zaskladneni">Zaskladnění do lokace</h2>

Aplikace slouží k potvrzení/zaskladnění nově přijatého zboží do lokací na skladě. Zboží se zaskladňuje pomocé potvrzovacích lístků na kterých je vytištěný barcode skladového jobu. Načtením tohoto čárového kódu se aplikace dozví o jaké jde zboží a z jakého přijmu. Tím umí doporučit a zkontrolovat uložení na lokaci kam je ideální zboží zaskladnit a také aby byl dodržen správný účetní sklad. 

Aplikaci spustím pomocí této dlaždice. 

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Zaskladneni/zaskladneni_dlazdice.png" alt="Přeskladnění" width="900" />
</a>

Jako první krok musím načíst čárový kód z potvrzovacího lístku (nebo z kontejneru, pokud je zboží v kontejneru)

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Zaskladneni/zaskladneni_nacti_job.png" alt="Přeskladnění" width="900" />
</a>

Po načtení se mi zobrazí jaký materiál k jobu patří, ten načtu. Tím potvrdím, že se mi nepomíchali potvrzovací lístky.

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Zaskladneni/zaskladneni_produkt.png" alt="Přeskladnění" width="900" />
</a>

Potom mi aplikace nabídne seznam lokací, kde už daný produkt je. Cílem je udržovat produkty u sebe, tedy aby to nebyl extrém jako na příkladu! Takže ideálně vyberu lokaci, kde již produkt je. Dojdu k ní a načtu ji.

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Zaskladneni/zaskladneni_seznam_lokaci.png" alt="Přeskladnění" width="900" />
</a>

Potom zadám počet ks, který chci na lokaci potvrdit. Počet může být i menší. Pokud zadám menší počet. Například se celé množství na lokaci nevejde. Tak mě pak systém vyzve k načtení další lokace a zadaní kusů. A takto tak dlouho, dokud nepotvrdím všechny kusy. Lze tedy množství rozdělit mezi více lokací. 

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Zaskladneni/zaskladneni_pocet.png" alt="Přeskladnění" width="900" />
</a>

Po zaskladnění celého množství se dostanu zpět na úvodní obrazovku se zeleným potvrzením, že je hotovo

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Zaskladneni/zaskladneni_OK.png" alt="Přeskladnění" width="900" />
</a>


[Zpět na začátek](#main)

---
