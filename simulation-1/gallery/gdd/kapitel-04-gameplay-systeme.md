# Kapitel 04 — Gameplay-Systeme

---

## 4.1 Kamera-System

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

**Universalregel: Jedes System muss in BEIDEN Perspektiven funktionieren.** Kein Feature ohne FP- und TP-Äquivalent.

| System | FP-Lösung | TP-Lösung |
|--------|-----------|-----------|
| Nervensystem-Leveling | Halbtransparente Körper-Overlay auf Screen | Kamera zoomt auf Charakter, Körper wird transparent |
| Dialog | Gesicht des NPC im Fokus, Blickkontakt | Over-the-Shoulder, Kamera zwischen Spieler und NPC |
| Kampf | Waffe/Schild sichtbar, physisches Gefühl | Vollkörper-Animation, Footwork sichtbar |
| Klettern | Hände greifen, visuelles Feedback, Höhenangst | Charakter-Silhouette gegen Umgebung, Routenplanung |
| Substanz-Effekte | Visuelle Verzerrung, Farbverschiebung | Charakter-Animation (Taumeln, Zittern), Partikeleffekte |

---

## 4.2 Combat-System

Real-Time Action Combat. Gewichtig, taktisch, positionsbasiert. Näher an Dark Souls als an Diablo, zugänglicher als Sekiro. Jeder Schwerthieb kostet Ausdauer, jeder Block hat ein Timing-Fenster, jeder Gegner hat erkennbare Muster.

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

**Schilde**: Aktive Waffe, nicht passive Ausrüstung. Schildstoß, Schildschlag, aktives Blocken (Parry), passives Blocken (Ausdauer-Drain). Varianten: Rundschild (mobil), Turmschild (stationär), Buckler (Parry-fokussiert).

### Kampf-Prinzipien

1. **Gewicht**: Jede Aktion hat Momentum und Recovery-Frames. Kein Abbrechen mid-Swing.
2. **Ausdauer als Universalwährung**: Angriff, Block, Dodge, Sprint kosten Ausdauer. Kein Buttonmashing.
3. **Positionierung**: Rückenangriffe, Flanken, Höhenvorteil, Engpässe als taktische Elemente.
4. **KI mit Absicht**: Jeder Gegnertyp hat eine erkennbare Kampfdoktrin:
   - **Banditen**: Aggressiv in Gruppen, fliehen bei Überzahl-Verlust
   - **Siedlervolk-Soldaten**: Formation, Schildwall
   - **Höhlenvolk-Krieger**: Gift an Klingen, Hit-and-Run
   - **Innenvolk-Wächter**: Chemisch verstärkt, unberechenbar
   - **Wildtiere**: Instinktbasiert, territorial

---

## 4.3 Leveling — Das Nervensystem

Halbtransparente Körpervisualisierung als Skill-System. Diegetisch: Das Innenvolk hat entdeckt, dass der sterbliche Körper Titanenspuren in seinen Zellen trägt. Wer sich verbessert, aktiviert schlafende biologische Kapazitäten.

### Die drei Systeme

#### 4.3.1 Herz-Kreislauf / Atmungssystem

**Visuell**: Rotes Netzwerk, pulsierend. **Regelt**: Ausdauer-Pool, Sprint-Dauer, Unterwasser-Atmen, Erholung, Höhenresistenz. **Steigerung durch**: Laufen, Klettern, Schwimmen — das System wächst durch Benutzung.

#### 4.3.2 Muskel-Skelett-System

**Visuell**: Weißes Skelett, rot-braune Muskelstränge. **Regelt**: Tragkraft (physisches Gewicht), Nahkampfschaden, Kletterreichweite, Waffenvoraussetzungen, physische Einschüchterung (NPCs reagieren auf sichtbare Masse). **Steigerung durch**: Nahkampf, schweres Tragen, Klettern, körperliche Arbeit.

#### 4.3.3 Lymphsystem

**Visuell**: Grün-gelbes Netzwerk, fließend. **Regelt**: Gift-/Krankheitsresistenz, **Substanz-Toleranz** (Kernmechanik), passive Regeneration, Narbenbildung. **Steigerung durch**: Vergiftungen überleben, Krankheiten durchstehen, kontrollierte Substanznutzung.

**Die Substanz-Schleife** (emergentes Gameplay):

