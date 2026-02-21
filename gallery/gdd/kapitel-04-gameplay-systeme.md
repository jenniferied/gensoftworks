---
agent: darius
day: 3
task: "GDD Kapitel 04 — Gameplay-Systeme"
memories_referenced: [darius-008, darius-012, darius-015, darius-019, darius-023, nami-024, cd-day3-morning]
feedback_received: [cd-day3-morning]
status: draft
---

# Kapitel 04 — Gameplay-Systeme

> *"Jedes System in diesem Spiel muss drei Tests bestehen: 1. Ist es spielbar? 2. Zahlt es auf die Kernfrage ein? 3. Kann ein Spieler es in 10 Sekunden verstehen und in 100 Stunden meistern? Wenn nicht — raus damit."*
> *— D. Engel, Game Director, Tag 3*

---

## 4.1 Kamera-System

### Spieler-Fantasie
*"Ich SEHE die Welt wie ICH will — aus meinen Augen oder über meiner Schulter. Das Spiel zwingt mir keine Perspektive auf."*

### Konzept

Nahtloses Umschalten zwischen First-Person (FP) und Third-Person (TP), Skyrim-Style. Kein Ladescreen, kein Cut, kein Übergang. Der Spieler drückt eine Taste und die Kamera zoomt stufenlos zwischen den Perspektiven.

### Spezifikation

**First-Person (FP)**:
- Standard-Exploration in engen Räumen, Innenräumen, Titanenadern
- Immersiver Modus: Wetterbedingungen sichtbar auf dem HUD (Asche auf dem Visor, Regen auf der Sichtlinie, Blut nach Kampf)
- Nahkampf-Feeling: Schwertklinge sichtbar, Schildarm links, physisches Gewicht spürbar
- Bogen/Armbrust: Iron-Sights-ähnliches Zielen, keine Fadenkreuz-Unterstützung (optional in Einstellungen)

**Third-Person (TP)**:
- Standard für Outdoor-Exploration, Klettern, Übersichtssituationen
- Stufenloser Zoom: nah (über der Schulter, ähnlich Resident Evil 4) bis weit (ähnlich Witcher 3 Reiten)
- Charakter-Modell vollständig sichtbar: Rüstung, Waffen, Statuseffekte visuell erkennbar
- Kamera-Kollision: Intelligentes System, das in engen Räumen automatisch näher zoomt statt durch Wände zu clippen

**Universalregel: Jedes System muss in BEIDEN Perspektiven funktionieren.**

Das ist kein Nice-to-Have. Das ist eine Architekturentscheidung. Wenn ein Feature nur in FP funktioniert (z.B. ein UI-Element, das den Bildschirm füllt), muss es ein TP-Äquivalent haben. Wenn es keins gibt, wird das Feature umgestaltet.

| System | FP-Lösung | TP-Lösung |
|--------|-----------|-----------|
| Nervensystem-Leveling | Halbtransparente Körper-Overlay auf Screen | Kamera zoomt auf Charakter, Körper wird transparent |
| Dialog | Gesicht des NPC im Fokus, Blickkontakt | Over-the-Shoulder, Kamera zwischen Spieler und NPC |
| Kampf | Waffe/Schild sichtbar, physisches Gefühl | Vollkörper-Animation, Footwork sichtbar |
| Klettern | Hände greifen, visuelles Feedback, Höhenangst | Charakter-Silhouette gegen Umgebung, Routenplanung |
| Substanz-Effekte | Visuelle Verzerrung, Farbverschiebung | Charakter-Animation (Taumeln, Zittern), Partikeleffekte |

**Gameplay-Beispiel**: Der Spieler erkundet eine Titanenader in FP — enge Gänge, Klaustrophobie, Fackelschein auf Knochenmetall-Wänden. Er findet einen Ausgang und tritt ins Freie. Die Kamera zoomt nahtlos auf TP, und der Spieler sieht zum ersten Mal den Knochenturm in voller Größe über sich. Dieser Perspektivwechsel IST das Storymoment.

---

## 4.2 Combat-System

### Spieler-Fantasie
*"Jeder Kampf fühlt sich an, als könnte ich sterben. Jeder Sieg fühlt sich verdient an. Mein Schwert hat Gewicht, mein Schild hat Zweck, und mein Gegner hat einen Plan."*

### Konzept

Real-Time Action Combat. Kein Turn-based, kein Hack-and-Slash. Gewichtig, taktisch, positionsbasiert. Näher an Dark Souls als an Diablo, aber zugänglicher als Sekiro. Jeder Schwerthieb kostet Ausdauer, jeder Block hat ein Timing-Fenster, jeder Gegner hat erkennbare Muster.

### Waffen-Klassen

**Nahkampf**:

