# Kapitel 06 — Art Direction

---

## 1. Visuelle Identität: Biotech-Mittelalter

Technologie wurde nie mechanisch, sondern biologisch. Statt Maschinen: gezüchtete Organismen. Statt Schaltkreisen: Nervenbahnen. Statt Stahl: Chitin. Ästhetik zwischen gotischer Kathedrale und lebendem Korallenriff.

**Leitgedanke**: Das Mittelalter, industrialisiert mit CRISPR statt mit dem Webstuhl.

---

## 2. Materialsprache

Die gesamte visuelle Welt teilt sich in zwei Material-Vokabulare. Dieser Kontrast ist **das** zentrale Designwerkzeug der Art Direction.

### 2.1 Lebende Materialien (aktive Zivilisation)

| Material | Visuelle Eigenschaften | Einsatz |
|----------|----------------------|---------|
| **Chitin** | Dunkel, glänzend, facettiert wie Käferpanzer. Harte Kanten, aber organische Kurven. Farbspektrum: Schwarz bis tiefes Burgunder. | Rüstungen, tragende Architekturelemente, Werkzeuge |
| **Keratin** | Elfenbein bis Bernstein, leicht transluzent an dünnen Stellen. Wächst in Schichten, zeigt Jahresringe bei Querschnitten. | Bögen, Brücken, dekorative Elemente, Schmuck |
| **Biolumineszenz** | Kaltes Cyan bis warmes Amber. Pulsiert langsam (2–4 Sekunden Zyklus). Reagiert auf Nähe. Nie gleichmäßig — immer in Adern, Netzen, Clustern. | Beleuchtung, UI-Elemente, Wegmarkierungen, Statusanzeigen an Gebäuden |

**Regel**: Lebende Technologie hat *keine geraden Linien über 2 Meter*. Alles krümmt sich, alles verjüngt sich, alles hat eine leichte Asymmetrie — wie Knochen, wie Hörner, wie Muscheln.

### 2.2 Tote Materialien (Ruinen, alte Welt)

| Material | Visuelle Eigenschaften | Einsatz |
|----------|----------------------|---------|
| **Rost** | Orange-Braun bis Dunkelrot. Blättert in Schichten. Hinterlässt Spuren auf umliegenden Oberflächen (Rosttränen auf Stein). | Metallische Überreste einer früheren Ära, die *mechanisch* dachte |
| **Patina** | Kupfergrün bis Türkis. Glatt, fast samtartig. Sitzt in Vertiefungen, betont Reliefs. | Statuen, Beschläge, ehemals repräsentative Oberflächen |
| **Verfall** | Risse folgen strukturellen Schwachstellen, nie zufällig. Pflanzenwuchs in Fugen. Staub in Ecken. | Alles, was nicht mehr gewartet wird |

**Regel**: Ruinen-Materialien erzählen *immer* eine zeitliche Abfolge. Ein verrostetes Tor hat zuerst die Farbe verloren (Patina), dann die Oberfläche (Rost), dann die Struktur (Verfall). Wer das rückwärts liest, rekonstruiert die Geschichte.

### 2.3 Der Kontrast

Das visuelle Kernerlebnis: **Lebendige Biotech-Strukturen wachsen durch und über tote Ruinen.**

Stell dir eine gotische Kathedrale vor, deren Deckenpfeiler aus rotem Sandstein bestehen — gebrochen, verwittert, mit Moos in den Fugen. Aber die Gewölbebögen darüber sind aus schwarzem Chitin, glänzend, makellos, und in ihren Adern pulsiert schwaches blaues Licht. Die alte Welt trug die neue. Die neue Welt weiß es nicht mehr.

Dieser Kontrast muss in **jeder Zone**, in **jedem Gebäude**, in **jedem Ausrüstungsteil** spürbar sein — in unterschiedlichen Mischungsverhältnissen.

---

## 3. Farbpalette

### 3.1 Basispalette

Die Welt ist **dunkel, aber nicht trist**. Drei Ankerfarben definieren den Grundton:

