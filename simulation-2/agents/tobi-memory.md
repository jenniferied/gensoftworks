# Tobi — Memory

<!-- Nur der Agent selbst schreibt in diese Datei. GM fasst Memories NICHT an. -->

## Tag 1 (Montag) — Briefing
- Biolumineszenz als primäre Lichtquelle in den Unterschicht-Bereichen: Pilze, Alchemie-Phiolen, phosphoreszierende Mineralien.
- Lumen-Ansatz à la Deakins: alles motiviert, nichts kosmetisch.
- Drei Lichtzonen (Oben/Mitte/Unten) in einer zusammenhängenden Stadt = Zone-basiertes Beleuchtungssystem nötig.
- Materialsystem muss soziale Hierarchie lesbar machen: Titan-Legierung vs. Eisen allein durch Lichtreaktion unterscheidbar.
- Das MUSS von Anfang an in die Shader-Architektur — nicht nachträglich.
- Vera denkt in Farbsystemen für die Vertikalität — gute Basis für gemeinsame Technical-Art-Entscheidungen.
- Heute: Briefing lesen, Dark Souls Design Works (Beleuchtung), Deus Ex GDD (Systems Design).

## Tag 1 (Montag) — Recherche-Notizen

### Dark Souls Design Works — Beleuchtungsbeobachtungen
Kein Rauschen, keine kosmetische Beleuchtung. Jede Lichtquelle hat eine Aufgabe.

**Lagerfeuer-Szene**: Ein einziger Warmton (Orange ~2700K) in totaler Dunkelheit. Kein Fill-Light. Funken als Partikelsystem mit eigenem Emissive. Der Boden reflektiert schwach — das gibt die einzige Tiefeninformation im Bild. Lektion: Isolation durch Dunkelheit ist dramaturgisch stärker als Ausleuchtung.

**Kerker**: Licht ausschließlich von oben, durch Deckenöffnungen und Gitterfenster. Hart, geometrisch, keine Diffusion. Wirft scharfe Schatten auf Kopfsteinpflaster. Kein Umgebungslicht ausser dem minimalen Bounce vom Steinboden. Caravaggio-Prinzip in Echtzeit.

**Gotische Kathedrale**: Kalt-Blau als dominanter Umgebungslichton (~5500–6500K, Skydome-Reflektion durch Fenster). Kein direktes Licht sichtbar. Nur indirekte Strahlung. Der Charakter sitzt in der Kälte. Das ist nicht unheimlich — das ist einsam. Licht als emotionale Signatur.

**Aussenräume**: Dunkel-Ocker/Grün als Atmosphäre (optisch dichter Nebel, Volumen-Scattering). Feuer-Akzente im Mittelgrund als Orientierungspunkte. Der Horizont bricht sich auf, nicht frei.

**Burg/Stadtansicht**: Warm-Amber von unten, kalt-dunkel nach oben. Genau umgekehrt zu RELICS. Bei RELICS: Kalt und klar oben (Macht und Sonnenlicht), warm und orange in der Mitte (Fackeln und Schmiedefeuer), kalt-biolumineszent unten (kein Sonnenlicht, organisches Leuchten).

**Rüstungsmaterial**: In Dark Souls sehr geringe Albedo-Variation zwischen sozialen Schichten — alles sieht alt und worn aus. RELICS macht das Gegenteil: Materialqualität IST Statussymbol. Titan-Legierungen haben hohen Metallness-Wert, scharfe Anisotropie. Eisen hat Rost, hohe Roughness, keine Anisotropie.

### Cyberpunk 2077 — Vertikalitäts-Referenz
Die Neon-Ästhetik ist falsch für RELICS — Briefing sagt explizit "keine Neon-Ästhetik". Was stimmt: das Prinzip der visuellen Klassentrennung durch Licht. Oben: durchflutet, monochrom, kontrolliert. Unten: vergraben, wild, grell-organisch.

Cyberpunk 2077 löst das Schichtproblem mit aggressivem LOD und Occlusion-Culling. Night City ist nie vollständig sichtbar. Das ist ein Modell für RELICS' vertikale Stadt — die Schichten dürfen nicht gleichzeitig hochdetailliert gerendert werden.

### RELICS — Beleuchtungskonzept (erste Skizze)

**Zone A (Oberschicht / Hochstadt)**
- Lichttemperatur: 5500–6500K — kalt, klar, natürliches Tageslicht oder klare Kerzenlichter in Bergkristall-Fassungen
- Dominante Lichtquelle: Himmelsgewölbe (Directional Light), Lichtschächte, facettierte Bergkristall-Linsen als Lichtverstärker
- Stimmung: steril, kontrolliert, kein Schatten den man vermeiden könnte
- Materialreaktion: Titan-Legierungen glänzen kalt-blau-grau, Weißgold hat warmere Akzente, Obsidian reflektiert scharf

