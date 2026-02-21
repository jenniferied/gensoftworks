# Kapitel 06 — Art Direction

> **Autorin**: Vera Kowalski, Concept Artist & Environment Designer
> **Stand**: Tag 3, GDD-Sprint
> **Status**: Erster vollständiger Entwurf

---

## 1. Visuelle Identität: Biotech-Mittelalter

Das hier ist kein Steampunk. Kein Zahnrad, kein Dampf, kein viktorianisches Messinggefrickel. Steampunk ist retrospektive Industrieromantik — wir machen das Gegenteil.

**Biotech-Mittelalter** bedeutet: Eine Welt, in der Technologie nie mechanisch wurde, sondern biologisch. Statt Maschinen hat diese Zivilisation *Organismen gezüchtet*. Statt Schaltkreisen verlaufen Nervenbahnen. Statt Stahl wächst Chitin. Die Ästhetik liegt irgendwo zwischen gotischer Kathedrale und lebendem Korallenriff — monumental, aber atmend.

**Visueller Leitgedanke**: Stell dir vor, jemand hätte das Mittelalter mit CRISPR statt mit dem Webstuhl industrialisiert.

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

### 5.1 Eisenmenschen (Menschen)

**Leitbild**: Präzise. Ingenieursmäßig. Funktional. MetaHuman-nah.

Die Eisenmenschen sind die technisch-rationale Spezies. Ihr Design kommuniziert Kontrolle.

- **Körperbau**: Realistische menschliche Proportionen. Keine Fantasy-Übertreibung. MetaHuman-Qualität als Baseline.
- **Gesichter**: Kantig bis oval, klare Knochenstruktur. Ethnische Vielfalt innerhalb der Fraktion.
- **Kleidung**: Sauber geschnittene Stoffe, präzise Nähte, sichtbare Knöpfe und Schnallen aus poliertem Chitin. Uniforme Elemente selbst in Zivilkleidung — Kragenspiegel, Manschetten, Gürtelschnallen mit Fraktions-Insignien.
- **Rüstung**: Geometrisch, plattenartig. Klare Kanten, präzise Passform. Die einzige Fraktion, bei der Rüstungsteile *geschliffen* aussehen statt gewachsen.
- **Haare**: Praktisch. Kurz, hochgesteckt, unter Helmen passend. Freie Haare = Off-Duty.
- **Farbpalette**: Stahl, Anthrazit, Dunkelblau. Rote Akzente für Offiziere. Weiß für Gelehrte.

### 5.2 Spitzen (Elfen)

**Leitbild**: Leicht alien. Organische Kurven. Perlmutt und Chitin als zweite Haut.

Die Spitzen sind die biologisch fortschrittlichste Spezies — ihr Design kommuniziert eine Zivilisation, die sich selbst *gezüchtet* hat.

- **Körperbau**: Schlanker als Menschen, 5–15 cm größer im Schnitt. Längere Finger, längerer Hals. Nicht zerbrechlich — *effizient*. Wie Windhunde.
- **Gesichter**: Hohe Wangenknochen, leicht vergrößerte Augen (110% Menschengröße, nicht mehr). Pupillen vertikal wie Katzen. Hauttöne mit leichtem Perlmutt-Schimmer bei bestimmtem Lichteinfall.
- **Kleidung**: Drapiert, fließend, mehrlagig. Haider-Ackermann-Ästhetik. Asymmetrische Wickelgewänder aus Materialien, die lebendig wirken — leichtes Schimmern, minimale Texturänderung bei Bewegung.
- **Rüstung**: Chitin-Platten, die wie natürliche Verlängerungen des Körpers wirken. Nahtlose Übergänge zwischen Haut und Panzer. Bei Elite-Einheiten ist unklar, ob die Rüstung getragen oder *gewachsen* ist.
- **Schmuck**: Perlmutt-Einlagen, Keratin-Ornamente, biolumineszente Linien an Schläfen und Handgelenken (kosmetisch? funktional? beides?).
- **Farbpalette**: Elfenbein, Perlmutt, blasses Violett. Dunkle Varianten in Schwarz-Irisierend für Krieger.