- **Anthrazit** `#2D2D2D` → `#4A4A4A` — Chitin, Schatten, Architektur. Die dominierende Farbe jedes Frames. Nie reines Schwarz — immer mit leichtem Warmstich.
- **Aubergine** `#4A0E4E` → `#7B2D8E` — Organisches Gewebe, Textilien, Abendhimmel. Die emotionale Farbe. Wird intensiver in Momenten von Magie oder Gefahr.
- **Kupfergrün** `#2E8B57` → `#507D6A` — Patina, alte Oberflächen, Vegetation. Die Farbe der Vergangenheit.

### 3.2 Akzentfarben (Biolumineszenz)

Biolumineszenz ist das **einzige Element, das gesättigt leuchten darf**. Alles andere bleibt gedämpft. Dadurch zieht jeder leuchtende Akzent den Blick.

- **Cyan** `#00E5FF` — Nervensystem, aktive Technologie, Orientierung
- **Amber** `#FFB300` — Warnung, Hitze, vulkanische Zonen
- **Violett** `#BF40BF` — Magie, Anomalien, Seltenes

**Regel für Biolumineszenz**: Maximal 5–8% der Bildfläche in jedem Frame. Wenn mehr leuchtet, leuchtet nichts.

### 3.3 Farbbalance pro Frame

Jeder Screenshot sollte ungefähr diese Verteilung haben:
- 60% Anthrazit-Töne (Struktur, Schatten)
- 25% Aubergine/Kupfergrün (Oberflächen, Tiefe)
- 10% Mitteltöne (Haut, Holz, Leder)
- 5% Biolumineszenz-Akzente (Fokuspunkte)

---

## 4. Designprinzipien

### 4.1 Die 50m-Silhouetten-Regel

**Jede Figur, jedes Gebäude, jedes Schlüssel-Asset muss auf 50 Meter Spielentfernung allein an seiner Silhouette erkennbar sein.**

Das heißt: keine Details, keine Farbe, keine Textur — nur der schwarze Umriss gegen den Himmel. Wenn zwei Figuren gleiche Silhouetten haben, ist eine davon falsch designt.

Praktische Umsetzung:
- Jeder Charakter hat ein **dominantes Formmerkmal** (z.B. asymmetrische Schulterplatte, überdimensionierter Kragen, gebogener Stab)
- Jedes Gebäude hat ein **Dach-Profil**, das es von allen anderen Gebäuden der Zone unterscheidet
- NPCs gleicher Fraktion teilen **ein Silhouetten-Element** (z.B. hohe Kragen bei Eisenmenschen-Adel), variieren aber den Rest
- **Silhouetten-Test**: Jedes Asset wird vor Freigabe als schwarze Fläche auf weißem Grund geprüft. Wenn jemand im Team es nicht zuordnen kann → Redesign.

### 4.2 Verfall als Storytelling

Ruinen sind keine Dekoration. Ruinen sind **Text ohne Buchstaben**.

Jede verfallene Struktur muss mindestens eine dieser Fragen beantworten:
- Wer hat hier gelebt?
- Warum sind sie gegangen?
- Was ist danach passiert?

Konkrete Regeln:
- **Verfall hat Richtung**: Wind, Wasser, Schwerkraft. Erosion kommt von einer Seite.
- **Verfall hat Stufen**: Zuerst geht das Dach, dann die Fenster, dann die Wände, zuletzt das Fundament.
- **Verfall hat Bewohner**: Jede Ruine, die länger als eine Generation steht, wird von *etwas* beansprucht — Pflanzen, Tiere, neue Bewohner, Biotech-Wucherungen.
- **Persönliche Spuren**: Ein umgekippter Stuhl. Kratzer an einer Türschwelle. Ein Kinderspielzeug in einem Aschefeld. Diese Mikro-Details sind wichtiger als grandiose Zerstörung.

### 4.3 Architektur = Kultur (vor NPC-Dialog)

Der Spieler muss die Kultur einer Siedlung verstehen, **bevor er mit einem einzigen NPC spricht**.