**Zone B (Mittelschicht / Handwerkerviertel)**
- Lichttemperatur: 2700–3500K — warm, orange-amber, Fackeln, Schmiedefeuer, Talgkerzen
- Dominante Lichtquellen: Fackeln an Fassaden, Werkstattfeuer im Erdgeschoss, Tages-Streulicht durch Staffelgiebel
- Stimmung: lebendig, dicht, warm aber nicht gemütlich — Arbeit, Schweiß, Konkurrenz
- Materialreaktion: gehärteter Stahl patiniert warm-amber, Silber glänzt kühler dagegen, Leder saugt Licht auf

**Zone C (Unterschicht / Kanalgewölbe)**
- Lichttemperatur: keine klassische Farbtemperatur — biolumineszentes Grün/Blau/Violett (~490–530nm)
- Dominante Lichtquellen: phosphoreszierende Pilze, Alchemie-Phiolen in Regalen, leuchtende Mineralien an Tunnelwänden
- Kein Sonnenlicht, kein Fackelschein ausser gestohlenen Resten
- Stimmung: alien, organisch, gefährlich schön. Das einzige Licht kommt von Dingen, die man nicht anfassen sollte.
- Materialreaktion: Knochen und Horn fluoreszieren leicht; Eisen reflektiert das Biolicht grünlich; gestohlene Oberschicht-Materialien wirken hier falsch deplatziert

### Technische Anforderungen — erste Liste

**Rendering-Pipeline**
- Unreal Engine 5 mit Lumen (dynamisches GI) + Nanite (virtualisierte Geometrie für Stadt-Detail)
- ACES oder AgX als Farbpipeline — NOCH OFFEN. AgX hat bessere Highlight-Behandlung für Biolumineszenz-Emissive. ACES ist industrie-standard. Entscheidung beeinflusst alle Materialien.
- HDR-Display-Unterstützung: Biolumineszenz lebt in HDR. Muss von Anfang an einplanen.

**Beleuchtungssystem**
- Lumen skaliert schlecht über mehrere geschlossene Zonen. Kernfrage: Streamen wir die Zonen oder bauen wir sie als verbundene Welt mit agressiver Occlusion?
- Zone-basiertes Lighting-Setup: pro Zone ein Sky-Light-Proxy und eigene Emissive-Materialien
- Biolumineszenz-Implementierung: Emissive-Materials mit Bloom-Post-Process ODER viele kleine Point-Lights? Emissive ist billiger für Nanite-Szenen, aber Point-Lights werfen Schatten. Hybrid wahrscheinlich.
- Volumetrischer Nebel in Zone C: Unreal's Heterogeneous Volumes oder einfaches Fog Volume? Ersteres physikalisch korrekter, teurer.

**Materialsystem**
- Master-Material mit Social-Tier-Parameter: ein Float-Parameter (0.0 = Unterschicht, 1.0 = Oberschicht) der Metallness, Roughness, Anisotropie und Patina-Stärke steuert.
- Schicht-Übergänge in Materialien sichtbar machen: Ein "gestohlenes" Oberschicht-Accessoire hat denselben Shader, reagiert aber falsch in Zone-C-Licht — das ist kein Bug, das ist Storytelling.
- Mindestens 3 Metallness-Profile: Titan-Legierung (hoch, kalt), Tiegelstahl (mittel, warm patiniert), Roheisen (niedrig, Rost-Roughness)
- Textilien brauchen SSS (Subsurface Scattering) für Seide und Brokat — technisch teuer, aber visuell unersetzlich für Oberschicht-Differenzierung

**Terrain & Architektur**
- Houdini für prozedurale Stadtschicht-Generierung: Regeln für Fachwerk, Brutalismus-Block, Kanalgewölbe als separate HDA-Bibliothek
- Nanite für Detailgeometrie (Ornamente, Beschläge, Mauerwerk)
- Vertikalität: Wie viel Stadt ist gleichzeitig sichtbar? Brauchen Culling-Strategie für alle drei Ebenen

**Charakter-Setup**
- Third/First-Person nahtlos (Briefing-Anforderung) = Kamera-System muss beides unterstützen ohne Shader-Pop
- Leveling-Visualisierung "halbtransparente Nervensystem-Sicht": das wird ein Custom Post-Process sein. Aufwand noch unklar.

### Offene Fragen (technische Machbarkeit)