### 5.3 Schlackige (Orks)

**Leitbild**: Massiv. Vulkanisch. Basalt-Texturen. Hochofen-Patina.

Die Schlackigen sind eine Spezies, die Hitze und Druck als Heimat empfindet. Ihr Design kommuniziert geologische Kraft.

- **Körperbau**: Breit, schwer, niedriger Schwerpunkt. 180–220 cm, aber wirken breiter als hoch. Massive Unterarme und Kiefer. Kurze Beine relativ zum Torso.
- **Haut**: Grafit- bis basaltfarben, mit sichtbarer *Textur* — nicht glatt, sondern wie gekühlte Lava. An Gelenken und Narben schimmert manchmal ein schwaches Orange durch (als wäre unter der Haut noch Glut).
- **Gesichter**: Breite Kiefer, schwere Brauen, flache Nasen. Keine Stoßzähne (kein Tolkien-Ork-Klischee). Stattdessen: verhärtete Hautplatten an Stirn und Wangenknochen, wie natürlicher Helm.
- **Kleidung**: Schwere Lederschürzen, Schmiedekleidung als Alltag. Ketten statt Schnallen. Eisenringe als Schmuck. Praktisch bis zur Rohheit.
- **Rüstung**: Geschichtete Platten mit Hammerschlag-Textur. Rost ist bei den Schlackigen *kein Verfall* — es ist Patina, bewusst zugelassen, ein Zeichen, dass die Rüstung Feuer gesehen hat.
- **Architektur-Echo**: Ihre Gebäude sehen aus wie sie — blockhaft, horizontal, hitzebeständig, mit schwach glühenden Fugen.
- **Farbpalette**: Dunkelgrau, Anthrazit, verbranntes Orange. Messingakzente bei Anführern.

### 5.4 Fellträger (Tiermenschen)

**Leitbild**: HÄNDLER-ÄSTHETIK. Seidenstraße. Brokat und Pelz. Versteckter Reichtum. Urban-nomadisch.**

**NICHT TRIBAL.** Keine Knochen-Halsketten, keine Lendenschurze, keine "edle Wilde"-Klischees. Die Fellträger sind die *ökonomische Macht* dieser Welt.

- **Körperbau**: Vielfältig — von fuchsartig-schlank bis bärenartig-massiv. Das Gemeinsame: dichtes, gepflegtes Fell als natürliche Isolation und Statussymbol.
- **Gesichter**: Tierische Grundzüge (Schnauze, Ohrenform, Augenstellung variieren je nach Linie), aber *ausdrucksfähig* — die Mimik muss Emotionen im Spiel transportieren können.
- **Kleidung**: Das ist der Kern. Die Fellträger kleiden sich wie **Seidenstraßen-Händler auf dem Höhepunkt ihres Reichtums**:
  - Mehrlagige Gewänder aus Brokat, Seide, besticktem Leinen
  - Pelz als Besatz, nicht als Hauptmaterial (sie tragen Pelz *über* Pelz — das ist ein bewusstes Luxussignal)
  - Versteckte Taschen, eingenähte Fächer, Gürtel mit Dutzend kleinen Beuteln (sie tragen ihr Vermögen am Körper)
  - Turbane, Hauben, Kapuzen mit Ohraussparungen — praktisch und dekorativ
- **Rüstung**: Leicht, unter Kleidung getragen. Chitin-Plättchen in Textil eingenäht, wie historische Brigandine. Panzer sieht aus wie Mantel. Das ist Absicht — Fellträger zeigen Stärke nie offen.
- **Schmuck**: Schwer, filigran, überall. Ohrgehänge, Armreife, Ketten mit Handelsmarken, gravierte Chitin-Plaketten. Schmuck *ist* Währung.
- **Farbpalette**: Warme Erdtöne — Sand, Zimt, Terrakotta. Dazu: tiefes Indigo und Purpur als Akzente. Gold-Einschläge bei Wohlhabenden.