```
Substanz einnehmen → Temporärer Boost
                   → Lymphsystem-Belastung
                   → Wenn Belastung > Toleranz:
                       → Sucht-Stufe steigt
                       → Entzugserscheinungen
                       → Langzeit: permanente Debuffs
```

Starkes Lymphsystem = kontrollierter Substanzeinsatz. Schwaches Lymphsystem + Substanzen = russisches Roulette. Wer nur die Substanzen nimmt ohne Innenvolk-Training, endet zerbrochen.

---

## 4.4 Substanzen — Chemie als Gameplay

Mittelalterliche Biochemie statt Steampunk. Titanengewebe ist chemisch aktiv. Das Innenvolk hat gelernt, daraus Substanzen zu gewinnen, die den Körper verändern.

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

**Chemische Reaktionen**: Substanzen interagieren nach interner Logik. Kombinationen erzeugen Synergien (Aschetinktur + Lymphwasser = verstärkte Heilung), Überdosen (Graukristall + Titanen-Adrenalin = Unverwundbarkeit + Bewusstlosigkeit), oder Halluzinationen. Lymphwasser dient als universelles Gegenmittel (30-Sekunden-Fenster).

---

## 4.5 Rüstung & Ausrüstung — Modulares Slot-System

Modulares Slot-System. Keine Rüstungs-Sets mit festen Boni. Einzelne Teile zum Kombinieren und Modifizieren. High Fashion Mittelalter.

### Slots

8 Slots: Kopf, Schultern, Torso, Arme, Beine, Füße, Rücken (Umhang/Rucksack/Köcher), Accessoire (Gürtel/Kette/Talisman).

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

Jedes Rüstungsteil modifizierbar: Verstärkung (Schutz/Gewicht), Polsterung, Substanz-Beschichtung (Gift-Resistenz, Kälteschutz), Fraktions-Insignien (ändert NPC-Reaktionen), Tarnung.

---

## 4.6 Einschüchterung & Soziale Mechaniken

Keine abstrakten Charisma-Checks. Die Welt reagiert auf den GESAMTEN Spieler — Ausrüstung, Ruf, physische Erscheinung, Taten, Fraktionszugehörigkeit. Kein separates System, sondern ein Layer über allem.

**Drei Eingabefaktoren**: Physische Präsenz (Muskel-Skelett-Stufe, Rüstung, sichtbare Waffen, Narben), Reputation (lokal, Fraktions-Ruf, spezifische Taten, Gerüchte), Kontext (Tageszeit, Territorium, Zahlenverhältnis).

**NPC-Reaktions-Spektrum** (nicht binär):

| Reaktion | Trigger | NPC-Verhalten |
|----------|---------|---------------|
| Verachtung | Schwach, kein Ruf | Ignoriert, beleidigt |
| Gleichgültigkeit | Unauffällig | Standard-Interaktion |
| Respekt | Kompetent, guter Ruf | Bessere Preise, Hinweise |
| Furcht | Stark, gewalttätiger Ruf | Kooperiert sofort |
| Panik | Massaker-Ruf, blutverschmiert | Flieht oder ergibt sich |
| Trotz | Einschüchternd, aber NPC hat Prinzipien | Weigert sich trotz Angst |

---

## 4.7 Wirtschaftssystem

Drei Wirtschafts-Schichten mit eigenen Währungen, Regeln und Konsequenzen:

**Tier 1 — Legaler Handel (Siedlervolk)**: Aschenmark als Währung. Feste, regional unterschiedliche Preise. Standard-Waren verfügbar, Substanzen/Knochenmetall/Gifte nicht. Marktsteuer finanziert das Siedlervolk — Handel ist politisch.

**Tier 2 — Händlernetzwerk (Höhlenvolk)**: Tausch und Versprechen statt Geld. Handelt mit ALLEM. Seltene Materialien, Substanzen, Informationen. Kein Verbraucherschutz. Loyalität wird belohnt, Betrug bestraft.

**Tier 3 — Schwarzmarkt**: Netzwerk aus Kontakten und Codewörtern. Gifte, militärische Ausrüstung, Auftragsmorde. Zugang durch kriminellen Ruf oder Höhlenvolk-Kontakte. Erwischtwerden = Ruf-Verlust, Verhaftung.

**Dynamik**: Angebot und Nachfrage reagieren auf Spieleraktionen. Wirtschaft IST Politik.

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

