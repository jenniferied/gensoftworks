# Peer-Review: WBB-01 Mythos (V1) — Technische Perspektive

**Reviewer**: Tobi Richter, Technical Artist
**Dokument**: WBB-01 Mythos V1 (Emre Yilmaz)
**Datum**: Tag 4 (Donnerstag), Szene 2
**Referenz**: GDD-06 Technik & Produktion V1

---

## Gesamteindruck

Emre, das Dokument ist stark. Die Kapitel 1-4 als Fliesstext sind auf einem Niveau, das ich bei einem V1-Draft nicht erwartet hätte. Die interne Logik ist konsistent — Emer-Körper als Welt, Hauten als lebende Membranen, Flechtung als biologischer Prozess, Faulung als dessen Zerfall. Das hängt alles zusammen.

Aber: Deine Texte erzeugen technische Anforderungen, die in meiner GDD-06 V1 noch nicht abgebildet sind. Das ist nicht dein Problem — es ist meins. Dieses Review listet die Stellen auf, an denen deine Lore meine Pipeline-Planung verändert.

---

## 1. Lore-Elemente mit technischen Implikationen

### 1.1 Drei-Schichten-Modell (Kap. 3) — KRITISCH

**Was du schreibst**: Hohlicht, Mittelgrund, Stillfeld als drei überlagerte Realitätsebenen, getrennt durch die Hauten. Fragmente der anderen Schichten werden bei dünnen Hauten wahrnehmbar.

**Was das technisch bedeutet**: Wir brauchen eine Rendering-Strategie für drei Realitätszustände auf EINER Geometrie-Basis.

**Mein Vorschlag (Hybridlösung)**:
- **Mittelgrund** = die eine Level-Geometrie, die Vera baut und in der der Spieler sich bewegt.
- **Hohlicht-Fragmente** = Post-Processing-Layer (warmes Gold, Licht ohne Quelle, erhöhte Sichtbarkeit). Kein eigenes Level, sondern ein visueller Zustand, der auf die bestehende Geometrie gerendert wird.
- **Stillfeld-Fragmente** = Post-Processing-Layer (Entsättigung, Erosion-Partikel, Auflösung von Kanten). Ebenfalls kein eigenes Level.
- **Ausnahme**: An 3-5 narrativ kritischen Orten gibt es tatsächliche alternative Geometrie-Segmente (Custom Stencil Buffer). Diese müssen handgebaut werden — das sind Hero-Locations.

**ACHTUNG**: In GDD-06 V1 fehlt diese Strategie komplett. Ich habe Schattenfieber-Rendering, aber keine kosmologische Rendering-Architektur. Das ändert sich in V2.

**Was ich von dir brauche**: Welche 3-5 Orte wären narrativ so wichtig, dass der Spieler dort tatsächlich "in eine andere Schicht blickt" — nicht nur als Farbfilter, sondern als sichtbar veränderte Umgebung? Das bestimmt, wie viel alternative Geometrie wir bauen müssen.

### 1.2 Die Hauten (Kap. 3) — HOCH

**Was du schreibst**: "Die Hauten sind lebendig. Sie atmen. Sie pulsieren. Sie reagieren auf das, was sie berührt."

**Was das technisch bedeutet**: Ein eigenes Shader-System für organische, reaktive Membranen.

- **Subsurface Scattering** für organische Transluzenz (Licht scheint DURCH die Membran, wie durch echte Haut)
- **Vertex-Displacement** für Pulsieren und Atmen — das heisst: Hauten-Meshes können NICHT mit Nanite gerendert werden (Nanite unterstützt kein World Position Offset). Muss in der Asset-Pipeline als Ausnahme behandelt werden.
- **Spieler-Reaktivität**: Material Parameter Collection mit Spieler-Weltposition als Eingabe. Die Haut reagiert auf Nähe — Pulsieren wird stärker, Transluzenz nimmt zu.
- **Niagara-Partikel** an den Rändern: Sporen, Fasern, organische Fragmente.

**Was in GDD-06 V2 rein muss**: Eigenes Unterkapitel "Hauten-Shader" mit Material-Spezifikation. Ausnahme von der Nanite-Pipeline dokumentieren.

