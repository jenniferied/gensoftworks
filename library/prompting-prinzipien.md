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

## Bildgenerierung: Modellspezifische Tipps

### Seedream 4.5 (ByteDance) — $0.04/img

- Natürliche Sprache, KEIN Keyword-Stacking
- **30–100 Wörter** ideal — wir over-prompten wahrscheinlich
- Reihenfolge zählt: Wichtigstes zuerst
- Negative Prompts funktionieren
- Zweck explizit angeben: "A concept art character sheet"
- Quality Tags ("masterpiece") weglassen

### Flux 2 Pro (BFL) — $0.03/img

- **Subject first, immer**
- KEINE negativen Prompts — beschreibe was du willst, nicht was nicht
- Quality Tags weglassen (Flux defaultet auf Pro-Qualität)
- Spezifische Kameras benennen: "Shot on Sony A7IV" >> "professional photo"
- HEX-Codes für präzise Farben: "#02eb3c"

### Nano Banana Pro (Google Gemini) — $0.15/img

- Prompts wie Design-Briefs schreiben — länger und detaillierter als bei anderen
- Präzise technische Begriffe: "85mm lens at f/8" statt "zoom in"
- Emphatische Constraints: "MUST obey ALL" verbessert Adherence ~40%
- Kämpft gegen Surreales — will Realismus

### GPT Image 1.5 (OpenAI) — $1.00/img

- Für Hero Shots und finale Illustrationen
- Layered Reasoning: Background → Subject → Details → Constraints

### Modellwahl nach Use Case

| Einsatz | Modell | Grund |
|---------|--------|-------|
| Batch-Exploration | Seedream | Günstigst, stark bei Concept Art |
| Cinematische Environments | Flux | Kamera-Kontrolle, Photorealismus |
| Hero-Finals (Text-lastig) | Nano | Text-Perfektion, Constraint-Treue |
| Charakter Concept Art | Seedream | Stilisiert, kostengünstig für Iteration |
| Waffen (Artbook-Stil) | Seedream | Gutes stilisiertes Rendering |
| Gottheiten/Folklore | Seedream | Stark bei imaginativen Szenen |

---

Quellen: Liu et al. (2023), Huang et al. (2025), Qian et al. (2024, ChatDev), Hong et al. (2024, MetaGPT), fal.ai docs, BFL docs, ByteDance docs
