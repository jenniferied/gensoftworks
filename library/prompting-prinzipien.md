# Prompting-Prinzipien für die Simulation

Zusammengestellt aus MA-Thesis-Recherche (Kap. 5, 7) und Community Research.

---

## LLM-Kontextverarbeitung

### Lost in the Middle (Liu et al. 2023)

Modelle verarbeiten Informationen am **Anfang und Ende** eines langen Kontexts zuverlässiger als in der Mitte. Konsequenz für unsere Dokumente:

- **Kritische Constraints** (Guardrails, Ausschlüsse) an den Anfang UND ans Ende
- **Vision/Kernkonzept** ganz nach vorne
- **Details** (Fraktionen, Regionen) können in die Mitte — werden aber weniger zuverlässig beachtet
- Je kürzer das Dokument, desto geringer der Effekt

### Halluzination (Huang et al. 2025)

Modelle erzeugen plausibel klingende Inhalte, die faktisch falsch oder in sich widersprüchlich sind. Gegenmaßnahmen:

- **Explizite Verbote** statt implizite Erwartungen ("KEIN Steampunk" > "mittelalterlich")
- **Gegenseitige Kontrolle** — REVIEW-Szenen sind Dehalluzinierung (ChatDev-Prinzip)
- **Logbook als Gedächtnis** — ohne Rückbezug auf vorherige Szenen driftet der Kontext

### Kaskadierende Halluzination (Hong et al. 2024, MetaGPT)

Fehler potenzieren sich von Agent zu Agent. Agent A macht kleinen Fehler → Agent B baut darauf auf → Agent C arbeitet mit doppelt verfälschtem Material.

- **REVIEW-Szenen** als Validierungspunkte einbauen
- **CD-Feedback** unterbricht die Kaskade
- **Briefing als Anker** — Agents müssen regelmäßig gegen das Briefing prüfen

---

## Strukturprinzipien für Agent-Prompts

| Prinzip | Beschreibung |
|---------|-------------|
| **Wichtigstes zuerst** | Modelle gewichten frühere Konzepte stärker |
| **Stichpunkte > Fließtext** | Leichter parsbar, weniger Lost-in-the-Middle-Risiko |
| **Explizite Ausschlüsse** | "Was es NICHT ist" verhindert Drift |
| **Rollenklarheit** | Ein Agent = eine Perspektive (ChatDev/MetaGPT-Erkenntnis) |
| **Frage statt erfinde** | Reduziert Halluzination an Unsicherheitsstellen |

---

Quellen: Liu et al. (2023), Huang et al. (2025), Qian et al. (2024, ChatDev), Hong et al. (2024, MetaGPT)