| Waffe | Geschwindigkeit | Schaden | Reichweite | Spieler-Fantasie |
|-------|----------------|---------|------------|------------------|
| Einhand-Schwert + Schild | Mittel | Mittel | Kurz | "Ich bin vorbereitet. Ich blocke, ich kontre, ich kontrolliere." |
| Zweihand-Schwert | Langsam | Hoch | Mittel | "Jeder Hieb zählt. Ich committe und zerstöre." |
| Dolch / Kurzschwert | Schnell | Niedrig | Sehr kurz | "Ich bin schneller als du denkst. Drei Schnitte, bevor du einen Hieb landest." |
| Streitaxt / Kriegshammer | Sehr langsam | Sehr hoch | Kurz | "Rüstung bedeutet nichts. Ich zertrümmere, was im Weg ist." |
| Speer / Hellebarde | Mittel | Mittel-Hoch | Lang | "Du kommst nicht nah genug heran. Die Distanz gehört mir." |

**Fernkampf**:

| Waffe | Feuerrate | Schaden | Vorbereitung | Spieler-Fantasie |
|-------|-----------|---------|--------------|------------------|
| Langbogen | Langsam | Hoch | Spannen + Zielen | "Ein Schuss, ein Treffer. Geduld ist meine Waffe." |
| Kurzbogen | Mittel | Mittel | Schnelles Spannen | "Mobilität + Fernkampf. Ich schieße im Laufen." |
| Armbrust | Sehr langsam | Sehr hoch | Laden (mechanisch) | "Panzerbrechend. Ein Schuss durch die Rüstung." |
| Wurfmesser / Wurfaxt | Schnell | Niedrig | Minimal | "Schneller Opener. Dann wechsle ich zu Nahkampf." |

**Schilde** (eigene Kategorie, kein Anhängsel):

Schilde sind keine passive Ausrüstung. Ein Schild ist eine WAFFE. Schildstoß, Schildschlag, aktives Blocken mit Timing-Fenster (Parry), passives Blocken (Ausdauer-Drain). Unterschied zwischen Rundschilden (mobiler, leichter), Turmschild (stationär, maximaler Schutz), Buckler (Parry-fokussiert, fast kein passiver Block).

### Kampf-Prinzipien

**1. Gewicht**
Jede Aktion hat Weight. Ein Zweihand-Schwert schwingt nicht wie ein Stab — es hat Momentum, Recovery-Frames, Commitment. Der Spieler kann nicht abbrechen mid-Swing. Das ist kein Bug, das ist Taktik. Wer committed, muss den Zeitpunkt richtig wählen.

**2. Ausdauer als Universalwährung**
Jede Aktion im Kampf kostet Ausdauer: Angriff, Block, Dodge, Sprint. Ausdauer regeneriert passiv, aber langsam im Kampf. Das zwingt zu Pausen, zu taktischem Rückzug, zu bewusster Ressourcenverwaltung. Kein Buttonmashing. Wer alles auf einmal tut, steht mit leerer Ausdauer da und stirbt.

**3. Positionierung**
Rückenangriffe machen mehr Schaden. Flanken umgehen Schilde. Höhenvorteil gibt Reichweitenbonus. Engpässe begrenzen Gegneranzahl. Der Spieler, der den Raum liest, hat einen Vorteil über den, der nur auf den Gegner schaut.

**4. KI mit Absicht**
Gegner sind keine HP-Pools mit Angriffsanimation. Jeder Gegnertyp hat eine erkennbare Kampfdoktrin:
- **Banditen**: Aggressiv, aber feige. Greifen in Gruppen an, fliehen bei Überzahl-Verlust.
- **Siedlervolk-Soldaten**: Diszipliniert, Formation, Schildwall. Einzeln schwächer, in Gruppen tödlich.
- **Höhlenvolk-Krieger**: Ausweich-fokussiert, Gift an Klingen, Hit-and-Run. Kämpfen nie fair.
- **Innenvolk-Wächter**: Chemisch verstärkt. Schneller und stärker als normal, aber unberechenbar. Manche brechen mid-Kampf zusammen, weil die Substanzen nachlassen.
- **Wildtiere**: Instinktbasiert. Territorial, nicht böswillig. Ein Wolf greift an, wenn er hungrig ist — nicht, weil er auf einer Spawn-Liste steht.

**Gameplay-Beispiel**: Der Spieler trifft auf drei Banditen an einer Brücke. In FP sieht er: zwei mit Schwertern, einer mit Bogen hinten. Option A — Frontalkampf: Schwert+Schild, den Bogenschützen ignorieren (riskant, aber schnell). Option B — Schleichen: Unter der Brücke klettern, den Bogenschützen zuerst ausschalten. Option C — Verhandeln: Der Spieler kennt ihren Anführer (vorherige Quest). Einschüchtern oder bestechen. Option D — Substanz: Ein Leistungsverstärker des Innenvolks. 30 Sekunden Übermenschlichkeit. Danach: Zittern, Sichtfeldeinschränkung, Ausdauer-Crash.

