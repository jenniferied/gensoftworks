# GDD-06 — Technische Spezifikation & Produktion

**Projekt:** RELICS
**Autoren:** Tobi Richter (Technik), Finn (Produktion)
**Version:** V1
**Stand:** Tag 3, Mittwoch — Produktionsphase
**Status:** Ausformuliertes Arbeitsdokument. Alle technischen Entscheidungen begruendet. Offene Punkte markiert.
**Aenderungslog:**
- V0.1 (Tag 2): Outline mit Kapitelstruktur und Kerntabellen
- V1 (Tag 3): Volltext, Budget-Aufschluesselung, Schattenfieber-Tech auf fuenf Stufen erweitert, Abstimmung mit GDD-02 (Darius) und GDD-01 (Design-Saeulen)

---

## 1. Engine & Rendering

### 1.1 Engine-Wahl

RELICS wird in **Unreal Engine 5.4+** entwickelt (bestaetigt Tag 1, Szene 3). Die Engine-Entscheidung basiert auf drei Faktoren: Nanite und Lumen liefern die Rendering-Qualitaet, die der Dark-Fantasy-Look erfordert, ohne dass wir eine eigene Render-Pipeline bauen muessen. Das Gameplay Ability System (GAS) ist die einzige Engine-native Loesung, die Darius' dreischichtiges Combat-System (GDD-02, Kap. 1.2) ohne Drittanbieter-Middleware abbilden kann. Und die Marketplace-Infrastruktur ist fuer ein kleines Team wie unseres ein realer Produktionsfaktor — nicht als Ersatz fuer eigene Assets, sondern als Basis zum Anpassen.

**Zielplattform:** PC first (Windows). Konsolen sind ein Stretch Goal, das fruehestens nach dem Vertical Slice evaluiert wird. Die Entscheidung fuer PC first ist keine Einschraenkung, sondern eine bewusste Scope-Steuerung: Konsolen-Portierung erfordert Anpassungen an Controller-UI, Performance-Optimierung fuer fixe Hardware und Zertifizierungsprozesse, die unser aktuelles Team nicht stemmen kann.

**Singleplayer.** Kein Multiplayer-Backend, kein Koop, keine Online-Features. Das vereinfacht die Architektur erheblich und eliminiert eine ganze Kategorie technischer Risiken.

### 1.2 Rendering-Architektur

#### Nanite (Virtualisierte Geometrie)

Nanite ist das primaere Geometrie-System fuer alle statischen Hard-Surface-Meshes: Architektur, Props, Waffen, Terrain-Deko, Felsen. Die Kernidee: Kuenstler muessen keine manuellen LOD-Ketten mehr bauen. Nanite uebernimmt die geometrische Vereinfachung zur Laufzeit, was besonders bei modularen Architektur-Kits (Kap. 4.1) die Produktionsgeschwindigkeit drastisch erhoeht.

Einschraenkungen, die den Workflow betreffen:
- **Skeletal Meshes** (Charaktere, Kreaturen, NPCs) unterstuetzen kein Nanite. Hier verwenden wir klassische LOD-Ketten mit drei Stufen (High, Mid, Low). Vera modelliert High-Poly, die LODs werden semi-automatisch generiert (Simplygon oder UE5-internes Proxy-System).
- **Vegetation** ist ein Hybrid: Baumstaemme und grosse Gehoelze als Nanite-Meshes, Blaetter und Gras als traditionelle Alpha-Karten mit Dithering. Der Grund: Nanite kann keine Alpha-Masken verarbeiten, und Wind-Animation (World Position Offset) funktioniert nur mit traditionellen Meshes.
- **Vertex-Animation** ist ueber Nanite nicht moeglich. Das ist direkt relevant fuer pulsierende Biotech-Elemente und Schattenfieber-Vegetation (Kap. 5). Diese Assets muessen als traditionelle Meshes mit Vertex-Animation gebaut werden — ein bewusster Ausschluss, den Vera kennen muss.

#### Lumen (Globale Beleuchtung)

Lumen ist das primaere GI-System. Wir verwenden keine gebackenen Lightmaps. Das ist eine fundamentale Entscheidung: In einer Welt, die auf Environmental Storytelling setzt (GDD-01, Saeule P4), muss Licht dynamisch auf Spieleraktionen reagieren koennen — eine Fackel geht aus, ein Feuer wird entzuendet, die Tageszeit wechselt. Gebackene Beleuchtung kann das nicht.

