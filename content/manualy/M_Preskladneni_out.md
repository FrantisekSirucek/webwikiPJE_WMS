<h1 id="main"> Postup pro přeskladnění na cizí sklad </h1>

1. [Přeskladnit pryč ze sklad](#preskladneni_ven)
2. [Příjem přeskladnení z jiného skladu](#preskladneni_dovnitr)

Níže jsou popsané postupy jak založit doklad na přeskladnění a vychystat ho směrem ven ze skladu a nebo přijmout přeskladnění, které vytvořil jiný sklad na naše účetní sklady. 
Obecné fungování je takové, že v případě vyskladnění z WMS pryč na cizí účetná sklad se do po založení a vychystání pošle doklad do SAP, kde se založí. A cílový sklad už jen provede druhý krok potvrzení, že zboží přijal. 
Pokud naopak někdo založí pohyb směrem k nám, WMS dostane ze SAP zprávu a tento doklad si natáhne do Příjmu, kde ho potvrdíme. Tím se pošle do SAP potvrzení. 

<h2 id="preskladneni_ven">Přeskladnit pryč ze skaldu</h2>
Pokud potřebuji založit výdej na přeskladnění, jdu do modulu "Doklady" -> "Objednávky" a kliknu na "Create transfer"

!["Vytvořit přeskladnění"](/content/manualy/images/preskl_out_vytvor.png)

Jako první vyberu sklad ze kterého se zboží vydá a sklad na který se má poslat. To se provádí ve vrchní části obrazovky

!["Vyber sklad"](/content/manualy/images/preskl_out_sklady.png)

Následně zadám materiál (SAP PN kompletní včetně 0 na začátku) a počet kusů, které potřebuji přeskladnit. A kliknu na <span style="background-color: green; color:white">Add line</span>

!["Vyber sklad"](/content/manualy/images/preskl_out_material.png)

Na doklad je možné vložit více materiálů ale vždy na zvolený směr (<span style="color: red;">❌</span>tzn nelze udělat jeden řádek z 3009 na 3007 a další řádek z 3007 na 3009)
Když mám vytvořený doklad se všemi položkami, které chci přeskladnit, tak kliknu na <span style="background-color: blue; color:white">Vytvořit</span>

!["Vyber sklad"](/content/manualy/images/preskl_out_vytvoritD.png)

Vytvoří se výdejový doklad, který funguje stejně jako jakýkoli jiný výdej. Od běžného výdeje se liší tím, že jeho WMS id začíná OT. Nyní už postupuji stejně jako při běžném výdeji. Dám <span style="background-color: green; color:white">Aktivovat</span>, tím se vytvoří výdejové joby a vytiskne se skladová výdejka a vyskladnění provedu pomocí aplikace pickování. [Návod zde](#terminal/T_pick).

!["Vyber sklad"](/content/manualy/images/preskl_out_hotovyDoklad.png)

Po vypickování musím ještě doklad odeslat do SAP tlačítkem <span style="background-color: white; color:orange">Dokončit</span>

!["Dokončit a odeslat do SAP"](/content/manualy/images/preskl_out_dokoncit.png)

<h2 id="preskladneni_dovnitr">Příjem přeskladnění na sklad</h2>

Pokud někdo provede přeskladnění k nám na sklad, tak WMS si do modulu [Příjem](#prijemky) doklad s ID začínajícím TR. SAP bohužel udělá co položka to jeden materiálový doklad. 
Pro jeho dokončené a potvrzení si doklad otevřu a dám Po vypickování musím ještě doklad odeslat do SAP tlačítkem <span style="background-color: green; color:white">Dokončit</span>

!["Přijmout"](/content/manualy/images/preskl_in_dokoncit.png)

Po přijmutí se vytvoří skladové joby a potvrdí se příjem do SAP a vytisknou potvrzovací lístky. Materiály pak zaskladním do lokace pomocí aplikace Zaskladnění [Návod zde](#terminal/T_Zaskladneni)