---

## 4.3 Leveling — Das Nervensystem

### Spieler-Fantasie
*"Ich werde nicht stärker, weil ich Punkte verteile. Ich werde stärker, weil mein KÖRPER sich verändert. Ich SEHE mein Wachstum — in mir."*

### Konzept

Beim Leveln wechselt die Ansicht in eine halbtransparente Körpervisualisierung. Der Spielercharakter wird durchsichtig, und der Spieler sieht sein eigenes Nervensystem, Kreislauf, Skelett — ein lebendiges Anatomie-Modell, das sich mit jedem Levelaufstieg verändert und wächst.

Das ist keine abstrakte Skill-Tree-Metapher. Das ist diegetisch. Das Innenvolk hat diese Technologie entwickelt — die Erkenntnis, dass der sterbliche Körper Titanenspuren in seinen Zellen trägt. Wer sich verbessert, aktiviert buchstäblich schlafende biologische Kapazitäten.

### Die Systeme

#### 4.3.1 Herz-Kreislauf / Atmungssystem

**Visuell**: Rotes Netzwerk. Herz pulsiert. Lungenflügel atmen. Arterien und Venen durchziehen den Körper. Je stärker das System, desto sichtbarer und leuchtender die Bahnen.

**Was es regelt**:
- **Ausdauer-Pool**: Maximale Ausdauer und Regenerationsrate
- **Sprint-Dauer**: Wie lange der Spieler sprinten kann, bevor er keucht
- **Unterwasser-Atmen**: Tauchzeit in überfluteten Titanenadern und Ascheseen
- **Erholung nach Kampf**: Wie schnell die Ausdauer außerhalb des Kampfes zurückkehrt
- **Höhenresistenz**: Auf Knochentürmen wird die Luft dünn. Starkes Kreislaufsystem = weniger Debuff in der Höhe

**Steigerung durch**: Laufen, Klettern, Schwimmen, ausdauerbasierte Aktionen. Das System wächst durch Benutzung — nicht durch Menüklicks.

**Gameplay-Beispiel**: Der Spieler entdeckt eine überflutete Titanenader, die zu einem Innenvolk-Labor führt. Mit Kreislaufsystem Stufe 2 schafft er 40 Sekunden unter Wasser — nicht genug. Er kann das System trainieren (schwimmen, tauchen, Ausdauer-Aktionen über Tage), oder eine Atemsalbe vom Innenvolk kaufen (temporärer Boost, aber: Lymphsystem-Belastung). Oder er findet einen anderen Weg rein.

#### 4.3.2 Muskel-Skelett-System

**Visuell**: Weißes Skelett, rot-braune Muskelstränge. Je stärker das System, desto dichter und definierter die Muskelfasern. Knochen werden massiver. Bei maximaler Stufe sieht der Charakter unter der Haut aus wie eine da-Vinci-Anatomiestudie.

**Was es regelt**:
- **Tragkraft**: Inventarlimit. Nicht als Zahl — als physisches Gewicht. Zu viel Last = langsamere Bewegung, kein Sprint, lauter (Stealth unmöglich)
- **Nahkampfschaden**: Basis-Schadensmultiplikator für alle Nahkampfwaffen
- **Klettern**: Reichweite und Geschwindigkeit beim Klettern. Schwaches System = nur niedrige Wände. Starkes System = Knochentürme
- **Waffenvoraussetzungen**: Schwere Waffen (Zweihand-Schwert, Kriegshammer) erfordern Mindest-Stufen im Muskel-Skelett-System
- **Physische Einschüchterung**: NPCs reagieren auf die physische Präsenz des Spielers. Ein Charakter mit maximalem Muskel-Skelett-System wird ANDERS behandelt als ein drahtiger Dolchkämpfer. Das ist kein Stat-Check — das ist sichtbar.

**Steigerung durch**: Nahkampf, schweres Tragen, Klettern, körperliche Arbeit (ja, dem Schmied beim Hämmern helfen trainiert dein Muskel-Skelett-System).

**Gameplay-Beispiel**: Ein Siedlervolk-Soldat versperrt den Weg. Der Spieler hat Muskel-Skelett Stufe 5, trägt eine Zweihand-Axt und sieht aus wie jemand, der Probleme verursacht. Der Soldat schluckt und tritt beiseite — kein Kampf nötig. Derselbe Spieler mit Stufe 1 und Dolch? "Verschwinde, Fremder." Gleiche Situation, anderes Ergebnis. Der Körper ist der Dialog.

#### 4.3.3 Lymphsystem

**Visuell**: Grün-gelbes Netzwerk, subtiler als die anderen Systeme. Lymphknoten als leuchtende Knotenpunkte. Je stärker das System, desto dichter das Netzwerk und desto heller die Knoten.