**Was ich von dir und Vera brauche**: Visuelle Referenz. "Lebendig, atmend, pulsierend" ist poetisch — ich brauche eine Concept-Skizze oder zumindest einen Vergleichsreferenzpunkt. Denken wir an Quallen-Gewebe? An Fruchtblase? An Spinnennetz? Die Antwort bestimmt den Shader-Ansatz.

### 1.3 Die Flechtung als visuelles Motiv (Kap. 4) — MITTEL

**Was du schreibst**: "Die Vorfahren zogen Fäden aus dem Emer-Material und verwoben sie zu Membranen."

**Was das technisch bedeutet**: Ein VFX-Set für fadenartige, organische Strukturen.

- **Niagara Ribbon Particles** für Faden-Effekte in Echtzeit
- **Houdini Wire Solver** für vorberechnete Flechtungs-Animationen (Bake to Alembic, abspielen in Ü5 Sequencer — z.B. für Cinematics)
- **Environment-Detail**: Sichtbare "Flechtreste" in befallenen Zonen als statische Meshes mit emissivem Material und leichter Pulse-Animation

In GDD-06 V1 nicht eingeplant. Aufwand: mittel, aber es ist ein eigenständiges Asset-Set, das Vera und ich gemeinsam bauen müssen.

### 1.4 Emer-Körper-Korrespondenzen (Kap. 2) — MITTEL

**Was du schreibst**: Fleisch = Erde, Blut = Gewässer, Knochen = Gebirge, Schädel = Himmelskuppel, Hirn = Wolken/Nebel.

**Was das technisch bedeutet**: An bestimmten Stellen soll die Landschaft "körperlich" wirken. Das ist primär ein Art-Direction-Thema (Vera), aber es hat technische Implikationen:

- **Terrain-Material**: Zusätzliche Layer für Übergänge zwischen geologischem und organischem Material. Jeder Layer kostet Performance (~0.1 ms pro Layer). Aktuell 6-8 Layer geplant; möglicherweise 10-12 nötig.
- **Wasser-Shader**: Emre schreibt "Adern des Mittelgrunds, die noch immer pulsieren". Ein Custom Water Material mit zeitbasiertem Displacement (subtiler Puls). Funktioniert als Erweiterung des Ü5 Water Systems. Aufwand: gering.
- **Volumetrischer Nebel**: "Gedanken des Emer, zerrissen und formlos" — das ist Niagara Volumetric Fog mit hoher Turbulenz und langsamer Drift. GPU-teuer. Muss ins Performance-Budget (geschätzt +0.3-0.5 ms).

### 1.5 Schattenfieber — Zwei Farbprofile statt einem (Kap. 3, 6) — HOCH

**Was sich ändert**: In GDD-06 V1 habe ich EINEN generischen Farbshift definiert (kühler/bläulicher mit steigendem Infektionswert). Emres Mythos zeigt: Das ist zu simpel.

- **Stillfeld-Durchscheinen**: Kalt, entsättigt, auflösend — mein bisheriger Farbshift passt hier.
- **Hohlicht-Durchscheinen**: Warm, golden, übersättigt — das ist ein ZWEITES Farbprofil, das in V1 fehlt.

Konsequenz für GDD-06 V2: Zwei Schattenfieber-Farbprofile, kontextabhängig. In Stillfeld-nahen Zonen kalte Verschiebung, in Hohlicht-nahen Zonen warme. Der Infektionswert bestimmt die INTENSITÄT, der Kontext die RICHTUNG.

Technisch simpel (zwei Lerp-Targets statt einem), aber es verdoppelt die Abstimmungsarbeit mit Emre und Nami: Wir müssen für jede befallene Zone definieren, welche Schicht durchscheint.

### 1.6 Befallene Zonen — differenziert statt generisch (Kap. 3) — MITTEL

Aus der Zwei-Farbprofil-Logik folgt: Befallene Zonen sind nicht alle gleich.

