<h1 id="main"> Postup zpracování replenishmentu přes aplikaci ve čtečce </h1>

Vygenerované replenishment joby se zpracovávají přes aplikaci Replenish, která se spustí následující dlaždicí. Replenish je prakticky spojení zjednodušeného picku a potvrzování. Probíhají oba pohyby, jak vyskladnění z jedné loakce. Tak zaskladnění na lokaci další. Celým procesem uživatele provede čtečka

<a href="javascript:void(0);" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/terminal/images/Replenish/replenish_dlazdice.png')">
    <img src="/content/terminal/images/Replenish/replenish_dlazdice.png" alt="Dlaždice" width="900" />
</a>

Po spuštění aplikace se dostaneme na obrazovku, kde si zvolíme co jdeme replenishovat. Buď znám číslo jobu, nebo obvykleji: Nechám si přiřadit job z fronty modrým tlačítkem <span style="background-color: blue; color:white">Z fronty</span>

<a href="javascript:void(0);" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/terminal/images/Replenish/replenish_1.png')">
    <img src="/content/terminal/images/Replenish/replenish_1.png" alt="Úvodní obrazovka" width="900" />
</a>

Následuje zobrazení informací co budu doplňovat a odkud kam. Vidím tendy název materiálu, množství k přesunu a zdrojovou a cílovou lokaci. Jako první po mě aplikace chce abych načetkl kód zdrojové lokace.

<a href="javascript:void(0);" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/terminal/images/Replenish/replenish_zdroj.png')">
    <img src="/content/terminal/images/Replenish/replenish_zdroj.png" alt="Zobrazení zdrojové lokace" width="900" />
</a>

následuje výzva k ověření materiálu

<a href="javascript:void(0);" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/terminal/images/Replenish/replenish_over_material.png')">
    <img src="/content/terminal/images/Replenish/replenish_over_material.png" alt="Ověření materiálu" width="900" />
</a>

Poté je potřeba zadat počet ks, které beru z lokace 

<a href="javascript:void(0);" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/terminal/images/Replenish/replenish_pocet_ks.png')">
    <img src="/content/terminal/images/Replenish/replenish_pocet_ks.png" alt="Zadání počtu kusů" width="900" />
</a>

Dalším krokem je fyzické nascanování kodu cílové lokace.

<a href="javascript:void(0);" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/terminal/images/Replenish/replenish_cil.png')">
    <img src="/content/terminal/images/Replenish/replenish_cil.png" alt="Ověření cílové lokace" width="900" />
</a>

zadání počtu ks, které jsem fyzicky vložil na cílovou lokaci

<a href="javascript:void(0);" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/terminal/images/Replenish/replenish_pocet_ks_cil.png')">
    <img src="/content/terminal/images/Replenish/replenish_pocet_ks_cil.png" alt="Zadání počtu kusů" width="900" />
</a>

Pokud jsem zadal veškeré množství, proces se ukončí

<a href="javascript:void(0);" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/terminal/images/Replenish/replenish_konec.png')">
    <img src="/content/terminal/images/Replenish/replenish_konec.png" alt="Konec" width="900" />
</a>

V případě, že ne, vrátím se na předchozí obrazovku. Pak mohu zbylé množství potvrdit jinak nebo zpět na SWAP lokaci