**Was es regelt**:
- **Gift-Resistenz**: Wie schnell Gifte abgebaut werden und wie stark sie wirken
- **Krankheitsresistenz**: Chance, Krankheiten abzuwehren (Aschelung, Knochenfäule, Titanenfieber)
- **Substanz-Toleranz**: DIE KERNMECHANIK. Wie viel chemische Verstärkung der Körper verträgt, bevor negative Effekte eintreten
- **Regeneration**: Passive Heilungsrate außerhalb des Kampfes
- **Narbenbildung**: Starkes Lymphsystem = weniger permanente Debuffs durch schwere Verletzungen

**Steigerung durch**: Überleben von Vergiftungen (wer Gift überlebt, wird resistenter), Krankheiten durchstehen, kontrollierte Substanznutzung, Innenvolk-Training.

**EMERGENTES GAMEPLAY — Die Substanz-Schleife**:

Das Lymphsystem ist das, was dieses Leveling-System von jedem Skill-Tree unterscheidet. Es schafft ein Risiko-Ertrags-System, das JEDE andere Mechanik im Spiel berührt:

```
Substanz einnehmen → Temporärer Boost (Stärke, Reflexe, Wahrnehmung)
                   → Lymphsystem-Belastung
                   → Wenn Belastung > Toleranz:
                       → Sucht-Stufe steigt
                       → Entzugserscheinungen ohne Substanz
                       → Krankheitsrisiko steigt
                       → Langzeit: permanente Debuffs
```

Der Spieler KANN sich chemisch verstärken. Die Boosts sind real und mächtig. Aber der Körper hat Grenzen. Ein Spieler mit schwachem Lymphsystem, der Leistungsverstärker nimmt, spielt russisches Roulette mit seinem Charakter. Ein Spieler mit starkem Lymphsystem kann Substanzen kontrolliert einsetzen — wie ein Werkzeug, nicht wie eine Krücke.

**Das ist die Kernmechanik des Innenvolks**: Sie haben gelernt, das Lymphsystem zu stärken UND Substanzen zu raffinieren. Wer sich mit ihnen einlässt, bekommt Zugang zu beidem. Wer nur die Substanzen nimmt, ohne das Training — der endet zerbrochen.

**Gameplay-Beispiel**: Bosskampf. Der Spieler kann ihn nicht besiegen — zu schnell, zu stark. Der Innenvolk-Händler bietet "Graukristall" an — ein Amphetamin-Äquivalent, das Reflexe und Wahrnehmung für 2 Minuten verdoppelt. Lymphsystem-Toleranz: 3. Graukristall-Belastung: 4. Der Spieler nimmt es trotzdem. 2 Minuten Übermenschlichkeit. Boss stirbt. Danach: Sucht-Stufe 1, 30 Minuten Entzugserscheinungen (Tremor, Sichtfeldeinschränkung, Ausdauer-Crash), und das nächste Mal braucht er eine höhere Dosis für denselben Effekt. War es das wert? Das ist die Frage, die wir verkaufen.

---

## 4.4 Substanzen — Chemie als Gameplay

### Spieler-Fantasie
*"Die Welt ist chemisch. Gifte, Drogen, Heilmittel — alles ist eine Frage der Dosis. Ich entscheide, was ich meinem Körper antue."*

### Konzept

Kein Steampunk. Kein Dampf. Kein viktorianischer Alchemisten-Kitsch. Das hier ist **Biotech** — mittelalterliche Biochemie, basierend auf der Erkenntnis, dass Titanengewebe chemisch aktiv ist. Das Innenvolk hat gelernt, aus Titanenresten Substanzen zu gewinnen, die den sterblichen Körper verändern. Echte Gifte. Echte Drogen. Echte Konsequenzen.

### Substanz-Kategorien

**1. Heilmittel (Legal, allgemein verfügbar)**

| Substanz | Wirkung | Herkunft | Preis |
|----------|---------|----------|-------|
| Aschetinktur | Langsame Heilung über Zeit | Siedlervolk-Apotheker | Niedrig |
| Knochenmehl-Paste | Stabilisiert Frakturen, reduziert Muskel-Skelett-Debuffs | Höhlenvolk-Händler | Mittel |
| Lymphwasser | Beschleunigt Giftabbau | Innenvolk-Händler (legal) | Hoch |

**2. Leistungsverstärker (Grauzone, regional unterschiedlich legal)**