---

## 6. Architektur pro Zone

### 6.1 Küste — Vertikale Flickwerk-Stadt

**Referenzen**: Kowloon Walled City + Leyndell (Elden Ring) + Dogtown (Cyberpunk 2077)

Eine Stadt, die zweimal gebaut wurde. Die untere Schicht: alte Steinarchitektur, zerbrochen, verwittert, mit Meeressalz-Patina und Muschelbewuchs. Die obere Schicht: Biotech-Konstruktionen, die aus den Ruinen wachsen wie Korallen aus einem gesunkenen Schiff.

- **Vertikalität**: 5–8 Stockwerke, verbunden durch Außentreppen, Brücken, Seilzüge
- **Flickwerk**: Kein einheitlicher Baustil. Jedes Stockwerk hat andere Materialien, andere Fensterformen, andere Dachneigung. Die Stadt ist ein Querschnitt durch Generationen.
- **Zwei Zeitschichten**: Unten Stein+Rost (alt, tot), oben Chitin+Biolumineszenz (neu, lebendig). Die Grenze verläuft nicht horizontal — sie ist gezackt, willkürlich, ein Kampf zwischen Verfall und Wachstum.
- **Licht**: Tageslicht erreicht den Boden kaum. Biolumineszente Adern an Wänden ersetzen Straßenlaternen. Marktplätze haben offene Decken.
- **Sound-Implikation**: Holz knarrt, Wasser tropft, Wind pfeift durch Spalten. Diese Stadt *klingt* lebendig.

### 6.2 Vulkan — Organische Höhlenstadt der Schlackigen

**Referenzen**: Petra (Jordanien) + Nidavellir (MCU) + Ironforge (WoW, aber horizontal)

Nicht auf dem Vulkan — *im* Vulkan. Nur 30% der Stadt ist von außen sichtbar. Der Rest erstreckt sich in Lavahöhlen und gegrabenen Tunneln.

- **Organisch**: Wände sind geglättet, aber nicht rechtwinklig. Räume folgen der Geologie, nicht dem Reißbrett. Korridore verengen und weiten sich wie Arterien.
- **Horizontal**: Keine Türme. Alles breitet sich seitwärts aus. Decken sind niedrig (2,5–3m, damit Schlackige sich wohlfühlen, Spitzen sich ducken müssen).
- **30% sichtbar**: Von außen: massive Portalöffnungen in der Felswand, mit Hammer-Relief-Rahmen, schwach orange glühende Fugen. Das Versprechen: *hier geht es weiter*.
- **Hitze als Designelement**: Metalloberflächen haben Anlauffarben. Wasser verdampft in Kanälen. Kristallisierte Mineralien wachsen an Wänden.
- **Licht**: Glutrot von unten (Magma-Kanäle unter Gitterrosten), Fackelgelb in Werkstätten, Dunkelheit dazwischen.

### 6.3 Siedler-Festung — Menschliche Ingenieurskunst

**Referenzen**: Minas Tirith + Carcassonne + Vauban-Festungen

Die Eisenmenschen bauen, wie sie denken: gerade, rechtwinklig, imposant. Ihre Festungen sind Manifestationen von Kontrolle über eine feindliche Landschaft.

- **Blockhaft**: Quaderförmige Grundrisse, klare Kanten, metrische Wiederholung. Fenster in Reih und Glied. Türme in gleichmäßigen Abständen.
- **Rechtwinklig**: Keine organischen Kurven. Jeder Winkel 90°. Wo Biotech-Elemente integriert sind, werden sie in rechtwinklige Rahmen *gezwungen* — ein Spannungsfeld zwischen lebender Technologie und menschlichem Ordnungswillen.
- **Imposant**: Mauern 8–12m hoch, 3m dick. Tore mit doppelten Fallgittern. Die Botschaft: *Wir bleiben*.
- **Ingenieurskunst**: Sichtbare Baulogik — Strebepfeiler, Wasserableitungen, Belagerungsrampen. Jedes Element hat eine Funktion. Dekoration ist *auch* funktional (Reliefs dienen als Handgriffe für Reparaturen).
- **Licht**: Fackeln und Öllampen. Die Eisenmenschen nutzen wenig Biotech-Beleuchtung — kulturelle Entscheidung, nicht technische Limitation.

