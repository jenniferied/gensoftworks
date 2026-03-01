# Peer-Review: GDD-05 Designsprache (V1)

**Reviewer:** Darius Engel, Game Director
**Autorin:** Vera Kowalski
**Datum:** Tag 4, Szene 2 (WORK)
**Referenzen:** GDD-02 Kernmechaniken (V0.5), GDD-01 Spielübersicht (V1)

---

## Gesamteindruck

Vera, das Dokument ist stark. Ehrlich gesagt ist es das koharenteste V1-Dokument, das wir bisher haben. Die visuelle Vision — "Organische Gotik" — ist kein Marketing-Label, sondern ein echtes Designprinzip, das sich durch alle zehn Kapitel zieht. Die drei ästhetischen Säulen (Organik, Grandeur, Ambivalenz) sind präzise genug, um als Entscheidungsfilter für jedes Asset zu funktionieren. Der Referenzkorridor (Gaudi, McQueen, Giger, Beksinski) gibt einem Art Team eine klare Suchrichtung, ohne einzüngen.

Die Lebende Krone als zentrales Designobjekt funktioniert. Die Farbsystematik ist durchdacht. Die Fraktionsvisuals sind sofort unterscheidbar. Das Dokument hält, was es verspricht.

Trotzdem habe ich vier substanzielle Punkte und drei kleinere Anmerkungen, die wir vor V2 klären müssen.

---

## 1. Schattenfieber-Stufen: Alignment-Problem

**Priorität: HOCH**

Das ist der wichtigste Punkt. In GDD-02 definiere ich fünf mechanische Stufen mit folgenden Wertebereichen:

| Stufe | Wert | Name |
|-------|------|------|
| 0 | 0 | Rein |
| 1 | 1-25 | Gezeichnet |
| 2 | 26-50 | Infiziert |
| 3 | 51-75 | Verwandelt |
| 4 | 76-100 | Entfesselt |

In deinem Kapitel 7 beschreibst du drei visuelle Stufen:

| Deine Stufe | Wert | Name |
|-------------|------|------|
| 1 | 1-40 | Rauschen |
| 2-3 | 41-75 | Risse |
| 4 | 76-100 | Schwelle |

Die Wertebereiche stimmen nicht überein. Dein "Rauschen" endet bei 40, mein "Gezeichnet" endet bei 25 und "Infiziert" beginnt bei 26. Das heisst: Ein Spieler mit Infektionswert 30 ist mechanisch in Stufe 2 (Infiziert, mit aktiven Kampf-Fähigkeiten wie Schattenreflex und Schatten-Schritt), aber visuell noch in deinem "Rauschen" (subtile Adern, kaum sichtbar).

Das ist ein Problem. Ein Spieler, der Schatten-Schritt einsetzt — eine sichtbare, aktive Kampf-Fähigkeit — muss das auch an seinem Körper sehen können. Die visuelle Manifestation muss die mechanische Realität spiegeln, sonst bricht die Spielerlogik.

**Vorschlag:** Wir einigen uns auf ein gemeinsames Stufen-Mapping. Entweder deine visuellen Stufen folgen meinen mechanischen Schwellen (0/25/50/75), oder wir definieren gemeinsam neue Schwellen und ich passe GDD-02 an. Das ist bilateral, und ich schlage vor, wir setzen uns dafür zusammen. Nami sollte dabei sein, weil ihre narrativen Zustände (Rauschen, Risse, Schwelle) ebenfalls auf dieses Mapping müssen.

---

## 2. Stufe 0 als visuelle Baseline fehlt

**Priorität: HOCH**

Dein Schattenfieber-Kapitel beginnt bei Stufe 1. Das ist nachvollziehbar — Stufe 0 hat kein Schattenfieber. Aber: Damit der Spieler die Veränderung WERTSCHÄTZEN kann, braucht er eine klare Baseline. Was sieht ein Stufe-0-Spieler? Wie sieht seine Haut aus? Wie verhalten sich Schatten für ihn? Wie sieht eine Schattenfieber-Zone aus, wenn er sie NUR mit Augen und ohne Schattensinne betrachtet?

Das ist gameplay-relevant, weil Stufe 0 ein vollwertiger Spielpfad ist ("Reiner Krieger", "Alchemist" — siehe GDD-02, Abschnitt 6.2). Dieser Spieler verbringt möglicherweise 40+ Stunden in Stufe 0. Er muss Schattenfieber-Zonen visuell erkennen können (unsere Bedingung 1: Transparenz vor Infektion), aber auf eine andere Art als ein infizierter Spieler. Das ist eine Designaufgabe.

**Vorschlag:** Ein kurzer Abschnitt "7.0: Stufe 0 — Die uninfizierte Baseline" vor deinen drei Manifestationsstufen. Was sieht der Spieler? Was sieht er NICHT? Wie erkennt er Schattenfieber-Gefahren ohne Schattensinne?