| Substanz | Boost | Dauer | Lymph-Belastung | Suchtpotenzial |
|----------|-------|-------|-----------------|----------------|
| Graukristall | Reflexe +50%, Wahrnehmung +30% | 120 Sek. | 4 | Hoch |
| Titanen-Adrenalin | Nahkampfschaden +40%, Schmerzresistenz +60% | 90 Sek. | 3 | Mittel |
| Ascheatem | Ausdauer-Regeneration x3, Unterwasser-Zeit x2 | 180 Sek. | 2 | Niedrig |
| Nervenfeuer | Sprint-Geschwindigkeit +30%, Klettergeschwindigkeit +50% | 60 Sek. | 3 | Mittel |
| Tiefblick | Nachtsicht, verborgene Objekte sichtbar | 300 Sek. | 5 | Sehr hoch |

**3. Gifte (Illegal, Schwarzmarkt)**

| Gift | Wirkung auf Ziel | Anwendung | Herstellung |
|------|-------------------|-----------|-------------|
| Aschenstaub | Langsame Erschöpfung, Ausdauer-Drain | Auf Klinge / ins Essen | Ascheextrakt + Pilzsporen |
| Knochenriss | Muskel-Skelett-Debuff, Bewegungseinschränkung | Auf Klinge | Knochenmehl + Säure |
| Lymphbrand | Zerstört Substanz-Toleranz, macht anfällig für alles | Ins Getränk | Titanenblut + Destillat (SELTEN) |
| Schlafgift | Bewusstlosigkeit (nicht-letal) | Pfeilspitze / Nahrung | Sumpfpilz-Extrakt |

**4. Chemische Reaktionen**

Substanzen interagieren miteinander. Das ist kein Random-System — es folgt einer internen Chemie-Logik:

- **Graukristall + Titanen-Adrenalin**: Überdosis. Sofortige Sucht-Stufe +2, aber 30 Sekunden völlige Unverwundbarkeit. Danach: Bewusstlosigkeit.
- **Aschetinktur + Lymphwasser**: Verstärkte Heilung. Synergieeffekt.
- **Tiefblick + Graukristall**: Halluzinationen. Die Wahrnehmungssteigerung kippt — der Spieler sieht Dinge, die nicht da sind. Oder doch?
- **Jedes Gift + Lymphwasser (rechtzeitig)**: Gegenmittel. Timing-Fenster: 30 Sekunden.

**Gameplay-Beispiel**: Der Spieler muss in eine Siedlervolk-Festung einbrechen. Plan: Schlafgift ins Wasser der Wache, warten bis Wirkung eintritt, einsteigen. Problem: Der Koch probiert das Essen vor dem Servieren. Lösung: Eine Dosis, die den Koch nur leicht benebelt (halbe Dosis = halber Effekt), aber die Wache komplett ausschaltet (volle Portion). Oder: den Koch bestechen. Oder: gar kein Gift, stattdessen Nervenfeuer und über die Mauer klettern. Das Substanz-System erweitert den Lösungsraum jeder Situation.

---

## 4.5 Rüstung & Ausrüstung — Modulares Slot-System

### Spieler-Fantasie
*"Meine Rüstung erzählt meine Geschichte. Jedes Teil wurde verdient, angepasst, repariert. Ich sehe anders aus als jeder andere Spieler — weil mein Weg ein anderer war."*

### Konzept

Modulares Slot-System. Keine Rüstungs-Sets mit festen Boni. Stattdessen: einzelne Teile, die der Spieler kombiniert, modifiziert und anpasst. Von einfachen Leder-Stücken bis zu Knochenmetall-Plattenrüstungen. High Fashion Mittelalter — nicht Fantasy-Kitsch, sondern Rüstung, die aussieht, als hätte ein Schmied sie für einen echten Körper gemacht.

### Slot-System

```
┌──────────────────────────────────────────────┐
│                   KOPF                        │
│   Helm / Kapuze / Maske / Krone / Nichts     │
├──────────────────────────────────────────────┤
│                 SCHULTERN                     │
│   Schulterstücke / Umhang-Ansatz / Nichts    │
├──────────────────────────────────────────────┤
│                  TORSO                        │
│   Brustpanzer / Kettenhemd / Lederharness    │
├──────────────────────────────────────────────┤
│                   ARME                        │
│   Armschienen / Handschuhe / Bandagen        │
├──────────────────────────────────────────────┤
│                   BEINE                       │
│   Beinschienen / Hose / Kilt                 │
├──────────────────────────────────────────────┤
│                   FÜSSE                       │
│   Stiefel / Sandalen / Wickel                │
├──────────────────────────────────────────────┤
│                   RÜCKEN                      │
│   Umhang / Rucksack / Köcher / Nichts        │
├──────────────────────────────────────────────┤
│                 ACCESSOIRE                    │
│   Gürtel / Kette / Talisman / Nichts         │
└──────────────────────────────────────────────┘
```

### Material-Hierarchie

