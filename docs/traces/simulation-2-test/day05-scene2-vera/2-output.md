# Vera — Tag 05, Szene 2 (WORK) — Output

## Prüfprotokoll: GDD-05 V2

### 1. Stufengrenzen

**Befund V1:** Grenzen standen schon korrekt in Kap. 7.2 (Rauschen 1-40, Risse 41-75, Schwelle 76-100) — aber ohne einheitliche Referenztabelle und ohne klare Trennung zwischen narrativen Zuständen (Nami) und mechanischen Stufen (Darius).

**Änderung V2:**
- Kap. 7.0 (neu): Verbindliche Referenztabelle, alle vier Systeme nebeneinander (Infektionswert / Narrativer Zustand / Mech. Stufe / Visueller Status)
- Halluzinations-Start = 76 explizit eingetragen
- Kapitelstruktur 7.2 → 7.2 umbenannt: Stufe-0-Baseline + "Rauschen / Risse / Schwelle" statt "Stufe 1 / Stufe 2-3 / Stufe 4"
- Ergebnis: **Konsistent. Kein Widerspruch zu GDD-02 oder GDD-03.**

### 2. Stufe-0-Baseline

**Befund V1:** Fehlte vollständig. GDD-05 sprang direkt in Rauschen.

**Änderung V2:**
- Kap. 7.2 Stufe-0-Block (neu): Körper-Beschreibung, Umgebungs-Beschreibung, Gameplay-Relevanz
- Stufe-0-Äquivalent zu Schattensinnen: Alchemie + Trainerfähigkeiten = anderer Spielstil, kein Nachteil
- Nervensystem-UI-Beschreibung: alle vier Äste klar, keine Schatten-Überlagerungen
- Ergebnis: **Vollständig. Visuelle Nulllinie definiert.**

### 3. Hex-Codes

**Befund V1:** Alle Hex-Codes korrekt vorhanden. Keine Abweichungen zu GDD-06 feststellbar.

**Änderung V2:**
- Kap. 4.4: ACES-Validierungshinweis ergänzt (sRGB-Kalibrierung für Ü5 ACES-Tonemapping, Offset-Begründung für warme Töne, HDR-Hinweis für Giftgrün)
- Alle Codes beibehalten, keine Änderungen:
  - Krone: `#3D3D3D` / `#8B1A2B` / `#C5A030`
  - Gilden: `#7A6E5D` / `#C49A20` / `#2EC4B6`
  - Orden: `#E8E4DE` / `#4A5568` / `#D4A017`
  - Schattenfieber: `#2D0A31` / `#39FF14`
  - Tiervolk: `#CC7722` / `#C04000` / `#C2B280`
- Ergebnis: **Codes korrekt. ACES-Hinweis dokumentiert. 1:1-Übernahme in GDD-06 bestätigt.**

### 4. Gameplay-Orte

**Befund V1:** Fehlten komplett. Nur Regionstypen (Krone-Stadt, Gilden-Stadt etc.) vorhanden.

**Änderung V2:**
- Kap. 8.5 (neu): Gameplay-Orte mit drei Ort-Typen × vier Varianten
  - **Alchemie-Station**: Krone (privates Labor, Altgold-Gerät), Gilden (öffentliche Werkstatt, Amber-Licht), Orden (Krankenhaus-Vorbereitungsraum, Bernstein-Glow)
  - **Trainer**: Krone (Fechtsaal, Sigvalt-Statuen), Gilden (Kämpfarena, Chitin-Dummies), Orden (meditativer Übungsraum, Kalkweiss)
  - **Händler**: Krone (privates Kontor), Gilden (offener Stand), Orden (kein Handel, Loyalitätsverteilung), Tiervolk (mobiler eklektischer Stand)
- Jede Variante: visueller Charakter, Lage, Signalelemente (Tabelle)
- Ergebnis: **Vollständig. Alle drei Gameplay-Orte, alle Fraktionsvarianten, visuell definiert.**

### 5. Dominanzprinzip

**Befund V1:** Kap. 5.4 erwähnte Customization, aber kein Regel-System.

**Änderung V2:**
- Kap. 5.4 ergänzt: Torso-Primat-Regel
  - Torso-Slot definiert Fraktionszugehörigkeit
  - Bis zu 2 abweichende Slots: Fraktion A mit Akzenten (noch lesbar)
  - 3+ abweichende Slots: visuell neutral, Händler-Lesart
  - Neutraler Torso: kein Fraktionssignal
- Schattenfieber-Override explizit: ab Risse (Wert 41+) überschreibt Infektion Outfitsignal
- NPC-Reaktion auf gemischte Sets dokumentiert (kein Bug, Spieloption)
- Ergebnis: **Klar und operationalisierbar. Art und Engineering können direkt damit arbeiten.**

---

## Gesamtbefund

| Prüfpunkt | Status V1 | Status V2 |
|-----------|-----------|-----------|
| Stufengrenzen konsistent | Teilweise (keine Tabelle, unklare Trennung) | Behoben |
| Stufe-0-Baseline | Fehlend | Ergänzt |
| Hex-Codes korrekt + ACES | Codes korrekt, ACES undokumentiert | Behoben |
| Gameplay-Orte mit Fraktionsvarianten | Fehlend | Ergänzt |
| Dominanzprinzip | Fehlend | Ergänzt |

**GDD-05 V2 ist fertig. Alle Darius-Review-Punkte adressiert. Alle CD-Vorgaben (Stufengrenzen Tag 4) integriert. Hex-Codes 1:1 aus V1 übernommen und ACES-validiert.**

---

## Artefakt

`/Users/jennifer/Documents/GitHub/gensoftworks/simulation-2-test/gallery/gdd/05-designsprache.md` — aktualisiert auf V2.