---

## 3. Biotech-Interaktion: Von der Grammatik zur Mechanik

**Priorität: MITTEL**

Deine Biotech-Übersetzungsregeln (Tabelle 3.2) sind präzise und konsistent. Das ist eine Art Direction, mit der man arbeiten kann. Aber mir fehlt die Brücke zur Spielerinteraktion.

Drei konkrete Beispiele:

**a) Alchemie-Stationen.** In GDD-02 sind das "feste Orte in der Welt". Du beschreibst in 3.4 Meso-Skala, wie Biotech in Räumen funktioniert. Aber wie sieht eine Alchemie-Station aus? Ist das ein Nervenknoten, den der Spieler anzapft? Ein organischer Tisch mit Membrangefässen? Wie signalisiert die Station dem Spieler visuell: "Hier kannst du craften"? Das ist Interaction Design, nicht nur Art Direction — aber es muss hier anfangen.

**b) Gezüchtete Rüstung und Wartung.** In 5.3 schreibst du, schwere Rüstung müsse "regelmässig genährt werden (Nährlösung, Pflege)". Das impliziert eine Wartungsmechanik. In GDD-02 gibt es aktuell keine Rüstungswartung. Entweder wir designen eine (möglich, passt zur Welt), oder du streichst die Formulierung. Ich kann nicht zulassen, dass das Art-Dokument eine Mechanik verspricht, die es nicht gibt. Wenn du das Feature willst, lass uns reden — ich finde die Idee interessant, aber sie muss durchdacht sein.

**c) Trainerstationen.** Das Trainer-System ist in GDD-02 definiert (Fähigkeiten bei NPCs in der Welt lernen). Wie sieht ein Trainingsbereich visuell aus? Gibt es fraktionsspezifische Trainings-Environments? Ein Krone-Fechtplatz sieht anders aus als ein Gilden-Labor. Das wäre eine starke visuelle Differenzierung, die das Gameplay unterstützt.

**Vorschlag:** Ein Abschnitt "Gameplay-Orte" in V2, der die wichtigsten interaktiven Orte (Alchemie-Station, Trainer, Händler, Ruhezonen) visuell definiert. Das können Thumbnail-Skizzen sein — aber die Designrichtung muss stehen.

---

## 4. Spieler-Customization und Fraktionslesbarkeit

**Priorität: MITTEL**

In 5.4 schreibst du: "Fraktionszugehörigkeit, Rüstungsklasse und Schattenfieber-Status müssen auf einen Blick erkennbar sein, auch bei frei kombinierten Sets." Das ist die richtige Anforderung. Aber du beschreibst nicht, WIE.

Die CD-Vorgabe ist klar: Customizable Rüstung/Kleidung, Skyrim-artige FP/TP-Kamera. Das heisst, der Spieler WIRD Teile verschiedener Herkunft mischen. Wie bleibt die Fraktionslesbarkeit erhalten?

Drei Optionen, die ich sehe:

1. **Farb-Dominanz:** Das sichtbarste Kleidungsstück (Torso/Umhang) bestimmt die Fraktionsfarb-Lesung. Egal was an den Füssen ist — der Spieler LIEST die Brust.
2. **Biotech-Signatur:** Jede Fraktion hat eine eigene Biotech-Signatur in ihren Rüstungen (Krone: verborgen, Gilden: offen, Orden: subdermal). Diese Signatur bleibt auch bei gemischten Sets sichtbar.
3. **Wappen/Insignien-Layer:** Ein optionaler Layer (Schulterplatten, Gürtel, Armreif), der die Fraktionszugehörigkeit anzeigt und visuell Vorrang hat.

Das ist eine Entscheidung, die wir gemeinsam treffen müssen — ich als Mechanik-Seite, du als Art-Seite. Für V2.

---

## Kleinere Anmerkungen

### 5. Biolumineszenz als einzige Lichtquelle — Gameplay-Implikation

In 8.4 schliesst du Fackeln, Kerzen und Öllampen komplett aus. Ich unterstütze das — es ist konsequent und mutig. Aber es hat Gameplay-Konsequenzen, die ich in GDD-02 V2 adressieren muss:

- **Stealth:** Wenn ich als Spieler kein Licht LÖSCHEN kann (keine Fackel zum Austreten), wie funktioniert Stealth in beleuchteten Räumen? Kann ich Biolumineszenz-Organe abtoeten? Verdecken? Das ist eine Interaktionsfrage.
- **Nachtzyklus:** Wie hell/dunkel ist die Welt nachts? Wenn nur Biolumineszenz leuchtet, haben Städte nachts ein völlig anderes Erscheinungsbild als am Tag. Das ist eine Chance, kein Problem — aber wir müssen es designen.
- **Schattenfieber-Zonen:** Dein Schattenfieber-Licht "leuchtet, ohne zu beleuchten". Das ist visuell stark. Mechanisch heisst das: Schattenfieber-Zonen sind dunkel, obwohl sie leuchten. Sichtbarkeitsmechanik?

