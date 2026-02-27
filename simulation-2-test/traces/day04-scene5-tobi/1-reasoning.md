# Reasoning — Tobi Richter, Tag 4 Szene 5

Sechs Aenderungen, alle klar abgegrenzt. Ich gehe sie einzeln durch.

**Hex-Codes:** V1 hatte ungenaue Farbbezeichnungen im Color-Grading und in den Material-Instanzen (Kap. 1.3, 4.1). Vera hat in GDD-05 praezise Hex-Werte definiert. Ich uebernehme die 1:1 — neun Werte fuer drei Fraktionen. Kein Interpretationsspielraum.

**Module 60:** V1 sagte "20-30 Module". Das war zu konservativ. Drei Fraktionen mit je 12-14 eigenen Modulen plus 20 neutrale Basis-Module ergibt ~60. Die neutralen Module (Wand, Ecke, Tuer, Fenster, Dach, Fundament etc.) bekommen Fraktions-Differenzierung weiterhin ueber Material-Instanzen — jetzt mit Veras Hex-Codes.

**Drei-Schichten-Rendering:** Das ist die groesste strukturelle Ergaenzung. Mittelgrund = Standard-Level-Geometrie (Nanite/Lumen). Hohlicht und Stillfeld = Post-Processing-Overlay plus 3-5 handgebaute Geometrie-Segmente pro Zone. Kein komplettes Parallel-Level — das waere Scope-Wahnsinn.

**Hauten-Shader:** SSS-Material mit Vertex-Displacement. Muss Nanite-Ausnahme sein, weil Vertex-Animation ueber Nanite nicht funktioniert. Spieler-Reaktivitaet ueber MPC-Kopplung an Infektionswert.

**Farbprofile:** Stillfeld = kalt (Violett-Shift, entsaettigte Cyan-Toene). Hohlicht = warm (Bernstein-Glow, roetliche Verzerrung). Zwei getrennte Post-Processing-Profile, die ueber Volume-Blending aktiviert werden.

**Halluzinations-Start:** V1 hatte den Beginn bei Wert 70. Korrektur auf 76 — passt zum Schwelle-Bereich (76-100) in Namis narrativem Schema.
