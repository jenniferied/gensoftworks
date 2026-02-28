# Day 02, Scene 2 — Reasoning (Tobi)

## Gedankenprozess

### Was liegt vor?
- Recherche-Notizen (Tag 1): Nanite, Lumen, Biolumineszenz-Klassen, Schattenfieber-PP 3 Stufen, vertikale Stadt, Kamerasystem
- Briefing-Ergebnis (heute Morgen): Premium-Release bestätigt, Schwellenanker-Zone als MPC-System, zwei Achsen (Spieler x Welt)
- Darius' GDD-Struktur: Kap 6 = Technische Spezifikation & Produktion, verantwortlich: Tobi + Finn

### Was muss rein?
Kapitel 06 hat laut Briefing-Struktur folgende Themen:
1. Engine & Zielplattformen
2. Rendering-Pipeline (Nanite, Lumen, Biolumineszenz)
3. Schwellenanker-System (MPC-Spec) — das Kernsystem, das heute Morgen besprochen wurde
4. Schattenfieber VFX-Pipeline (Post-Process-Stufen)
5. Kamerasystem (Third/First Person)
6. World Partition & vertikale Stadt
7. Audio-Pipeline (Grundriss — Details fehlen noch, markieren)
8. Release-Modell & Monetarisierung (Premium, kein Live-Service)
9. Team-Sizing (realistisch für ein Indie-AA-Studio)
10. Produktions-Roadmap (Phasen)
11. Risikomatrix

### Schwellenanker MPC-Spec
Das ist das technisch Neue von heute. Im Briefing habe ich vorgeschlagen:
- Material Parameter Collection mit Zentrum + Radius
- Distanz-Falloff: 50m (Farbtemperatur-Shift, Volumetrics), 10m (Oberflächen-Veränderung), 2m (voller Effekt)
- Kompatibel mit Schattenfieber-PP: beide lesen aus derselben MPC
- Additive Überlagerung: Spieler mit Schattenfieber + Schwellenanker-Zone = verstärkter Effekt

Ich definiere die MPC-Parameter-Struktur als Tabelle. Kein C++-Code in einem GDD, aber die Parameter-Namen und Wertebereiche müssen klar sein.

### Release-Modell
- Premium (Vollpreis)
- Main Release
- Streamer-Alpha (vorab für Content Creators)
- Geschlossene Beta (0,5-1 Jahr vor Release)
- Große DLCs (keine Mikrotransaktionen)
- Kein Live-Service

### Team-Sizing
GenSoftworks ist ein Indie-Studio in Detmold. 7 Leute Kern. Für Produktion brauchen wir Outsourcing und Freelancer. Ich muss realistisch sein — kein AAA-Team, aber auch kein Hobbyisten-Setup.

### Was ich NICHT erfinde
- Audio-System: nur Grundriss, muss mit jemandem abgestimmt werden
- Netzwerk/Multiplayer: nicht im Scope (Singleplayer-RPG)
- Detaillierte Budget-Zahlen: nicht mein Bereich, Finn übernimmt

### Struktur-Entscheidung
Ich orientiere mich an Spectors Technik-Abschnitt (knapp, aber vollständig) und erweitere um die für RELICS spezifischen Systeme. Das GDD ist kein technisches Designdokument (TDD) — es ist die technische Sektion im GDD. Tiefe genug, dass ein Leser versteht, WAS gebaut wird und WARUM. Das WIE im Detail kommt in die Pipeline-Bibel.
