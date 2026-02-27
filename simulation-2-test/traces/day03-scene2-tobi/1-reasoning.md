# Trace — Tobi Richter — Tag 3, Szene 2 (WORK) — Reasoning

## Überlegungen vor dem Schreiben

### Was sich von V0.1 ändern muss

Die Outline war strukturell solide. Die Kapitelgliederung bleibt. Was fehlt:

1. **Fliesstext statt Stichpunkte** — V1 muss ein lesbares Dokument sein, nicht nur eine Checkliste. Jede Entscheidung braucht eine Begründung.

2. **Schattenfieber-Tech ist unterdimensioniert** — Darius hat in GDD-02 fünf mechanische Stufen definiert (0-4, Infektionswert 0-100) mit graduellen Übergängen. Meine V0.1 hatte nur vier Stufen. Muss auf fünf erweitert werden, und die weichen Grenzen müssen technisch abgebildet werden (kein harter Stufenschalter, sondern parametergesteuertes Blending).

3. **Budget-Aufschlüsselung fehlt** — CD hat 45k EUR Freelancer-Budget bestätigt. Das muss aufgeschlüsselt werden: Gameplay-Programmer ist die kritischste Position. Der Rest verteilt sich auf Animations-Assets, Audio, QA.

4. **Motion Matching braucht mehr Detail** — Ü 5.4+ hat das System nativ. Aber: Datenbank-Grösse, Capture-Quellen, Fallback für Mixamo-Prototyping müssen definiert werden.

5. **Abstimmung mit Darius' GAS-Architektur** — GDD-02 definiert drei Kampfebenen, Cancel-Windows, Setup-Plays. Die technische Seite muss das spiegeln: Ability-Hierarchie, Gameplay Tags, Cooldown-Management.

### Risiken, die ich ehrlich benennen muss

- **Gameplay-Programmer**: Ohne diese Person kein Combat, kein Vertical Slice. Bridge-Lösung (Marketplace-Framework) ist riskant, weil GAS-Integration nicht garantiert ist.
- **Schattenfieber-Rendering**: Fünf Stufen mit graduellen Übergängen sind 100 Parametersets. Das ist ein eigenes Projekt. Muss früher getestet werden als geplant.
- **Houdini-Terrain für Vera**: Ich verspreche vereinfachte HDAs, aber die müssen WIRKLICH einfach sein. Vera ist schnelle Lernerin, aber Houdini ist Houdini.
- **Performance-Budget**: Lumen + Niagara-Schattenfieber + Motion Matching + Nanite. Das ist ambitioniert für Minimum-Tier (GTX 1070). Muss früher benchmarkt werden.

### Farb-Pipeline — warum ich darauf bestehe

ACES als Arbeitsfarbraum ist keine technische Eitelkeit. Wenn Vera in Substance arbeitet, ich in Houdini, und alles in Ü5 zusammenläuft, MÜSSEN die Farben konsistent sein. Ein falscher Farbraum-Transform und das gesamte Fraktions-Farbschema bricht. Das ist Tag-1-Infrastructure, nicht Luxus.

### Meilensteine — realistisch bleiben

Die Phasen aus V0.1 sind ambitioniert aber machbar. Kernrisiko: Wochen 5-12 (Vertical Slice Prototype) hängen komplett am Gameplay-Programmer. Wenn der in Woche 6 statt Woche 5 kommt, rutscht alles. Puffer einplanen.

### Schattenfieber-Tech Detail

Darius definiert fünf Stufen. Nami hat drei narrative Zustände (Rauschen, Risse, Schwelle). Technisch muss das ein parametergesteuertes System sein:

- Infektionswert 0-100 als Float
- Post-Processing Volume mit Material Parameter Collection (MPC)
- MPC interpoliert alle Effekte basierend auf dem Float
- Keine harten Stufenschalter — das System atmet
- Niagara-Partikel skalieren mit demselben Float
- Halluzinatorische Elemente (Stufe 3-4): Shader-basierte Geometrieverzerrung, möglicherweise Custom Stencil für selektives Rendering von "Nicht-Echtem"

Das ist das technisch anspruchsvollste System im ganzen Projekt. Muss ich so benennen.