| Material | Schutz | Gewicht | Lautstärke | Verfügbarkeit | Ästhetik |
|----------|--------|---------|------------|---------------|----------|
| Stoff / Leinen | Minimal | Sehr leicht | Still | Überall | Einfach, funktional |
| Leder (gegerbt) | Niedrig | Leicht | Leise | Verbreitet | Robust, gebrauchsspurig |
| Kettenglieder | Mittel | Mittel | Laut (klirrt) | Siedlervolk-Schmiede | Klassisch, militärisch |
| Platte (Stahl) | Hoch | Schwer | Sehr laut | Siedlervolk-Meister | Imposant, autoritär |
| Knochenmetall | Sehr hoch | Mittel (leichter als Stahl!) | Summt leise | Selten, Knochenturm-Abbau | Alien, organisch, irisierend |
| Innenvolk-Biogewebe | Variabel | Sehr leicht | Still | Innenvolk-Labore | Verstörend, lebendig aussehend |

### Modifikation

Jedes Rüstungsteil kann modifiziert werden:
- **Verstärkung**: Zusätzliches Material auf kritische Stellen. Mehr Schutz, mehr Gewicht.
- **Polsterung**: Innenpolster gegen Schlagschaden. Weniger Mobilität, mehr Überleben.
- **Substanz-Beschichtung**: Innenvolk-Technologie. Rüstungsteile mit Substanzen imprägnieren — z.B. Gift-Resistenz-Beschichtung, Kälteschutz, Asche-Abweisung.
- **Fraktions-Insignien**: Rüstung mit Fraktionssymbolen kennzeichnen. Ändert NPC-Reaktionen. Siedlervolk-Emblem? Die Wache lässt dich durch. Höhlenvolk-Markierungen? Die Händler geben dir bessere Preise.
- **Tarnung**: Rüstung anpassen an Umgebung. Asche-graue Färbung für die Einöden, dunkle Töne für Nacht-Operationen.

**Gameplay-Beispiel**: Der Spieler hat einen Knochenmetall-Brustpanzer gefunden — den besten Schutz im Spiel. Aber: Knochenmetall summt. In Stealth-Situationen verrät es ihn. Also modifiziert er ihn: Innenvolk-Biogewebe als Dämpfung unter dem Panzer (reduziert das Summen), Höhlenvolk-Leder-Polster an den Gelenken (für Mobilität), Siedlervolk-Schulterplatten (für Einschüchterung). Das Ergebnis ist einzigartig — kein anderer Spieler wird exakt diese Kombination tragen.

---

## 4.6 Einschüchterung & Soziale Mechaniken

### Spieler-Fantasie
*"Die Welt sieht mich. Sie reagiert auf das, was ich bin — nicht auf ein Menü, in dem ich 'Einschüchtern' auswähle."*

### Konzept

Keine abstrakten Charisma-Checks. Kein Dialogue-Wheel mit "[Einschüchtern]"-Option. Die Welt reagiert auf den GESAMTEN Spieler — seine Ausrüstung, seinen Ruf, seine physische Erscheinung, seine bekannten Taten, seine Fraktionszugehörigkeit. Das ist kein separates System. Das ist ein LAYER über allem anderen.

### Die Einschüchterungs-Matrix

Wie ein NPC auf den Spieler reagiert, basiert auf einem Zusammenspiel von Faktoren:

**Physische Präsenz** (automatisch berechnet):
- Muskel-Skelett-Stufe (körperliche Masse)
- Ausrüstungsgewicht und -typ (volle Plattenrüstung vs. Lumpen)
- Sichtbare Waffen (Zweihand-Axt am Rücken vs. versteckter Dolch)
- Sichtbare Narben / Kampfspuren (akkumulieren über das Spiel)
- Blut an der Rüstung (frisch? — extremer Einschüchterungsfaktor, aber Ruf-Malus bei Zivilisten)

**Reputation** (reaktiv, akkumulativ):
- Lokaler Ruf: Was hat der Spieler IN DIESER REGION getan?
- Fraktions-Ruf: Zu welcher Fraktion wird der Spieler gezählt?
- Spezifische Taten: "Der Typ, der den Banditenchef in der Knochenschlucht getötet hat" — das spricht sich rum. Wachen sind nervöser, Banditen vorsichtiger, Händler höflicher.
- Gerüchte: NPCs reden über den Spieler. Nicht immer korrekt. Ein Spieler, über den wilde Gerüchte kursieren (ob wahr oder nicht), wird anders behandelt.

**Kontext** (situativ):
- Tageszeit: Nachts in einer dunklen Gasse ist der Einschüchterungsfaktor höher
- Umgebung: In DEINEM Territorium bist du einschüchternder als in fremdem
- Zahlenverhältnis: Allein gegen fünf — die fünf sind mutiger. Allein gegen einen — der eine ist nervöser
- Wissen: Hat der NPC den Spieler schon kämpfen SEHEN? Dann weiß er, was er kann

### NPC-Reaktions-Spektrum

