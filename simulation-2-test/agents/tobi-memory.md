# Tobi — Memory

<!-- GM aktualisiert diese Datei nach jeder Szene aus Tobis Perspektive -->

## Tag 1, Szene 1 (BRIEFING)
Habe nach Engine-Festlegung gefragt. Arbeite mit UE5 als Annahme.

## Tag 1, Szene 2 (WORK)
Machbarkeitsanalyse V0.1 fertig. Drei kritische Engpässe: (1) Kein Gameplay-Programmer — Melee Combat braucht Middleware oder Freelancer. (2) Asset-Produktion — Vera allein reicht nicht, modulares Design + Marketplace + prozedurale Systeme sind Pflicht. (3) Scope — empfehle Semi-Open-World (4-6 km², Gothic-Stil). Kamerasystem: TP als Primärmodus, echtes FP verdoppelt Animationsaufwand.

## Tag 1, Szene 3 (MEETING)
UE5 bestätigt. Semi-Open-World bestätigt. TP Primärmodus bestätigt, FP ist V2. Alle drei lösen meine größten Scope-Concerns. Heute Nachmittag: Pipeline-Architektur beginnen. Modulare Asset-Pipeline mit Nanite, Houdini-Terrain, PCG-Vegetation als Kern.

## Tag 1, Szene 5 (WORK)
Pipeline-Architektur V0.1 fertig: Nanite hybrid (Hard-Surface + traditionelle Vegetation), Lumen GI (HW RT Shipping, Software Fallback), Spring Arm Kamera mit drei Kontext-Modi, GAS als Combat-Basis, Motion Matching. Schattenfieber als eigener Post-Processing-Layer.

## Tag 1, Szene 6 (REVIEW)
CD: PC first, Konsolen Stretch Goal. Freelancer-Budget für Gameplay-Programmer. Singleplayer bestätigt (implizit). Morgen: Pipeline-Bibel V1 beginnen, Kamera-Prototyp in UE5 skizzieren.

## Tag 2, Szene 1 (BRIEFING)
Konzeptionstag. GDD-06 Technik & Produktion als V1-Outline vorbereiten.

## Tag 2, Szene 2 (WORK)
GDD-06 Outline: 8 Kapitel — Engine & Rendering (UE5, Nanite, Lumen), Kamerasystem (Spring Arm, 4 Modi), Combat-Architektur (GAS), Asset-Pipeline (Houdini, modulares Kit), Schattenfieber-Tech (Post-Processing), Performance (3 Tiers), Produktions-Pipeline, Meilensteine + Budget.

## Tag 2, Szene 3 (MEETING)
Pipeline-Architektur vorgestellt. Darius fragt nach GAS-Flexibilität für Schattenfieber-Abilities. Antwort: GAS kann das, braucht aber eigene Ability-Kategorie.

## Tag 2, Szene 5 (WORK)
GDD-06 Outline erweitert. Budget-Schätzung: 45k EUR Freelancer-Budget für Gameplay-Programmer (6 Monate, Melee-Combat + GAS). Schattenfieber-Tech detailliert: Custom Post-Processing Stack, Material Parameter Collection, 5 Shader-Stufen.

## Tag 2, Szene 6 (REVIEW)
CD akzeptiert 45k Budget-Schätzung. Morgen: GDD-06 als vollständige V1 schreiben.

## Tag 3, Szene 1 (BRIEFING)
Produktionstag. GDD-06 Technik V1 schreiben.

## Tag 3, Szene 2 (WORK)
GDD-06 Technik & Produktion V1 fertig. 8 Kapitel komplett: Engine (UE5.3+, Nanite hybrid, Lumen GI), Kamera (Spring Arm, 4 Kontext-Modi), Combat (GAS-basiert, Motion Matching), Asset-Pipeline (Houdini-Terrain, modulare Kits), Schattenfieber-Tech (5 Shader-Stufen), Performance (3 Tiers: 1080p30 bis 4K60), Produktions-Pipeline, Meilensteine + 45k EUR Budget.

## Tag 3, Szene 4 (PAUSE)
Mittagspause mit Finn und Darius. Freelancer-Profil diskutiert: GAS-Erfahrung Pflicht, Motion Matching Bonus, Melee-Combat ideal. Darius kennt Ex-Blue-Byte-Kollegen. Finn kontaktiert den heute Abend.

## Tag 3, Szene 5 (WORK)
Nachmittags: GDD-06 mit Schattenfieber-Tech-Details ergänzt. Darius' GDD-02 technisch gegengelesen — 5 Infektionsstufen sind mit Shader-System machbar. Offener Punkt: Partikelsystem für Stufe 4+5 muss nächste Woche detailliert werden.