Architektonische Signale, die das leisten:
- **Türhöhe** = Status der Bewohner (Schlackige brauchen 3m-Türen; Spitzen bevorzugen schmale, hohe Durchgänge)
- **Fensteranteil** = Vertrauen (viele Fenster = offene Kultur; Schlitze = Festung/Paranoia)
- **Materialwahl** = Wohlstand (roher Stein = arm; bearbeitetes Chitin = Mittelschicht; biolumineszente Akzente = Oberschicht)
- **Symmetrie** = Ordnung (militärische Siedlungen sind symmetrisch; organisch gewachsene Orte nie)
- **Vertikalität** = Ambition (Türme = Macht; flache Bauten = Pragmatismus oder Tradition)

### 4.4 Layered Armor statt Fantasy-Kitsch

Keine Bikini-Rüstungen. Keine Schulterplatten so groß wie Scheunen. Kein Schwert-am-Rücken-das-nicht-ziehbar-wäre.

**Modulares Rüstungssystem mit visueller Logik:**

Jede Rüstung besteht aus sichtbaren Schichten (Layern), die der Spieler einzeln tauscht:

1. **Unterkleidung** — Textil, immer sichtbar an Gelenken und unter Plattenrändern
2. **Kettenlage** — Feines Geflecht oder Chitinschuppen-Netz, sichtbar wo Platten enden
3. **Plattenelemente** — Schultern, Brust, Schienbeine. Modulare Slots. Asymmetrie erlaubt.
4. **Überwurf** — Mantel, Umhang, Wappenrock. Kulturelles Statement.
5. **Accessoires** — Gürtel, Taschen, Amulette. Erzählen Backstory.

**Visuelle Regel**: Man muss an jeder Rüstung erkennen können, *wie man sie anzieht*. Wenn es keine logische Reihenfolge gibt → Redesign.

### 4.5 Biotech über Materialmix, nicht Formbruch

Die Biotechnologie dieser Welt sieht nicht aus wie Science-Fiction. Keine glühenden Schaltkreise, keine holographischen Displays, keine Alien-Ästhetik.

Stattdessen: **Vertraute Formen aus unvertrauten Materialien.**

- Ein Schwert hat die Form eines Schwerts — aber die Klinge ist ein einzelner Chitinzahn, leicht gebogen, mit sichtbarer Maserung
- Eine Laterne hat die Form einer Laterne — aber statt Flamme pulsiert eine biolumineszente Blase in einem Keratinkäfig
- Eine Brücke hat die Form einer Brücke — aber die Pfeiler sind gewachsen, nicht gebaut, und zeigen Wachstumsringe

**Kein Formbruch**: Der Spieler muss jeden Gegenstand auf den ersten Blick funktional einordnen können. Die Fremdheit kommt aus dem Material, nicht aus der Form.

### 4.6 High Fashion Mittelalter

Die Ästhetik dieses Spiels ist **Alexander McQueen × HR Giger × Haider Ackermann**.

Was das bedeutet:
- **McQueen**: Theatralische Silhouetten, skulpturale Kleidung, Natur als Muster (Schmetterlings-Korsetts → Chitin-Brustharnische). Mode als Armor. Armor als Mode.
- **Giger**: Biomechanische Verschmelzung von Körper und Umgebung. Wo hört die Rüstung auf, wo fängt der Körper an? Diese Grenze soll unklar sein — besonders bei höherstufiger Ausrüstung.
- **Ackermann**: Drapierung, Layering, monochrome Farbflächen mit einem einzigen Akzent. Eleganz durch Zurückhaltung. Jede Figur sieht aus, als wäre sie angezogen worden, nicht ausgerüstet.

**Anti-Referenz**: World of Warcraft, Guild Wars 2, jedes Spiel, in dem High-Level-Ausrüstung wie ein explodierter Weihnachtsbaum aussieht. Mehr ist nicht mehr. Mehr ist visuelles Rauschen.

---

## 5. Rassen-Ästhetik

