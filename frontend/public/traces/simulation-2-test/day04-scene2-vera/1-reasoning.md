# Reasoning — Vera, Tag 4 Szene 2 (WORK)

## Mein Ansatz

Ich gehe GDD-06 kapitelweise durch und gleiche ab mit GDD-05. Die Kernfrage ist immer: Kann ICH das liefern, und stimmt die technische Beschreibung mit dem überein, was ich visuell entworfen habe?

## Kapitel 1 — Engine & Rendering

**Nanite:** Tobi sagt korrekt, dass Skeletal Meshes kein Nanite unterstützen. Das betrifft mich direkt — alle Charaktere, Kreaturen und NPCs brauchen manuelle LOD-Ketten. Er schreibt "Vera modelliert High-Poly, die LODs werden semi-automatisch generiert." Das stimmt als Workflow, aber er unterschätzt den Aufwand: Die automatischen LOD-Tools produzieren bei organischen Meshes (und unsere Biotech-Elemente SIND organisch) oft Mist. Ich muss mindestens LOD1 manuell kontrollieren, sonst verlieren die Biotech-Adern und Membranstrukturen ihre Lesbarkeit bei mittlerer Distanz.

**Vertex-Animation und Nanite:** KRITISCH. Tobi sagt explizit, dass pulsierende Biotech-Elemente als traditionelle Meshes gebaut werden müssen, weil Nanite keine Vertex-Animation kann. Das betrifft einen RIESIGEN Teil meiner Designsprache. In GDD-05 pulsiert praktisch alles — Adern, Membranen, Leuchtorgane, Biotech-Türen, Kronleuchter. Wenn jedes pulsierende Element ein separates Nicht-Nanite-Mesh sein muss, wird das Level Design extrem fragmentiert. Ich brauche von Tobi eine klare Regel: Was pulsiert (als animiertes Mesh) und was nur leuchtet (als animiertes Material, das MIT Nanite funktioniert)? Die Unterscheidung ist: Vertex-Displacement vs. emissive Pulse via Material. Letzteres geht mit Nanite. Ersteres nicht.

**Lumen:** Passt. HW RT Lumen ist genau richtig für unsere Innenräume. Die Control-Referenz für Lichtstimmung — ja, absolut. Deakins-Prinzip — Tobi hat aufgepasst, sehr gut.

