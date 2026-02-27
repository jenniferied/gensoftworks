# Technische Machbarkeitsanalyse — RELICS

**Autor**: Tobi Richter, Technical Artist
**Datum**: Tag 1 (Montag), WORK-Session
**Status**: Erste Einschaetzung (V0.1) — zur Diskussion im Standup

---

## 1. Zusammenfassung

RELICS ist als Vision stark. Als technisches Vorhaben fuer ein 7-Personen-Team ist es extrem ambitioniert. Es ist machbar — aber nur, wenn wir den Scope ehrlich definieren und frueher als uns lieb ist Entscheidungen treffen, die wehtun.

Die groessten Risiken sind nicht die Engine-Features. UE5 gibt uns Nanite, Lumen, World Partition, PCG. Das Problem ist **Manpower fuer Content-Produktion** und **Gameplay-Programmierung**.

---

## 2. Engine & Rendering-Pipeline

### 2.1 Nanite (Virtualisierte Geometrie)

| Aspekt | Einschaetzung |
|--------|---------------|
| Statische Umgebung | Ideal. Felsen, Architektur, Vegetation (ab UE 5.4 experimentell) direkt in Nanite. Kein manuelles LOD-Authoring noetig. |
| Charaktere / NPCs | Nicht unterstuetzt. Skeletal Meshes brauchen klassische LOD-Ketten. Das ist Handarbeit. |
| Empfehlung | Nanite fuer die gesamte statische Welt. Charaktere: max. 3 LOD-Stufen, aggressiv optimiert. |

### 2.2 Lumen (Globale Beleuchtung)

| Aspekt | Einschaetzung |
|--------|---------------|
| Innenraeume | Hervorragend. Gotische Hallen, Kerzenlicht, Farbspiel — genau das, was wir wollen. Vergleich: Control. |
| Aussenraeume | Funktioniert, aber teuer. Grosse offene Landschaften mit vielen Lichtquellen sind problematisch. |
| Software vs. Hardware RT | Software Lumen fuer Mindest-Spec. Hardware RT als Quality-Option. |
| Empfehlung | Beleuchtung als kreativen Vorteil nutzen. Kontrollierte Umgebungen (Staedte, Dungeons, Waelder) statt endlose Ebenen. |

### 2.3 Farb-Pipeline

Ich setze ACES (Academy Color Encoding System) als Arbeitsfarbraum auf. Gruende:
- Konsistente Farben von Substance ueber Houdini bis UE5
- Filmischer Look ohne Post-Processing-Krücken
- Kontrollierbare Tonalitaet fuer "duestere, geerdete" Vision

Das ist meine Domaene — ich kuemmere mich darum, dass das steht, bevor der erste Asset importiert wird.

---

## 3. Kamerasystem

### Das Problem

FP/TP nahtlos umschaltbar klingt einfach. Es ist eines der technisch aufwaendigsten Features, das wir implementieren koennen.

**Warum**:
- FP braucht eigene Arm-Modelle und Animationen (oder ein Vollkoerper-IK-System)
- Waffenanimationen muessen in beiden Perspektiven gut aussehen
- UI/HUD-Design aendert sich fundamental
- Kamerakollision in TP ist ein eigenes System
- Combat-Balancing unterscheidet sich (Sichtfeld, Timing)

### Meine Empfehlung

**Third Person als Primaermodus**, mit einem Zoom-System, das naeher an den Charakter heranfaehrt (bis Ueber-die-Schulter). Kein echter First-Person-Modus.

Begründung:
- 70% weniger Animationsarbeit
- Ein Kamerasystem statt zwei
- Trotzdem "immersives" Gefuehl durch Close-TP
- Gothic, Dark Souls, Witcher — alle erfolgreich in TP

**Falls die CD auf echtes FP besteht**: Dann ist das ein Feature fuer V2 oder DLC, nicht fuer den Vertical Slice.

---

## 4. Combat-System

### Realitaetscheck

Real-time Melee Combat ist eines der schwersten Systeme in der Spieleentwicklung. Skyrim hatte dafuer ein dediziertes Kampf-Team. Dark Souls hat ueber Jahre iteriert.

**Was wir brauchen**:
- Hit Detection (Capsule-based oder Animation-driven)
- Stamina-System
- Blocking / Parrying
- Stagger und Hit Reactions
- Waffentypen (Schwert, Bogen, Armbrust, Schild)
- Feind-AI fuer Kampf

**Was wir haben**: Keinen dedizierten Gameplay-Programmer.

### Meine Empfehlung

1. **Middleware evaluieren**: Es gibt UE5-Combat-Frameworks im Marketplace. Nicht ideal, aber als Basis realistischer als alles von Null.
2. **Prototyp in Blueprints**: Ich kann einen groben Kampf-Prototypen in Blueprints bauen. Nicht performant fuer Shipping, aber ausreichend fuer den Vertical Slice.
3. **Scope reduzieren**: Lieber 2 Waffentypen (Schwert + Bogen) mit gutem Gefuehl als 5 Typen, die sich alle matschig anfuehlen.

**Kritischer Pfad**: Ohne jemanden, der sich Vollzeit um Combat kuemmert, wird das der Faktor, an dem das Projekt steht oder faellt. Das muss frueh auf den Tisch.

---

## 5. Welt-Scope

### Open-World vs. Semi-Open-World