| Rasse | Leitbild | Körperbau | Farbpalette | Rüstungs-Stil |
|-------|----------|-----------|-------------|---------------|
| **Eisenmenschen** (Menschen) | Präzise, funktional, MetaHuman-nah | Realistische Proportionen, ethnisch vielfältig | Stahl, Anthrazit, Dunkelblau | Geometrisch, plattenartig, geschliffen |
| **Spitzen** (Elfen) | Alien, organisch, Perlmutt | Schlank, 5–15cm größer, vertikale Pupillen | Elfenbein, Perlmutt, blasses Violett | Chitin-Platten als Körperverlängerung, Haider-Ackermann-Drapierung |
| **Schlackige** (Orks) | Massiv, vulkanisch, Basalt | Breit, 180–220cm, Haut wie gekühlte Lava | Dunkelgrau, verbranntes Orange | Hammerschlag-Platten, Rost als Patina |
| **Fellträger** (Tiermenschen) | Seidenstraßen-Händler, NICHT tribal | Vielfältig (fuchsartig bis bärenartig) | Sand, Zimt, Terrakotta, Indigo | Leichte Chitin-Brigandine unter Brokat, Schmuck ist Währung |

---

## 6. Architektur pro Zone

| Zone | Referenzen | Kernmerkmale | Licht |
|------|-----------|--------------|-------|
| **Küste** | Kowloon + Leyndell + Dogtown | Vertikales Flickwerk, 5–8 Stockwerke. Unten Stein+Rost, oben Chitin+Biolumineszenz. Generationen-Schichtung. | Biolumineszente Adern statt Laternen |
| **Vulkan** | Petra + Nidavellir | *Im* Vulkan. 30% sichtbar. Horizontal, niedrige Decken. Wände folgen Geologie. Hitze als Designelement. | Glutrot von unten, Fackelgelb in Werkstätten |
| **Festung** | Minas Tirith + Vauban | Blockhaft, rechtwinklig, imposant. Mauern 8–12m, 3m dick. Biotech in rechtwinklige Rahmen gezwungen. | Fackeln und Öllampen (kulturelle Entscheidung) |
| **Untergrund** | Großer Basar Istanbul + Derinkuyu | Gewölbte Basare, Amber-Biolumineszenz. Jeder Raum hat mindestens zwei Ausgänge. Organische Tunnel als Schmuggelrouten. | Warm, gedämpft, golden |

---

## 7. Character Screen / Nervensystem-UI

### 7.1 Konzept

Der Character Screen ist kein Statistik-Menü. Er ist ein **medizinisches Diagramm eines lebenden Wesens**.

Beim Öffnen des Screens sieht der Spieler seinen Charakter — und kann ihn *häuten*. Drei halbtransparente Layer, zwischen denen stufenlos geblendet wird:

1. **Rüstungs-Layer** (Default) — Charakter in voller Ausrüstung, drehbar. Slots sichtbar als leuchtende Umrisse.
2. **Haut-Layer** — Rüstung wird transparent. Darunter: der nackte Körper mit sichtbaren Narben, Tattoos, Rassmerkmalen. Hier werden kosmetische Anpassungen vorgenommen.
3. **Nervensystem-Layer** — Haut wird transluzent. Darunter: ein Netzwerk biolumineszenter Linien — das Nervensystem, das als Skill-Tree fungiert.

**Übergangs-Animation**: Weicher Blend, 0.5s. Die Rüstung wird glasartig, die Haut schimmert durch, dann wird sie selbst glasartig, und das Leuchten der Nerven wird sichtbar. Wie ein Röntgenbild, aber *schön*.

### 7.2 Die drei Subsysteme

Das Nervensystem besteht aus drei visuell unterscheidbaren Netzwerken, die sich überlagern, aber eigene Farben und Bewegungsmuster haben:

**Cardio-System (rot, pulsierend)**
- **Farbe**: Tiefes Rot `#CC0000` bis helles Arterien-Rot `#FF3333`
- **Bewegung**: Pulsiert rhythmisch (60–80 BPM, synchron mit einem gedämpften Herzschlag-Sound)
- **Form**: Dicke Hauptadern, die sich in feinere Kapillaren verzweigen. Konzentriert um Herz und Kopf.
- **Gameplay**: Ausdauer, Lebenskraft, Regeneration. Upgrades lassen das Netzwerk *dichter* werden — mehr Kapillaren, intensiveres Pulsieren.
- **Visuelles Feedback**: Bei niedrigem HP wird der Puls schneller und schwächer. Bei vollem HP: langsam, kräftig, satt.