**Farb-Pipeline (ACES):** Gut, dass er das explizit macht. ACES in Substance und Ü5 muss identisch konfiguriert sein. Ich habe in GDD-05 Hex-Codes definiert — die sind sRGB. Frage: Wie verhalten sich meine Hex-Werte in ACES? Muss ich die Palette nochmal in ACES-Werten angeben, oder wird die Konvertierung automatisch gehandelt? Das ist keine akademische Frage — wenn mein Karmin (#8B1A2B) in ACES anders aussieht als in sRGB, stimmt die gesamte Fraktions-Farbsprache nicht mehr.

## Kapitel 4 — Asset-Pipeline

**Modulares Kit-System:** 20-30 Module. Das klingt machbar, ABER: Tobi schreibt, dass die Fraktions-Differenzierung über Material-Instanzen läuft, nicht über separate Meshes. Das funktioniert NUR, wenn die Grundform neutral genug ist. Krone-Architektur hat gotische Spitzbögen. Gilden hat schwere horizontale Blöcke. Orden hat geometrische Perfektion. Diese FORMEN sind fundamental verschieden — da kann ich nicht dasselbe Mesh nehmen und nur das Material tauschen. Ich brauche mindestens 3 Fraktions-spezifische Module (Fenster, Türrahmen, Ornament-Elemente) PLUS neutrale Basis-Module (Wände, Böden, Decken). Das sind nicht 20-30 Module, das sind eher 50-60.

**Fraktions-Farbzuweisung in Kap. 4.1:** PROBLEM. Tobi schreibt "Krone: Warm (Amber, Dunkelgold, Efeugrün)" und "Gilden: Kühle Toene (Blaugrün, Bronze, Schwarz)" und "Orden: Entsättigt (Grau, Weiss, Eisblau)." Das widerspricht meinem Farbsystem in GDD-05 teilweise. Krone ist bei mir Aschgrau/Karmin/Altgold — kein Amber, kein Efeugrün. Gilden ist Warmer Beton/Amber/Cyan — nicht "kühle Toene". Orden ist Kalkweiss/Schieferblau/Bernstein — nicht "Eisblau". Tobi hat die Palette aus dem Gedächtnis beschrieben statt aus GDD-05 abzulesen. Das MUSS korrigiert werden, bevor die ersten Material-Instanzen entstehen.

**HDAs für mich:** Tobi ist ehrlich — "die HDAs müssen WIRKLICH einfach sein." Ja. Bitte. Ich will Parameter schieben, nicht Houdini-Nodes debuggen. Dass er sagt "erste HDA-Version muss in Woche 3 getestet werden" ist gut. Ich halte ihn dran.

**8-12 Vegetations-Assets pro Biom:** Realistisch? Wieviele Biome hat Emre geplant? Wenn es 4 Biome sind, rede ich über 32-48 Vegetations-Assets. Plus die Schattenfieber-Varianten. Plus Architektur-Module. Plus Charaktere, Props, Waffen. Für eine Person ist das ein Mammutprogramm. Tobi erwähnt Megascans als Basis — das hilft bei Vegetation, aber nicht bei fraktionsspezifischen Assets.

## Kapitel 5 — Schattenfieber-Tech

**Fünf Stufen vs. drei Stufen:** In GDD-05 habe ich drei Stufen definiert (Rauschen, Risse, Schwelle), analog zu Namis Narrativsystem. Tobi hat fünf Stufen (0-4). Das ist kein Widerspruch — Stufe 0 ist "rein", und meine drei Stufen mappen auf seine Stufen 1-2 (Rauschen), 3 (Risse), 4 (Schwelle). Aber er verwendet andere Labels: "Gezeichnet", "Infiziert", "Verwandelt", "Entfesselt". Das müssen wir vereinheitlichen, sonst reden wir aneinander vorbei.

**Stufe 3 und 4 — visuelle Komplexität:** Stufe 3 ("Verwandelt") beinhaltet "geometrische Verzerrung am Bildrand", "alternative Geometrie via Custom Stencil Buffer", "fragwürdige NPCs mit Flimmer-Shader." Stufe 4 ("Entfesselt") hat "Vertex-Displacement auf Welt-Geometrie (atmende Wände)", "Doppelbilder", "Farbkanal-Separation", "Parallel-Geometrie: ganze Raum-Segmente in alternativer Version." Das ist technisch beeindruckend, aber ich habe keine Concept-Art-Referenz dafür. Tobi braucht von mir visuelle Targets — und ich muss die erst mal malen. Das ist genau der Engpass, den er selbst in 5.7 erwähnt: "Ohne Referenz baue ich ins Blaue."

**Mein Problem mit Stufe 4:** "NPCs, die möglicherweise nicht existieren, haben identisches Rendering — kein visueller Unterschied zu echten NPCs." Das ist narrativ brilliant, aber für mich als Concept Artist: Wie stelle ich das in einem Concept Sheet dar? Ein NPC, der identisch aussieht, aber nicht existiert? Das ist ein Game-Design- und Tech-Problem, kein Art-Problem. Ich kann dafür kein Concept machen. Was ich KANN: den visuellen Zustand der Welt in Stufe 4 zeigen — die atmenden Wände, die Farbverschiebung, die Auflösung der Architektur. Das ist mein Deliverable.

**Graduelle Interpolation:** Die Float-Kurven-Idee ist elegant. Dass Emre und Nami die Kurven mitgestalten sollen — gut. Aber ich muss die ENDPUNKTE definieren: Was ist der visuelle Zustand bei Wert 0, was bei 25, 50, 75, 100? Das sind fünf Concept Sheets. Minimum.

## Kapitel 8 — Meilensteine & Budget

**Art-Pipeline-Validierung bis Woche 6:** Tobi sagt, das modulare Kit muss bis Woche 6 beweisen, dass es skaliert. Einverstanden. Aber: 3 Concept Sheets bis Ende Pre-Production (Woche 4)? Das ist hart. Drei Concept Sheets PLUS 30+ Architektur-Module PLUS Farbpaletten-Validierung in ACES PLUS Vegetations-Assets — in 4 Wochen? Für eine Person?

**Asset-Bottleneck (Vera):** Tobi nennt das Risiko "MITTEL". Ich würde sagen: HOCH. Ich bin eine Person. Ich mache Concept Art, 3D-Modelling, Texturierung, UI-Mockups. Die Tool-Chain listet Blender, Substance Painter, Photoshop/Krita — alles meine Tools. Aber ich bin EINE Person. Der Vorschlag "ggf. zweiten Artist-Freelancer für 4 Wochen (3.000-4.000 EUR aus Puffer)" klingt nett, aber wann genau? In welcher Phase? Und wer briefed den? Ich, die sowieso schon am Limit ist?

## Zusammenfassung meiner Kritikpunkte

1. FARBPALETTE: Tobis Fraktionsfarben in Kap. 4.1 weichen von GDD-05 ab. Muss korrigiert werden.
2. MODULANZAHL: 20-30 Module reichen nicht für drei visuell fundamental verschiedene Fraktionen. Eher 50-60.
3. VERTEX-ANIMATION VS. EMISSIVE: Brauche klare Abgrenzung, was pulsiert (Mesh) und was leuchtet (Material).
4. SCHATTENFIEBER-STUFEN: Terminologie vereinheitlichen (drei vs. fünf Stufen, verschiedene Labels).
5. CONCEPT-ART FÜR SCHATTENFIEBER: Tobi braucht visuelle Targets, ich brauche Zeit sie zu machen. Das Meeting diese Woche ist Pflicht.
6. ASSET-BOTTLENECK: Risiko ist HOCH, nicht MITTEL. Pipeline-Validierung bis Woche 6 ist ambitioniert.
7. HEX-CODES IN ACES: Muss geklärt werden — mein Farbsystem ist in sRGB definiert.
8. LOD für organische Meshes: Automatische LOD-Generierung reicht für Biotech-Strukturen nicht aus.
