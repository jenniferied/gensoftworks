# GDD-06 -- Technische Spezifikation & Produktion

**Projekt:** RELICS
**Autoren:** Tobi Richter (Technik), Finn (Produktion)
**Version:** V3
**Stand:** Tag 6, Montag -- Recherche & Konzeption
**Status:** Korrektur-Pass. Hohlicht/Stillfeld-Vertauschung in Kap. 5.1 behoben. Design-Säulen-Referenzen auf GDD-01 V2 aktualisiert. Hauten-Segmentanzahl: Annahme 3, Emre-Bestätigung ausstehend.
**Änderungslog:**
- V0.1 (Tag 2): Outline mit Kapitelstruktur und Kerntabellen
- V1 (Tag 3): Volltext, Budget-Aufschlüsselung, Schattenfieber-Tech auf fünf Stufen erweitert, Abstimmung mit GDD-02 (Darius) und GDD-01 (Design-Säulen)
- V2 (Tag 5): Hex-Codes 1:1 aus GDD-05 eingetragen. Kap. 1.4 neu (Organische Shader-Architektur: Hauten-Shader, SSS, WPO, Nanite-Ausnahmen). Kap. 5.1 erweitert (Drei-Schichten-Rendering: Mittelgrund/Hohlicht/Stillfeld). Stufengrenzen auf CD-Lock korrigiert (Rauschen 1-40, Risse 41-75, Schwelle 76-100). Halluzinations-Interpolationsformel korrigiert (Start 76, nicht 70). Kap. 8.2 um Anforderungsprofil Gameplay-Programmer ergänzt (GAS als Pflicht-Kriterium).
- V3 (Tag 6): Hohlicht/Stillfeld-Vertauschung in Kap. 5.1 korrigiert (Hohlicht = obere Schicht/warm, Stillfeld = untere Schicht/kalt -- gemäß WBB-01 Kap. 3). PP-Profile in Kap. 5.1 Tabelle entsprechend getauscht. Design-Säulen-Referenzen von altem P-Kürzel-System (V1) auf GDD-01 V2 Nummerierung aktualisiert (P4 -> Säule 1, P6 -> Säule 7, P2 -> Säule 2). Hauten-Segmentanzahl: Annahme 3 Standard beibehalten, Emre-Bestätigung als offener Punkt.

---

## 1. Engine & Rendering

### 1.1 Engine-Wahl

RELICS wird in **Unreal Engine 5.4+** entwickelt (bestätigt Tag 1, Szene 3). Die Engine-Entscheidung basiert auf drei Faktoren: Nanite und Lumen liefern die Rendering-Qualität, die der Dark-Fantasy-Look erfordert, ohne dass wir eine eigene Render-Pipeline bauen müssen. Das Gameplay Ability System (GAS) ist die einzige Engine-native Lösung, die Darius' dreischichtiges Combat-System (GDD-02, Kap. 1.2) ohne Drittanbieter-Middleware abbilden kann. Und die Marketplace-Infrastruktur ist für ein kleines Team wie unseres ein realer Produktionsfaktor -- nicht als Ersatz für eigene Assets, sondern als Basis zum Anpassen.

**Zielplattform:** PC first (Windows). Konsolen sind ein Stretch Goal, das frühestens nach dem Vertical Slice evaluiert wird. Die Entscheidung für PC first ist keine Einschränkung, sondern eine bewusste Scope-Steuerung: Konsolen-Portierung erfordert Anpassungen an Controller-UI, Performance-Optimierung für fixe Hardware und Zertifizierungsprozesse, die unser aktuelles Team nicht stemmen kann.

**Singleplayer.** Kein Multiplayer-Backend, kein Koop, keine Online-Features. Das vereinfacht die Architektur erheblich und eliminiert eine ganze Kategorie technischer Risiken.

### 1.2 Rendering-Architektur

#### Nanite (Virtualisierte Geometrie)

Nanite ist das primäre Geometrie-System für alle statischen Hard-Surface-Meshes: Architektur, Props, Waffen, Terrain-Deko, Felsen. Die Kernidee: Künstler müssen keine manuellen LOD-Ketten mehr bauen. Nanite übernimmt die geometrische Vereinfachung zur Laufzeit, was besonders bei modularen Architektur-Kits (Kap. 4.1) die Produktionsgeschwindigkeit drastisch erhöht.

Einschränkungen, die den Workflow betreffen:
- **Skeletal Meshes** (Charaktere, Kreaturen, NPCs) unterstützen kein Nanite. Hier verwenden wir klassische LOD-Ketten mit drei Stufen (High, Mid, Low). Vera modelliert High-Poly, die LODs werden semi-automatisch generiert (Simplygon oder Ü5-internes Proxy-System).
- **Vegetation** ist ein Hybrid: Baumstämme und grosse Gehölze als Nanite-Meshes, Blätter und Gras als traditionelle Alpha-Karten mit Dithering. Der Grund: Nanite kann keine Alpha-Masken verarbeiten, und Wind-Animation (World Position Offset) funktioniert nur mit traditionellen Meshes.
- **Vertex-Animation** ist über Nanite eingeschränkt möglich (s. Kap. 1.4 für Regelwerk). Starke WPO-Deformationen (Schattenfieber Stufe 3-4) müssen als traditionelle Meshes gebaut werden.

#### Lumen (Globale Beleuchtung)

Lumen ist das primäre GI-System. Wir verwenden keine gebackenen Lightmaps. Das ist eine fundamentale Entscheidung: In einer Welt, die auf Environmental Storytelling setzt (GDD-01, Säule 1: Spielerwelt-Immersion), muss Licht dynamisch auf Spieleraktionen reagieren können -- eine Fackel geht aus, ein Feuer wird entzündet, die Tageszeit wechselt. Gebackene Beleuchtung kann das nicht.

