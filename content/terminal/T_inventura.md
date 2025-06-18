<h1 id="main"> Postu pro inventarizaci zásob </h1>

1. [Kusová inventura](#inventura)
1. [Inventura seriových čísel](#inventuraSN)


Aplikace pro inventruy slouží primárně k inventarizaci zásob po lokacích. Proces obou inventur je shodný. Uživatel přijde k lokaci, kterou chce inventarizovat a načte její kód. Následně oscanuje a sečte počty všech produktů na lokaci a potvrdí. Tím vytvoří inventurní doklad, který je potřeba následně schválit v modulu [Inventury](#/inventury). 
Dokud nedojde ke schválení inventury, tak opakované načtení lokace bude pořád ukazovat původní stavy produktů.
Rozdíl mezi kusovou inventurou a inventurou sériových čísel je, že při druhé zmiňované budu sečtení serializovaných produktů provádět pomocí scanování jejich SN/UID. Jde o delší proces, který je určen zejména pro velké roční inventury, kde se pak scan SN exportuje a porovnává se systémem SAP. 

<span style="color: #0d6efd;">ℹ️</span>  To ze využít například, pokud jsem udělal inventuru špatně a chci ji předělat ale v takovém případě musím <span style="color: red;">❗</span> nahlásit vedoucím, který doklad nemá schvalovat <span style="color: red;">❗</span>

<span style="color: #0d6efd;">ℹ️</span> Inventura (zejména kusová) lze také využívat k cílené opravě stavu zásob. Lze tak změnit účetní sklad zboží na lokaci nebo šarže. Vždy je ale potřeba nejdříve daný produkt inventárně vydat - tedy udělat ivneturu na 0ks a schválit ji. Následně pak udělat inventuru znovu, kde se zadá správný sklad a šarže produktu.
<span style="color: orange;">⚠️</span> Pokud chci opravit jen jeden produkt a nalokaci je produktů více, musím si dát pozor na to co schvaluji. V takovém případě bych měl buď u ostatních produktů zadat při obou inventurách počet ks bez diference. Nebo na detailu dokladu nejprve schválím jen řádek s produktem. A následně celý doklad (tedy ostatní neschválené řádky) dám <span style="color: red;">❗</span> <span style="background-color: red; color:black">Odmítnout</span>


<h2 id="inventura">Kusová inventura</h2>


---
[Zpět na začátek](#main)

---

<h2 id="inventuraSN">Inventura seriových čísel</h2>


---
[Zpět na začátek](#main)

---


**To be done**