### 6.4 Untergrund — Fellträger-Basare

**Referenzen**: Großer Basar Istanbul + Derinkuyu (Kappadokien) + Novigrad-Unterwelt (Witcher 3)

Unter der sichtbaren Welt liegt das Nervensystem des Handels.

- **Basare**: Gewölbte Gänge, an beiden Seiten Verkaufsnischen. Stoffe hängen von der Decke als Raumteiler. Laternen (biolumineszent in Keratinkäfigen) alle 5m. Gerüche werden Teil des Designs — Gewürze, Leder, Räucherwerk (als Partikeleffekte darstellbar).
- **Geheimgänge**: Hinter Wandteppichen, unter Bodenfliesen, durch drehbare Regale. Die Fellträger bauen *immer* einen zweiten Weg. Jeder Raum hat mindestens zwei Ausgänge — sichtbar oder nicht.
- **Organische Tunnel**: Zwischen den bebauten Bereichen verlaufen naturbelassene Tunnelsysteme — Wurzelwerk, tropfendes Wasser, Pilz-Biolumineszenz. Hier verliert sich der menschliche Einfluss. Perfekte Schmuggelrouten.
- **Licht**: Warm, gedämpft, golden. Die Fellträger nutzen Biolumineszenz in Amber-Tönen — Behaglichkeit als Verkaufsstrategie. Dunkle Ecken nur in den Geheimgängen.
- **Sound-Implikation**: Stimmengewirr, Münzklirren, gedämpfter Gesang. Das Echo verrät die Raumgröße.

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

| Referenz | Relevanz für dieses Projekt |
|----------|---------------------------|
| **Craig Mullins** | Atmosphärische Beleuchtung, Farbtemperatur-Kontraste, das Gefühl von *Ort*. Jedes Environment-Concept muss Mullins' Lichtqualität anstreben. |
| **Elden Ring — Leyndell** | Vertikale Stadt, architektonische Schichtung, Verfall als Welterzählung. Unsere Küstenzone lernt von Leyndell. |
| **Cyberpunk 2077 — Dogtown** | Architektonische Dichte, kulturelles Layering, wie eng bebaute Räume sich anfühlen. Vorbild für die Flickwerk-Ästhetik. |
| **Alexander McQueen — Runway** | Skulpturale Mode, Natur-als-Material, Brutalität und Schönheit in einem Atemzug. Rüstungsdesign-Philosophie. |
| **HR Giger** | Biomechanische Verschmelzung, organisch-technische Grenzauflösung. Hochstufige Rüstungen und Spitzen-Architektur. |
| **Haider Ackermann** | Drapierung, monochromes Layering, textiles Understatement. Fellträger-Mode und zivile Kleidung aller Fraktionen. |

### Ergänzende visuelle Quellen

- **Zdzisław Beksiński** — Verfalls-Ästhetik, Knochen-Architektur, traumartige Ruinen
- **Kentaro Miura (Berserk)** — Rüstungsdesign, Körper-unter-Panzer-Spannung, dunkle Monumentalität
- **Moebius (Jean Giraud)** — Weltweite, klare Linien in komplexen Environments, Farbe als Emotion
- **Petra, Jordanien** — Reale Felsenarchitektur als Referenz für die Vulkanzone
- **Großer Basar, Istanbul** — Raumgefühl, Lichtstimmung, Dichte der Untergrund-Basare

---

> *"Jeder Frame ist eine Komposition. Jede Silhouette erzählt. Jedes Material hat eine Geschichte. Wenn der Spieler anhält, um einen Screenshot zu machen — nicht wegen eines Questmarkers, sondern weil der Ort schön ist — dann haben wir gewonnen."*
>
> — V.K., Art Station, Mittwochabend