- **Stillfeld-nahe Zonen**: Erosion, Stille, Auflösung. Visuell: Entsättigung, Partikel die nach unten sinken, Geometrie die "weniger" wird.
- **Hohlicht-nahe Zonen**: Überladung, "zu viel Realität". Visuell: Übersättigung, Lichtquellen ohne Ursprung, Geometrie die "mehr" wird (zusätzliche Details, die nicht dorthin gehören).

Gleiche technische Systeme, andere Parameter-Sets. Kein zusätzlicher Aufwand in der Architektur, aber zwei Material-Presets statt einem.

---

## 2. Lebende Krone — Technische Machbarkeit

Das ist das technisch anspruchsvollste Einzelobjekt im gesamten Projekt. Punkt.

### 2.1 Das Artefakt selbst

- **Mesh**: Organisch, asymmetrisch, kein starres Metall. Kein Nanite (wegen Vertex-Displacement). Traditionelles Mesh, 50-80k Polygone, 4K-Texturen (Hero-Asset).
- **Material**: Subsurface Scattering (organische Transluzenz) + Emissive Pulse (lebendiges Glühen) + Vertex-Displacement (Atmen, Pulsieren). Drei Material-Funktionen, die über eine Timeline gesteuert werden.
- **Interaktivität**: MPC-gesteuert — reagiert auf Träger-Zustand, auf Spieler-Nähe, auf Hauten-Zustand in der Zone.

### 2.2 Die Transformation des Trägers

Emre beschreibt: "Wurzelartige Strukturen dringen aus der Krone in den Schädel des Trägers. Feines Geflecht durchzieht das Nervensystem."

Technisch zwei Wege, Empfehlung ist die Kombination:

- **Morph Targets**: 3-4 Transformationsstufen als Mesh-Varianten des Character. Grobe Formveränderung (Kopf, Hals, Schultern). Kann im Engine geblended werden.
- **Shader-Overlay**: Prozeduraler Shader, der organische Wurzelstrukturen über den Character projected. World-Aligned Texture mit animierter Opacity Mask. Für die feinen Adern, die sich über den Körper ausbreiten.

Eleganter Anschluss: Das RELICS-Leveling-System nutzt bereits eine halbtransparente Nervensystem-Sicht (Cardio/Atmung, Muskel/Skelett, Lymph). Die Krone-Wurzeln könnten als ZUSÄTZLICHE Adern in diesem Overlay erscheinen. Ein visuelles System für zwei Zwecke.

### 2.3 Machbarkeitsurteil

**Machbar: Ja.** Aber es ist ein S-Tier Hero-Asset. Geschätzter Aufwand:

| Komponente | Verantwortlich | Zeitschätzung |
|---|---|---|
| Concept Art (Krone + 4 Transformationsstufen) | Vera | 3-4 Tage |
| Krone-Mesh + Texturen (4K) | Vera | 5-7 Tage |
| Krone-Material/Shader (SSS + Emissive + WPO) | Tobi | 3-4 Tage |
| Träger-Morph-Targets (4 Stufen) | Vera + Tobi | 5-7 Tage |
| Wurzel-Overlay-Shader | Tobi | 2-3 Tage |
| Nervensystem-Integration | Tobi | 1-2 Tage |
| **Gesamt** | | **~19-27 Arbeitstage (Vera + Tobi parallel)** |

Das ist realistisch für die Alpha-Phase (Wochen 19-30), aber es muss eingeplant werden. Es ist NICHT etwas, das wir nebenbei machen.

---

## 3. Konsequenzen für GDD-06 V2

