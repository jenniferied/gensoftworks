# Day 02, Scene 2 — Reasoning | Leo Fischer

## Gedankenprozess

### Ausgangslage
Tag 1 hat mir die Spieler-Perspektive geklärt: vier Zielgruppen, fünf Konkurrenten, vier Kernrisiken. Heute geht es darum, diese Erkenntnisse in prüfbare Werkzeuge umzuwandeln. Ab morgen gibt es v0.1 -- und ich brauche ein System, um jeden Draft systematisch zu reviewen.

### Wolf (2013) als Grundlage
Das Briefing referenziert Wolfs neun Infrastrukturen bereits als Vollständigkeits-Checkliste. Mein Job ist es, diese akademische Taxonomie in ein praktisches QA-Werkzeug zu übersetzen. Ich habe Kapitel 3 vollständig gelesen (S. 154-197).

**Kernerkenntnisse aus Wolf:**
- Die neun Infrastrukturen sind: Maps, Timelines, Genealogies, Nature, Culture, Language, Mythology, Philosophy, Tying Together
- Nicht jede Welt braucht alle neun, aber jede Lücke muss bewusst sein
- Die QUALITÄT einer Welt zeigt sich in den Verknüpfungen zwischen Infrastrukturen, nicht in der Tiefe einzelner
- Für Videospiele besonders relevant: Kultur kann visuell und interaktiv vermittelt werden, nicht nur textlich (S. 183)

**Mein Ansatz:** Jede Infrastruktur bekommt einen "Spieler-Test" -- eine Frage, die ein Spieler nach 30 Minuten beantworten können sollte, OHNE Codex. Das macht die akademische Checkliste spielbar.

### QA-Framework
Das Framework muss drei Dinge können:
1. Briefing-Compliance prüfen (Hard Fails vs. Soft Checks)
2. Cross-Referenzen zwischen GDD und WBB sicherstellen
3. Spielerperspektiv-Tests durchführen

Ich habe mich an JIRA-Severity-Levels orientiert (BLOCKER bis TRIVIAL), weil das Team damit arbeitet und es klare Eskalationswege gibt.

### Streamer-Alpha
Mein Content-Creator-Wissen ist hier der USP. Ich weiß aus eigener Erfahrung:
- YouTube Retention fällt nach 10 Min auf ~38%
- Twitch-Clips entstehen bei Player-Agency, nicht bei Cutscenes
- Chat-Engagement ist der beste Proxy für Spieler-Interesse

Die erste Stunde habe ich Minute für Minute durchgeplant, basierend auf dem Briefing (Fremder kommt an, Fraktionen, Material, Schattenfieber) und meinen Tag-1-Erkenntnissen (Angebot statt Tutorial, Agentschaft statt Exposition).

### Entscheidungen
- Wolf-Checkliste: Cross-Reference-Tabelle (Infrastruktur x WBB-Kapitel) hinzugefügt, damit Emre und Nami sehen, wo ihre Kapitel welche Infrastrukturen abdecken müssen
- QA-Framework: Versionsspezifische Checklisten (v0.1, v0.2, v0.3) für jeden Tag
- Streamer-Alpha: Konkrete Metriken mit Zielen, damit Finn die Erfolgsmessung hat

## Output
1. `gallery/gdd/00-wolf-checkliste-leo.md` -- Wolf-Infrastrukturen als QA-Werkzeug
2. `gallery/gdd/00-qa-framework-v01-leo.md` -- Konsistenz-Prüfung für GDD & WBB
3. `gallery/gdd/00-streamer-alpha-konzept-leo.md` -- Erste-Stunde-Konzept + Community-Strategie