**Shipping-Konfiguration:** Hardware Ray Tracing (HW RT Lumen). Das liefert die beste Qualitaet bei Innenraeumen (die fuer RELICS' gotische Architektur zentral sind) und haelt die visuellen Artefakte minimal, die Software Lumen in engen Raeumen mit vielen Lichtquellen produziert.

**Fallback:** Software Lumen fuer Hardware ohne RT-Unterstuetzung (Minimum-Tier, siehe Kap. 6). Die visuellen Unterschiede sind akzeptabel, solange wir Innenraeume nicht auf mehr als 4-5 Bouncen angewiesen machen.

**Referenz-Look:** Control (Remedy) fuer Innenraeume — praezise Lichtfuehrung, dramatische Schatten, praktische Lichtquellen als Gestaltungselement. Alan Wake 2 fuer Aussenraeume — natuerliches Licht, atmosphaerische Streuung, keine ueberbelichteten Himmel.

#### Virtual Shadow Maps (VSM)

Standard bei Lumen-Projekten. VSM liefert hochaufloesende Schatten ohne die Artefakte klassischer Cascaded Shadow Maps. Das Budget: maximal 8-12 dynamische Lichtquellen gleichzeitig pro Szene. Das klingt nach wenig, ist aber ausreichend, wenn wir konsequent mit praktischen Lichtquellen arbeiten (Fackeln, Feuer, Laternen) und globale Beleuchtung den Rest uebernimmt.

Risiko: VSM hat in UE 5.3/5.4 noch Performance-Spitzen bei vielen ueberlappenden Schatten. Epic verbessert das kontinuierlich, aber wir muessen in der Prototyping-Phase Worst-Case-Szenen testen (z.B. Marktplatz mit 12 Laternen).

#### Farb-Pipeline

Die Farb-Pipeline ist eine der Entscheidungen, die unsichtbar ist, wenn sie funktioniert, und katastrophal, wenn sie es nicht tut. RELICS verwendet **ACES (Academy Color Encoding System)** als Arbeitsfarbraum ueber die gesamte Tool-Chain: Substance Designer/Painter, Houdini, Unreal Engine 5. Das stellt sicher, dass Farben konsistent bleiben, egal welches Tool sie erzeugt hat.

Warum ACES und nicht sRGB? Weil RELICS eine duester-farbige Palette braucht (Briefing: "Duester, aber farbig. Kein Entsaettigungs-Klischee.") und sRGB im Low-Key-Bereich Farbinformationen verliert. ACES hat einen groesseren dynamischen Umfang und bewahrt Farbnuancen in den Schatten — genau dort, wo unser Spiel lebt.

**Tone Mapping:** ACES als Standard-Tone-Mapper in UE5, mit der Option auf eine Custom LUT, wenn der generische ACES-Look zu "filmlastig" wirkt. Evaluation im Prototyp.

**Deakins-Prinzip (intern):** Roger Deakins arbeitet mit reduzierter Beleuchtung, aber nie mit entsaettigten Farben. Ein dunkler Raum ist nicht grau — er ist tiefblau, warm-orange am Rand, mit Farbtemperatur-Kontrast. Dieses Prinzip gilt fuer jeden beleuchteten Raum in RELICS.

### 1.3 Post-Processing Stack

Der Post-Processing Stack ist bewusst zurueckhaltend. Jeder Effekt muss einen narrativen oder gameplay-relevanten Grund haben. "Sieht cool aus" ist kein Grund.

| Effekt | Einstellung | Begruendung |
|--------|-------------|-------------|
| Color Grading | Gedaempfte Palette, fraktionsspezifisch | Krone: warme Verrottung (Gold/Amber). Gilden: kuehle Praezision (Blaugruen/Bronze). Orden: entsaettigte Monochromie (Grau/Weiss) |
| Vignette | Subtil (0.3-0.4) | Fokussiert den Blick, verstaerkt Tunneleffekt in engen Raeumen |
| Depth of Field | Cinematisch in Dialogen (f/2.8-Simulation), minimal im Gameplay | Dialog-Kamera braucht Bokeh fuer Portraitqualitaet. Im Gameplay wuerde DOF die Lesbarkeit stoeren |
| Bloom | Nur praktische Lichtquellen | Fackeln, Feuer, Schmelzoefen. Kein Lens-Flare. Kein Glow auf Materialien ohne Emissionsgrund |
| Motion Blur | Per-Object (Waffen-Swings, Feindangriffe) | Verstaerkt das Gewicht von Kampfaktionen. Kein Camera Motion Blur — das erzeugt Uebelkeit und stoert die Lesbarkeit |
| Film Grain | Optional (Spielereinstellung) | Manche Spieler moegen den filmischen Look, andere nicht. Keine Default-Aktivierung |
| Chromatische Aberration | Nur Schattenfieber (Kap. 5) | Kein genereller CA-Effekt. Ausschliesslich als Infektionsindikator |

---

## 2. Kamerasystem

### 2.1 Architektur

Das Kamerasystem basiert auf UE5s **Spring Arm Component**. Die Entscheidung fuer Spring Arm (statt eines vollstaendig custom Kamerasystems) ist pragmatisch: Spring Arm loest Wandkollision, Lagging und Distanz-Management out of the box. Custom-Erweiterungen koennen darueber gebaut werden, ohne die Basis neu zu erfinden.

**Third Person ist der Primaermodus** (bestaetigt Tag 1). Der Spielercharakter ist sichtbar, customizable Ruestung und Kleidung sind ein visuelles Belohnungssystem (Briefing). Ein reiner First-Person-Modus wuerde den Animationsaufwand verdoppeln (Arm-Rigs, FP-Waffen-Meshes, separate Animationssets) und ist daher als V2/DLC-Stretch-Goal klassifiziert.

**Architektonische Vorbereitung fuer FP:** Die Spring-Arm-Architektur erlaubt einen Arm-Length-Wert von 0, was mathematisch einem FP-Modus entspricht. Wir bauen keine FP-Features, aber wir verbauen auch nichts, was FP spaeter unmoeglich machen wuerde. Kein Gameplay-Code darf die Existenz eines sichtbaren Spielercharakters voraussetzen.

**Zoom:** Stufenlos via Mausrad (PC) oder rechtem Stick (Controller). Der Zoom interpoliert zwischen den Kontext-Modi-Parametern, nicht nur die Arm-Distanz.

### 2.2 Kontext-Modi

Das Kamerasystem wechselt kontextabhaengig zwischen vier Modi. Der Wechsel ist kein harter Cut, sondern ein parametrischer Blend ueber die angegebene Dauer.

| Modus | Arm Length | FOV | Offset | Blend-Dauer | Ausloeser |
|-------|-----------|-----|--------|-------------|-----------|
| Exploration | 350 cm | 78 deg | Leicht rechts (+30 cm) | Standard | Default-Modus, aktiv bei freier Bewegung |
| Combat | 200 cm | 82 deg | Ueber Schulter (+50 cm, +20 cm hoch) | 0.3 s | Feind im Engagement-Radius oder Waffe gezogen |
| Dialog | 100 cm | 72 deg | Schulterblick, Blick auf NPC-Gesicht | 0.5 s | Dialog-Trigger |
| Inspect | 400 cm | 70 deg | Zentriert (Offset 0) | 0.3 s | Inventar, Karte, Nervensystem-UI |

**Exploration** ist der Ruhezustand. Die leichte Rechts-Verschiebung gibt dem Spieler Sichtfeld links vom Charakter — das ist intuitiver fuer rechtsdominante Spieler und laesst Raum fuer UI-Elemente am linken Rand.

**Combat** zieht die Kamera naeher heran und erhoeht das FOV leicht. Das erzeugt ein Gefuehl von Geschwindigkeit und Enge, ohne die Uebersicht zu verlieren. Die Schulter-Perspektive erlaubt praeziseres Zielen (relevant fuer Bogen/Armbrust).

**Dialog** simuliert einen cinematischen Schulterblick. Die niedrige Arm Length erzeugt Portraitqualitaet. Hier greift der DOF-Effekt (f/2.8-Simulation, siehe Kap. 1.3).

**Inspect** zieht die Kamera zurueck und zentriert, damit der Spieler seinen Charakter und dessen Ausruestung in voller Groesse sieht — wichtig fuer das Nervensystem-Leveling-UI (GDD-02, Kap. 3).

### 2.3 Kollision und Verhalten

- **Sphere Trace** fuer Wandkollision: Die Kamera faehrt naeher an den Charakter heran, statt durch Geometrie zu clippen. Radius: 12 cm (gross genug, um Ecken zu glaetten, klein genug, um nicht auf Moebel zu reagieren).
- **Enge Raeume:** Automatischer Nah-Zoom mit Minimum-Distance von 80 cm. Unter 80 cm wuerde der Charakter die gesamte Sicht blockieren.
- **Vegetation:** Dithering-Fadeout bei Kamera-Naehe (Radius 60 cm um Kameraposition). Keine harte Kollision mit Blaettern und Gras — das wuerde in einem bewaldeten Gebiet staendig die Kamera ruckeln lassen.
- **Camera Lag:** Speed 8-10. Das erzeugt eine geschmeidige Nachfuehrung, die sich organisch anfuehlt, ohne den Charakter "hinter sich herzuziehen".
- **Pitch Range:** -60 bis +70 Grad. Der erweiterte Aufwaerts-Bereich (+70) ist essentiell fuer Dishonored-Vertikalitaet (GDD-01, Saeule P6): Der Spieler muss nach oben schauen koennen, um Kletterwege und Dachlandschaften zu erkennen.

### 2.4 Offene Punkte

- [ ] Kamera-Blueprint V0.1 prototypen — Prio fuer diese Woche. Vier Modi muessen spielbar sein, bevor Combat-Prototyping beginnt
- [ ] FP-Vorbereitung: Smoke-Test mit Arm Length 0 — funktioniert das mit dem aktuellen Charakter-Mesh ohne Clipping-Artefakte?
- [ ] Controller-Konfiguration: Rechter Stick fuer Kamera, linker Trigger fuer Zoom? Abstimmung mit Darius (Combat-Controls)

---

## 3. Combat-Architektur

### 3.1 Grundsystem

Das Combat-System basiert auf dem **Gameplay Ability System (GAS)**, das in UE5 nativ integriert ist. GAS ist die einzige Engine-Loesung, die die Komplexitaet von Darius' dreischichtigem Combat-Design (GDD-02, Kap. 1.2) abbilden kann, ohne auf Drittanbieter-Middleware angewiesen zu sein. Das reduziert das Abhaengigkeitsrisiko, erfordert aber einen Entwickler mit GAS-Erfahrung.

**Fundamentale Abhaengigkeit:** Das Combat-System setzt einen **dedizierten Gameplay-Programmer** voraus. Kein Teammitglied hat die C++-Tiefe, um GAS auf Produktionsniveau zu implementieren. Das Freelancer-Budget (Kap. 8.2) ist primaer fuer diese Position reserviert. Ohne diese Person gibt es kein Combat, kein Vertical Slice, kein Spiel.

### 3.2 GAS-Architektur (V1 Scope)

| Komponente | GAS-Element | Implementierung | Prioritaet |
|------------|-------------|-----------------|------------|
| Basis-Attribute | Attribute Set | HP, Stamina, Infektionswert als GAS Attributes. Float-basiert, repliziert (Singleplayer: lokal) | Kern |
| Leichter/Schwerer Angriff | Gameplay Abilities | Ability-Klassen mit Montage-Referenz, Damage-Calculation, Stamina-Kosten | Kern |
| Block / Ausweichen | Gameplay Abilities | State-Machine: Idle > Block > Active. Parry = Frame-Window innerhalb von Block | Kern |
| Hit Detection | Animation Notifies | Notify-basiert: Sweep/Overlap bei definierten Frames. Keine Hitbox-Volumes, sondern Trace-basiert (praeziser, weniger Collider-Overhead) | Kern |
| Stamina-Management | GAS Gameplay Effects | Kosten pro Aktion als Gameplay Effect. Regeneration als Duration-Effect mit Period | Kern |
| Hit Reactions / Stagger | Gameplay Cues + Montages | Gameplay Cues triggern VFX/Sound, Montages uebernehmen die Animations-Reaktion | Kern |
| Schattenfieber-Faehigkeiten | Custom Abilities + MPC | Abilities mit doppeltem Kosten-System (Stamina + Infektionswert-Erhoehung). Post-Processing-Feedback ueber Material Parameter Collection | V1 nach Emre/Darius-Sync |
| Feind-KI | StateTree (UE5-nativ) | Verhaltenslogik in StateTree, Combat-Aktionen als GAS Abilities. Feinde nutzen dasselbe System wie der Spieler | Kern |
| Gameplay Tags | Tag-Hierarchie | `Combat.State.Blocking`, `Combat.State.Staggered`, `Infection.Level.1` etc. Tags steuern, welche Abilities wann aktivierbar sind | Kern |

**Waffentypen V1-Scope:** Schwert (Einhand) + Bogen. Das ist das Minimum, um die Kern-Combat-Loop zu validieren. Armbrust, Schild, Zweihand-Waffen und Dolche sind V2 (GDD-02, Kap. 1.3 definiert sechs Waffenklassen — wir liefern zwei fuer den Vertical Slice).

### 3.3 Animation

**Motion Matching** (UE 5.4+) ist das Bewegungssystem. Der Vorteil gegenueber klassischen Blend Trees: natuerlichere Uebergaenge zwischen Gehen, Laufen, Stoppen, Richtungswechsel. Das reduziert das "Eislaufen"-Problem, das viele Third-Person-Spiele haben, und unterstuetzt das gewichtige Kampfgefuehl (GDD-01, Saeule P2).

**Animations-Datenbank:** Motion Matching braucht grosse Datensaetze. Die Strategie ist dreistufig:
1. **Prototyping:** Mixamo als Basis. Kostenlos, sofort verfuegbar, ausreichend fuer Gameplay-Iteration
2. **Produktion:** Marketplace-Animation-Packs als Startpunkt. Packs mit gewichtigem Melee-Combat (z.B. "Medieval Combat Animset") als Grundlage, angepasst
3. **Hero-Animations:** Custom oder MoCap fuer Kern-Movesets. Budget-Abhaengig (Kap. 8.2)

**Control Rig:** IK fuer Fussplatzierung (Terrain-Anpassung), Waffenausrichtung (Aim Offset), und Rueckenpanzerung (Socket-basiert). Control Rig ist UE5-nativ und ersetzt die frueheren AnimDynamics-Workarounds.

**Gewichtiges Kampfgefuehl — technische Hebel:**
- **Hitlag:** 2-4 Frames Pause bei Treffer (sowohl Spieler als auch Feind). Erzeugt das Gefuehl von Masse und Impact
- **Camera Shake:** Subtil, richtungsabhaengig. Kein Bildschirm-Schuetteln, sondern ein kurzer Impuls in Angriffsrichtung
- **Zeitlupe:** Optional fuer kritische Treffer (0.2 s bei 0.7x Speed). Muss sich verdient anfuehlen, nicht inflationaer
- **Impact VFX:** Funken, Staub, Blutspuren. Niagara-Partikel, physikbasiert

### 3.4 Risiken und Mitigationen

| Risiko | Schwere | Mitigation | Fallback |
|--------|---------|------------|----------|
| Gameplay-Programmer verzoegert sich | KRITISCH | Suche beginnt sofort (Woche 1). Finn fuehrt Gespraeche | Marketplace-Combat-Framework als Bridge (Risiko: GAS-Inkompatibilitaet) |
| GAS-Lernkurve zu steil | HOCH | Lyra-Projekt (Epic) als Referenz-Implementierung. Iterativer Aufbau, keine Gross-Architektur am Anfang | GAS-Kurs/Beratung einkaufen (500-1000 EUR Budget) |
| Kampf fuehlt sich nicht "gewichtig" an | HOCH | Fruehe Prototyp-Iteration. Game-Feel-Workshop in Woche 6-7: Hitlag, Kamera, Sound als isolierte Variablen testen | Referenz-Videos von Gothic/Dark Souls als Benchmark-Reihe |
| Motion Matching Daten unzureichend | MITTEL | Frueh mit Mixamo-Daten testen. Marketplace-Packs evaluieren (Woche 4) | Fallback auf klassische Blend Trees (funktioniert, sieht schlechter aus) |

---

## 4. Asset-Pipeline

### 4.1 Modulares Kit-System

Die Asset-Strategie fuer RELICS ist modular. Das bedeutet: Wir bauen keine fertigen Gebaeude, sondern einen Baukasten aus 20-30 Architektur-Modulen (Wand-Segmente, Ecken, Tuerrahmen, Fenster, Dach-Elemente, Fundamente), aus denen sich hunderte Gebaeude-Varianten zusammensetzen lassen.

Dieses Prinzip ist nicht optional, sondern ueberlebensnotwendig: Vera ist die einzige dedizierte Kuenstlerin im Team. Ohne modulares System muessen wir jedes Gebaeude einzeln modellieren. Mit modularem System modelliert Vera 30 Module, und Level Design baut daraus eine Stadt.

**Fraktions-Differenzierung** erfolgt ueber Material-Instanzen, nicht ueber separate Meshes. Dieselbe Wand bekommt je nach Fraktion ein anderes Material:
- **Krone:** Eleganter Zerfall. Gold-Patina, Risse in edlem Stein, verwilderte Ornamente. Farben: Warm (Amber, Dunkelgold, Efeugruen)
- **Gilden:** Industrielle Eleganz. Bronze, Glas, Praezision. Saubere Kanten, polierte Oberflaechen. Farben: Kuehle Toene (Blaugruen, Bronze, Schwarz)
- **Orden:** Monolithisch. Dunkelstein, glatte Oberflaechen, schmucklos. Architektur als Machtdemonstration. Farben: Entsaettigt (Grau, Weiss, Eisblau)

### 4.2 Standards

| Standard | Wert | Begruendung |
|----------|------|-------------|
| Texel Density (Hero) | 10.24 px/cm | Fuer Assets in Nahsicht (Waffen, Ruestungen, Interaktionsobjekte). Entspricht ~1024px auf 1m |
| Texel Density (Background) | 5.12 px/cm | Fuer Hintergrund-Assets (Architektur-Module, Terrain-Deko). Spart VRAM ohne sichtbaren Qualitaetsverlust |
| Naming (Static Mesh) | `SM_[Kat]_[Name]_[Var]` | z.B. `SM_Wall_Stone_01`, `SM_Door_Wood_Gilden_02` |
| Naming (Material Instance) | `MI_[Fraktion]_[Material]` | z.B. `MI_Krone_Stein_Verwittert`, `MI_Gilden_Bronze_Poliert` |
| Naming (Skeletal Mesh) | `SK_[Typ]_[Name]` | z.B. `SK_Char_PlayerMale`, `SK_Creature_Infizierter_01` |
| LOD (Skeletal) | 3 Stufen | LOD0: Voll, LOD1: 50%, LOD2: 25%. Automatisch via Simplygon oder UE5-Proxy |
| LOD (Static/Nanite) | Automatisch | Nanite uebernimmt. Kein manueller LOD-Workflow noetig |
| Textur-Format | BC7 (Farbe), BC5 (Normal) | Standard-Kompression fuer UE5. BC7 hat bessere Qualitaet als DXT5 bei gleicher Groesse |
| Max. Texturgroesse | 4096x4096 (Hero), 2048x2048 (Standard) | 4K nur fuer Hero-Assets. Alles andere 2K |

### 4.3 Prozedurale Systeme

#### Houdini-Terrain

Houdini ist das Kern-Tool fuer Terrain-Generierung. Der Workflow: Heightfield-Generation in Houdini, Erosion (hydraulisch + thermisch), Pfade und Strassen als Masken, Export ueber das Houdini Engine Plugin direkt in UE5.

**Scope:** 4-6 km2, organisiert ueber UE5 World Partition mit 256m x 256m Zellen. World Partition erlaubt, dass nur die sichtbaren Terrain-Zellen geladen werden — essentiell fuer die Semi-Open-World ohne Ladebildschirme (GDD-01, Saeule P4).

**HDAs fuer Vera:** Ich baue Houdini Digital Assets mit vereinfachter Oberflaeche. Vera soll nicht Houdini lernen muessen — sie soll Parameter schieben koennen: Biom-Typ (Wald, Sumpf, Fels), Vegetationsdichte, Hoehenvariation, Pfad-Breite. Das HDA generiert, sie iteriert, wir exportieren. Das ist der Produktivitaetshebel.

Ehrliche Einschaetzung: Die HDAs muessen WIRKLICH einfach sein. Vera ist eine schnelle Lernerin, aber Houdini hat die steilste Lernkurve in unserer gesamten Tool-Chain. Wenn die HDAs zu komplex werden, wird Vera sie nicht nutzen, und ich werde zum Flaschenhals. Erste HDA-Version muss in Woche 3 getestet werden.

#### PCG-Vegetation

UE5s Procedural Content Generation (PCG) Framework fuer regelbasierte Vegetations-Platzierung. Die Regeln: Neigung (Gras nicht an Steilhaengen), Hoehe (Baumgrenze), Bodentyp (Sumpfpflanzen nur in Feuchtgebieten), Distanz zu Pfaden (keine Baeume AUF dem Weg), Distanz zu Gebaeuden (Lichtung um Siedlungen).

Vera liefert 8-12 Vegetations-Assets pro Biom. PCG verteilt sie nach Regeln. Das spart hunderte Stunden manueller Platzierung.

#### Substance Designer

Prozedurale Materialien fuer sich wiederholende Oberflaechen: Stein, Holz, Metall, Erde. Substance-Graphen exportieren direkt in UE5-kompatible Texturen (Base Color, Normal, ORM). Die ACES-Konfiguration in Substance muss identisch zur UE5-Konfiguration sein — sonst driften die Farben.

### 4.4 Asset-Quellen

| Quelle | Einsatzbereich | Budget-Implikation | Risiko |
|--------|----------------|--------------------|--------|
| Vera (Eigenproduktion) | Characters, Hero-Props, Concept Art, UI-Elemente | Intern (Gehalt) | Flaschenhals — eine Person fuer alles Visuelle |
| Tobi (prozedural) | Terrain, Felsen, Materialien, Vegetation-Verteilung | Intern (Gehalt) + Houdini-Lizenz | Houdini-Know-how ist nicht uebertragbar |
| Megascans (UE5 inklusive) | Umgebungs-Assets: Felsen, Boden, Vegetation-Basis | Kostenlos (Quixel Bridge) | Qualitaet gut, aber generisch — braucht Anpassung fuer RELICS-Look |
| Marketplace (selektiv) | Basis-Assets zum Anpassen, Animation Packs, VFX | Budget: 2.000-3.000 EUR (Kap. 8.2) | Qualitaetsschwankung. Jedes Asset muss vor Kauf geprueft werden |
| Photogrammetrie (optional) | Texturen, Fels/Mauerwerk-Referenz | Gering (eigene Ausruestung) | Detmold/Lemgo-Umgebung als Quelle. Mittelalterliche Architektur vor der Haustuer |

---

## 5. Schattenfieber-Tech

### 5.1 Systemuebersicht

Das Schattenfieber ist das technisch anspruchsvollste System in RELICS. Es ist kein einzelner Effekt, sondern ein Querschnittssystem, das Rendering, VFX, Gameplay, Audio und Narrative verbindet. Jede technische Entscheidung in diesem Kapitel muss gegen Darius' fuenf mechanische Stufen (GDD-02, Kap. 2.3) und Namis drei narrative Zustaende (Rauschen, Risse, Schwelle) validiert werden.

**Kernprinzip:** Der Infektionswert (0-100, Float) ist der einzige Eingabeparameter. Alle visuellen Effekte leiten sich von diesem einen Wert ab. Es gibt keine harten Stufenschalter — das System interpoliert kontinuierlich. Ein Spieler mit Infektionswert 24 sieht leicht andere Effekte als einer mit Wert 25, aber der Unterschied ist graduell, nicht sprunghaft. Das ist eine explizite Design-Entscheidung (GDD-02, Kap. 2.3: "Stufenuebergaenge sind KEINE harten Schalter").

### 5.2 Technische Architektur

Das System besteht aus drei Schichten:

**Schicht 1: Material Parameter Collection (MPC)**
Eine zentrale MPC (`MPC_Schattenfieber`) haelt den Infektionswert als skalaren Parameter. Alle Post-Processing-Materialien, Niagara-Systeme und Welt-Shader lesen diesen Wert. Aenderungen am Infektionswert propagieren automatisch in alle Systeme — kein manuelles Update noetig.

**Schicht 2: Post-Processing Volume**
Ein eigener Post-Processing Volume, der dem Spielercharakter folgt (nicht level-global). Die Material-Instanzen in diesem Volume lesen die MPC und skalieren ihre Effekte entsprechend.

**Schicht 3: Niagara VFX**
GPU-Partikel-Systeme, die ebenfalls die MPC lesen. Schattensporen, Flimmern, Verzerrungspartikel — alles skaliert mit dem Infektionswert.

### 5.3 Fuenf-Stufen-Rendering

| Stufe | Infektionswert | Post-Processing Effekte | Niagara VFX | Welt-Effekte | Technische Komplexitaet |
|-------|---------------|------------------------|-------------|--------------|------------------------|
| 0 (Rein) | 0 | Keine | Keine | Keine | Baseline |
| 1 (Gezeichnet) | 1-25 | Leichte Farbverschiebung in den Schatten (kuehler, blaeulicher). Subtiles Vignette-Pulsieren (Atmung, 0.05 Hz) | Vereinzelte Schattensporen im Sichtfeld (2-5 Partikel, kaum sichtbar) | Schattensinne: Versteckte Objekte erhalten Custom Stencil Outline (nur fuer infizierte Spieler sichtbar) | Niedrig |
| 2 (Infiziert) | 26-50 | + Chromatische Aberration (subtil, 0.1-0.3). Farb-Saettigung beginnt sich zu verschieben (Gruen > Cyan). Leichtes Rauschen am Bildrand | + Partikel-Overlay (Schattensporen dichter, 10-20 Partikel). Emotionsauren an NPCs als farbige Niagara-Systeme | + Gespraechsoptionen-Shader: UI-Text fuer Schattenfieber-Dialoge mit leichtem Glitch-Effekt | Mittel |
| 3 (Verwandelt) | 51-75 | + Geometrische Verzerrung am Bildrand (Barrel Distortion, animiert). Farbpalette kippt merklich (warme Toene > kalte Toene). Depth-of-Field-Schimmer auf mittlerer Distanz | + Schattenranken-Partikel am Bildrand. Tiefensicht als Niagara-Overlay (geologische Schichten, Adern im Terrain) | + Alternative Geometrie: Custom Stencil Buffer fuer Objekte, die nur ab Stufe 3 sichtbar sind. Fragwuerdige NPCs mit Flimmer-Shader | Hoch |
| 4 (Entfesselt) | 76-100 | + Halluzinatorische Elemente: Vertex-Displacement auf Welt-Geometrie (atmende Waende). Doppelbilder (Ghost-Rendering). Farbkanal-Separation. Intermittierender Realitaets-Glitch (kurzer Blitz in eine "andere" Renderebene) | + Vollstaendiges Sporen-Feld. Schatten bewegen sich autonom. Lichtquellen flackern asynchron | + Parallel-Geometrie: Ganze Raum-Segmente in alternativer Version (Stencil-Switch). NPCs, die moeglicherweise nicht existieren, haben identisches Rendering — kein visueller Unterschied zu "echten" NPCs | Sehr hoch |

### 5.4 Graduelle Interpolation — Technik

Der Trick ist, dass alle Effekte nicht bei Stufengrenzen "anspringen", sondern ueber Kurven interpoliert werden:

- **Farbverschiebung:** Lerp zwischen normaler und verschobener Farbmatrix, gesteuert durch `InfektionswertFloat / 100`
- **Chromatische Aberration:** Intensitaet = `max(0, (Infektionswert - 20) / 80)`. Beginnt bei ~20, erreicht Maximum bei 100
- **Geometrische Verzerrung:** Intensitaet = `max(0, (Infektionswert - 45) / 55)`. Beginnt bei ~45, graduell
- **Halluzinationen:** Aktivierung ab Wert 70, Intensitaet skaliert mit `(Infektionswert - 70) / 30`

Alle Kurven sind in UE5 als **Float Curve Assets** hinterlegt und koennen im Editor angepasst werden, ohne Code zu aendern. Das ist wichtig, weil Emre und Nami diese Kurven mitgestalten muessen — sie definieren, WANN sich etwas "richtig" anfuehlt, wir liefern die Parameterraeder.

### 5.5 Welt-Effekte (Befallene Zonen)

Befallene Zonen in der Spielwelt haben eigene Post-Processing Volumes mit vorab gesetzten Schattenfieber-Effekten — unabhaengig vom Infektionswert des Spielers. Diese Zonen sind fuer ALLE Spieler sichtbar (als Warnung, Bedingung 1 aus GDD-02: Transparenz vor Infektion).

- **Biotech-Vegetation:** Organische Auswuechse, pulsierende Ranken. Vertex-Animation (kein Nanite), emissive Materialien mit Pulse-Funktion
- **Boden-Shader:** Terrain-Material mit zusaetzlichem Schattenfieber-Layer (organische Textur, leicht animiert)
- **Niagara-Atmosphaere:** Schattensporen als GPU-Partikel, Nebel mit volumetrischem Scattering. Emres poetische Nebelbeschreibungen muessen hier technisch uebersetzt werden — "Nebel, der sich anfuehlt wie Trauer" ist eine Farb- und Bewegungsfrage: langsame Partikel, tiefe Saettigung, Gewicht nach unten

### 5.6 Performance-Implikation

Das Schattenfieber-System hat ein eigenes Performance-Budget von **2 ms GPU-Zeit** (bei empfohlener Hardware). Aufgeteilt:
- Post-Processing: 0.8 ms (selbst bei Stufe 4 vertretbar, da die meisten Effekte Screen-Space sind)
- Niagara-Partikel: 0.7 ms (GPU-Partikel, LOD-aware — Partikel-Count reduziert sich mit Distanz)
- Custom Stencil / Welt-Effekte: 0.5 ms (nur in befallenen Zonen aktiv)

Bei Stufe 0 ist das Budget nahe 0 ms. Das System kostet nur, wenn es aktiv ist.

### 5.7 Abhaengigkeiten und offene Punkte

| Abhaengigkeit | Von wem | Status | Dringlichkeit |
|--------------|---------|--------|---------------|
| Visuelle Referenz: "Wie sieht Stufe 3 aus?" | Emre (Lore), Vera (Concept) | Offen | HOCH — ohne Referenz baue ich ins Blaue |
| Infektionswert-Gameplay-Logik | Darius (GDD-02) | V0.5 vorhanden | Mittel — Stufen definiert, Details offen |
| Narrative Zustaende → visuelle Parameter | Nami | Rauschen/Risse/Schwelle definiert | Mittel — brauche konkrete Beispiele pro Zustand |
| Audio-Verzerrung (Stufe 2+) | Offen (kein Audio-Lead) | Nicht begonnen | Niedrig fuer V1, hoch fuer VS |
| Abstimmungsmeeting Schattenfieber-Tech | Tobi + Emre + Darius + Vera | Noch nicht terminiert | HOCH — diese Woche |

---

## 6. Performance-Ziele

### 6.1 Hardware-Tiers

RELICS definiert drei Hardware-Tiers. Die Ziel-Framerates sind ambitioniert, aber durch Upscaling-Technologie erreichbar.

| Tier | GPU-Referenz | CPU-Referenz | RAM | Ziel-FPS | Aufloesung | Rendering |
|------|-------------|-------------|-----|----------|-----------|-----------|
| Minimum | GTX 1070 / RX 5700 | i5-8400 / R5 3600 | 16 GB | 30 fps | 1080p | Software Lumen, Low Settings, FSR Quality |
| Empfohlen | RTX 3070 / RX 6800 | i7-10700 / R7 5800X | 16 GB | 60 fps | 1440p | HW RT Lumen, High Settings, DLSS/FSR Quality |
| High-End | RTX 4080+ / RX 7900 XT | i7-12700+ / R7 7800X3D | 32 GB | 60 fps | 4K | Max Settings, RT Reflections, DLSS/FSR Performance |

**Ehrliche Einschaetzung zum Minimum-Tier:** GTX 1070 mit Software Lumen, Nanite, Motion Matching UND Schattenfieber-Effekten bei 30 fps ist ambitioniert. UE5-Titel wie Fortnite und The Matrix Awakens zeigen, dass es moeglich ist, aber wir muessen frueh benchmarken (Woche 6-8). Falls der Minimum-Tier nicht haltbar ist, verschiebt sich die Untergrenze auf GTX 1660 / RX 5700 XT. Das muss eine datenbasierte Entscheidung sein, keine Hoffnung.

### 6.2 Upscaling (Pflicht)

Upscaling ist nicht optional, sondern ein Kern-Feature:
- **DLSS 3** (Nvidia): Super Resolution + Frame Generation
- **FSR 3** (AMD): Super Resolution + Fluid Motion Frames
- **XeSS** (Intel): Optional, niedriger Prio

DLSS und FSR sind der Grund, warum 60 fps bei 4K realistisch ist: Das Spiel rendert intern bei niedrigerer Aufloesung und skaliert hoch. Ohne Upscaling waere 4K/60 auf keiner Consumer-Hardware erreichbar.

Frame Generation (DLSS 3 / FSR 3) als Option fuer unterstuetzte Hardware. Nicht als Standard aktiviert, da Frame Generation Eingabe-Latenz erhoehen kann — bei einem Action-Combat-Spiel ist das eine Spieler-Entscheidung.

### 6.3 Performance-Budgets

| Kategorie | Budget | Begruendung |
|-----------|--------|-------------|
| Draw Calls | < 5.000 pro Frame | Nanite reduziert Draw Calls drastisch. 5.000 ist konservativ und laesst Raum fuer UI und Partikel |
| Dynamische Lichter | 8-12 gleichzeitig | VSM-Limit. Darueber hinaus Performance-Einbruch |
| Vegetation Draw Distance | Gras: 50-80 m, Baeume: 500 m | Gras ist der teuerste Vegetationstyp. 80 m ist ein guter Kompromiss zwischen Dichte und Performance. Baeume als Impostors ab 300 m |
| NPC-Count (sichtbar) | 20-30 gleichzeitig | StateTree + Mass Entity System. 30 NPCs mit eigenem Verhalten sind eine realistische Obergrenze |
| Partikel (Schattenfieber) | GPU-Budget: 2 ms | Kap. 5.6. LOD-aware: Partikel-Count sinkt mit Distanz |
| Speicher (VRAM) | 6 GB (Minimum), 8 GB (Empfohlen) | Nanite-Geometrie + Streaming-Texturen + Lumen-Datenstrukturen |
| Level-Streaming | World Partition, 256 m Zellen | Laderadius: 3-4 Zellen um Spieler. Asynchrones Streaming ohne Hitches unter 16 ms |

### 6.4 Offene Punkte

- [ ] Prototyp-Benchmarks (Woche 6-8): Terrain-Scene mit Vegetation, 3 NPCs, Lumen, Schattenfieber-Stufe 2. Auf allen drei Tiers testen
- [ ] Scalability Settings definieren (Low/Medium/High/Ultra): Welche Effekte skalieren wir zuerst? Empfehlung: Vegetation Density > Schattenfieber-Partikel > Shadow Quality > Lumen Bounces
- [ ] Konsolen-Performance-Analyse (erst relevant, wenn Stretch Goal aktiviert wird)
- [ ] Shader-Compilation-Hitches: PSO-Caching-Strategie definieren (Blueprint-Szene fuer PSO-Sammlung)

---

## 7. Produktions-Pipeline

### 7.1 Versionskontrolle

Zwei Systeme, klar getrennt:

**Perforce (Helix Core)** fuer das UE5-Projekt. Das umfasst alle Binaer-Assets (Meshes, Texturen, Maps, Blueprints, Sound). Perforce ist der Industriestandard fuer Unreal-Projekte, weil es Binaer-Dateien nativ sperren kann (File Locking) — zwei Personen koennen nicht gleichzeitig dieselbe Map bearbeiten. Das verhindert Merge-Konflikte, die bei Git mit Binaer-Dateien unloesbar sind.

**Git** fuer Dokumentation (GDD, WBB, dieses Dokument), Scripts, Pipeline-Tools. Textbasiert, mergebar, versionierbar.

Kein Git LFS fuer Engine-Assets. Das ist eine bewusste Entscheidung: Git LFS ist ein Kompromiss, der in der Praxis bei UE5-Projekten mehr Probleme schafft als er loest (Bandwidth-Kosten, Lock-Verhalten, Repository-Groesse).

### 7.2 Ordnerstruktur (UE5-Projekt)

```
Content/
  RELICS/
    Characters/
      Player/
      NPCs/
      Creatures/
    Environment/
      Architecture/
        Modules/          -- Modulare Baukastenteile
        Assembled/        -- Zusammengesetzte Gebaeude
      Vegetation/
        Trees/
        Ground/
        Schattenfieber/   -- Befallene Vegetation (eigener Ordner)
      Terrain/
    Props/
      Weapons/
      Furniture/
      Interactive/
    Materials/
      Master/             -- Master-Materials (max. 10-15)
      Instances/
        Krone/
        Gilden/
        Orden/
        Schattenfieber/
    VFX/
      Niagara/
        Combat/
        Schattenfieber/
        Environment/
    Audio/
      SFX/
      Music/
      Ambience/
    UI/
      HUD/
      Menus/
      Nervensystem/
    Blueprints/
      Core/               -- Game Mode, Game State, Player Controller
      Combat/             -- GAS Abilities, Attribute Sets
      Camera/             -- Spring Arm, Kontext-Modi
      AI/                 -- StateTree Assets, Behavior
      Schattenfieber/     -- MPC, PP-Volumes, Infektionslogik
    Maps/
      Persistent/         -- World-Partition-Hauptlevel
      Sublevels/          -- World-Partition-Zellen
      Test/               -- Prototyping-Levels (Whiteboxing, Benchmarks)
    Data/
      DataTables/         -- Waffen-Stats, NPC-Daten, Alchemie-Rezepte
      Curves/             -- Float Curves (Schattenfieber-Parameter, Kamera-Blends)
      GameplayTags/       -- Tag-Definitionen
```

**Naming-Konvention fuer Ordner:** Keine Umlaute, keine Leerzeichen, CamelCase. Jeder Ordner hat maximal eine Verschachtelungstiefe von 3. Tiefere Hierarchien deuten auf ein Strukturproblem hin.

### 7.3 Tool-Chain

| Tool | Version | Einsatz | Verantwortlich | Lizenzkosten (jaehrlich) |
|------|---------|---------|----------------|-------------------------|
| Unreal Engine 5.4+ | Latest stable | Runtime, Level Design, Blueprints, Sequencer | Tobi, Darius, Gameplay-Programmer | Kostenlos (5% Royalty ab 1M USD) |
| Houdini Indie | 20.5+ | Terrain, prozedurale Assets, FX-Prototyping | Tobi | ~270 EUR/Jahr |
| Houdini Engine (UE5 Plugin) | Matching | Houdini-UE5-Bridge | Tobi | In Indie-Lizenz enthalten |
| Substance Painter | Latest | Texturierung, Materialien | Vera, Tobi | ~220 EUR/Jahr (Indie) |
| Substance Designer | Latest | Prozedurale Materialien | Tobi | In Substance-Abo enthalten |
| Blender | 4.x | 3D-Modelling, Rigging, UV-Layout | Vera | Kostenlos |
| Photoshop / Krita | Latest | Concept Art, Texturen, UI-Mockups | Vera | ~290 EUR/Jahr (PS) oder kostenlos (Krita) |
| Perforce Helix Core | Latest | Asset-Versionskontrolle | Tobi (Admin) | Kostenlos bis 5 User |
| Jira / Notion | TBD | Taskmanagement, Sprint-Planung | Finn | ~0-100 EUR/Jahr |
| DaVinci Resolve | 19+ | Color Grading Referenz, Trailer-Schnitt | Tobi | Kostenlos (Free Version) |

**Gesamte jaehrliche Tool-Kosten:** ~780-1.080 EUR. Das ist bemerkenswert niedrig und ein Vorteil der aktuellen Tool-Landschaft.

### 7.4 Abstimmungsbedarf mit Finn

- [ ] Taskmanagement-Tool festlegen (Jira vs. Notion vs. Linear). Empfehlung: Notion fuer die aktuelle Teamgroesse — Jira ist Overkill
- [ ] Sprint-Rhythmus: Empfehlung 2 Wochen. Eine Woche ist zu kurz fuer sinnvolle Iterationen an technischen Systemen
- [ ] Review-Prozess fuer Assets: Vorschlag — Vera modelliert > Tobi prueft Technical Standards > Darius prueft Gameplay-Relevanz > Merge
- [ ] Build-Pipeline: Naechtliche automatisierte Builds (UE5 BuildGraph). Braucht einen Build-Server oder Cloud-Instanz. Nicht sofort, aber ab Vertical Slice

---

## 8. Meilensteine & Budget

### 8.1 Phasen

| Phase | Zeitraum | Kern-Deliverables | Abhaengigkeit | Exit-Kriterium |
|-------|----------|-------------------|---------------|----------------|
| **Pre-Production** | Wochen 1-4 | GDD V1 + WBB V1 fertig. UE5-Projekt steht (Ordnerstruktur, Perforce, Master Materials). Kamera-Prototyp spielbar. Terrain-Prototyp (1 km2). Art-Style-Targets validiert (3 Concept Sheets von Vera) | Team komplett (minus Gameplay-Programmer) | CD gibt Design-Lock. Alle koennen im UE5-Projekt arbeiten |
| **Vertical Slice Prototype** | Wochen 5-12 | Spielbare Szene: 1 Region (~1 km2), Hauptquest-Ausschnitt (30 min Gameplay), Combat-Grundsystem (Schwert + Bogen, 3 Feindtypen), 1 Stadt (Blockout), Schattenfieber-Tech Stufe 0-2 | Gameplay-Programmer an Bord (spaetestens Woche 5) | Szene ist von Anfang bis Ende spielbar. Combat fuehlt sich "gewichtig" an |
| **Vertical Slice Polish** | Wochen 13-18 | VS spielbar und praesentabel: Beleuchtung (Lumen-Pass), Asset-Polish (Nanite-Architektur, Material-Instanzen), Quest komplett mit Dialogen, Performance-Ziele auf empfohlener Hardware erreicht, Schattenfieber Stufe 0-3 | Asset-Pipeline laeuft. Vera liefert Final-Assets | VS ist vorzeigbar (CD, Publisher, Presse) |
| **Alpha** | Wochen 19-30 | Gesamte Kernregion (4-6 km2) blockiert. Alle Quests implementiert (Greybox): Hauptquest + 3 Fraktionsquests + 2 Nebenquests. Kampfsystem V2 (alle 6 Waffenklassen). Nervensystem-Leveling spielbar. Alchemie-System V1. NPC-Routinen. Schattenfieber alle 5 Stufen | Scope-Lock (spaetestens Ende Woche 18) | Feature-Complete (kein neues Feature nach Alpha) |
| **Beta** | Wochen 31-40 | Content-Complete. Polish-Pass auf alle Assets. QA-Runden (Leo koordiniert). Performance-Optimierung auf allen drei Tiers. Bug-Fixing. Balancing (Schattenfieber-Stufenuebergaenge) | QA-Kapazitaet | Alle bekannten Blocker gefixt. Performance-Ziele auf allen Tiers erreicht |
| **Release** | Woche 40+ | Steam Early Access oder Full Release | CD-Entscheidung | Spielbar, stabil, repraesentativ |

### 8.2 Budget-Aufschluesselung (45.000 EUR Freelancer-Budget)

Das Freelancer-Budget ist begrenzt und muss strategisch eingesetzt werden. Die folgende Aufschluesselung priorisiert nach Abhaengigkeit: Was blockiert am meisten, wenn es fehlt?

| Position | Geschaetztes Budget | Zeitraum | Begruendung |
|----------|-------------------|----------|-------------|
| **Gameplay-Programmer (GAS/Combat)** | 20.000-25.000 EUR | Wochen 5-18 (14 Wochen) | Kritischste Abhaengigkeit. Ohne diese Person kein Combat, kein VS. ~1.400-1.800 EUR/Woche (Freelancer-Rate Junior/Mid fuer UE5 C++/GAS) |
| **Animations-Assets** | 5.000-8.000 EUR | Wochen 8-18 | Marketplace-Packs + Custom-Anpassung. Motion-Matching-Datenbank braucht Umfang. Ggf. auch MoCap-Session (ca. 2.000 EUR fuer einen Tag) |
| **Audio/Sound Design** | 5.000-7.000 EUR | Wochen 13-30 | Kein Audio-Lead im Team. MetaSounds-Setup, Combat-SFX, Ambient, Schattenfieber-Audio. Freelancer oder Asset-Packs + Implementierung |
| **QA-Support** | 3.000-5.000 EUR | Wochen 25-40 | Externe Tester fuer Schattenfieber-Stufenuebergaenge (Leos 40%-Einschaetzung ist realistisch). Crowdsource oder kleine QA-Firma |
| **Marketplace-Assets** | 2.000-3.000 EUR | Laufend | Architektur-Bases, Vegetation-Packs, VFX-Bibliotheken zum Anpassen |
| **Puffer** | 2.000-5.000 EUR | Reserve | Unvorhergesehenes: Tool-Lizenzen, zusaetzliche Freelancer-Tage, Hardware-Ersatz |
| **Gesamt** | ~37.000-53.000 EUR | | Mittelwert: ~45.000 EUR |

**Ehrliche Einschaetzung:** 45.000 EUR ist ein sehr knappes Budget. Der Gameplay-Programmer allein verbraucht die Haelfte. Wenn diese Person laenger als 14 Wochen braucht oder teurer ist als geschaetzt, wird der Rest des Budgets komprimiert. Risiko-Mitigation: Frueh mit der Suche beginnen (Woche 1), klaren Scope kommunizieren, Milestone-basierte Bezahlung vereinbaren.

### 8.3 Kritischer Pfad

```
Woche 1 ──────────────── Woche 5 ──────── Woche 12 ──── Woche 18 ────── Woche 30
   |                        |                  |              |               |
   PRE-PRODUCTION           VS PROTOTYPE       VS POLISH      ALPHA           BETA
   |                        |                  |              |               |
   GDD/WBB ────────────>    |                  |              |               |
   UE5 Setup ──────────>    |                  |              |               |
   Kamera-Proto ───────>    |                  |              |               |
   Terrain-Proto ──────>    |                  |              |               |
   Art Targets ────────>    |                  |              |               |
                            |                  |              |               |
   GP-PROGRAMMER SUCHE ──> AN BORD ──────────────────────────>|               |
                            |                  |              |               |
                            Combat V1 ────────>|              |               |
                            Blockout ─────────>|              |               |
                            Quest-Scripting ──>|              |               |
                                               |              |               |
                                               Lighting ─────>|               |
                                               Asset Polish ─>|               |
                                               SF Tech 0-3 ──>|               |
                                                              |               |
                                                              Full Region ───>|
                                                              All Quests ────>|
                                                              Combat V2 ────>|
                                                              SF Tech 0-4 ──>|
                                                                              |
                                                                              QA
                                                                              Polish
                                                                              Perf Opt
```

**Engpaesse:**
1. **Gameplay-Programmer** — der gesamte Vertical Slice haengt an dieser Person. Wenn sie in Woche 7 statt Woche 5 startet, verschieben sich die Wochen 12-18 entsprechend. Es gibt keinen Workaround ausser einem Marketplace-Framework, das aber eigene Integrationsrisiken traegt.
2. **Art-Pipeline-Validierung** — das modulare Kit muss bis Woche 6 beweisen, dass es skaliert. Wenn nicht, brauchen wir mehr Marketplace-Assets oder einen zweiten Kuenstler (nicht im Budget).
3. **Scope-Lock** — spaetestens Ende Pre-Production (Woche 4) muss der Feature-Umfang fixiert sein. Jedes Feature, das nach Woche 4 dazukommt, verdraengt ein anderes.

### 8.4 Risiken fuer den Zeitplan

| Risiko | Wahrscheinlichkeit | Auswirkung | Mitigation |
|--------|-------------------|-----------|-----------|
| Programmer-Verzoegerung | HOCH | Verschiebt alles ab VS Prototype | Bridge: Marketplace-Framework. Backup: Scope auf Non-Combat-VS reduzieren (Exploration + Narrative) |
| Scope Creep | HOCH | Feature-Liste waechst, nichts wird fertig | CD + Finn als Scope-Waechter. Jedes neue Feature braucht einen "Was faellt dafuer weg?"-Satz |
| Asset-Bottleneck (Vera) | MITTEL | Welt sieht leer aus, wirkt nicht | Prozedurale Systeme maximieren, Marketplace nutzen, ggf. zweiten Artist-Freelancer fuer 4 Wochen (3.000-4.000 EUR aus Puffer) |
| Technische Schulden | MITTEL | Performance-Probleme spaet im Projekt | Fruehe Benchmarks (Woche 6-8), woechentliche Perf-Checks ab VS Prototype |
| Schattenfieber-Komplexitaet | MITTEL | System funktioniert technisch, fuehlt sich aber nicht "richtig" an | Fruehe Abstimmung mit Emre/Nami/Darius. Prototyp-Szene bis Woche 8 |
| Team-Burnout | NIEDRIG | Qualitaet sinkt, Motivation faellt | Finn achtet auf Workload. Realistische Meilensteine. Kein Crunch |

---

## Anhang A: Offene Fragen (Priorisiert)

### Kritisch (diese Woche klaeren)

1. **Schattenfieber-Abstimmung** mit Emre, Darius und Vera — Was genau passiert visuell auf jeder Stufe? Ich brauche Concept-Referenzen, bevor ich Shader baue. Vorschlag: 30-Minuten-Meeting, Vera skizziert live
2. **Asset-Standards-Review** mit Vera — Naming, Texel Density, LOD-Workflow bestaetigen. Muss vor dem ersten Asset-Import in UE5 stehen
3. **Gameplay-Programmer-Profil** mit Finn — Was genau brauchen wir? GAS-Erfahrung, UE5 C++, Freelancer-Modalitaeten. Stellenbeschreibung schreiben

### Wichtig (Pre-Production)

4. **Dialog-System-Middleware** mit Nami — Brauchen wir eine? Yarn Spinner, Ink, oder UE5-eigenes System? Beeinflusst die Pipeline
5. **Audio-Pipeline** — Wer verantwortet MetaSounds-Setup? Brauchen wir einen Audio-Freelancer frueher als geplant?
6. **Terrain-Biome** mit Emre — Wie viele, welche? Jedes Biom braucht ein Houdini-HDA und eigene Vegetations-Assets

### Nachrangig (Vertical Slice)

7. **Konsolen-Stretch-Goal** — Ab wann evaluieren wir das ernsthaft? Empfehlung: Nach VS Polish (Woche 18)
8. **Lokalisierung** — Nur Deutsch? Deutsch + Englisch? Beeinflusst UI-Layout und Text-Pipeline
9. **Accessibility** — Farbblindheits-Modi, Untertitel-Groessen, Remapping. Sollte frueh in der UI-Architektur beruecksichtigt werden

---

## Anhang B: Glossar

| Begriff | Erklaerung |
|---------|-----------|
| ACES | Academy Color Encoding System. Industriestandard fuer konsistenten Farbraum ueber mehrere Tools |
| GAS | Gameplay Ability System. UE5-natives Framework fuer Faehigkeiten, Attribute und Gameplay-Effekte |
| HDA | Houdini Digital Asset. Wiederverwendbarer, parametrischer Houdini-Node mit vereinfachter Oberflaeche |
| MPC | Material Parameter Collection. UE5-System, um globale Werte an alle Materialien gleichzeitig zu senden |
| Nanite | UE5-System fuer virtualisierte Geometrie. Automatisches LOD ohne kuenstlerischen Aufwand |
| Lumen | UE5-System fuer dynamische globale Beleuchtung. Kein Baking noetig |
| PCG | Procedural Content Generation. UE5-Framework fuer regelbasierte Asset-Platzierung |
| VSM | Virtual Shadow Maps. UE5-Schattensystem mit hoher Aufloesung |
| VS | Vertical Slice. Spielbarer, repraesentativer Ausschnitt des fertigen Spiels |
| MoCap | Motion Capture. Aufzeichnung realer Bewegungen fuer Spielanimationen |

---

*Tobi Richter, Tech Corner, Tag 3 Mittwoch Vormittag — V1, Produktionsphase*
*Naechster Schritt: Schattenfieber-Abstimmung terminieren, Kamera-Blueprint beginnen, Asset-Standards mit Vera finalisieren*