**Muskel-System (blau, statisch)**
- **Farbe**: Tiefes Blau `#003366` bis Electric Blue `#0066CC`
- **Bewegung**: Keine Pulsation. Stattdessen: *Kontraktion* bei Hover — wenn der Spieler über einen Muskel-Knoten fährt, spannt sich das Netzwerk kurz an (wie ein Muskelzucken).
- **Form**: Breite Faserbündel entlang der Gliedmaßen, Knotenpunkte an Gelenken. Sichtbare Verankerungspunkte an Knochen (angedeutet als dunkle Schatten unter dem Netz).
- **Gameplay**: Stärke, Geschwindigkeit, physische Skills. Upgrades machen die Fasern *dicker* und *definierter*.
- **Visuelles Feedback**: Angespannte Muskeln leuchten heller. Ungenutzte/nicht-freigeschaltete Bereiche sind blass, fast unsichtbar.

**Lymph-System (grün, fließend)**
- **Farbe**: Blasses Grün `#00CC66` bis leuchtendes Jade `#33FF99`
- **Bewegung**: Kontinuierliches, langsames Fließen — wie Flüssigkeit in transparenten Schläuchen. Partikel treiben sichtbar durch die Bahnen. Richtung: immer vom Rumpf zu den Extremitäten.
- **Form**: Dünne, gewundene Kanäle. Knotige Verdickungen (Lymphknoten) als Skill-Knoten. Weniger dicht als die anderen Systeme, dafür weitverzweigt.
- **Gameplay**: Resistenzen, Immunität, Gift-/Magie-Abwehr, passive Buffs. Upgrades lassen die Flüssigkeit *schneller fließen* und die Farbe *intensiver* werden.
- **Visuelles Feedback**: Bei Vergiftung wird die Flüssigkeit trüb. Bei aktiven Buffs leuchten einzelne Lymphknoten auf.

### 7.3 Interaktion

- **Zoom**: Der Spieler kann in jeden Körperteil hineinzoomen. Auf höchster Zoomstufe sind einzelne Nervenknoten sichtbar, die als Skill-Punkte funktionieren.
- **Hover**: Nervenbahnen leuchten heller bei Hover, zeigen ihren Systemtyp und den Skill-Namen.
- **Klick**: Öffnet den Skill-Detail-Dialog — eingebettet als Biotech-Panel, das aus dem Nervensystem *herauszuwachsen* scheint.
- **Aktivierung**: Freischaltung eines Skills lässt die entsprechende Nervenbahn aufleuchten und mit dem Rest des Netzwerks verbinden. Eine kurze Puls-Animation breitet sich vom neuen Knoten über das gesamte System aus.

### 7.4 Perspektive-Kompatibilität

Das Nervensystem-UI muss in zwei Spielperspektiven funktionieren:

**First Person (FP)**:
- Arme und Hände sind sichtbar. Bei aktiviertem Nervensystem-View schimmern biolumineszente Linien unter der Haut des Spielercharakters — subtil im Gameplay, deutlich im Menü.
- Statuseffekte (Vergiftung, Buff, Erschöpfung) werden durch Farbänderung der sichtbaren Nervenbahnen an den Armen kommuniziert.
- Character Screen: Zeigt Ganzkörper-Ansicht in separatem UI-Panel (wie ein medizinischer Scanner).

**Third Person (TP)**:
- Nervensystem-Linien schimmern unter der Rüstung durch — besonders an Gelenken, Hals, Handgelenken.
- Bei starker Magie/Skill-Nutzung leuchten die Bahnen kurz über die gesamte Figur auf.
- Character Screen: Direkte Manipulation der 3D-Figur (drehen, zoomen, Layer-Blend).

---

## 8. Referenzen

| Referenz | Relevanz |
|----------|----------|
| Craig Mullins | Atmosphärische Beleuchtung, Farbtemperatur-Kontraste |
| Elden Ring — Leyndell | Vertikale Stadt, Verfall als Welterzählung |
| Alexander McQueen | Skulpturale Mode, Natur-als-Material |
| HR Giger | Biomechanische Verschmelzung, organisch-technische Grenzauflösung |
| Haider Ackermann | Drapierung, monochromes Layering |
| Beksiński | Verfalls-Ästhetik, Knochen-Architektur |
| Kentaro Miura (Berserk) | Rüstungsdesign, dunkle Monumentalität |