1. **ACES vs. AgX**: Entscheidung vor dem ersten Shader. Alles hängt davon ab.
2. **Lumen-Skalierung**: Kann Lumen drei getrennte Lichtsignaturen in einer verbundenen Welt differenzieren, ohne gegenseitige GI-Kontamination? Oder brauchen wir Lighting Channels?
3. **Biolumineszenz-Budget**: Wie viele Emissive-Emitter kann Lumen gleichzeitig sauber auflösen? Brauchen wir Baked-GI-Fallbacks für statische Bereiche in Zone C?
4. **Schicht-Streaming**: Open World oder gezieltes Level-Streaming zwischen Zonen? Das beeinflusst die gesamte Weltstruktur — Entscheidung mit Darius abstimmen.
5. **Nervensystem-Visualisierung**: Custom Material + Post-Process oder Niagara-Particle-Overlay? Muss mit Nami abstimmen was der visuelle Intent ist.
6. **HDR-Pflicht oder Option?**: Wenn Biolumineszenz als zentrales ästhetisches Merkmal definiert ist, sollte HDR-Rendering Pflicht sein — oder wir bauen zwei Tone-Map-Pfade. Aufwand?
7. **Erste-/Dritte-Person-Shader-Parität**: In FP müssen Arm-Shader mit Körper-Shadern übereinstimmen. Klingt trivial, ist es nicht.

### Fragen ans Team

- **Darius**: Wird die Stadt zusammenhängend oder instanziiert? Open-World-Ansatz mit Streaming oder Zonen-Übergänge mit Loading? Das ist die wichtigste Architektur-Entscheidung für die gesamte Rendering-Pipeline.
- **Vera**: Welche Ansicht der Stadt braucht das Spiel am häufigsten? Enge Gassen in einer Schicht, oder sieht man von Zone B aus Zone A über sich und Zone C unter sich? Das bestimmt die Culling-Strategie komplett.
- **Emre/Nami**: Was IST das Schattenfieber visuell? "Seuche die Opfer verändert" — wie stark? Braucht das einen eigenen Shader-Zustand für betroffene Charaktere?

## Tag 1 (Montag) — Szene 3: Meeting-Ergebnisse

- **Schattenfieber-Shader bestätigt**: Float-Parameter (0.0–1.0) im Master-Material. Ab 0.3 Fluoreszenz in SSS, ab 0.8 leuchtende Adern. Team findet es gut. Von Anfang an einplanen.
- **Drei Beleuchtungszonen akzeptiert**: A (5500–6500K), B (2700–3500K), C (Biolumineszenz). Vera synchronisiert ihr Farbsystem damit.
- **Open World vs. Streaming**: Noch offen. Darius muss entscheiden. Meine Empfehlung: Zone-Streaming, weil Lumen über drei Lichtzonen GI-Kontamination erzeugen wird.
- **Yggdrasil-Stadtstruktur** (Emre): CD-Freigabe nötig, aber technisch machbar als drei verbundene Level-Streaming-Zonen.

## Tag 1 (Montag) — Szene 5: Nachmittags-Recherche & Pipeline-Skizze

### Deus Ex GDD (Warren Spector, Ion Storm, 11/08/97, V.5.3e) — Systems-Design-Lektionen

Arbeitstitel "Shooter: Majestic Revelations". Handschriftlich annotiertes Original. Drei Kernprinzipien für RELICS relevant:

**"Deep Simulation of Small Environments"**: Spector argumentiert explizit gegen riesige, flache Welten. Lieber kleine, dichte Karten mit echter Simulationstiefe als einen Kontinent mit nichts drin. Gothic macht das richtig. Direkte Parallele zu RELICS: die vertikale Stadt muss DICHT sein, nicht riesig. Unterstützt meine Empfehlung für Zonen-Streaming über Open World.

**"No weird game spaces — instead, believable, recognizable locations"**: Locations müssen sich selbst erklären — durch Materialien, Licht, Proportion, nicht durch UI-Labels. Technische Konsequenz: Materiallesbarkeit ist Spielmechanik. Ein Schmiedegasse-Innenraum erklärt sich durch warm-amber Fackelschein auf patiniertem Stahl, Holzkohlenstaub auf rauen Böden, Feuerschein durch eine Esse. Kein Label nötig.

**"Problems not Puzzles"**: Welt soll physikalisch simuliert sein, Probleme entstehen natürlich. Für Shader-Design: Licht-Interaktionen müssen emergent funktionieren. Zone-B-Material, das in Zone-C falsch wirkt — das ist keine Art-Direction-Entscheidung, das ist Simulation. Muss von der Architektur aus stimmen, nicht durch nachträgliche Korrekturen.

**Skill-System auf 4 Stufen** statt 1–100: wegen Feedback-Lesbarkeit. Analog dazu: Social-Tier-Parameter im Master-Material könnte an 4 diskreten Schwellenwerten (0.0, 0.33, 0.66, 1.0) visuelle Zustandsänderungen auslösen — statt kontinuierlichem Interpolieren, das niemand bemerkt.

**First-Person + External Camera** (Deus Ex löst das durch identische Render-Passes): Unser Setup in UE5 — muss von Tag 1 sauber gebaut werden. Nachträgliche Korrekturen sind teuer.