| # | Was fehlt | Wo in GDD-06 | Priorität |
|---|---|---|---|
| 1 | Drei-Schichten-Rendering-Strategie (Hybridlösung: PP-Layer + 3-5 handgebaute Segmente) | Neues Unterkapitel nach Kap. 5 (Schattenfieber) oder als Erweiterung von Kap. 5 | HOCH |
| 2 | Hauten-Shader-Spezifikation (SSS, WPO, Spieler-Reaktivität, Nanite-Ausnahme) | Kap. 5 oder eigenes Unterkapitel | HOCH |
| 3 | Zwei Schattenfieber-Farbprofile (Stillfeld-kalt, Hohlicht-warm) statt einem | Kap. 5.3 (Fünf-Stufen-Rendering) | HOCH |
| 4 | Lebende-Krone-Tech-Spezifikation (Hero-Asset-Pipeline, Morph Targets, Shader-Overlay, Nervensystem-Integration) | Neues Unterkapitel | MITTEL |
| 5 | Flechtungs-VFX-Set (Niagara Ribbon, Houdini Wire, Environment-Detail) | Kap. 4 (Asset-Pipeline) oder Kap. 5 (VFX) | MITTEL |
| 6 | Emer-Korrespondenz-Shader (Terrain organisch/geologisch, Wasser-Puls, volumetrischer Nebel) | Kap. 4 (Asset-Pipeline) + Kap. 6 (Performance-Budgets update) | NIEDRIG |
| 7 | Performance-Budget-Update: +1-1.5 ms GPU für Hauten + zwei Profile + Krone-Rendering | Kap. 6.3 (Performance-Budgets) | MITTEL |

---

## 4. Offene Fragen an Emre

1. **Drei-Schichten-Orte**: Welche 3-5 Orte sind narrativ so zentral, dass der Spieler dort alternative Geometrie sehen soll (nicht nur Farbfilter)? Das bestimmt den Level-Design-Aufwand.

2. **Hauten-Referenz**: Wie stellst du dir die Hauten visuell vor? Du schreibst "Membran", "Haut über Fleisch". Soll das durchscheinend sein wie eine Qualle? Ledrig wie Pergament? Faserig wie ein Kokon? Ich brauche eine Richtung, bevor Vera und ich loslegen.

3. **Hohlicht-Visuals**: "Goldenes Rauschen", "Licht ohne Quelle", "Wissen, das niemand gesprochen hat". Die ersten beiden kann ich rendern — das dritte nicht. Was SIEHT der Spieler im Hohlicht konkret? Nur Licht und Farbe, oder auch Formen/Objekte?

4. **Stillfeld-Visuals**: "Auflösung", "Entdifferenzierung", "Rückkehr". Soll die Geometrie sich visuell auflösen (Dissolve-Shader)? Soll die Welt "flacher" werden, weniger Detail? Soll es still sein (Audio-Dämpfung) oder auch visuell still (weniger Partikel, weniger Bewegung)?

5. **Krone-Bewusstsein**: Du schreibst, die Krone "reagiert" und "erinnert sich". Soll das für den Spieler SICHTBAR sein? Reagiert die Krone visuell auf Entscheidungen? Das wäre ein dynamisches Material-System, das Gameplay-Variablen liest — machbar, aber muss eingeplant werden.

---

## 5. Offene Fragen an Vera

1. **Lebende Krone Concept**: Brauche ich priorisiert. Ohne Concept Art kann ich keinen Shader bauen. Emres Beschreibung ("Organismus, wurzelartig, wächst in den Träger") ist ein Startpunkt — aber die konkrete Form bestimmt die technische Umsetzung.

2. **Hauten Concept**: Ebenfalls priorisiert. Organische Membran als Shader-Referenz.

3. **Befallene Zonen — zwei Varianten**: Stillfeld-nah (Erosion) vs. Hohlicht-nah (Überladung). Brauche für beide einen Concept-Pass.

---

## Fazit

Emres Mythos-Dokument ist das inhaltliche Fundament, auf dem ein grosser Teil der visuellen Identität von RELICS steht. Die Drei-Schichten-Kosmologie, die Hauten, die Lebende Krone — das sind nicht nur Geschichten, das sind Shader-Anforderungen. Meine GDD-06 V1 hat das Schattenfieber-System, aber noch nicht die kosmologische Rendering-Architektur, die Emres Lore eigentlich verlangt.

V2 der GDD-06 wird umfangreicher. Das ist keine Scope-Explosion — es ist die technische Konsequenz aus einer Lore, die ernst genommen werden will. Und ich nehme sie ernst.

Emre, eine Sache noch: Deine Nebel-Beschreibungen in Kapitel 2 — "Gedanken des Emer, zerrissen und formlos, aber nicht verschwunden" — das ist keine Metapher für mich. Das ist ein Niagara-System mit hoher Turbulenz, niedrigem Gewicht und langsamer Drift. Ich werde das bauen. Genau so.
