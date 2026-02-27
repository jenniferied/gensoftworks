# Darius — Tag 2, Szene 5 (WORK) — Reasoning

## Kernfrage
Wie integriere ich Leos QA-Input und Namis Narrativ-Mapping so, dass GDD-02 eine belastbare V0.5 wird — nicht nur Stichpunkte, aber auch noch nicht V1-Volltext?

## Entscheidungen

### 1. Leos drei Bedingungen: Wo im Dokument?
**Problem:** Leos Bedingungen sind Querschnittsanforderungen — sie betreffen nicht nur den Schattenfieber-Abschnitt, sondern auch Combat (1.5), Alchemie (4.x) und Exploration (5.x).

**Entscheidung:** Eigener Abschnitt 2.1 direkt unter der Systemuebersicht, VOR den Stufen-Details. Die Bedingungen sind das Fundament — sie muessen zuerst gelesen werden. Zusaetzlich Querverweise in den anderen Abschnitten, wo sie sich konkret auswirken (z.B. Schutz-Alchemie in 4.2, Sichtbarkeitsschichten in 5.4).

**Begruendung:** Wenn jemand nur Abschnitt 2 liest, muss er die Bedingungen sehen. Wenn jemand Abschnitt 4 liest, muss er verstehen, WARUM es eine Schutz-Kategorie gibt.

### 2. Stufen-Mapping: Fuenf auf drei?
**Problem:** Ich habe fuenf mechanische Stufen (0-4), Nami hat drei narrative Zustaende (Rauschen, Risse, Schwelle) plus "Gesund". Das sind verschiedene Granularitaeten.

**Entscheidung:** Die narrativen Zustaende sind die ERLEBBARE OBERFLAECHENERSCHEINUNG. Die mechanischen Stufen sind die SYSTEM-EBENE. Mapping:
- Stufe 0 = Gesund
- Stufe 1-2 = Rauschen (mit gradueller Intensivierung)
- Stufe 2-3 = Uebergang Rauschen→Risse (Stufe 2 ist die Bruecke)
- Stufe 3 = Risse
- Stufe 4 = Schwelle

**Begruendung:** Stufe 2 als Brueckenzone ist wichtig. Bei Wert 26 ist man gerade erst "infiziert" — da sollten noch keine vollen "Risse" einsetzen. Die narrativen Zustaende koennen innerhalb einer Stufe variieren. Namis Vorschlag in GDD-03 hatte Stufe 1-2 als "Rauschen" und Stufe 3-4 als "Risse" — aber sie hatte auch fuenf Stufen statt vier (0-5 statt 0-4), und ihr Infektionswert ging bis 100 statt zu meinen Schwellen. Ich habe ihren Ansatz uebernommen und auf mein System angepasst.

### 3. CD-Entscheidung "Tod = kein Infektionsanstieg"
**Problem:** Das war eine offene Frage in der V1-Outline (1.5 und 2.6). Jetzt haben wir eine Antwort.

**Entscheidung:** In 1.5 als klare Aussage mit Begruendung. Begruendung: Tod ist bereits Strafe genug; Infektionsanstieg bei Tod wuerde die BEWUSSTE Entscheidung verwischen (direkte Verbindung zu Bedingung 3).

### 4. Lebende Krone als Relikt
**Problem:** In der V1-Outline war das Relikt nicht spezifiziert. Jetzt haben wir es.

**Entscheidung:** Neuer Abschnitt 2.7 — das Relikt ist so fundamental fuer das Schattenfieber-System, dass es in GDD-02 behandelt werden MUSS, nicht nur in WBB-01. Querverweise zu Emres Kapitel 4 und 6.

### 5. Schutz-Alchemie als neue Kategorie
**Problem:** Bedingung 3 (kein versehentliches Infizieren) erfordert, dass Stufe-0-Spieler taktische Werkzeuge haben, um infektionsgefaehrliche Situationen zu bewaeltigen.

**Entscheidung:** Neue Produktkategorie "Schutz" in 4.2 mit expliziter Begruendung. Das ist gleichzeitig ein Stufe-0-Aequivalent (Balancing-Massnahme) und eine Antwort auf Bedingung 3.

**Begruendung:** Ohne Schutz-Alchemie waere ein Stufe-0-Spieler in verseuchten Gebieten hilflos — er muesste entweder Gebiete meiden (= Inhalte gesperrt) oder sich infizieren (= nicht gewollt). Die Schutz-Kategorie loest beide Probleme.

### 6. Transparenz-UI
**Problem:** Bedingung 1 (Transparenz) braucht ein konkretes UI-Modul. Das ist normalerweise Veras Territorium, aber die ANFORDERUNG muss von mir kommen.

**Entscheidung:** Neuer Abschnitt 2.8 mit Anforderungen an das UI. Keine Wireframes (das macht Vera), aber klare funktionale Anforderungen: Was muss angezeigt werden, wann, wie.

### 7. Risikomatrix
**Problem:** Leo denkt in Risiken. Das muss ins Dokument.

**Entscheidung:** Abschnitt 6.5 als QA-Risikomatrix — nicht im Schattenfieber-Abschnitt, sondern bei den Querschnittsthemen. Die Risiken betreffen mehrere Systeme.

### 8. Eigene Namenssysteme
**Problem:** CD will eigene Namen, keine nordischen. Das betrifft Stufennamen, Fraktionsnamen, Artefaktnamen.

**Entscheidung:** Neuer Abschnitt 6.1 mit der CD-Entscheidung und ihren Auswirkungen auf GDD-02. Die jetzigen Stufennamen sind Arbeitsnamen.

### 9. Stufe-0-Aequivalente
**Problem:** Leos Community-Analyse zeigt: "Beide Wege muessen vollwertig sein." Die V1-Outline hatte das als Balancing-Leitlinie, aber nicht konkret.

**Entscheidung:** Neue Spalte "Stufe-0-Aequivalent" in der Kosten-Nutzen-Matrix (2.5). Jede Schattenfieber-Faehigkeit hat eine nicht-infizierte Alternative, die denselben Spielraum abdeckt. Das macht die Gleichwertigkeit pruefbar.

## Was NICHT in diese Version gehoert
- V1-Volltext fuer jeden Abschnitt (ab Mittwoch)
- Detaillierte Waffenklassen-Movesets (Tag 3)
- Vollstaendige Alchemie-Rezeptliste (Tag 3)
- Wireframes fuer das Transparenz-UI (Vera, Tag 4)
- RELICS-eigene Namen (Emre + Nami, Tag 3-4)

## Qualitaetspruefung
- [x] Alle CD-Entscheidungen eingearbeitet
- [x] Leos drei Bedingungen als harte Constraints mit Veto-Recht
- [x] Namis drei Zustaende auf fuenf Stufen gemappt
- [x] Bloodborne Insight als Goldstandard referenziert
- [x] Skyrim Vampirismus als Anti-Referenz referenziert
- [x] Lebende Krone eingebaut mit Querverweisen zu WBB-01
- [x] Stufe-0-Aequivalente in der Kosten-Nutzen-Matrix
- [x] Schutz-Alchemie als neue Kategorie
- [x] QA-Risikomatrix
- [x] Tod/Infektion geklaert
- [x] Namenssystem-Hinweis
- [x] Briefing-Konsistenz geprueft