Nicht binär (Angst/keine Angst), sondern ein Spektrum:

| Reaktion | Trigger | NPC-Verhalten |
|----------|---------|---------------|
| **Verachtung** | Spieler schwach, kein Ruf, schlechte Ausrüstung | NPC ignoriert, beleidigt, verweigert Service |
| **Gleichgültigkeit** | Spieler unauffällig, neutraler Ruf | Standard-Interaktion |
| **Respekt** | Spieler kompetent, guter Ruf in Fraktion | Bessere Preise, mehr Dialogoptionen, Hinweise |
| **Furcht** | Spieler stark, gewalttätiger Ruf, schwere Rüstung | NPC kooperiert sofort, gibt Info, weicht aus |
| **Panik** | Spieler bekannt für Massaker, blutverschmiert, bewaffnet | NPC flieht, ruft Wachen, oder ergibt sich wortlos |
| **Trotz** | Spieler einschüchternd, aber NPC hat Prinzipien/Todesmut | NPC weigert sich trotz Angst — die härtesten Quests |

**Gameplay-Beispiel**: Gleicher NPC, gleiche Frage ("Wo ist die Schmuggler-Höhle?"), drei Spielertypen:

*Spieler A — Der Diplomierte*: Küstenvolk-Robe, Bücher im Rucksack, kein sichtbares Blut, bekannt als Forscher. NPC antwortet ausführlich, gibt historischen Kontext, bietet an, mitzukommen. Kein Preis, kein Kampf. Wissen als Eintrittskarte.

*Spieler B — Der Söldner*: Volle Plattenrüstung, Blut an den Handschuhen, zwei Köpfe am Gürtel (Banditen-Trophäen), lokaler Ruf als "der Knochenbrecher." NPC antwortet sofort, stottert, zeigt den Weg, und verschwindet. Die Info ist gratis — weil die Alternative tödlich scheint.

*Spieler C — Der Niemand*: Tag 1, Lumpen, kein Ruf, keine sichtbare Waffe. NPC lacht. "Was willst du, Fremder? Verschwinde." Der Spieler muss ARBEITEN für die Information — bezahlen, einen Gefallen tun, oder den NPC auf anderem Weg überzeugen. Gothic-Feeling: Du bist nichts. Noch.

---

## 4.7 Wirtschaftssystem

### Spieler-Fantasie
*"Geld ist Macht, Handel ist Politik, und der Schwarzmarkt kennt kein Gewissen. Ich entscheide, mit wem ich Geschäfte mache — und jedes Geschäft hat einen Preis, der über Gold hinausgeht."*

### Konzept

Drei Wirtschafts-Schichten: legaler Handel (Siedlervolk-dominiert), Händlernetzwerk (Höhlenvolk), Schwarzmarkt. Jede Schicht hat eigene Währungen, Regeln und Konsequenzen.

### Tier 1 — Legaler Handel (Siedlervolk)

Das Siedlervolk kontrolliert den offiziellen Handel. Feste Preise, regulierte Waren, Steuern.

- **Währung**: Aschenmark (Münzen, standardisiert)
- **Verfügbar**: Grundnahrung, Standard-Rüstung, einfache Waffen, Werkzeug, Baumaterial
- **Nicht verfügbar**: Substanzen (über Heilmittel hinaus), Knochenmetall (staatlich kontrolliert), Gifte, Innenvolk-Biotech
- **Preise**: Fest, aber regional unterschiedlich. Knochenmetall ist in der Nähe der Minen billig und in der Stadt teuer.
- **Steuern**: Der Spieler zahlt Marktsteuer. Wer handelt, finanziert das Siedlervolk. Das ist nicht neutral — das ist politisch.

### Tier 2 — Händlernetzwerk (Höhlenvolk)

Das Höhlenvolk operiert parallel zum offiziellen Handel. Nicht illegal, aber außerhalb der Siedlervolk-Kontrolle. Tauschhandel, Gefälligkeiten, Beziehungen.

- **Währung**: Kein Geld — Tausch und Versprechen. "Ich gebe dir das Schwert, du bringst mir das Kraut aus der Schlucht." Oder: Gefälligkeits-Schulden, die eingefordert werden.
- **Verfügbar**: ALLES, was jemand anbietet. Höhlenvolk-Händler handeln mit allem. Moralische Urteile sind schlecht fürs Geschäft.
- **Spezialität**: Seltene Materialien, Substanzen (legal und illegal), Informationen, Kontakte. Wer etwas Bestimmtes sucht, fragt das Höhlenvolk.
- **Risiko**: Kein Verbraucherschutz. Gefälschte Waren, überhöhte Tauschforderungen, Informationen, die halb wahr und halb Falle sind.
- **Vertrauen**: Langfristiger Handel mit denselben Händlern verbessert Angebote. Das Höhlenvolk belohnt Loyalität — und bestraft Betrug.

