# Skladové joby

Každý dokument (příjemka, objednávka) má přiřazený job a každá řádka dokumentu odpovídá jedné řádce v jobu (jobline). Job obsahuje informace o tom, které materiály je třeba zpracovat, a jeho řádky popisují jednotlivé položky a jejich manipulaci.

<h2 id="vsechny-skladove-joby">Všechny skladové joby</h2>

`http://10.10.30.4:8080/modules/store-jobs/`

<a href="#" data-bs-toggle="modal" data-bs-target="#imageModal" onclick="showImage('/content/images/skladove-joby/prehled-jobu.png')">
   <img src="/content/images/skladove-joby/prehled-jobu.png" alt="Přehled skladových jobů" width="900" />
</a>

Obrazovka „Všechny skladové joby" slouží k přehledu všech skladových jobů, které systém generuje v rámci různých procesů manipulace s materiálem ve skladu. Joby zde zahrnují vychystávací úlohy (Pick Jobs), úlohy pro doplnění (Replenish Jobs), přesuny materiálů mezi lokacemi (StoreOnLocationJob), balicí úlohy (Packing Jobs), a další.

**Popis jednotlivých sloupců:**
- **Kód:** Jedinečný identifikátor skladového jobu v systému. Každý job má své unikátní číslo, pod kterým je veden.
- **Priorita:** Číselné vyjádření priority, která určuje, jak urgentní je daný job. Priority mohou být použity k tomu, aby skladníci řešili nejdůležitější úkoly jako první.
- **Typ:** Určuje typ jobu:
   - ZPickJob (vychystávací job)
   - StoreOnLocationJob (potvrzení na lokaci)
   - ZPackingJob (balení)
   - ReplenishJob (job pro provedení doplnění pick lokace)
   - Typ jobu ovlivňuje konkrétní činnosti, které se mají provést.
- **Zóna:** Označuje zónu, ve které se job nachází nebo ve které má být proveden. Zóny jsou logicky vymezené části skladu.
- **Vytvořeno:** Datum a čas, kdy byl job vytvořen.
- **Vytvořil:** Uživatel, který job vytvořil. Může to být skladník, vedoucí směny nebo automatický systém.
- **Přiřazeno:** Zobrazuje, ke komu je job aktuálně přiřazen.
- **Přiřazeno k:** Odkazuje na lokaci nebo úlohu, ke které je job přidružen.
- **Dokončeno:** Datum a čas, kdy byl job dokončen.
- **Zrušeno:** Označuje, zda byl job zrušen, a případně zobrazuje čas zrušení.
- **Doklad:** Odkaz na příslušný dokument, ke kterému je job přiřazen (např. objednávka, příjemka).

Obrazovka poskytuje možnost rychlého přehledu a filtrování skladových jobů podle různých kritérií. Skladníci a správci skladu tak mohou snadno monitorovat stav úloh, přidělovat nebo přeřazovat joby, kontrolovat jejich stav dokončení, případně řešit zrušené nebo neúspěšné úlohy.
