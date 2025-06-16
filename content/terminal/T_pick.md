**To be done**

# Výdej

Výdej pomocí čtečky probíhá tak, že se rozhodnu zda chci vychystat jeden doklad nebo chci vychystávat více jobů současně. 
Podle toho si zvolím jestli otevřu aplikaci **Pick** nebo **Multipick**
Obě aplikace po zvolení dokladu/dokladů seřadí všechny jednotlivé picky do jedné cesty podle lokací. 

Aplikace **Pick** slouží k vychystání jednoho výdejového jobu. 

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Pick/pick-dlazdice.png" alt="Příjem" width="900" />
</a>

Aplikace **Multipick** umožní zvolení více výdejových jobů a vychystání všech položek z tšchto dokladů najednou. 

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Pick/multipick-dlazdice.png" alt="Příjem" width="900" />
</a>


Po spuštění jedné z aplikací se zobrazí obrazovka, který uživatele vyzve k načtení job(ů), které(ý) chce začít pickovat. 
Nebo si uživatel může nechat nějaký pick přiřadit pomocí modrého tlačítka **Přiřadit z fronty** app **Pick** pak vezme nejstarší job a přiřadího ho uživateli. App **Multipick** vezme až 5 nejstarších jobů a přiřadí je. 

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/doklady/doklady-prijemky.png')">
    <img src="/content/terminal/images/Pick/pick_start.png" alt="NačtiJoby" width="900" />
</a>

V případě **Pick** aplikace po načtení dokladu rovnou jdeme na obrazovku prvního picku
U **Multipick** zezelanají načtené joby a dokud nemám vybrané všechny co chci pokračuji v načítání. Až jsem spokojený, tak kliknu na zelené tlačítko <span style="backround-color:rgb(3, 201, 3) color:rgb(248, 252, 249);"> **Začít**</span>