### Tier 3 — Schwarzmarkt

Existiert in den Schatten aller Fraktionen. Kein zentraler Ort — ein Netzwerk aus Kontakten, Codewörtern, toten Briefkästen.

- **Währung**: Aschenmark (unversteuert), Knochenmetall-Fragmente (als Wertanlage), Geheimnisse
- **Verfügbar**: Alles, was verboten ist. Gifte, militärische Ausrüstung, gestohlene Knochenmetall-Lieferungen, gefälschte Fraktions-Insignien, Auftragsmorde (als Käufer ODER Verkäufer)
- **Zugang**: Nicht offen. Der Spieler muss den Schwarzmarkt FINDEN. Durch Ruf (krimineller Ruf öffnet Türen), Kontakte (Höhlenvolk-Händler als Vermittler), oder eigene Recherche
- **Risiko**: Erwischtwerden = Ruf-Verlust, Verhaftung, Fraktions-Feindschaft. Der Schwarzmarkt ist lukrativ, aber jede Transaktion ist ein Risiko.

### Wirtschafts-Dynamik

**Angebot und Nachfrage**: Wenn der Spieler einen Knochenmetall-Konvoi des Siedlervolks ausraubt, steigt der Knochenmetall-Preis in der Region. Wenn der Spieler eine Handelsroute sichert, sinken die Preise. Die Wirtschaft reagiert.

**Monopole und Machtkämpfe**: Wer die Knochenmetall-Minen kontrolliert, kontrolliert die Region. Der Spieler kann in diesen Machtkampf eingreifen — als Händler, als Söldner, als Saboteur. Wirtschaft IST Politik.

**Inflation**: Je mehr Aschenmark im Umlauf, desto weniger wert. Keine abstrakte Mechanik — der Spieler sieht die Preise steigen, hört NPCs klagen, sieht Händler schließen. Wirtschaftliche Konsequenzen sind spürbar.

**Gameplay-Beispiel**: Der Spieler braucht Graukristall für einen Bosskampf. Legaler Weg: gibt es nicht — Graukristall ist verboten in Siedlervolk-Territorium. Höhlenvolk-Händler: hat es, will aber einen Gefallen — "Bring mir die Frachtliste des nächsten Siedlervolk-Konvois." Schwarzmarkt: hat es, will Knochenmetall-Fragmente als Bezahlung. Innenvolk direkt: haben es, geben es umsonst — aber nur, wenn der Spieler sich einer "Behandlung" unterzieht (permanente Lymphsystem-Modifikation, Risiko unklar). Vier Wege zum gleichen Item. Jeder hat einen anderen Preis. Keiner ist kostenlos.

---

## 4.8 System-Interaktion — Wie alles zusammenhängt

Kein System existiert isoliert. Die Stärke dieses Designs liegt in den Verbindungen:

```
NERVENSYSTEM ←→ SUBSTANZEN
    │                │
    │   Lymphsystem  │
    │   reguliert    │
    │   Toleranz     │
    ▼                ▼
COMBAT ←→ EINSCHÜCHTERUNG
    │                │
    │   Rüstung +    │
    │   Ruf formen   │
    │   Reaktionen   │
    ▼                ▼
WIRTSCHAFT ←→ FRAKTIONEN
    │                │
    │   Handel =     │
    │   Politik      │
    └────────────────┘
```

**Beispiel einer System-Kette**: Der Spieler trainiert sein Lymphsystem (Nervensystem) → kann Graukristall sicher verwenden (Substanzen) → gewinnt einen schwierigen Kampf (Combat) → wird bekannt als "der Aschenteufel" (Einschüchterung) → Händler bieten bessere Deals an aus Angst (Wirtschaft) → das Siedlervolk wird misstrauisch, das Innenvolk fasziniert (Fraktionen) → neue Questlinien öffnen sich.

Das ist kein linearer Pfad. Das ist ein Netzwerk. Und der Spieler schreibt seinen eigenen Weg hindurch.

---

*Erster Entwurf. 8 Systeme, 3 Stunden, 2 Kaffee, 1 Millimeterpapier-Block. Die Systeme stehen. Was fehlt: Balancing-Tabellen (Google Sheets, morgen), Prototyping-Prioritäten (mit Finn besprechen), und die Frage, ob das Nervensystem-Leveling technisch machbar ist (Tobi fragen — der wird entweder grinsen oder weinen).*

*Post-It am Monitor: "JEDES SYSTEM → KERNFRAGE PRÜFEN: Dient es der Erfahrung des Fremden?"*

*Zweites Post-It: "KEIN SYSTEM DARF ALLEIN STEHEN. Wenn ein System keine Verbindung zu zwei anderen hat, ist es das falsche System."*

— Darius Engel, Game Director
