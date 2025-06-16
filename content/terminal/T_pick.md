1. [Průběh procesu výdeje](#vydej_terminalem)
2. [Chyby a jejich řešení](#vydej_chyby)


<h2 id="vydej_terminalem">Průběh procesu výdeje</h2>

Výdej pomocí čtečky probíhá tak, že se rozhodnu, zda chci vychystat jeden doklad, nebo chci vychystávat více jobů současně.  
Podle toho si zvolím, jestli otevřu aplikaci **Pick** nebo **Multipick**.  
Obě aplikace po zvolení dokladu/dokladů seřadí všechny jednotlivé picky do jedné cesty podle lokací.

Aplikace **Pick** slouží k vychystání jednoho výdejového jobu.

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Pick/pick_dlazdice.png" alt="Pick" width="900" />
</a>

Aplikace **Multipick** umožní zvolení více výdejových jobů a vychystání všech položek z těchto dokladů najednou. 

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Pick/multipick_dlazdice.png" alt="Pick" width="900" />
</a>

Po spuštění jedné z aplikací se zobrazí obrazovka, která uživatele vyzve k načtení job(ů), které(ý) chce začít pickovat. 
Nebo si uživatel může nechat nějaký pick přiřadit pomocí modrého tlačítka **Přiřadit z fronty**. App **Pick** pak vezme nejstarší job a přiřadí ho uživateli. App **Multipick** vezme až 5 nejstarších jobů a přiřadí je.

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Pick/pick_start.png" alt="NačtiJoby" width="900" />
</a>

V případě **Pick** aplikace po načtení dokladu rovnou jdeme na obrazovku prvního picku.  
U **Multipick** zezelenají načtené joby a dokud nemám vybrané všechny, co chci, pokračuji v načítání. Až jsem spokojený, tak kliknu na zelené tlačítko <strong><span style="background-color:rgb(3, 201, 3); color:rgb(248, 252, 249);">Začít</span></strong>

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Pick/multipick_start.png" alt="NačtiJoby" width="900" />
</a>

Čtečka nás následně pošle na lokaci, ze které máme produkt vzít, a bude vyžadovat načtení lokace jako potvrzení, že bereme produkt ze správné.

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Pick/pick_scan_lokace.png" alt="NačtiJoby" width="900" />
</a>

Po úspěšném ověření lokace musíme ověřit, že bereme správný produkt.

Pokud produkt má SN (UIID), tak nás čtečka rovnou vyzve k načtení SN/UIID. 

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Pick/pick_scan_SN.png" alt="NačtiJoby" width="900" />
</a>

Pokud pickujeme produkt, který se neeviduje na sériová čísla, tedy kusovku nebo kabel, nejprve nás čtečka vyzve k načtení produktového kódu jako ověření, že máme správný produkt. 

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Pick/pick_overeni_nonsn.png" alt="NačtiJoby" width="900" />
</a>

Následně nás vyzve k zadání počtu kusů v případě kusovky. Je potřeba zadat přesně ten počet, který máme z dané lokace vzít. Čtečka nás nepustí vzít více nebo méně. V případě, že zadáme méně kusů, nebo klikneme na tlačítko <span style="color:red;">SHORTPICK</span>, systému tím řekneme, že produkt na lokaci není nebo je ho málo. V takovém případě se systém pokusí najít náhradní lokaci a zařadit ji do picku. Nebo se dokončí pick bez tohoto a uživatel bude na konci upozorněn, že to má před odesláním do SAP vyřešit. 

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Pick/pick_zadej_pocet.png" alt="NačtiJoby" width="900" />
</a>

V případě MCFE - kabelů - produktů nás čtečka vyzve k načtení cívky (šarže/batch), ze které budeme požadované množství do výdeje odebírat.
<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Pick/pick_vydej_mcfe.png" alt="NačtiJoby" width="900" />
</a>

Následně se spustí aplikace přešaržování (stříhání) kabelů, kde je ve vrchní části předvyplněno, kolik metrů mám odebrat a případně zadám průměr bubnu, na který dané množství namotám.  
Ve spodní části vidím, kolik metrů a na jakém bubnu zbyde. V případě potřeby může některé údaje změnit. 

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Pick/pick_vydej_mcfe_strih.png" alt="NačtiJoby" width="900" />
</a>

Tím je dokončen pick jedné položky jobu a pokračujeme stejným procesem pickovat všechny zbývající položky.  
Když jsou všechny položky vypickované, čtečka nás vyzve k odložení materiálů na lokaci výdeje a k jejímu načtení. 

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Pick/pick_konec_scan_vydej.png" alt="NačtiJoby" width="900" />
</a>

Pokud všechno proběhlo v pořádku, systém nám zobrazí zelenou hlášku <strong><span style="color:rgb(39, 78, 2); background-color:rgb(186, 245, 131);">OK</span></strong> 

<h2 id="vydej_chyby">Chyby a jejich řešení</h2>

<span style="color: rgb(245, 173, 173); background-color rgb(252, 7, 7)">    SAP returned: Material 40840938 CZ03 3004 does not exist   </span>

**Vysvětlení:** SAP říká, že daná kombinace materiálu a skladu neexistuje. Pravděpodobná příčina je, že v SAP je materiál na jiném účetním skladě nebo není vůbec. 
**Možná náprava:** Upravit stav v SAPu, nebo vypickovat výdej znovu bez tohoto materiálu. 

<span style="color: rgb(245, 173, 173); background-color rgb(252, 7, 7)">    	SAP returned: Enter batch (Original SAP message M7_018).In case of GI, ensure that all provided equipments exist. Non existent UIIs(limited by 100 entries):CZUI-CR9X363381-000000000040920091.   </span>

**Vysvětlení:** SAP říká, že daná kombinace materiálu UDI neexistuje. Dané SN má nejspíš v SAP přiřazené jiné UID
**Možná náprava:** Upravit stav v SAPu, UID na daném SN, nebo vypickovat jiné SN. - tato chyba by měla být vyřešena a už by se v budoucnu neměla opakovat


<span style="color: rgb(245, 173, 173); background-color rgb(252, 7, 7)">    	SAP returned: Batch 47101035 CZ02 NEW does not exist   </span>

**Vysvětlení:** SAP říká, že daná šarže daného materiálu není v SAP skladem
**Možná náprava:** Naskladnit danou šarži do SAP nebo opravit šarži ve WMS a vypickovat Order znovu. 