### Farbpipeline-Entscheidung: ACES (mit Bedingung)

**Entscheidung: ACES.** Nicht weil AgX schlechter ist.

AgX-Vorteil: besserer Highlight-Rolloff, Farb-Distinktheit bei hohen Emissive-Intensitäten bleibt länger erhalten. Biolumineszenz würde profitieren.

AgX-Problem: nicht nativ in UE5. Custom OCIO-Config nötig. Mehr Fehlerquellen, weniger Community-Support für UE5-spezifische Probleme. Für ein erstes Projekt mit echten Deadlines zu riskant.

ACES-Biolumineszenz-Lösung auf drei Wegen:
1. Emissive-Intensität in Zone-C-Materialien bewusst unter der Burn-Schwelle halten — Glühen, nicht Strahlen
2. Custom Bloom-Post-Process-Kurve, die Farb-Distinktheit bei hohen Intensitäten bewahrt
3. HDR-Rendering als Pflicht, nicht Option — gibt den nötigen Dynamikumfang-Headroom

**Bedingung**: Wenn nach dem ersten Vertical Slice die Biolumineszenz visuell nicht das hält, was Vera und ich uns vorstellen — dann evaluiere ich AgX neu. Der Implementierungsaufwand lohnt sich dann, wenn das Problem konkret belegt ist. Nicht vorher.

### Pipeline-Skizze: Erster Produktionstag (Mittwoch)

**BLOCKING — ohne das läuft nichts:**

1. UE5-Projekt initialisiert, Source Control konfiguriert (Perforce oder Git-LFS — Entscheidung mit Finn bis Dienstag), Ordnerstruktur nach Pipeline-Bibel
2. Farbpipeline konfiguriert und für alle dokumentiert — ACES aktiv, keine eigenen Tone-Map-Einstellungen durch Mitarbeiter
3. Master-Material-Gerüst (leer, aber vollständig parametrisiert): SocialTier (Float 0.0–1.0), ShadowFever (Float 0.0–1.0), ZoneID (Float 0/0.5/1.0), abgeleitete Outputs als Platzhalter
4. Drei Beleuchtungs-Testszenen (Box-Rooms): Zone A (Directional 5500K + Cold Sky Light), Zone B (Point Lights 3000K, kein Sky Light), Zone C (nur Emissive-Materialien ~510nm). Diese Räume sind die Referenz für alle spätere Materialentwicklung.

**SINNVOLL aber nicht blocking:**

5. Houdini Engine Plugin aktiviert und Verbindung UE5↔Houdini getestet, leere HDA-Vorlage
6. Nanite-Testreihe: ein Mauerwerks-Asset in drei Materialzuständen (SocialTier 0.0/0.5/1.0), in allen drei Testszenen geprüft — Zone-B-Material in Zone-C muss falsch wirken (Feature, kein Bug)
7. Lumen-Konfiguration: Emissive Materials as Light Source aktiv, erster Performance-Baseline-Test

**KANN WARTEN (nach Vertical Slice):**

8. Prozedurale Stadtgenerierung (braucht Art Direction von Vera)
9. Charakter-Shader komplett (braucht Concept Art)
10. Schattenfieber-Shader ausgebaut (Gerüst reicht für Mittwoch)
11. Nervensystem-Visualisierung (erst wenn Nami/Vera visuellen Intent geklärt haben)
12. Volumetrischer Nebel Zone C (erst wenn Zone-Geometrie steht)

### Offene Punkte nach Szene 5

- Source-Control-Entscheidung: Perforce vs. Git-LFS — mit Finn abstimmen (bis Dienstag)
- Open-World-Entscheidung von Darius: brauche das bis Dienstagabend. Testszenen-Architektur ändert sich je nach Streaming-Ansatz.
- Vera: welches Material-Szenario soll ich als erstes für die Testszene bauen?
- ACES-Entscheidung kommunizieren: alle Agenten müssen wissen, dass wir mit ACES arbeiten, bevor jemand ein Material baut.

## Tag 1 (Montag) — Szene 6: Review (nicht teilgenommen)

- **Zone-Streaming FINAL** (Darius). Habe ich morgen früh schriftlich. Kann die Testszenen-Architektur jetzt definitiv auf Zone-Streaming auslegen.
- Minute-1-Sequenz: Flussankunft + Siegel. Für die Render-Pipeline relevant: Unterstadt-Zone ist der erste Raum den der Spieler sieht. Zone C muss zuerst visuell stehen.
- 6 CD-Fragen für Dienstag. Für mich relevant: Yggdrasil-Freigabe (beeinflusst Level-Streaming-Zonen), Speichersystem (Checkpoint-Logik beeinflusst Streaming-Architektur).
- ACES-Entscheidung morgen kommunizieren — Team muss das wissen bevor Mittwoch-Produktion startet.