Kein Blocker — aber ein Thema für unser bilaterales Gespräch.

### 6. Tiervolk-Erkennbarkeit auf Distanz

Dein Tiervolk-Design (Kap. 6) trifft die CD-Vorgabe präzise. Subtile Fremdheit, keine offensichtlichen Tiermerkmale. Das ist der richtige Ansatz. Aber: Wie erkenne ich ein Tiervolk-NPC im FP-Modus auf 30 Meter Distanz? Die Details (Pupillenformen, Hautstrukturen, leicht falsche Proportionen) funktionieren auf Nahsicht. Auf Distanz brauchen wir ein anderes Signal.

Die Farbpalette hilft teilweise (Ocker/Terrakotta/Sand vs. Fraktionsfarben). Aber in neutralen Übergangszonen, wo alle Paletten neutral sind, verschwindet dieses Signal. Vielleicht ist die eklektische Kleidung (zusammengesammelt aus allen Fraktionen) das Distanzsignal — ein visuelles Durcheinander, das selbst ein Signal ist. Das würde ich visuell austesten.

### 7. Lebende Krone — Transformationsstufen

Die Beschreibung der Lebenden Krone (1.3) ist exzellent. Die Reaktivität (Farbveränderung, Verschmelzung mit dem Träger) ist genau die visuelle Umsetzung des mechanischen Konzepts aus GDD-02, Abschnitt 2.7. Ein Punkt fehlt mir: Die Krone reagiert laut Emres WBB-01 auf die Daseinsebenen und auf das Schattenfieber. Wie verändert sich die Krone visuell, wenn sie in einer Schattenfieber-Zone liegt? Nimmt sie Schattenfieber-Farben an (Violett-Schwarz, Giftgrün)? Oder widersteht sie — und ihre Elfenbein-Bernstein-Palette bleibt stabil? Das wäre ein starkes visuelles Statement über die Natur der Krone (kontrolliertes vs. unkontrolliertes Emer-Material). Für V2 als Concept Art-Aufgabe.

---

## Zusammenfassung: Aktionspunkte für V2

| # | Aktion | Wer | Priorität |
|---|--------|-----|------------|
| 1 | Schattenfieber-Stufen-Mapping harmonisieren | Darius + Vera + Nami | HOCH |
| 2 | Stufe-0-Baseline-Visuals definieren | Vera (mit Input Darius) | HOCH |
| 3 | Gameplay-Orte visuell definieren (Alchemie-Station, Trainer, etc.) | Vera (mit Input Darius) | MITTEL |
| 4 | Rüstungswartung: Designen oder streichen | Darius + Vera | MITTEL |
| 5 | Fraktionslesbarkeit bei gemischten Sets lösen | Darius + Vera | MITTEL |
| 6 | Biolumineszenz-Gameplay-Implikationen (Stealth, Nachtzyklus) | Darius (GDD-02 V2) | MITTEL |
| 7 | Tiervolk-Distanzerkennbarkeit | Vera | NIEDRIG |
| 8 | Lebende Krone in Schattenfieber-Zonen (Concept Art) | Vera | NIEDRIG |

---

## Fazit

Vera, das Dokument ist solide Arbeit. Die Art Direction trägt. Die Biotech-Grammatik ist das stärkste Stück — die Übersetzungsregeln und Sichtbarkeitsgrade sind exakt das, was ein Art Team braucht, um konsistent zu produzieren. Die Fraktionsvisuals sind sofort unterscheidbar, und die Farbsystematik ist wasserdicht.

Die Hauptarbeit für V2 ist das Stufen-Alignment beim Schattenfieber. Das ist kein Qualitätsproblem deines Dokuments — das ist ein Synchronisationsproblem zwischen unseren Dokumenten, und das lösen wir gemeinsam.

Meine Lieblingsfrage: Macht es Spass? Die Antwort, basierend auf diesem Dokument: Ja. Ein Spieler, der zum ersten Mal eine Gilden-Stadt betritt und die Wände atmen sieht, hat seinen Moment. Ein Spieler, der im Orden die Schwelle von Kalkstein zu pulsierendem Gewebe überschreitet, hat seinen Moment. Und ein Spieler, der auf Stufe 3 in eine Schattenfieber-Zone geht und sieht, wie die Farben kippen — der hat seinen Moment. Das sind die Spieler-Fantasien, die dieses Dokument unterstützt.

Gute Arbeit. Lass uns die offenen Punkte zusammen klären.

*Darius Engel, Game Design Corner, Tag 4 Vormittag*