## Tag 3, Szene 6 (REVIEW)
Sechs V1-Dokumente fertig. Performance-Budget passt. Nächste Woche: V2 mit Partikelsystem-Details, Kamera-Prototyp beginnen.

## Tag 4, Szene 1 (BRIEFING)
Peer-Review-Tag. Reviewe Emres WBB-01 Mythos aus technischer Perspektive.

## Tag 4, Szene 2 (WORK)
Peer-Review WBB-01 fertig. Sechs Lore-Elemente mit technischen Implikationen: (1) KRITISCH — Drei-Schichten-Modell braucht Rendering-Strategie: Mittelgrund=Level-Geometrie, Hohlicht/Stillfeld=Post-Processing-Layer + 3-5 handgebaute alternative Geometrie-Segmente. Fehlt in GDD-06 V1 komplett. (2) HOCH — Hauten-Shader: SSS + Vertex-Displacement + Spieler-Reaktivität, KEIN Nanite. (3) HOCH — Zwei Schattenfieber-Farbprofile statt einem (Stillfeld=kalt, Hohlicht=warm). (4) MITTEL — Lebende Krone: S-Tier Hero-Asset, ~19-27 Arbeitstage Vera+Tobi. (5) MITTEL — Flechtungs-VFX-Set (Niagara Ribbon + Houdini Wire). (6) NIEDRIG — Emer-Korrespondenz-Shader. Veras Review meiner GDD-06: Farbpalette falsch (muss Hex-Codes aus GDD-05 1:1 übernehmen), Modulanzahl zu niedrig, ACES-Farbcheck nötig.

## Tag 4, Szene 3 (MEETING)
Standup. CD bestätigt Stufengrenzen: Rauschen 1-40, Risse 41-75, Schwelle 76-100, Halluzinations-Start 76. Nachmittags: GDD-06 V2 (Hex-Codes fixen, Module 60, Drei-Schichten-Rendering, Hauten-Shader, zwei Farbprofile).

## Tag 4, Szene 5 (WORK)
GDD-06 V2: Hex-Codes aus GDD-05 1:1 übernommen, Module auf ~60 (20 neutral + 40 fraktionsspezifisch), Drei-Schichten-Rendering (Mittelgrund=Level, Hohlicht/Stillfeld=PP-Layer + 3-5 handgebaute Segmente), Hauten-Shader (SSS + WPO + Spieler-Reaktivität, Nanite-Ausnahme), zwei Schattenfieber-Farbprofile (Stillfeld-kalt, Hohlicht-warm), Halluzinations-Start auf 76 korrigiert.

## Tag 4, Szene 6 (D&D)
D&D-Session. Entspannt. Emres NPC Toves war interessant — fraktionslos. Leos doppelte 1 war der Comedy-Moment des Tages.

## Tag 5, Szene 1 (BRIEFING)
Freitag. V2 finalisieren, abends Wochen-Review. Mein Fokus: GDD-06 V2 finalisieren.

## Tag 5, Szene 2 (WORK)
GDD-06 V2 finalisiert. Korrekturen: Halluzinations-Start von 70 auf 76, Stufen-Tabelle auf CD-Grenzen (1-40/41-75/76-100). Neu: Hauten-Shader-Architektur (Burley-SSS + WPO, Nanite-Ausnahmen), Drei-Schichten-Rendering (5 PP-Volume-Profile), Hex-Code-Tabellen 1:1 aus GDD-05, Anforderungsprofil Gameplay-Programmer (GAS als Ausschlusskriterium). Offener Punkt: Hauten-Segmentanzahl 3 oder 5 — braucht Emres Bestätigung.

## Tag 5, Szene 3 (MEETING)
Standup. GDD-06 V2 sauber, keine Beanstandungen. Ymir→Emer Fix in GDD-02 übernimmt Leo. Stufenzahl offen. Nachmittags Review-Vorbereitung.

## Tag 5, Szene 4 (PAUSE)
Mittagspause mit Vera. Rho: Vera plant Balancepunkt-Design — anderer Schwerpunkt, Kopf dreht sich statt Schultern. Clothing Physics müssen custom sein. Schweigehaus: Veras "Fehler-als-Weltaussage" ist stark. Mein Beitrag: Lumen-Schatten, die geometrisch nicht zur Außen-Hülle passen. Spieler liest es als Fehler in der Welt, nicht als Bug. Nächste Woche zusammen an Schweigehaus-Konzept.