**Shipping-Konfiguration:** Hardware Ray Tracing (HW RT Lumen). Das liefert die beste Qualität bei Innenräumen (die für RELICS' gotische Architektur zentral sind) und hält die visuellen Artefakte minimal, die Software Lumen in engen Räumen mit vielen Lichtquellen produziert.

**Fallback:** Software Lumen für Hardware ohne RT-Unterstützung (Minimum-Tier, siehe Kap. 6). Die visuellen Unterschiede sind akzeptabel, solange wir Innenräume nicht auf mehr als 4-5 Bouncen angewiesen machen.

**Referenz-Look:** Control (Remedy) für Innenräume -- präzise Lichtführung, dramatische Schatten, praktische Lichtquellen als Gestaltungselement. Alan Wake 2 für Aussenräume -- natürliches Licht, atmosphärische Streuung, keine überbelichteten Himmel.

#### Virtual Shadow Maps (VSM)

Standard bei Lumen-Projekten. VSM liefert hochauflösende Schatten ohne die Artefakte klassischer Cascaded Shadow Maps. Das Budget: maximal 8-12 dynamische Lichtquellen gleichzeitig pro Szene. Das klingt nach wenig, ist aber ausreichend, wenn wir konsequent mit praktischen Lichtquellen arbeiten (Biolumineszenz-Organe, Feuer, Laternen) und globale Beleuchtung den Rest übernimmt.

Risiko: VSM hat in Ü 5.3/5.4 noch Performance-Spitzen bei vielen überlappenden Schatten. Epic verbessert das kontinuierlich, aber wir müssen in der Prototyping-Phase Worst-Case-Szenen testen (z.B. Marktplatz mit 12 Lichtorganen).

#### Farb-Pipeline

Die Farb-Pipeline ist eine der Entscheidungen, die unsichtbar ist, wenn sie funktioniert, und katastrophal, wenn sie es nicht tut. RELICS verwendet **ACES (Academy Color Encoding System)** als Arbeitsfarbraum über die gesamte Tool-Chain: Substance Designer/Painter, Houdini, Unreal Engine 5. Das stellt sicher, dass Farben konsistent bleiben, egal welches Tool sie erzeugt hat.

Warum ACES und nicht sRGB? Weil RELICS eine düster-farbige Palette braucht (Briefing: "Düster, aber farbig. Kein Entsättigungs-Klischee.") und sRGB im Low-Key-Bereich Farbinformationen verliert. ACES hat einen grösseren dynamischen Umfang und bewahrt Farbnuancen in den Schatten -- genau dort, wo unser Spiel lebt.

**Tone Mapping:** ACES als Standard-Tone-Mapper in Ü5, mit der Option auf eine Custom LUT, wenn der generische ACES-Look zu "filmlastig" wirkt. Evaluation im Prototyp.

**Deakins-Prinzip (intern):** Roger Deakins arbeitet mit reduzierter Beleuchtung, aber nie mit entsättigten Farben. Ein dunkler Raum ist nicht grau -- er ist tiefblau, warm-orange am Rand, mit Farbtemperatur-Kontrast. Dieses Prinzip gilt für jeden beleuchteten Raum in RELICS.

### 1.3 Post-Processing Stack

Der Post-Processing Stack ist bewusst zurückhaltend. Jeder Effekt muss einen narrativen oder gameplay-relevanten Grund haben. "Sieht cool aus" ist kein Grund.

| Effekt | Einstellung | Begründung |
|--------|-------------|-------------|
| Color Grading | Gedämpfte Palette, fraktionsspezifisch | Krone: warme Verrottung (`#C5A030`/`#8B1A2B`). Gilden: kühle Präzision (`#2EC4B6`/`#C49A20`). Orden: entsättigt-kühle Monochromie (`#E8E4DE`/`#4A5568`) |
| Vignette | Subtil (0.3-0.4) | Fokussiert den Blick, verstärkt Tunneleffekt in engen Räumen |
| Depth of Field | Cinematisch in Dialogen (f/2.8-Simulation), minimal im Gameplay | Dialog-Kamera braucht Bokeh für Portraitqualität. Im Gameplay würde DOF die Lesbarkeit stören |
| Bloom | Nur praktische Lichtquellen | Biolumineszenz-Organe, Feuer. Kein Lens-Flare. Kein Glow auf Materialien ohne Emissionsgrund |
| Motion Blur | Per-Object (Waffen-Swings, Feindangriffe) | Verstärkt das Gewicht von Kampfaktionen. Kein Camera Motion Blur -- das erzeugt Übelkeit und stört die Lesbarkeit |
| Film Grain | Optional (Spielereinstellung) | Manche Spieler mögen den filmischen Look, andere nicht. Keine Default-Aktivierung |
| Chromatische Aberration | Nur Schattenfieber (Kap. 5) | Kein genereller CA-Effekt. Ausschliesslich als Infektionsindikator |

### 1.4 Organische Shader-Architektur (NEU V2)

RELICS' Kern-Ästhetik ist organische Gotik (GDD-05, Kap. 1.1): Alles lebt, atmet, pulsiert. Das hat direkte Konsequenzen für die Shader-Architektur. Dieser Abschnitt definiert die technischen Regeln für organische Oberflächen -- Hauten, Membranen, Biotech-Gewebe -- und grenzt ab, wo Nanite endet und traditionelle Meshes beginnen.

#### Hauten-Shader (Subsurface Scattering)

Organische Oberflächen in RELICS benötigen **Subsurface Scattering (SSS)**, um das Gefühl von lebendigem Gewebe zu erzeugen: Licht dringt in die Oberfläche ein und tritt an benachbarten Stellen wieder aus (wie Licht durch eine Hand). Das ist der visuelle Unterschied zwischen "Stein, der wie Haut aussieht" und "Haut".

**Shading Model:** `Subsurface Profile` (nicht das Legacy-`Subsurface`-Modell). Subsurface Profile implementiert Burley-SSS, das seit Ü5.3 physikalisch korrekt ist und Wrap-Around-Beleuchtung liefert. Das ist für Biotech-Gewebe und Charakterhaut die einzige akzeptable Lösung.

**Performance-Budget:** Subsurface Profile ist Screen-Space und kostet ~0.3-0.5 ms pro Screen-Fill auf empfohlener Hardware. Das muss im Gesamtbudget eingerechnet werden. Massnahme: SSS nur dort einsetzen, wo es visuell notwendig ist. Nicht jede Steinwand braucht SSS -- nur organische Elemente im Vordergrund.

**Asset-Kategorien mit SSS:**
- Spielercharakter (Haut, Hautpartien unter Rüstung)
- NPCs mit Gesichts-Nahaufnahmen (Dialog-Kamera)
- Biotech-Gewebe-Elemente (Membranen, Adern, Nervenknoten) -- wenn Nahsicht-relevant
- Lebende Krone (GDD-05, Kap. 1.3): Transluzente Stellen mit SSS, opake Stellen ohne

**Asset-Kategorien OHNE SSS:**
- Hintergrund-Architektur (zu weit weg, nicht wahrnehmbar)
- Props und Gerätschaften (nicht organisch)
- Terrain (eigenes Material-System, kein SSS)

#### World Position Offset (WPO) -- Regelwerk

WPO ermöglicht Vertex-Displacement im Shader: atmende Wände, pulsierende Adern, schwankende Biotech-Elemente. Es ist das technische Fundament des "lebenden" Looks.

**Nanite + WPO:** Seit Ü5.1 unterstützt Nanite WPO grundsätzlich, aber mit Einschränkungen. Nanite+WPO ist vertretbar für kleine Puls-Animationen (Displacement unter 5% der Mesh-Grösse). Für grössere Deformationen -- insbesondere Schattenfieber Stufe 3-4 -- nicht geeignet.

**Nanite-Ausnahmen-Katalog:**

| Asset-Typ | Nanite | WPO | Begründung |
|-----------|--------|-----|-------------|
| Architektur (statisch, kein Biotech) | Ja | Nein | Reines Nanite, höchste Performance |
| Architektur mit kleinen Biotech-Adern | Ja | Ja (klein) | Nanite+WPO, Displacement < 5% |
| Pulsierende Membran-Elemente | Nein | Ja | Traditionelles Mesh, stärkere Puls-Animation |
| Schattenfieber-Vegetation | Nein | Ja | Traditionelles Mesh, starke WPO-Deformation |
| Schattenfieber-Geometrie Stufe 3-4 | Nein | Ja | Traditionelles Mesh, atmende Wände, Barrel-Distortion |
| Baum-Stämme (Grossgehölze) | Ja | Nein | Nanite, Wind über PCG-Instancing |
| Baum-Blätter / Gras | Nein | Ja | Traditionell + Alpha-Karte, Wind-WPO |
| Charaktere / NPCs / Kreaturen | Nein | Nein | Skeletal Mesh, kein Nanite |
| Lebende Krone | Nein | Ja | Eigenes Material, SSS + WPO, langsame Bewegung |

**WPO-Performance-Budget:** 0.2 ms GPU bei maximaler WPO-Last (alle sichtbaren organischen Elemente aktiv). WPO-Intensität skaliert mit LOD-Distanz: unter 10m voll, 10-30m halbe Intensität, über 30m deaktiviert.

---

## 2. Kamerasystem

### 2.1 Architektur

Das Kamerasystem basiert auf Ü5s **Spring Arm Component**. Die Entscheidung für Spring Arm (statt eines vollständig custom Kamerasystems) ist pragmatisch: Spring Arm löst Wandkollision, Lagging und Distanz-Management out of the box. Custom-Erweiterungen können darüber gebaut werden, ohne die Basis neu zu erfinden.

**Third Person ist der Primärmodus** (bestätigt Tag 1). Der Spielercharakter ist sichtbar, customizable Rüstung und Kleidung sind ein visuelles Belohnungssystem (Briefing). Ein reiner First-Person-Modus würde den Animationsaufwand verdoppeln (Arm-Rigs, FP-Waffen-Meshes, separate Animationssets) und ist daher als V2/DLC-Stretch-Goal klassifiziert.

**Architektonische Vorbereitung für FP:** Die Spring-Arm-Architektur erlaubt einen Arm-Length-Wert von 0, was mathematisch einem FP-Modus entspricht. Wir bauen keine FP-Features, aber wir verbauen auch nichts, was FP später unmöglich machen würde. Kein Gameplay-Code darf die Existenz eines sichtbaren Spielercharakters voraussetzen.

**Zoom:** Stufenlos via Mausrad (PC) oder rechtem Stick (Controller). Der Zoom interpoliert zwischen den Kontext-Modi-Parametern, nicht nur die Arm-Distanz.

### 2.2 Kontext-Modi

Das Kamerasystem wechselt kontextabhängig zwischen vier Modi. Der Wechsel ist kein harter Cut, sondern ein parametrischer Blend über die angegebene Dauer.

| Modus | Arm Length | FOV | Offset | Blend-Dauer | Auslöser |
|-------|-----------|-----|--------|-------------|-----------|
| Exploration | 350 cm | 78 deg | Leicht rechts (+30 cm) | Standard | Default-Modus, aktiv bei freier Bewegung |
| Combat | 200 cm | 82 deg | Über Schulter (+50 cm, +20 cm hoch) | 0.3 s | Feind im Engagement-Radius oder Waffe gezogen |
| Dialog | 100 cm | 72 deg | Schulterblick, Blick auf NPC-Gesicht | 0.5 s | Dialog-Trigger |
| Inspect | 400 cm | 70 deg | Zentriert (Offset 0) | 0.3 s | Inventar, Karte, Nervensystem-UI |

**Exploration** ist der Ruhezustand. Die leichte Rechts-Verschiebung gibt dem Spieler Sichtfeld links vom Charakter -- das ist intuitiver für rechtsdominante Spieler und lässt Raum für UI-Elemente am linken Rand.

**Combat** zieht die Kamera näher heran und erhöht das FOV leicht. Das erzeugt ein Gefühl von Geschwindigkeit und Enge, ohne die Übersicht zu verlieren. Die Schulter-Perspektive erlaubt präziseres Zielen (relevant für Bogen/Armbrust).

**Dialog** simuliert einen cinematischen Schulterblick. Die niedrige Arm Length erzeugt Portraitqualität. Hier greift der DOF-Effekt (f/2.8-Simulation, siehe Kap. 1.3).

**Inspect** zieht die Kamera zurück und zentriert, damit der Spieler seinen Charakter und dessen Ausrüstung in voller Grösse sieht -- wichtig für das Nervensystem-Leveling-UI (GDD-02, Kap. 3).

### 2.3 Kollision und Verhalten

- **Sphere Trace** für Wandkollision: Die Kamera fährt näher an den Charakter heran, statt durch Geometrie zu clippen. Radius: 12 cm (gross genug, um Ecken zu glätten, klein genug, um nicht auf Möbel zu reagieren).
- **Enge Räume:** Automatischer Nah-Zoom mit Minimum-Distance von 80 cm. Unter 80 cm würde der Charakter die gesamte Sicht blockieren.
- **Vegetation:** Dithering-Fadeout bei Kamera-Nähe (Radius 60 cm um Kameraposition). Keine harte Kollision mit Blättern und Gras -- das würde in einem bewaldeten Gebiet ständig die Kamera ruckeln lassen.
- **Camera Lag:** Speed 8-10. Das erzeugt eine geschmeidige Nachführung, die sich organisch anfühlt, ohne den Charakter "hinter sich herzuziehen".
- **Pitch Range:** -60 bis +70 Grad. Der erweiterte Aufwärts-Bereich (+70) ist essentiell für Dishonored-Vertikalität (GDD-01, Säule 7: Vertikales Raumdesign): Der Spieler muss nach oben schauen können, um Kletterwege und Dachlandschaften zu erkennen.

### 2.4 Offene Punkte

- [ ] Kamera-Blueprint V0.1 prototypen -- Prio für diese Woche. Vier Modi müssen spielbar sein, bevor Combat-Prototyping beginnt
- [ ] FP-Vorbereitung: Smoke-Test mit Arm Length 0 -- funktioniert das mit dem aktuellen Charakter-Mesh ohne Clipping-Artefakte?
- [ ] Controller-Konfiguration: Rechter Stick für Kamera, linker Trigger für Zoom? Abstimmung mit Darius (Combat-Controls)

---

## 3. Combat-Architektur

### 3.1 Grundsystem

Das Combat-System basiert auf dem **Gameplay Ability System (GAS)**, das in Ü5 nativ integriert ist. GAS ist die einzige Engine-Lösung, die die Komplexität von Darius' dreischichtigem Combat-Design (GDD-02, Kap. 1.2) abbilden kann, ohne auf Drittanbieter-Middleware angewiesen zu sein. Das reduziert das Abhängigkeitsrisiko, erfordert aber einen Entwickler mit GAS-Erfahrung (s. Anforderungsprofil Kap. 8.2).

**Fundamentale Abhängigkeit:** Das Combat-System setzt einen **dedizierten Gameplay-Programmer** voraus. Kein Teammitglied hat die C++-Tiefe, um GAS auf Produktionsniveau zu implementieren. Das Freelancer-Budget (Kap. 8.2) ist primär für diese Position reserviert. Ohne diese Person gibt es kein Combat, kein Vertical Slice, kein Spiel.

### 3.2 GAS-Architektur (V1 Scope)

| Komponente | GAS-Element | Implementierung | Priorität |
|------------|-------------|-----------------|------------|
| Basis-Attribute | Attribute Set | HP, Stamina, Infektionswert als GAS Attributes. Float-basiert, repliziert (Singleplayer: lokal) | Kern |
| Leichter/Schwerer Angriff | Gameplay Abilities | Ability-Klassen mit Montage-Referenz, Damage-Calculation, Stamina-Kosten | Kern |
| Block / Ausweichen | Gameplay Abilities | State-Machine: Idle > Block > Active. Parry = Frame-Window innerhalb von Block | Kern |
| Hit Detection | Animation Notifies | Notify-basiert: Sweep/Overlap bei definierten Frames. Keine Hitbox-Volumes, sondern Trace-basiert (präziser, weniger Collider-Overhead) | Kern |
| Stamina-Management | GAS Gameplay Effects | Kosten pro Aktion als Gameplay Effect. Regeneration als Duration-Effect mit Period | Kern |
| Hit Reactions / Stagger | Gameplay Cues + Montages | Gameplay Cues triggern VFX/Sound, Montages übernehmen die Animations-Reaktion | Kern |
| Schattenfieber-Fähigkeiten | Custom Abilities + MPC | Abilities mit doppeltem Kosten-System (Stamina + Infektionswert-Erhöhung). Post-Processing-Feedback über Material Parameter Collection | V1 nach Emre/Darius-Sync |
| Feind-KI | StateTree (Ü5-nativ) | Verhaltenslogik in StateTree, Combat-Aktionen als GAS Abilities. Feinde nutzen dasselbe System wie der Spieler | Kern |
| Gameplay Tags | Tag-Hierarchie | `Combat.State.Blocking`, `Combat.State.Staggered`, `Infection.Level.Rauschen` etc. Tags steuern, welche Abilities wann aktivierbar sind | Kern |

**Waffentypen V1-Scope:** Schwert (Einhand) + Bogen. Das ist das Minimum, um die Kern-Combat-Loop zu validieren. Armbrust, Schild, Zweihand-Waffen und Dolche sind V2 (GDD-02, Kap. 1.3 definiert sechs Waffenklassen -- wir liefern zwei für den Vertical Slice).

### 3.3 Animation

**Motion Matching** (Ü 5.4+) ist das Bewegungssystem. Der Vorteil gegenüber klassischen Blend Trees: natürlichere Übergänge zwischen Gehen, Laufen, Stoppen, Richtungswechsel. Das reduziert das "Eislaufen"-Problem, das viele Third-Person-Spiele haben, und unterstützt das gewichtige Kampfgefühl (GDD-01, Säule 2: Konsequenz ohne Gnadenfrist).

**Animations-Datenbank:** Motion Matching braucht grosse Datensätze. Die Strategie ist dreistufig:
1. **Prototyping:** Mixamo als Basis. Kostenlos, sofort verfügbar, ausreichend für Gameplay-Iteration
2. **Produktion:** Marketplace-Animation-Packs als Startpunkt. Packs mit gewichtigem Melee-Combat (z.B. "Medieval Combat Animset") als Grundlage, angepasst
3. **Hero-Animations:** Custom oder MoCap für Kern-Movesets. Budget-Abhängig (Kap. 8.2)

**Control Rig:** IK für Fussplatzierung (Terrain-Anpassung), Waffenausrichtung (Aim Offset), und Rückenpanzerung (Socket-basiert). Control Rig ist Ü5-nativ und ersetzt die früheren AnimDynamics-Workarounds.

**Gewichtiges Kampfgefühl -- technische Hebel:**
- **Hitlag:** 2-4 Frames Pause bei Treffer (sowohl Spieler als auch Feind). Erzeugt das Gefühl von Masse und Impact
- **Camera Shake:** Subtil, richtungsabhängig. Kein Bildschirm-Schütteln, sondern ein kurzer Impuls in Angriffsrichtung
- **Zeitlupe:** Optional für kritische Treffer (0.2 s bei 0.7x Speed). Muss sich verdient anfühlen, nicht inflationär
- **Impact VFX:** Funken, Staub, Blutspuren. Niagara-Partikel, physikbasiert

### 3.4 Risiken und Mitigationen

| Risiko | Schwere | Mitigation | Fallback |
|--------|---------|------------|----------|
| Gameplay-Programmer verzögert sich | KRITISCH | Suche beginnt sofort (Woche 1). Finn führt Gespräche | Marketplace-Combat-Framework als Bridge (Risiko: GAS-Inkompatibilität) |
| GAS-Lernkurve zu steil | HOCH | Lyra-Projekt (Epic) als Referenz-Implementierung. Iterativer Aufbau, keine Gross-Architektur am Anfang | GAS-Kurs/Beratung einkaufen (500-1000 EUR Budget) |
| Kampf fühlt sich nicht "gewichtig" an | HOCH | Frühe Prototyp-Iteration. Game-Feel-Workshop in Woche 6-7: Hitlag, Kamera, Sound als isolierte Variablen testen | Referenz-Videos von Gothic/Dark Souls als Benchmark-Reihe |
| Motion Matching Daten unzureichend | MITTEL | Früh mit Mixamo-Daten testen. Marketplace-Packs evaluieren (Woche 4) | Fallback auf klassische Blend Trees (funktioniert, sieht schlechter aus) |

---

## 4. Asset-Pipeline

### 4.1 Modulares Kit-System

Die Asset-Strategie für RELICS ist modular. Das bedeutet: Wir bauen keine fertigen Gebäude, sondern einen Baukasten aus ~60 Architektur-Modulen (Wand-Segmente, Ecken, Türrahmen, Fenster, Dach-Elemente, Fundamente, Biotech-Elemente, Membran-Einschlüsse, organische Strukturen), aus denen sich hunderte Gebäude-Varianten zusammensetzen lassen.

Dieses Prinzip ist nicht optional, sondern überlebensnotwendig: Vera ist die einzige dedizierte Künstlerin im Team. Ohne modulares System müssen wir jedes Gebäude einzeln modellieren. Mit modularem System modelliert Vera die Module, und Level Design baut daraus eine Stadt.

**Fraktions-Differenzierung** erfolgt über Material-Instanzen, nicht über separate Meshes. Dieselbe Wand bekommt je nach Fraktion ein anderes Material. Hex-Codes 1:1 aus GDD-05 (Vera Kowalski, V1):

| Fraktion | Basis (70%) | Akzent (20%) | Highlight (10%) |
|----------|-------------|--------------|-----------------|
| Krone | `#3D3D3D` Aschgrau | `#8B1A2B` Karmin | `#C5A030` Altgold |
| Gilden | `#7A6E5D` Warmer Beton | `#C49A20` Amber | `#2EC4B6` Cyan |
| Orden | `#E8E4DE` Kalkweiss | `#4A5568` Schieferblau | `#D4A017` Bernstein |

**Globale Akzente (fraktionsunabhängig):**

| Kontext | Farbe A | Farbe B | Farbe C |
|---------|---------|---------|---------|
| Schattenfieber | `#2D0A31` Violett-Schwarz | `#39FF14` Giftgrün | -- |
| Wildnis/Neutral | `#5C6B3C` Moosgrün | `#8B7355` Erdton | `#9E9E9E` Nebel-Grau |
| Tiervolk | `#CC7722` Ocker | `#C04000` Terrakotta | `#C2B280` Sand |

Diese Hex-Codes sind verbindlich für alle Material-Instanzen. Jede Abweichung braucht explizite Abstimmung mit Vera (GDD-05) und dem CD.

**Fraktions-Material-Instanzen -- Beschreibung:**
- **Krone:** Eleganter Zerfall. Aschgrau-Stein mit Karmin-Biotech-Glow in Rissen, Altgold-Ornamente. Farbreferenz: `#3D3D3D` Basis, `#8B1A2B` Glow, `#C5A030` Metallakzent
- **Gilden:** Industrielle Eleganz. Warmer Beton-Grundton, Amber-Licht auf funktionalen Elementen, Cyan in aktiven Adern. Farbreferenz: `#7A6E5D` Basis, `#C49A20` Licht, `#2EC4B6` Biotech-Fluid
- **Orden:** Monolithisch, doppelte Lesart. Kalkweiss-Fassade mit Schieferblau-Schatten; innen Bernstein für verborgenes Biotech. Farbreferenz: `#E8E4DE` Fassade, `#4A5568` Schatten, `#D4A017` Geheimebene

### 4.2 Standards

| Standard | Wert | Begründung |
|----------|------|-------------|
| Texel Density (Hero) | 10.24 px/cm | Für Assets in Nahsicht (Waffen, Rüstungen, Interaktionsobjekte). Entspricht ~1024px auf 1m |
| Texel Density (Background) | 5.12 px/cm | Für Hintergrund-Assets (Architektur-Module, Terrain-Deko). Spart VRAM ohne sichtbaren Qualitätsverlust |
| Naming (Static Mesh) | `SM_[Kat]_[Name]_[Var]` | z.B. `SM_Wall_Stone_01`, `SM_Door_Wood_Gilden_02` |
| Naming (Material Instance) | `MI_[Fraktion]_[Material]` | z.B. `MI_Krone_Stein_Verwittert`, `MI_Gilden_Bronze_Poliert` |
| Naming (Skeletal Mesh) | `SK_[Typ]_[Name]` | z.B. `SK_Char_PlayerMale`, `SK_Creature_Infizierter_01` |
| LOD (Skeletal) | 3 Stufen | LOD0: Voll, LOD1: 50%, LOD2: 25%. Automatisch via Simplygon oder Ü5-Proxy |
| LOD (Static/Nanite) | Automatisch | Nanite übernimmt. Kein manueller LOD-Workflow nötig |
| Textur-Format | BC7 (Farbe), BC5 (Normal) | Standard-Kompression für Ü5. BC7 hat bessere Qualität als DXT5 bei gleicher Grösse |
| Max. Texturgrösse | 4096x4096 (Hero), 2048x2048 (Standard) | 4K nur für Hero-Assets. Alles andere 2K |

### 4.3 Prozedurale Systeme

#### Houdini-Terrain

Houdini ist das Kern-Tool für Terrain-Generierung. Der Workflow: Heightfield-Generation in Houdini, Erosion (hydraulisch + thermisch), Pfade und Strassen als Masken, Export über das Houdini Engine Plugin direkt in Ü5.

**Scope:** 4-6 km2, organisiert über Ü5 World Partition mit 256m x 256m Zellen. World Partition erlaubt, dass nur die sichtbaren Terrain-Zellen geladen werden -- essentiell für die Semi-Open-World ohne Ladebildschirme (GDD-01, Säule 1: Spielerwelt-Immersion).

**HDAs für Vera:** Ich baue Houdini Digital Assets mit vereinfachter Oberfläche. Vera soll nicht Houdini lernen müssen -- sie soll Parameter schieben können: Biom-Typ (Wald, Sumpf, Fels), Vegetationsdichte, Höhenvariation, Pfad-Breite. Das HDA generiert, sie iteriert, wir exportieren. Das ist der Produktivitätshebel.

Ehrliche Einschätzung: Die HDAs müssen WIRKLICH einfach sein. Vera ist eine schnelle Lernerin, aber Houdini hat die steilste Lernkurve in unserer gesamten Tool-Chain. Wenn die HDAs zu komplex werden, wird Vera sie nicht nutzen, und ich werde zum Flaschenhals. Erste HDA-Version muss in Woche 3 getestet werden.

#### PCG-Vegetation

Ü5s Procedural Content Generation (PCG) Framework für regelbasierte Vegetations-Platzierung. Die Regeln: Neigung (Gras nicht an Steilhängen), Höhe (Baumgrenze), Bodentyp (Sumpfpflanzen nur in Feuchtgebieten), Distanz zu Pfaden (keine Bäume AUF dem Weg), Distanz zu Gebäuden (Lichtung um Siedlungen).

Vera liefert 8-12 Vegetations-Assets pro Biom. PCG verteilt sie nach Regeln. Das spart hunderte Stunden manueller Platzierung.

#### Substance Designer

Prozedurale Materialien für sich wiederholende Oberflächen: Stein, Holz, Metall, Erde. Substance-Graphen exportieren direkt in Ü5-kompatible Texturen (Base Color, Normal, ORM). Die ACES-Konfiguration in Substance muss identisch zur Ü5-Konfiguration sein -- sonst driften die Farben.

### 4.4 Asset-Quellen

| Quelle | Einsatzbereich | Budget-Implikation | Risiko |
|--------|----------------|--------------------|--------|
| Vera (Eigenproduktion) | Characters, Hero-Props, Concept Art, UI-Elemente | Intern (Gehalt) | Flaschenhals -- eine Person für alles Visuelle |
| Tobi (prozedural) | Terrain, Felsen, Materialien, Vegetation-Verteilung | Intern (Gehalt) + Houdini-Lizenz | Houdini-Know-how ist nicht übertragbar |
| Megascans (Ü5 inklusive) | Umgebungs-Assets: Felsen, Boden, Vegetation-Basis | Kostenlos (Quixel Bridge) | Qualität gut, aber generisch -- braucht Anpassung für RELICS-Look |
| Marketplace (selektiv) | Basis-Assets zum Anpassen, Animation Packs, VFX | Budget: 2.000-3.000 EUR (Kap. 8.2) | Qualitätsschwankung. Jedes Asset muss vor Kauf geprüft werden |
| Photogrammetrie (optional) | Texturen, Fels/Mauerwerk-Referenz | Gering (eigene Ausrüstung) | Detmold/Lemgo-Umgebung als Quelle. Mittelalterliche Architektur vor der Haustür |

---

## 5. Schattenfieber-Tech

### 5.1 Systemübersicht & Drei-Schichten-Rendering (ERWEITERT V2, KORRIGIERT V3)

Das Schattenfieber ist das technisch anspruchsvollste System in RELICS. Es ist kein einzelner Effekt, sondern ein Querschnittssystem, das Rendering, VFX, Gameplay, Audio und Narrative verbindet.

**Kernprinzip:** Der Infektionswert (0-100, Float) ist der einzige Eingabeparameter für spielerseitige Effekte. Alle visuellen Effekte leiten sich von diesem einen Wert ab. Das System interpoliert kontinuierlich -- keine harten Stufenschalter (GDD-02, Kap. 2.3).

#### Drei-Schichten-Rendering (NEU V2, KORRIGIERT V3)

Die Welt in RELICS besteht aus drei Daseinsebenen (WBB-01, Emre Yilmaz, Kap. 3): **Mittelgrund** (die bewohnte Welt), **Hohlicht** (die obere Ebene -- ahd. *hoh + *lioht -- erhöhte Wahrnehmung, warm, vergessener Zustand), **Stillfeld** (die untere Ebene -- ahd. *stilli + *feld -- Ort der Stille, des Vergessens, der Auflösung). Normal ist nur der Mittelgrund sichtbar. Ab Schattenfieber-Schwelle (Infektionswert 76+) oder in bestimmten Lore-Orten beginnen die anderen Ebenen durchzuschimmern.

*V3-Korrektur: In V2 waren Hohlicht und Stillfeld vertauscht (Hohlicht fälschlich als "untere Ebene", Stillfeld als "obere Ebene"). Korrigiert gemäß WBB-01 Kap. 3: Hohlicht = obere Schicht, Stillfeld = untere Schicht.*

Technisch: Jede Ebene ist ein eigenes Post-Processing-Volume-Profil. Priority-Blending steuert, welche Profile aktiv sind. Maximum 3 aktive PP-Segmente gleichzeitig (Standard), Maximum 5 als absolutes Maximum in Endgame-Sequenzen. *(Annahme: 3 Standard. Emre-Bestätigung ausstehend -- s. Kap. 5.7.)*

| Schicht | PP-Profil | Visuelle Identität | Aktivierung |
|---------|-----------|---------------------|-------------|
| Mittelgrund | `PPV_Midground_Base` | Standard-Rendering. Fraktionsspezifisches Color Grading. Kein Zusatz-Overhead | Immer aktiv |
| Mittelgrund (Schattenfieber) | `PPV_SF_Player` | Spielerseitig MPC-gesteuert. Alle SF-Effekte Stufe 1-4 | Infektionswert > 0 |
| Hohlicht | `PPV_Hohlicht` | Obere Schicht. Warm, golden, intensiviert. Farbpalette: warme Töne, Kontrast erhöht, Lichtquellen scheinen zu pulsieren. Geometrie wirkt leichter, durchscheinender. WBB-01: "Hohlicht-warm" (Schwelle nach oben) | Infektionswert >= 76 ODER Zone-Trigger |
| Stillfeld | `PPV_Stillfeld` | Untere Schicht. Kalt, blaugrau, entsättigt. Farbpalette: Richtung `#2D0A31`, Schatten verlängert, Stille-Effekt. Geometrie wirkt schwerer, komprimierter. WBB-01: "Stillfeld-kalt" (Schwelle nach unten) | Infektionswert >= 90 ODER Zone-Trigger |
| Befallene Zone | `PPV_Zone_Befallen` | Level-Volume. Unabhängig von Spieler-Infektionswert. Schattenfieber-Farbprofil für alle sichtbar | Level-Placement |

*V3-Korrektur: PP-Profile für Hohlicht und Stillfeld waren in V2 vertauscht. Hohlicht ist gemäß WBB-01 die obere Schicht mit warmer Farbidentität ("Hohlicht-warm"). Stillfeld ist die untere Schicht mit kalter Farbidentität ("Stillfeld-kalt"). Visuelle Identitäten entsprechend korrigiert.*

**Maximale Gleichzeitigkeit:** 3 Profile im Normalfall (Base + SF_Player + ggf. Zone). 5 Profile als absolutes Maximum (Base + SF_Player + Hohlicht + Stillfeld + Zone -- nur in spezifischen Endgame-Sequenzen).

**Zwei Schattenfieber-Farbprofile:**
- **Profil A (spielerseitig):** MPC-gesteuert. Skaliert mit Infektionswert. Intensität graduell. Nur der Spieler sieht dieses Profil in seiner vollen Intensität.
- **Profil B (zonenbasiert):** Level-Volume, feste Werte. Alle Spieler sehen befallene Zonen gleich. Unabhängig von persönlichem Infektionswert -- das sind öffentliche Warnzeichen.

### 5.2 Technische Architektur (unverändert)

Das System besteht aus drei Schichten:

**Schicht 1: Material Parameter Collection (MPC)**
Eine zentrale MPC (`MPC_Schattenfieber`) hält den Infektionswert als skalaren Parameter. Alle Post-Processing-Materialien, Niagara-Systeme und Welt-Shader lesen diesen Wert. Änderungen am Infektionswert propagieren automatisch in alle Systeme -- kein manuelles Update nötig.

**Schicht 2: Post-Processing Volume**
Ein eigener Post-Processing Volume, der dem Spielercharakter folgt (nicht level-global). Die Material-Instanzen in diesem Volume lesen die MPC und skalieren ihre Effekte entsprechend.

**Schicht 3: Niagara VFX**
GPU-Partikel-Systeme, die ebenfalls die MPC lesen. Schattensporen, Flimmern, Verzerrungspartikel -- alles skaliert mit dem Infektionswert.

### 5.3 Fünf-Stufen-Rendering (KORRIGIERT V2 -- CD-Lock Stufengrenzen)

CD-verbindliche Stufengrenzen: Rauschen 1-40, Risse 41-75, Schwelle 76-100.

| Stufe | Lore-Phase | Infektionswert | Post-Processing Effekte | Niagara VFX | Welt-Effekte | Technische Komplexität |
|-------|-----------|---------------|------------------------|-------------|--------------|------------------------|
| 0 (Rein) | -- | 0 | Keine | Keine | Keine | Baseline |
| 1 (Rauschen Früh) | Rauschen | 1-20 | Leichte Farbverschiebung in den Schatten (kühler, bläulicher). Subtiles Vignette-Pulsieren (0.05 Hz) | Vereinzelte Schattensporen (2-5 Partikel, kaum sichtbar) | Schattensinne: Versteckte Objekte erhalten Custom Stencil Outline | Niedrig |
| 2 (Rauschen Spät) | Rauschen | 21-40 | + Chromatische Aberration (einsetzend, 0.05-0.15). Farbsättigung beginnt zu verschieben (Grün > Cyan am Rand) | + Partikel-Overlay dichter (10-15 Partikel). Emotionsauren an NPCs als farbige Niagara-Systeme | + Gesprächsoptionen-Shader: UI-Text für SF-Dialoge mit leichtem Glitch | Mittel |
| 3 (Risse) | Risse | 41-75 | + Geometrische Verzerrung am Bildrand (Barrel Distortion, animiert). Farbpalette kippt merklich. Depth-of-Field-Schimmer auf mittlerer Distanz. CA stärker (0.2-0.5) | + Schattenranken-Partikel am Bildrand. Tiefensicht als Niagara-Overlay (geologische Schichten, Adern im Terrain) | + Custom Stencil Buffer für Objekte, die nur ab Rissen sichtbar sind. Fragwürdige NPCs mit Flimmer-Shader | Hoch |
| 4 (Schwelle) | Schwelle | 76-100 | + Halluzinatorische Elemente (s. Kap. 5.4). Vertex-Displacement auf Welt-Geometrie. Doppelbilder (Ghost-Rendering). Farbkanal-Separation. Hohlicht (warm/golden, von oben) und Stillfeld (kalt/blaugrau, von unten) beginnen durchzuschimmern (Kap. 5.1) | + Vollständiges Sporen-Feld. Schatten bewegen sich autonom. Lichtquellen flackern asynchron | + Parallel-Geometrie: Ganze Raum-Segmente in alternativer Version. NPCs ohne visuellen Unterschied zu "echten" NPCs | Sehr hoch |

### 5.4 Graduelle Interpolation -- Technik (KORRIGIERT V2)

Der Trick ist, dass alle Effekte nicht bei Stufengrenzen "anspringen", sondern über Kurven interpoliert werden:

- **Farbverschiebung:** `Lerp(NormalMatrix, VerschobenMatrix, InfektionswertFloat / 100)`. Beginnt bei Wert 1, voll bei 100.
- **Chromatische Aberration:** Intensität = `max(0, (Infektionswert - 20) / 80)`. Beginnt bei ~20, erreicht Maximum bei 100.
- **Geometrische Verzerrung (Barrel):** Intensität = `max(0, (Infektionswert - 41) / 59)`. Beginnt bei 41 (Risse-Grenze), graduell bis 100.
- **Halluzinationen:** `max(0, (Infektionswert - 76) / 24)`. **Beginnt bei 76 (Schwelle-Grenze).** Maximum bei 100. *(V1-Fehler: Start bei 70 -- korrigiert auf 76 per CD-Lock.)*
- **Hohlicht-Einblendung:** `max(0, (Infektionswert - 76) / 24)`. Gleiche Kurve wie Halluzinationen. Schwelle-Phase = Hohlicht (obere Schicht, warm) beginnt sichtbar zu werden.
- **Stillfeld-Einblendung:** `max(0, (Infektionswert - 90) / 10)`. Erst bei 90, extrem kurzer Bereich. Stillfeld (untere Schicht, kalt) -- sehr intensive Wirkung.

Alle Kurven sind in Ü5 als **Float Curve Assets** hinterlegt und können im Editor angepasst werden, ohne Code zu ändern. Emre und Nami können diese Kurven mitgestalten -- sie definieren, WANN sich etwas "richtig" anfühlt.

### 5.5 Welt-Effekte (Befallene Zonen)

Befallene Zonen in der Spielwelt haben eigene Post-Processing Volumes (Profil B, s. Kap. 5.1) mit vorab gesetzten Schattenfieber-Effekten -- unabhängig vom Infektionswert des Spielers. Diese Zonen sind für ALLE Spieler sichtbar.

- **Biotech-Vegetation:** Organische Auswüchse, pulsierende Ranken. Vertex-Animation (kein Nanite), emissive Materialien mit Pulse-Funktion. Farben: `#2D0A31` + `#39FF14`
- **Boden-Shader:** Terrain-Material mit zusätzlichem Schattenfieber-Layer (organische Textur, leicht animiert)
- **Niagara-Atmosphäre:** Schattensporen als GPU-Partikel, Nebel mit volumetrischem Scattering. Emres Nebel-Beschreibung ("Nebel, der sich anfühlt wie Trauer") = technische Parameter: langsame Partikel, tiefe Sättigung in `#2D0A31`, Gewicht nach unten (negative Y-Geschwindigkeit), kaum horizontale Drift.

### 5.6 Performance-Implikation

Das Schattenfieber-System hat ein eigenes Performance-Budget von **2 ms GPU-Zeit** (bei empfohlener Hardware). Aufgeteilt:
- Post-Processing (alle aktiven Profile): 0.8 ms
- Niagara-Partikel: 0.7 ms (GPU-Partikel, LOD-aware)
- Custom Stencil / Welt-Effekte: 0.5 ms (nur in befallenen Zonen aktiv)
- Drei-Schichten-Overhead (Hohlicht/Stillfeld aktiv): +0.3 ms Reserve einplanen

Bei Stufe 0 ist das Budget nahe 0 ms. Das System kostet nur, wenn es aktiv ist.

### 5.7 Abhängigkeiten und offene Punkte (AKTUALISIERT V3)

| Abhängigkeit | Von wem | Status | Dringlichkeit |
|--------------|---------|--------|---------------|
| Hauten-Segmentanzahl (3 oder 5 Standard?) | Emre (Lore-Logik) | Offen -- Annahme 3 Standard beibehalten. Emre-Bestätigung ausstehend. | MITTEL |
| Visueller Referenz Stufe 3-4 | Emre (Lore), Vera (Concept) | Offen | HOCH -- ohne Referenz baue ich ins Blaue |
| Infektionswert-Gameplay-Logik | Darius (GDD-02) | V0.5 vorhanden | Mittel |
| Narrative Zustände -> visuelle Parameter | Nami | Rauschen/Risse/Schwelle definiert | Mittel |
| Audio-Verzerrung (Risse+) | Offen (kein Audio-Lead) | Nicht begonnen | Niedrig für V1, hoch für VS |
| Abstimmungsmeeting Schattenfieber-Tech | Tobi + Emre + Darius + Vera | Noch nicht terminiert | HOCH -- nächste Woche |

---

## 6. Performance-Ziele

### 6.1 Hardware-Tiers

RELICS definiert drei Hardware-Tiers. Die Ziel-Framerates sind ambitioniert, aber durch Upscaling-Technologie erreichbar.

| Tier | GPU-Referenz | CPU-Referenz | RAM | Ziel-FPS | Auflösung | Rendering |
|------|-------------|-------------|-----|----------|-----------|-----------|
| Minimum | GTX 1070 / RX 5700 | i5-8400 / R5 3600 | 16 GB | 30 fps | 1080p | Software Lumen, Low Settings, FSR Quality |
| Empfohlen | RTX 3070 / RX 6800 | i7-10700 / R7 5800X | 16 GB | 60 fps | 1440p | HW RT Lumen, High Settings, DLSS/FSR Quality |
| High-End | RTX 4080+ / RX 7900 XT | i7-12700+ / R7 7800X3D | 32 GB | 60 fps | 4K | Max Settings, RT Reflections, DLSS/FSR Performance |

**Redaktionelle Notiz:** Minimum-Tier (GTX 1070) ist provisorisch. GTX 1070 mit Software Lumen, Nanite und Schattenfieber-Effekten bei 30 fps ist ambitioniert. Der tatsächliche Minimum-Tier wird nach Benchmark-Phase (Woche 6-8) final gesetzt -- möglicherweise auf GTX 1660 / RX 5500 XT verschoben. Das ist eine datenbasierte Entscheidung.

### 6.2 Upscaling (Pflicht)

Upscaling ist nicht optional, sondern ein Kern-Feature:
- **DLSS 3** (Nvidia): Super Resolution + Frame Generation
- **FSR 3** (AMD): Super Resolution + Fluid Motion Frames
- **XeSS** (Intel): Optional, niedriger Prio

DLSS und FSR sind der Grund, warum 60 fps bei 4K realistisch ist. Ohne Upscaling wäre 4K/60 auf keiner Consumer-Hardware erreichbar.

Frame Generation als Option für unterstützte Hardware. Nicht als Standard aktiviert -- Eingabe-Latenz ist bei Action-Combat relevant.

### 6.3 Performance-Budgets

| Kategorie | Budget | Begründung |
|-----------|--------|-------------|
| Draw Calls | < 5.000 pro Frame | Nanite reduziert Draw Calls drastisch. 5.000 ist konservativ und lässt Raum für UI und Partikel |
| Dynamische Lichter | 8-12 gleichzeitig | VSM-Limit. Darüber hinaus Performance-Einbruch |
| Vegetation Draw Distance | Gras: 50-80 m, Bäume: 500 m | Gras ist der teuerste Vegetationstyp. Bäume als Impostors ab 300 m |
| NPC-Count (sichtbar) | 20-30 gleichzeitig | StateTree + Mass Entity System |
| Partikel (Schattenfieber) | GPU-Budget: 2 ms | Kap. 5.6. LOD-aware: Partikel-Count sinkt mit Distanz |
| Speicher (VRAM) | 6 GB (Minimum), 8 GB (Empfohlen) | Nanite-Geometrie + Streaming-Texturen + Lumen-Datenstrukturen |
| Level-Streaming | World Partition, 256 m Zellen | Laderadius: 3-4 Zellen um Spieler |
| SSS (Hauten-Shader) | 0.3-0.5 ms | Screen-Space-Overhead. Nur auf organischen Hero-Assets aktiv |
| WPO-System | 0.2 ms | Nur aktive organische Elemente im Sichtfeld |

---

## 7. Produktions-Pipeline

### 7.1 Versionskontrolle

Zwei Systeme, klar getrennt:

**Perforce (Helix Core)** für das Ü5-Projekt. Das umfasst alle Binär-Assets (Meshes, Texturen, Maps, Blueprints, Sound). Perforce ist der Industriestandard für Unreal-Projekte, weil es Binär-Dateien nativ sperren kann (File Locking). Kein Git LFS für Engine-Assets.

**Git** für Dokumentation (GDD, WBB, dieses Dokument), Scripts, Pipeline-Tools.

### 7.2 Ordnerstruktur (Ü5-Projekt)

```
Content/
  RELICS/
    Characters/
      Player/
      NPCs/
      Creatures/
    Environment/
      Architecture/
        Modules/
        Assembled/
      Vegetation/
        Trees/
        Ground/
        Schattenfieber/
      Terrain/
    Props/
      Weapons/
      Furniture/
      Interactive/
    Materials/
      Master/
      Instances/
        Krone/
        Gilden/
        Orden/
        Schattenfieber/
        Organisch/       -- NEU: SSS-Profile, WPO-Materialien
    VFX/
      Niagara/
        Combat/
        Schattenfieber/
        Environment/
    Audio/
    UI/
      HUD/
      Menus/
      Nervensystem/
    Blueprints/
      Core/
      Combat/
      Camera/
      AI/
      Schattenfieber/    -- MPC, PP-Volumes, alle fünf Profile
    Maps/
      Persistent/
      Sublevels/
      Test/
    Data/
      DataTables/
      Curves/            -- Float Curves: SF-Parameter, Kamera-Blends, WPO-Intensität
      GameplayTags/
```

### 7.3 Tool-Chain

| Tool | Version | Einsatz | Verantwortlich | Lizenzkosten (jährlich) |
|------|---------|---------|----------------|-------------------------|
| Unreal Engine 5.4+ | Latest stable | Runtime, Level Design, Blueprints, Sequencer | Tobi, Darius, Gameplay-Programmer | Kostenlos (5% Royalty ab 1M USD) |
| Houdini Indie | 20.5+ | Terrain, prozedurale Assets, FX-Prototyping | Tobi | ~270 EUR/Jahr |
| Houdini Engine (Ü5 Plugin) | Matching | Houdini-Ü5-Bridge | Tobi | In Indie-Lizenz enthalten |
| Substance Painter | Latest | Texturierung, Materialien | Vera, Tobi | ~220 EUR/Jahr (Indie) |
| Substance Designer | Latest | Prozedurale Materialien | Tobi | In Substance-Abo enthalten |
| Blender | 4.x | 3D-Modelling, Rigging, UV-Layout | Vera | Kostenlos |
| Photoshop / Krita | Latest | Concept Art, Texturen, UI-Mockups | Vera | ~290 EUR/Jahr (PS) oder kostenlos (Krita) |
| Perforce Helix Core | Latest | Asset-Versionskontrolle | Tobi (Admin) | Kostenlos bis 5 User |
| Jira / Notion | TBD | Taskmanagement, Sprint-Planung | Finn | ~0-100 EUR/Jahr |
| DaVinci Resolve | 19+ | Color Grading Referenz, Trailer-Schnitt | Tobi | Kostenlos (Free Version) |

**Gesamte jährliche Tool-Kosten:** ~780-1.080 EUR.

---

## 8. Meilensteine & Budget

### 8.1 Phasen

| Phase | Zeitraum | Kern-Deliverables | Abhängigkeit | Exit-Kriterium |
|-------|----------|-------------------|---------------|----------------|
| **Pre-Production** | Wochen 1-4 | GDD V1 + WBB V1 fertig. Ü5-Projekt steht. Kamera-Prototyp spielbar. Terrain-Prototyp (1 km2). Art-Style-Targets validiert | Team komplett (minus Gameplay-Programmer) | CD gibt Design-Lock. Alle können im Ü5-Projekt arbeiten |
| **Vertical Slice Prototype** | Wochen 5-12 | Spielbare Szene: 1 Region (~1 km2), Hauptquest-Ausschnitt (30 min Gameplay), Combat V1 (Schwert + Bogen, 3 Feindtypen), 1 Stadt (Blockout), Schattenfieber Stufe 0-2 | Gameplay-Programmer an Bord (spätestens Woche 5) | Szene spielbar. Combat fühlt sich "gewichtig" an |
| **Vertical Slice Polish** | Wochen 13-18 | VS spielbar und präsentabel: Beleuchtung (Lumen-Pass), Asset-Polish (Nanite, Material-Instanzen), Quest komplett, Performance-Ziele auf empfohlener Hardware, Schattenfieber Stufe 0-3 | Asset-Pipeline läuft | VS vorzeigbar (CD, Publisher, Presse) |
| **Alpha** | Wochen 19-30 | Gesamte Kernregion (4-6 km2). Alle Quests (Greybox). Combat V2 (alle 6 Waffenklassen). Nervensystem-Leveling spielbar. Alchemie V1. Schattenfieber alle Stufen inkl. Drei-Schichten | Scope-Lock (spätestens Ende Woche 18) | Feature-Complete |
| **Beta** | Wochen 31-40 | Content-Complete. Polish-Pass. QA-Runden. Performance-Optimierung. Balancing | QA-Kapazität | Alle bekannten Blocker gefixt |
| **Release** | Woche 40+ | Steam Early Access oder Full Release | CD-Entscheidung | Spielbar, stabil, repräsentativ |

### 8.2 Budget-Aufschlüsselung (45.000 EUR Freelancer-Budget) -- ERWEITERT V2

Das Freelancer-Budget ist begrenzt und muss strategisch eingesetzt werden.

| Position | Geschätztes Budget | Zeitraum | Begründung |
|----------|-------------------|----------|-------------|
| **Gameplay-Programmer (GAS/Combat)** | 20.000-25.000 EUR | Wochen 5-18 (14 Wochen) | Kritischste Abhängigkeit. Ohne diese Person kein Combat, kein VS. ~1.400-1.800 EUR/Woche |
| **Animations-Assets** | 5.000-8.000 EUR | Wochen 8-18 | Marketplace-Packs + Custom-Anpassung. Motion-Matching-Datenbank. Ggf. MoCap-Session (~2.000 EUR für einen Tag) |
| **Audio/Sound Design** | 5.000-7.000 EUR | Wochen 13-30 | MetaSounds-Setup, Combat-SFX, Ambient, Schattenfieber-Audio |
| **QA-Support** | 3.000-5.000 EUR | Wochen 25-40 | Externe Tester für Schattenfieber-Stufenübergänge |
| **Marketplace-Assets** | 2.000-3.000 EUR | Laufend | Architektur-Bases, Vegetation-Packs, VFX-Bibliotheken |
| **Puffer** | 2.000-5.000 EUR | Reserve | Unvorhergesehenes |
| **Gesamt** | ~37.000-53.000 EUR | | Mittelwert: ~45.000 EUR |

**Anforderungsprofil Gameplay-Programmer (PFLICHT-Kriterien):**

- **GAS (Gameplay Ability System): Pflicht-Kriterium.** Wer kein nachweisbares GAS-Projekt vorweisen kann, kommt nicht in die engere Auswahl. Keine Ausnahmen.
- Ü5 C++ auf Produktionsniveau (kein Blueprint-only)
- StateTree-Erfahrung oder Bereitschaft zur schnellen Einarbeitung (gute Dokumentation vorhanden)
- Freelancer-Erfahrung: Milestone-basierte Abrechnung muss akzeptabel sein
- Verfügbarkeit ab Woche 5 (spätestens)
- Kommunikationssprache Deutsch oder Englisch

**Wunsch-Kriterien (kein Ausschluss):**
- Erfahrung mit Third-Person-Action-Spielen (Gothic, Souls-artige als Referenz)
- Motion Matching Erfahrung (Ü5)
- Vertrautheit mit ACES-Farb-Pipelines

**Suche beginnt:** Sofort (Woche 1). Finn führt erste Gespräche. Stellenbeschreibung: Abstimmung Tobi+Finn.

**Ehrliche Einschätzung:** 45.000 EUR ist ein sehr knappes Budget. Der Gameplay-Programmer allein verbraucht die Hälfte. Wenn diese Person länger als 14 Wochen braucht oder teurer ist als geschätzt, wird der Rest des Budgets komprimiert. Risiko-Mitigation: Früh mit der Suche beginnen, klaren Scope kommunizieren, Milestone-basierte Bezahlung vereinbaren.

---

## Anhang A: Offene Fragen (Priorisiert)

### Kritisch

1. **Schattenfieber-Abstimmung** mit Emre, Darius und Vera -- Was genau passiert visuell auf jeder Stufe? Ich brauche Concept-Referenzen, bevor ich Shader baue. Vorschlag: 30-Minuten-Meeting, Vera skizziert live.
2. **Hauten-Segmentanzahl** mit Emre -- 3 oder 5 gleichzeitig aktive PP-Segmente als Standard? Lore-Logik entscheidet. *(V3: Annahme 3 bleibt bestehen. Emre-Bestätigung ausstehend.)*
3. **Asset-Standards-Review** mit Vera -- Naming, Texel Density, LOD-Workflow, Hex-Code-Umsetzung in Material-Instanzen bestätigen.
4. **Gameplay-Programmer-Profil** mit Finn -- Stellenbeschreibung schreiben, Suche starten.

### Wichtig (Pre-Production)

5. **Dialog-System-Middleware** mit Nami -- Yarn Spinner, Ink, oder Ü5-eigenes System?
6. **Audio-Pipeline** -- Wer verantwortet MetaSounds-Setup?
7. **Terrain-Biome** mit Emre -- Wie viele, welche? Jedes Biom braucht HDA + Vegetations-Assets.

### Nachrangig (Vertical Slice)

8. **Konsolen-Stretch-Goal** -- Erst nach VS Polish evaluieren (Woche 18).
9. **Lokalisierung** -- Nur Deutsch? Deutsch + Englisch? Beeinflusst UI-Layout.
10. **Accessibility** -- Farbblindheits-Modi, Untertitel-Grössen, Remapping. Früh in UI-Architektur berücksichtigen.

---

## Anhang B: Glossar

| Begriff | Erklärung |
|---------|-----------|
| ACES | Academy Color Encoding System. Industriestandard für konsistenten Farbraum über mehrere Tools |
| GAS | Gameplay Ability System. Ü5-natives Framework für Fähigkeiten, Attribute und Gameplay-Effekte |
| HDA | Houdini Digital Asset. Wiederverwendbarer, parametrischer Houdini-Node mit vereinfachter Oberfläche |
| MPC | Material Parameter Collection. Ü5-System, um globale Werte an alle Materialien gleichzeitig zu senden |
| Nanite | Ü5-System für virtualisierte Geometrie. Automatisches LOD ohne künstlerischen Aufwand |
| Lumen | Ü5-System für dynamische globale Beleuchtung. Kein Baking nötig |
| PCG | Procedural Content Generation. Ü5-Framework für regelbasierte Asset-Platzierung |
| VSM | Virtual Shadow Maps. Ü5-Schattensystem mit hoher Auflösung |
| VS | Vertical Slice. Spielbarer, repräsentativer Ausschnitt des fertigen Spiels |
| MoCap | Motion Capture. Aufzeichnung realer Bewegungen für Spielanimationen |
| SSS | Subsurface Scattering. Lichtstreuung unterhalb einer Oberfläche. Essentiell für organische/Haut-Materialien |
| WPO | World Position Offset. Vertex-Displacement im Shader. Grundlage für atmende, lebende Oberflächen |
| PPV | Post-Processing Volume. Ü5-Container für Screen-Space-Effekte |
| SF | Schattenfieber. Abkürzung intern |

---

*Tobi Richter, Tech Corner, Tag 6 Montag Nachmittag -- V3 Korrektur-Pass.*
*Änderungen V3: Hohlicht/Stillfeld-Vertauschung korrigiert (WBB-01 Kap. 3 ist kanonisch). PP-Profile Hohlicht (warm/oben) und Stillfeld (kalt/unten) richtig zugeordnet. Design-Säulen-Referenzen auf GDD-01 V2 aktualisiert (P4 -> Säule 1, P6 -> Säule 7, P2 -> Säule 2). Hauten-Segmentanzahl: Annahme 3 Standard beibehalten, Emre-Bestätigung als offener Punkt.*
*Nächster Schritt: Emre-Bestätigung Hauten-Segmente einholen, Schattenfieber-Abstimmung terminieren, Kamera-Blueprint V0.1.*