| Kriterium | Open-World (Skyrim) | Semi-Open (Gothic) |
|-----------|---------------------|---------------------|
| Terrain-Groesse | 30-60 km2 | 3-8 km2 |
| Einzigartige Assets | Tausende | Hunderte |
| Streaming-Komplexitaet | Hoch | Moderat |
| QA-Aufwand | Enorm | Handhabbar |
| Team-Groesse (typisch) | 100+ | 20-40 |

### Meine Empfehlung: Semi-Open-World

**Eine zusammenhaengende Kernregion** (ca. 4-6 km2) mit:
- 1 Stadt (gross, dicht, vertikal — Dishonored-Inspiration)
- 2-3 kleinere Siedlungen
- Verbindende Wildnis (Wald, Felder, Wege)
- 1-2 Dungeons

Das passt zum Briefing ("Dichte statt Breite", Gothic-Referenz) und ist fuer unser Team realistisch.

**Terrain-Pipeline**: Houdini-generiert, in UE5 importiert, mit PCG fuer Vegetation und Detail-Platzierung. Das ist mein Kernbeitrag — ich kann eine Houdini-Pipeline bauen, die uns Terrain in Stunden statt Wochen liefert.

---

## 6. Asset-Pipeline

### Das ehrliche Bild

| Rolle | Kann Assets produzieren? | Anmerkung |
|-------|--------------------------|-----------|
| Vera (Concept Artist) | Ja — 2D und 3D | Einzige dedizierte Kuenstlerin |
| Tobi (ich) | Teilweise — prozedural | Terrain, Felsen, Vegetation-Systeme, Materialien. Kein Character Art. |
| Rest des Teams | Nein | |

Fuer ein Spiel dieses Umfangs brauchen wir geschaetzt:
- 50-100 einzigartige Architektur-Meshes
- 30-50 Requisiten-Sets
- 10-20 Charaktermodelle (Spieler + NPCs)
- 5-10 Kreaturenmodelle
- Hunderte Texturen und Materialien
- Dutzende Animationen

### Strategie

1. **Prozedurale Generierung maximieren** (Tobi)
   - Houdini: Terrain, Felsen, Mauern, Grundformen
   - UE5 PCG: Vegetation, Scatter, Detail-Platzierung
   - Substance Designer: Materialien prozedural

2. **Modulare Architektur** (Vera + Tobi)
   - Baukasten-System: 20-30 Module ergeben hunderte Gebaeude
   - Vera designed die Module, ich baue die Regeln fuer Zusammensetzung

3. **Marketplace als Basis**
   - Megascans (im UE5-Abo enthalten) fuer Umgebungs-Assets
   - Selektiver Marketplace-Einkauf fuer Basis-Assets, die wir anpassen

4. **Photogrammetrie** (optional)
   - Fuer Fels- und Mauerwerk-Texturen
   - Detmold und Umgebung haben genuegend mittelalterliche Substanz

---

## 7. Risikomatrix

| Risiko | Schwere | Wahrscheinlichkeit | Mitigation |
|--------|---------|---------------------|------------|
| Kein Gameplay-Programmer | Kritisch | Hoch | Middleware, Blueprint-Prototyp, ggf. Freelancer |
| Asset-Produktion zu langsam | Hoch | Hoch | Prozedurale Pipeline, Marketplace, modulares Design |
| Scope Creep (Open-World-Ambition) | Kritisch | Mittel | Fruehe CD-Entscheidung fuer Semi-Open, Vertical Slice als Scope-Anker |
| Lumen-Performance auf Ziel-Hardware | Mittel | Mittel | Fruehe Performance-Tests, DLSS/FSR Pflicht, Scalability Settings |
| FP/TP-Kamerasystem zu aufwaendig | Hoch | Hoch | TP-only Empfehlung, FP als Stretch Goal |
| Animationsqualitaet (Kampf) | Hoch | Hoch | Mixamo/Marketplace-Basisanimationen, selektive Custom-Arbeit |

---

## 8. Offene Fragen an die CD

1. **Kamera**: Koennen wir mit Third-Person + Close-Zoom leben, oder ist echtes First-Person nicht verhandelbar?
2. **Zielplattform**: PC-only oder auch Konsolen? (Beeinflusst Performance-Budget massiv)
3. **Marketplace-Budget**: Duerfen wir Marketplace-Assets als Basis kaufen und anpassen?
4. **Vertical Slice**: Was genau soll drin sein? Eine Stadt, ein Dungeon, ein Quest-Strang?
5. **Combat-Tiefe**: Wie tief soll das Kampfsystem sein? Dark Souls oder eher Skyrim?

---

## 9. Naechste Schritte (diese Woche)

- [ ] UE5-Projekt aufsetzen (Projektstruktur, Ordnerkonventionen, Versionskontrolle)
- [ ] Color-Pipeline konfigurieren (ACES, OCIO)
- [ ] Houdini-Terrain-Prototyp starten (1 km2 Testregion)
- [ ] Kamera-Blueprint-Prototyp (TP + Zoom)
- [ ] Marketplace-Recherche: Combat-Frameworks, Basis-Assets
- [ ] Pipeline-Bibel anlegen (lebendes Dokument)

---

*"Man kann alles bauen. Die Frage ist nur, was man mit diesem Team in dieser Zeit bauen SOLLTE."*
