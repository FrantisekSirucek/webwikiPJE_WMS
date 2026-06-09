<h1 id="main"> Postup stříhání kabelů přes aplikaci ve čtečce </h1>

Aplikace slouží pro rozdělení délky kabelu na dvě různé šarže i mimo pick pro potřeby skladu. 
Pro spuštění aplikace použijeme příslušnou dlaždici.

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Strihani/strihani_dlazdice.png" alt="Dlaždice" width="900" />
</a>

Následně se zobrazí obrazovka, kam načteme buď přímo materiál nebo pokud neznám číslo materiálu tak konkrétní lokaci na které je uložený.

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Strihani/strihani_start.png" alt="Stříhání" width="900" />
</a>

V případě načtení materiálu se zobrazí všechny šarže, které k němu patří a na jaké jsou lokaci. V případě načtení lokace se zobrazí materiály se šaržemi na dané lokaci

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Strihani/strihani_nacten_material.png" alt="načten materiál" width="900" />
</a>

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Strihani/strihani_nacten_lokace.png" alt="načten lokace" width="900" />
</a>

Vyberu požadovanou šarži buď načtením z bubnu, napsání nebo kliknutím v seznamu. A přejdu do obrazvky stříhání. 
Zde v horní části zadám délku v metrech, kterou chci odebrat. A průměr bubnu na který chci tuto délku namotat (není nutné). 
Spodní část se dopočítá automaticky.
Dále zkontroluji SAP plant (obvykle CZ02 pro INS ale nemusí být pravidlem)
A jako psolední vyberu tiskárnu, na kterou chci vytisknout nové štítky na bubny (nebo, že tisknout nechci)

Potvrdím tlačítkem OK. WMS pošle do SAPu volání aby došlo k rozdělení i v SAP a (pokud bylo zadáno) vytisknou se nové štítky na bubny.

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Strihani/strihani_zadani.png" alt="Zadání rozdělení" width="900" />
</a>