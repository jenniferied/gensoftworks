# Reasoning — Leo Fischer, Tag 2, Szene 2 (WORK)

## Was mache ich heute?

Zwei Dinge: Einen Spielerperspektiv-Bericht und einen QA-Input fuer GDD-02.

## Gedankengang: Spielerperspektiv-Bericht

Ich versetze mich in den Spieler, der RELICS zum ersten Mal auf Steam sieht, die Store-Page liest, das Spiel kauft und die ersten Stunden spielt. Was FUEHLT der?

**Positive Impulse:**
- "Medieval aber Biotech" -- das klingt frisch. Das klingt nach etwas, das ich noch nicht gespielt habe. Wenn der Trailer das rueberbringt, klicke ich drauf.
- Nervensystem-Leveling -- SOFORT Neugier. Wie funktioniert das? Das will ich sehen. Das ist ein Hook, der staerker ist als "noch ein Skill Tree."
- Drei Fraktionen, keine ist gut/boese -- als BG3/Gothic-Spielerin will ich genau das. Grau ist spannender als Schwarz/Weiss.
- Real-time Kampf mit Gewicht -- ja bitte. Skyrim-Kampf mit mehr Substanz ist ein Community-Traum.
- Schattenfieber veraendert die Welt -- wenn das wirklich Bloodborne-maessig ist, bin ich ALL IN. Das waere der Moment, an dem ich meinen Freunden sage: Spiel das.

**Sorgen:**
- Schattenfieber nicht reversibel -- das ist meine groesste Sorge. Gestern habe ich sechs Community-Erwartungen formuliert, und "reversibel mit Aufwand" war Nummer 4. Die CD hat entschieden: nein. Ich respektiere das -- aber ich muss ehrlich sein: Spieler WERDEN das als Problem empfinden, wenn wir es nicht extrem gut kommunizieren. Das save-scumming-Problem aus meiner Analyse ist real.
- Wie viel Biotech sieht man in der ersten Stunde? Wenn das Setting-USP erst in Stunde 5 sichtbar wird, verlieren wir Spieler vorher.
- Combat-Skill-Ceiling "zugaenglich bis belohnend" klingt gut auf Papier, aber das ist EXTREM schwer zu balancen. Das ist das Design-Problem, an dem Hunderte von Spielen scheitern.
- Semi-Open-World vs. Open-World: Spieler, die "Skyrim-Referenz" lesen, erwarten Open World. Wenn sie Semi-Open bekommen, gibt es eine Erwartungsenttaeuschung. Kommunikation muss das framen.

## Gedankengang: QA-Input fuer GDD-02

Fuer den QA-Teil denke ich in Test-Szenarien: Welche Mechaniken haben die hoechste Wahrscheinlichkeit fuer Balancing-Probleme?

1. **Schattenfieber-Stufensystem**: Jede Stufe muss sich lohnen UND kosten. Die Achse "Macht vs. Bestrafung" aus meiner Community-Analyse ist hier der Leitfaden. Jede Stufe braucht eigene Test-Szenarien: Ist der Nutzen fuehlbar? Ist der Preis fair? Kippt die Balance irgendwo ins Negative?

2. **Combat-Skill-Ceiling**: "Zugaenglich" und "belohnend" muessen GLEICHZEITIG funktionieren. Das heisst: Casual-Spieler muessen Kaempfe gewinnen koennen (ohne Parieren/Timing zu meistern), UND erfahrene Spieler muessen SICHTBAR besser sein. Die Spannweite dazwischen ist das Testfeld.

3. **Nervensystem-Leveling**: Drei Systeme (Cardio/Atmung, Muskel/Skelett, Lymph) muessen a) verstaendlich sein, b) sich UNTERSCHIEDLICH anfuehlen, und c) alle viable sein. Wenn ein System objektiv besser ist, wird es zum "Meta-Build" und die anderen werden irrelevant. Das ist das klassische Balancing-Problem.

4. **Alchemie statt Magie**: Ohne Magie muss Alchemie die Luecke fuer "uebernatuerliche" Spielerhandlungen fuellen. Das muss sich MAECHTIG genug anfuehlen, um Spieler zu befriedigen, die "Feuerball werfen" gewohnt sind. Harte QA-Frage: Ist Alchemie-Combat spassig genug, um 40+ Stunden zu tragen?

5. **Fraktions-Balance**: Drei Fraktionen, keine "gut/boese" -- aber Spieler optimieren. Wenn eine Fraktion bessere Belohnungen gibt, wird sie der Default-Weg. Jede Fraktion muss EIGENE, GLEICHWERTIGE Vorteile bieten.

6. **Irreversibles Schattenfieber + Fraktionen**: Der Orden jagt Infizierte. Was passiert, wenn ein Spieler sich infiziert UND beim Orden ist? Wird er rausgeschmissen? Kann er infiltrieren? Das ist narrativ spannend, aber mechanisch ein Alptraum zum Testen.

## Entscheidung fuer den Output

Ich schreibe zwei Dokumente in einem:
1. Spielerperspektiv-Bericht ("Wenn ich RELICS heute kaufe")
2. QA-Risikomatrix mit Test-Prioritaeten

Der Ton ist ehrlich, direkt, nicht akademisch. Ich schreibe, wie ich auf meinem Kanal sprechen wuerde.
