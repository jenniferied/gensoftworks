---
agents: [emre, nami]
day: 3
task: "GDD Kapitel 3 — Welt & Fraktionen (Sync-Session Besprechungsraum)"
memories_referenced: [emre-022, emre-025, emre-026, emre-027, emre-028, emre-030, nami-021, nami-024, nami-027, nami-028]
feedback_received: [cd-day3-morning]
status: draft
---

# RELICS — Game Design Document
# Kapitel 3: Welt & Fraktionen

> *Autoren: Emre Yilmaz (Worldbuilder), Nami Okafor (Narrative Design)*
> *Version: v1.0 — Tag 3 Vormittag*
> *Status: GDD-Entwurf, zur Review durch Darius freigegeben*

---

## 3.1 Die Insel

### Prämisse

Die Spielwelt ist eine **einzelne Insel** ohne offiziellen Namen. Jede Fraktion nennt sie anders — das Küstenvolk sagt *Deutoland* (das noch zu deutende Land), das Siedlervolk sagt *Neugrund*, das Höhlenvolk hat gar keinen Namen dafür (die Insel ist für sie nur ein Knotenpunkt im Netz). Der Spieler erfährt nie den "richtigen" Namen. Es gibt keinen richtigen Namen.

Die Insel liegt isoliert. Kontakt zur Außenwelt existiert, aber ist selten und teuer — Schifffahrt über offenes Meer, kontrolliert durch das Küstenvolk. Wer auf die Insel kommt, bleibt meistens.

### Geographie — Fünf Zonen

Die Insel gliedert sich in fünf Klimazonen, die durch geologische Besonderheiten entstanden sind. Die Zonen sind nicht gleichmäßig verteilt — die Insel ist asymmetrisch, mit dem Vulkan im Nordosten und der Festung leicht südlich der Mitte.

```
               N
          ┌─────────────┐
         /  VULKANLAND    \
        / (Nordost, heiß,  \
       /   mineral-reich)    \
      ├──────────┬───────────┤
      │ HINTER-  │           │
      │  LAND    │ FESTUNG   │
      │(Zentral, │ (Hub,     │  ── KÜSTE (Ost/Süd,
      │ bewaldet,│  Plateau) │     Klippen, Häfen,
      │ Farmen)  │           │     Nebel)
      ├──────────┴───────────┤
       \   UNTERWELT         /
        \  (unter allem,    /
         \ Tunnelnetze)    /
          └──────────────┘
```

**Zone 1 — Die Küste (Ost- und Südseite)**
- **Klima**: Feucht, neblig, salzige Luft, kurze milde Sommer
- **Geologie**: Steilklippen aus dunklem Basalt, schmale Felsbuchten, vorgelagerte Schären. Gezeiten sind extrem — bei Ebbe werden Höhleneingänge sichtbar, bei Flut verschwinden ganze Strände
- **Vegetation**: Moos, Seegras, verkrüppelte Schwarzkiefern an den Klippen. Keine Wälder, nur Wind
- **Besonderheit**: Die Küste ist das Tor zur Außenwelt. Wer per Schiff kommt (wie der Spieler), landet hier. Die Ruinen am Ufer sind älter als jede lebende Erinnerung
- **Stimmung**: Grau-grün, horizontal, endloser Horizont. Caspar David Friedrich, aber ohne Romantik

**Zone 2 — Das Vulkanland (Nordosten)**
- **Klima**: Trocken-heiß im Sommer, Ascheschnee im Winter. Schwefeldämpfe steigen ständig auf
- **Geologie**: Aktiver Schildvulkan, flache Lavafelder, Obsidianbrüche. Heiße Quellen, Geysire, Fumarolen. Der Boden ist warm — an manchen Stellen kocht Regenwasser beim Auftreffen
- **Vegetation**: Thermophile Flechten, Knollenpilze an Dampfschloten, vereinzelte hitzeresistente Moose. Im Umkreis von 2 km um die Caldera: nichts
- **Besonderheit**: Mineralreichtum — Erze, Schwefel, Obsidian, und tief unter der Oberfläche: Relikte. Schwellstellen, an denen altes biologisches Material an die Oberfläche tritt
- **Stimmung**: Orange-schwarz, vertikal (Rauchsäulen, Felstürme), laut (Zischen, Grollen). Mordor ohne die Orks — funktional, nicht dekorativ böse

**Zone 3 — Das Hinterland (Zentrum und Westen)**
- **Klima**: Gemäßigt-kühl, vier Jahreszeiten. Regen häufig im Herbst, kalte Winter mit Bodenfrost
- **Geologie**: Hügeliges Waldland, Lehmböden, Bachläufe. Keine dramatische Geologie — das ist der "normale" Teil der Insel
- **Vegetation**: Mischwald (Buche, Eiche, Fichte), Wiesen, landwirtschaftliche Rodungsflächen. Die einzige Zone mit konventioneller Landwirtschaft
- **Besonderheit**: Wirkt friedlich, ist es auch — weitgehend. Das Hinterland ist Pufferzone zwischen Festung und Wildnis. Hier leben die meisten Menschen
- **Stimmung**: Braun-grün, sanft, vertraut. Der Schwarzwald, aber mit etwas Falschem unter der Oberfläche, das man nicht benennen kann

**Zone 4 — Die Festung und ihr Plateau (leicht südlich der Mitte)**
- Siehe Abschnitt 3.3

**Zone 5 — Die Unterwelt (unter allen Zonen)**
- **Klima**: Konstant kühl-feucht, kein Tageslicht, eigenes Ökosystem
- **Geologie**: Natürliche Kalksteinhöhlen, erweitert durch Grabung. Manche Tunnel sind offensichtlich nicht natürlichen Ursprungs — zu regelmäßig, zu glatt. Stalaktiten, unterirdische Seen, Phosphoreszenz
- **Vegetation**: Biolumineszente Pilzkulturen, Wurzelnetzwerke von der Oberfläche, blinde Fische in den Seen
- **Besonderheit**: Die Unterwelt verbindet ALLE Oberflächenzonen. Wer den Weg kennt, kann von der Küste zum Vulkan gelangen, ohne je Tageslicht zu sehen. Das Höhlenvolk nutzt dieses Netz seit Generationen
- **Stimmung**: Blau-violett (Biolumineszenz), eng, echoreich. Jeder Ton hallt. Claustrophobie wechselt sich ab mit Momenten gewaltiger unterirdischer Kavernen

### Klimazyklen (spielrelevant)

| Jahreszeit | Dauer (Ingame-Tage) | Effekt |
|------------|---------------------|--------|
| Frühling | 15 | Schneeschmelze, Tunnelüberflutung, neue Handelsrouten |
| Sommer | 20 | Vulkanaktivität steigt, Küstennebel lichtet sich, Reisezeit |
| Herbst | 15 | Erntezeit, Festungsmärkte, diplomatische Saison |
| Winter | 15 | Pässe zu, Küste stürmisch, Unterwelt wird Hauptverkehrsweg |

---

## 3.2 Die Fraktionen

### Designprinzip

Fraktionen in RELICS sind **ontologische Positionen** — jede beantwortet die Frage *"Was ist die Welt?"* fundamental anders. Es gibt keine gute und keine böse Fraktion. Jede hat eine innere Logik, eine Ästhetik, eine Moral — und jede hat blinde Flecken.

Der Spieler wählt nie explizit eine Fraktion. Der Spieler **wird** eine Fraktion durch Handeln: Wem er hilft, welche Aufträge er annimmt, wessen Sprache er übernimmt. Das passiert über den **Zugehörigkeitsindex** (siehe GDD Kapitel 5: Systeme).

Es gibt **fünf Fraktionen**, plus einen Nicht-Status (die Zerbrochenen) als Ausgangslage des Spielers.

---

### I. DAS HÖHLENVOLK — *"Alles hat seinen Preis."*

**Alternativname**: Die Fahrenden, die Tunnelhändler, *Marktkin* (Selbstbezeichnung)

**Rasse**: Tiermenschen — humanoid mit tierischen Merkmalen (Fell, Ohren, Nachtsicht, Geruchssinn). Keine einheitliche Tierart; die Varianz ist groß (fuchsartig, dachsartig, fledermausartig). Leicht alien, aber nicht monströs.

**Weltsicht**: Die Welt ist ein Marktplatz. Alles — Erz, Information, Loyalität, Stille — hat einen Preis. Wert ist nicht inhärent, Wert wird verhandelt. Wer den Preis kennt, hat Macht. Wer ihn vergisst, ist tot.

**Zone**: Die Unterwelt (Zone 5), mit Knotenpunkten unter jeder Oberflächenzone.

**Architektur-Signatur**:
- **Material**: Ausgehöhlter Kalkstein, Pilzholz (gehärtete Pilzstrukturen), gewebte Wurzelfasern
- **Form**: Organisch-asymmetrisch. Keine rechten Winkel. Tunnel optimiert auf Flucht und Durchfluss, nicht auf Repräsentation. Die Form folgt dem Weg, nicht dem Raum
- **Kennzeichen**: Unterirdische Basare mit Biolumineszenz-Beleuchtung. Ware hängt von der Decke. Wände sind Lagerfläche. Jeder Basar hat mindestens drei Fluchttunnel. Kein Eingang ist offensichtlich
- **Vera-Notiz**: Seidenstraßen-Ästhetik unter der Erde. Schmuck statt Rüstung. Stoffbahnen in den Tunneln als Wegmarkierung. Nomaden-Eleganz, nicht Höhlenmensch

**Wirtschaft**:
- **Funktion**: Distribution. Das Höhlenvolk produziert fast nichts — es BEWEGT alles. Erz vom Vulkan zur Küste. Kräuter vom Hinterland zum Innenvolk. Information überallhin
- **Währung**: Vertrauen und Schulden. Physisches Geld existiert (Festungsprägung), aber das Höhlenvolk bevorzugt Gegenleistungen. "Ich schulde dir" ist wertvoller als Gold
- **Monopol**: Tunnelnetz-Wissen. Kein Außenstehender kennt den vollständigen Weg. Das ist ihre Lebensversicherung
- **Schmuggel**: Die Grenze zwischen Handel und Schmuggel ist fließend. Das Höhlenvolk sieht darin keinen moralischen Unterschied — nur einen preislichen

**Kultur**:
- **Sozialstruktur**: Karawanen-Clans, nicht Dörfer. Ein Clan = eine Handelsroute. Status kommt durch das Netzwerk, nicht durch Besitz
- **Geburtsritual**: Neugeborene bekommen keinen festen Namen. Der Name kommt mit dem ersten abgeschlossenen Geschäft
- **Totenkultur**: Verstorbene werden an den Tunnel-Kreuzungen begraben. Ihre Knochen werden zu Wegmarkern — die Toten zeigen den Weg
- **Tabu**: Eine Schuld nicht begleichen. Schlimmer als Mord
- **Sprache**: Sprichwort-reich, indirekt, metaphorisch. "Man sagt in meiner Karawane..." Humor als Verhandlungstaktik. Leises Sprechen — in Tunneln trägt der Schall weit

**Beziehung zur Festung**: Ambivalent. Die Festung ist der größte Markt der Insel — gutes Geschäft. Aber die Festung will Kontrolle, und das Höhlenvolk hasst Kontrolle. Sie handeln dort, aber sie wohnen dort nicht. Die Festungswache toleriert sie, weil sie unverzichtbar sind, und misstraut ihnen, weil sie unkontrollierbar sind.

**Germanische Mythologie**: Die Zwerge der Edda — Handwerker und Trickster, unterirdisch, reich, unheimlich. Aber dekonstruiert: Keine Schmiede, sondern Händler. Nicht die, die machen, sondern die, die bewegen. Andvari mit seinem Gold, Brokk mit seinen Deals — die Edda-Zwerge waren immer auch Geschäftsleute.

---

### II. DAS KÜSTENVOLK — *"Die Welt wartet auf Deutung."*

**Alternativname**: Die Deuter, die Chronisten, *Strandgeborne* (Selbstbezeichnung)

**Rasse**: Elfisch-inspiriert — hochgewachsen, blass, langlebig (nicht unsterblich, aber 150+ Jahre möglich). Dünnes Haar, lichtempfindliche Augen (deshalb der Nebel der Küste als Lebensraum). Kein Tolkien-Adel — eher: abgenutzt, akademisch, leicht entrückt.

**Weltsicht**: Die Welt ist ein Text, der gelesen werden will. Jedes Relikt, jede Ruine, jede Gesteinsschicht ist ein Zeichen. Die Vergangenheit ist realer als die Gegenwart — weil die Gegenwart nur eine flüchtige Interpretation der Vergangenheit ist.

**Zone**: Die Küste (Zone 1), konzentriert um Häfen, Leuchtturm-Akademien und Ruinen.

**Architektur-Signatur**:
- **Material**: Treibholz, Seetang-Beton (ein Gemisch aus Seetang, Kalk und Muschelsplitt — erstaunlich haltbar), Basalt
- **Form**: Vertikal, schmal, Flickwerk. Gebäude wachsen nach oben, nicht in die Breite. Jede Generation baut eine Etage drauf, in leicht anderem Stil. Man SIEHT die Geschichte des Gebäudes an seiner Fassade
- **Kennzeichen**: Bibliotheken in Leuchtturm-Ruinen. Chronik-Tafeln an jeder Hauswand (wer hier wohnte, wann, warum). Fernrohre auf jedem Dach — das Küstenvolk schaut nach draußen, immer
- **Vera-Notiz**: Gaudí trifft Fischerdorf. Organisch gewachsen, asymmetrisch, nie fertig. Farbpalette: Grau, Meeresgrün, verblasstes Blau. Kein Prunk, aber eine stille Schönheit im Verfall

**Wirtschaft**:
- **Funktion**: Seehandel und Wissensmonopol. Jedes Schiff von und zur Insel legt an ihren Häfen an. Zölle finanzieren die Akademien
- **Export**: Deutungen. Das klingt abstrakt, ist es aber nicht — das Küstenvolk kartographiert, übersetzt, archiviert. Wer eine Ruine datieren will, braucht einen Küstendeuter. Wer ein Relikt identifizieren will, ebenso
- **Import**: Alles, was die Außenwelt hat und die Insel nicht — Nachrichten, fremde Bücher, seltene Materialien
- **Schwäche**: Produzieren fast keine Nahrung. Abhängig vom Hinterland und vom Höhlenvolk-Netzwerk

**Kultur**:
- **Sozialstruktur**: Akademien als Machtbasis. Jede Hafenstadt hat eine Akademie; die Akademie-Leitung ist de facto die Stadtregierung
- **Geburtsritual**: Neugeborene werden mit der aktuellen Gezeitenposition registriert. Nicht Datum, nicht Uhrzeit — Gezeitenstand. Die See misst die Zeit, nicht die Sonne
- **Totenkultur**: Seebestattung. Die Toten gehören dem Wasser, nicht dem Land
- **Tabu**: Ein Dokument fälschen. Schlimmer noch: ein Dokument vernichten
- **Sprache**: Präzise, leicht archaisch, zitat-schwer. "In der Vierten Chronik steht..." Rhetorische Fragen als Denkwerkzeug. Lange Sätze, Nebensätze, die sich selbst kommentieren

**Beziehung zur Festung**: Distanziert-kooperativ. Das Küstenvolk sieht die Festung als interessantes Studienobjekt — wer hat sie gebaut? warum? welche Schichten? — aber nicht als politische Heimat. Sie zahlen Tribut, aber sie fühlen sich nicht zugehörig. Ihre wahre Heimat ist der Horizont.

**Germanische Mythologie**: Die Nornen, die am Brunnen Urds sitzen und das Schicksal einritzen. Das Küstenvolk liest, was geschrieben wurde — aber wer hat geschrieben? Die Runen-Tradition der Edda: Odin opfert sein Auge für Wissen. Das Küstenvolk opfert Gegenwart für Vergangenheit. Der Preis des Wissens.

---

### III. DAS SIEDLERVOLK — *"Die Welt gehört dem, der sie nimmt."*

**Alternativname**: Die Nehmer, die Gründer, *Festungskinder* (Selbstbezeichnung)

**Rasse**: Menschen. Keine übernatürlichen Merkmale. Vielfältig in Erscheinung (verschiedene Ethnien — die Siedler kamen über Generationen von überall her). Was sie verbindet, ist nicht Blut, sondern Ideologie.

**Weltsicht**: Die Welt ist Ressource. Was da ist, darf genutzt werden — muss genutzt werden. Fortschritt legitimiert sich selbst. Stillstand ist Rückschritt. Die Vergangenheit ist Material, nicht Heiligtum.

**Zone**: Die Festung und das Hinterland (Zonen 3 und 4). Die größte territoriale Ausdehnung aller Fraktionen.

**Architektur-Signatur**:
- **Material**: Stein (gebrochen, nicht gewachsen), Holz, Ziegel. Später: Knochenmetall-Legierungen aus Vulkan-Importen
- **Form**: Blockhaft, rechtwinklig, symmetrisch. Mauern, Türme, Straßenraster. Funktion vor Form. Jedes Gebäude sagt: "Hier ist jemand, der bleibt"
- **Kennzeichen**: Stadtmauern (auch um Dörfer), gepflasterte Straßen, Markthallen, Kasernen. Schilder an jeder Ecke — Straßennamen, Verordnungen, Preislisten. Die Siedler beschriften die Welt
- **Vera-Notiz**: Hochmittelalterlich-clean. Rothenburg ob der Tauber, aber funktional statt pittoresk. Farbpalette: Ocker, Steingrau, Fahnenrot. Sauber — verdächtig sauber

**Wirtschaft**:
- **Funktion**: Landwirtschaft, Handwerk, Verwaltung. Die Siedler produzieren Nahrung, verarbeiten Rohstoffe, organisieren Märkte
- **Stärke**: Selbstversorgung und Bevölkerungsgröße. Es gibt schlicht mehr Siedler als alle anderen zusammen
- **Schwäche**: Brauchen Rohstoffe von außerhalb — Erz vom Vulkan, Wissen von der Küste, Biotech-Produkte vom Innenvolk. Ohne Handelspartner stagnieren sie
- **Machtmittel**: Die Festung. Wer die Festung kontrolliert, kontrolliert den zentralen Markt, die Gerichtsbarkeit und die Straßen des Hinterlandes

**Kultur**:
- **Sozialstruktur**: Gilden und Stadträte. Kein König, kein Adel — aber eine de-facto-Oligarchie der mächtigsten Gildenmeister. Meritokratie als Ideologie, Nepotismus als Praxis
- **Geburtsritual**: Registrierung im Stadtbuch. Name, Datum, Eltern, Gilde-Zugehörigkeit des Vaters/der Mutter. Existenz beginnt mit Bürokratie
- **Totenkultur**: Bestattung in Familiengräbern innerhalb der Stadtmauern. Land ist wertvoll — Grabplätze sind Statussymbole. Wer kein Grab leisten kann, kommt auf den Ascheacker vor der Mauer
- **Tabu**: Vertragsbruch. Die Siedlerkultur basiert auf schriftlichen Vereinbarungen. Mündliche Versprechen zählen nicht
- **Sprache**: Direkt, sachlich, bürokratisch. Dekrete statt Geschichten. "Laut Stadtordnung §14..." Nicht humorlos, aber ihr Humor ist trocken und auf Effizienz getrimmt. Keine Metaphern — Metaphern verschwenden Zeit

**Beziehung zur Festung**: DIE Festung IST das Siedlervolk — oder das behaupten sie. Sie haben die Festung nicht gebaut (niemand weiß, wer das tat), aber sie haben sie besetzt, ausgebaut und zum Zentrum der Insel gemacht. Die Festung legitimiert ihren Anspruch auf Führung.

**Germanische Mythologie**: Die Asen — Götter der Ordnung, des Gesetzes, der Zivilisation. Thor mit seinem Hammer ist ein Baumeister so viel wie ein Krieger. Asgards Mauern, von einem Riesen gebaut — die Siedler bauen auf Fundamenten, die sie nicht verstehen, und nennen sie trotzdem ihr Eigen. Odin als Allvater: der Anspruch, über alle zu herrschen, weil man sich als Erster hingesetzt hat.

---

### IV. DAS INNENVOLK — *"Der Körper ist die letzte Grenze."*

**Alternativname**: Die Destillateure, die Körperkundigen, *Nervengeher* (Selbstbezeichnung)

> **Design-Entscheidung (Emre + Nami, Tag 3)**:
> Emres "Destillateure" und Namis "Innenvolk" sind **dieselbe Fraktion**, betrachtet aus zwei Winkeln. Emre beschreibt die ökologische Nische (Biotech-Produktion, Substanzen, Gewächshäuser), Nami die philosophische Position (der Körper als Forschungsgegenstand, Nervensystem-Leveling als deren Technologie). Das Ergebnis: **Innenvolk** als Fraktionsname, **Destillateure** als Berufsbezeichnung innerhalb der Fraktion — so wie "Schmiede" kein Volksname ist, aber jeden beschreibt der in einer Esse arbeitet.

**Rasse**: Rassenübergreifend. Jede Rasse hat Innenvolk-Mitglieder — das ist keine biologische Gruppe, sondern eine ideologische. Was sie verbindet, ist die Praxis: Selbstexperiment.

**Weltsicht**: Die Wahrheit liegt nicht in der Welt — sie liegt im Körper. Die Insel, die Ruinen, die Relikte — alles Äußerlichkeiten. Was zählt, ist das Nervensystem, das Blut, die Chemie. Der Körper erinnert sich an Dinge, die der Geist vergessen hat. Wer sich selbst erforscht, erforscht die Grundlagen der Welt.

**Zone**: Kein festes Territorium — ein **loses Netzwerk**, verteilt über alle Zonen. Schwerpunkte: Vulkanland (Rohstoffe für Destillation), Unterwelt (verborgene Labore), Festung (Absatzmärkte). Überall dort, wo man ungestört arbeiten kann.

**Architektur-Signatur**:
- **Material**: Knochen, Haut (tierisch, gegerbt), Chitin, Keratin, Biolumineszenz-Pilze als Lichtquelle. Organische Materialien, die atmen und riechen
- **Form**: Gewächshäuser aus Rippenbögen. Destillationsapparate, die aussehen wie Organe. Labore, die aussehen wie das Innere eines Tieres. Nichts ist rechtwinklig; alles ist feucht
- **Kennzeichen**: Geruch. Man riecht ein Innenvolk-Labor bevor man es sieht — Schwefel, Kräuter, etwas Süßlich-Fauliges. Schläuche statt Rohre. Membranen statt Türen
- **Vera-Notiz**: Giger trifft mittelalterliche Apotheke. Farbpalette: Bernstein, Fleischrot, Knochengelb, Violett (Biolumineszenz). Schön auf eine verstörende Weise. Fashion: High Fashion Mittelalter — Innenvolk-Mitglieder kleiden sich exzessiv, weil Kleidung auch Experiment ist (Haut-kontakt-Stoffe, imprägnierte Gewebe)

**Wirtschaft**:
- **Funktion**: Produktion von Biotech-Substanzen. Alles, was der Körper braucht oder fürchtet, stellt das Innenvolk her
- **Produkte**:
  - **Verstärker** (*Sporen*): Temporäre Leistungssteigerung — Ausdauer, Reflexe, Nachtsicht. Legaler Markt an der Festung
  - **Gifte** (*Tinkturen*): Waffen, Fallen, Assassinen-Werkzeug. Illegaler Markt über das Höhlenvolk
  - **Drogen** (*Tiefstoffe*): Bewusstseinserweiternde Substanzen. Manche ermöglichen Zugang zu Nervensystem-Schichten, die sonst verschlossen sind. Suchtgefahr. Rechtliche Grauzone
  - **Heilmittel** (*Balsame*): Medizin. Die beste auf der Insel. Teuer
- **Monopol**: Niemand sonst versteht die biochemischen Prozesse. Rezepturen werden mündlich weitergegeben — nichts Schriftliches (zum Ärger des Küstenvolks)
- **Abhängigkeit**: Brauchen Rohstoffe aus dem Vulkanland (Schwefel, Mineralien, thermophile Pilze) und aus der Unterwelt (seltene Pilzarten, Höhlenwasser)

**Kultur**:
- **Sozialstruktur**: Meister-Schüler-Beziehungen, keine formale Hierarchie. Ein Destillateur wird nicht gewählt oder ernannt — er wird anerkannt, wenn seine Substanzen wirken
- **Initiation**: Selbstversuch. Wer Innenvolk werden will, muss eine selbst hergestellte Substanz an sich selbst testen. Manche bestehen. Manche nicht
- **Totenkultur**: Dissektion. Die Toten werden seziert, ihre Organe studiert, ihre Chemie analysiert. Der Tod ist die letzte Datenerhebung. Für Außenstehende barbarisch — für das Innenvolk der höchste Respekt
- **Tabu**: Eine Substanz verkaufen, deren Wirkung man nicht am eigenen Körper getestet hat
- **Sprache**: Klinisch, fasziniert, leicht verstörend. Beschreiben Schmerz als Daten. Reden über Gift wie Sommeliers über Wein. "Eine exquisite Dosis — spürst du, wie dein Sehnerv reagiert?" Fachvokabular, das anderen kryptisch erscheint

**Beziehung zur Festung**: Parasitär-symbiotisch. Die Festung braucht Heilmittel und Verstärker (die Stadtwache kauft in Massen). Das Innenvolk braucht Absatzmärkte und Schutz vor Verfolgung. Man duldet sich. Man vertraut sich nicht. Die Innenvolk-Labore innerhalb der Festungsmauern sind offiziell "Apotheken." Alle wissen, dass das nicht stimmt.

**Germanische Mythologie**: Die Völva — die Seherin, die durch Trance und Substanzen Zugang zu verborgenem Wissen findet. Odins Selbstopfer am Weltenbaum: neun Tage hängend, durchbohrt, zwischen Leben und Tod — um die Runen zu empfangen. Das Innenvolk hängt sich nicht an Bäume, aber das Prinzip ist dasselbe: Wissen durch Selbstverletzung. Auch Loki, der Gestaltwandler, der seinen eigenen Körper verändert. Der Körper als Werkzeug, nicht als Tempel.

---

### V. DIE ZERBROCHENEN — *"Ich bin, was übrig bleibt."*

**Alternativname**: Keine. Sie haben keinen Kollektivnamen, weil sie kein Kollektiv sind.

**Rasse**: Alle. Die Zerbrochenen sind keine Ethnie, keine Kultur, keine Organisation. Sie sind ein **Zustand**.

**Weltsicht**: Es gibt keine richtige Weltsicht. Oder: es gab eine, aber sie ist verloren. Die Zerbrochenen stehen zwischen allen Positionen — Exilierte, Überläufer, Entwurzelte, Fremde.

**Zone**: Überall und nirgends. Auf den Straßen, in verlassenen Häusern, an den Rändern jeder Siedlung. Am sichtbarsten: in der Festung, wo die Entwurzelten sich sammeln.

**Architektur-Signatur**: Keine eigene. Zerbrochene besetzen, was andere verlassen haben. Improvisierte Lager, umfunktionierte Ruinen, gestapelte Kisten als Wände. Die Ästhetik der Notlösung.

**Wirtschaft**: Gelegenheitsarbeit, Betteln, Kleinkriminalität. Manche Zerbrochene sind hochqualifiziert (ehemalige Akademiker des Küstenvolks, ehemalige Destillateure) — aber ohne Netzwerk ist Qualifikation wertlos.

**Kultur**:
- **Sozialstruktur**: Keine. Temporäre Zweckbündnisse, die zerbrechen, sobald der Zweck erfüllt ist
- **Sprache**: Fragmentarisch, persönlich, ohne Formel. Keine Sprichwörter, keine Zitate, keine Rhetorik. "Ich war mal..." und "Ich weiß nicht mehr..."
- **Companions**: Kommen überproportional aus dieser Gruppe. Die interessantesten Geschichten der Insel gehören denen, die alles verloren haben

**Beziehung zur Festung**: Die Festung toleriert Zerbrochene als billige Arbeitskraft und ignoriert sie als politische Größe. Es gibt ein Armenviertel im Außenring — *die Scherben* — das offiziell nicht existiert.

**Spieler-Relevanz**: **Der Spielercharakter startet als Zerbrochener.** Ein Fremder, der per Schiff auf die Insel kommt — ohne Zugehörigkeit, ohne Geschichte, ohne Weltsicht. Der gesamte Spielverlauf ist der Prozess, von Zerbrochen zu Zugehörig zu werden. Oder eben nicht. Manche Spieler werden bewusst zerbrochen bleiben.

**Germanische Mythologie**: Die Riesen nach Ragnarök. Die Jötunn, die zwischen den Welten stehen. Aber auch: der Wanderer. Odin selbst, in Verkleidung, der sich unter die Sterblichen mischt. Der Spieler als Unbekannter, der mehr sein könnte als er scheint — oder auch nicht. Die Edda ist voller Figuren, die erst herausfinden müssen, wer sie sind.

---

## 3.3 Die Festung

### Was sie ist

Die Festung ist der **zentrale Hub** der Spielwelt — der Ort, an den der Spieler immer zurückkehrt. Geographisch liegt sie auf einem Plateau leicht südlich der Inselmitte, mit Sichtlinien zu allen Zonen. Sie ist groß genug für eine Stadt, alt genug für Geheimnisse und umkämpft genug für Politik.

### Wer hat sie gebaut?

Niemand weiß es. Das ist kein Plothole — das ist der Plot.

Die Festung ist älter als jede lebende Erinnerung, älter als das Küstenvolk-Archiv, älter als die tiefsten Tunnelmarkierungen des Höhlenvolks. Die Bauweise passt zu keiner bekannten Kultur auf der Insel:
- Zu groß für die Siedler (die sie nur besetzt und ausgebaut haben)
- Zu geometrisch für das Höhlenvolk (das organisch baut)
- Zu alt für das Küstenvolk (das erst später kam)
- Zu materiell für das Innenvolk (das kein Interesse an Stein hat)

Die Festung ist aus einem Material gebaut, das nirgendwo sonst auf der Insel vorkommt — ein dunkler, fast schwarzer Stein, glatt wie Obsidian, aber deutlich härter. Das Küstenvolk nennt ihn *Grundstein*. Das Innenvolk hat ihn analysiert und Spuren organischer Verbindungen gefunden. Niemand spricht gerne darüber, was das bedeuten könnte.

### Struktur

```
Äußerer Ring — Märkte, Handwerkerviertel, Scherben (Armenviertel)
│
├── Mittlerer Ring — Gilden, Kasernen, Akademie-Außenstelle, Apotheken (Innenvolk-Labore)
│
├── Innerer Ring — Ratsgebäude, Archive, Wohnviertel der Gildenmeister
│
└── Kern — Verschlossen. Niemand darf hinein. Bewacht, aber nicht von der Stadtwache.
    Was ist drin? Wer bewacht es? Das ist eine der zentralen Fragen der Hauptquest.
```

### Politische Struktur

Die Festung wird regiert durch den **Rat der Gilden** — ein Gremium aus den Meistern der wichtigsten Handwerks- und Handelsgilden. De facto Siedlervolk-dominiert, aber mit formalen Sitzen für:
- Einen Küstenvolk-Gesandten (Beobachterstatus, kein Stimmrecht)
- Einen Höhlenvolk-Marktmeister (Stimmrecht in Handelsfragen, sonst nicht)
- Keinen Innenvolk-Vertreter (offiziell existiert das Innenvolk innerhalb der Festungsmauern nicht)
- Keine Zerbrochenen-Vertretung (selbstverständlich)

### Funktion im Spiel

| Gameplay-Funktion | Umsetzung |
|---|---|
| Questgeber-Hub | Rat der Gilden, Marktplatz, Akademie-Außenstelle, Scherben |
| Handels-Hub | Zentraler Markt (Äußerer Ring) + Schwarzmarkt (Unterwelt-Zugang) |
| Crafting-Hub | Handwerkerviertel (Schmieden, Gerbereien, Destillations-"Apotheken") |
| Narrativer Hub | Kern-Mysterium, Gildenrat-Politik, Fraktions-Konflikte |
| Ruhezone | Gasthäuser, eigene Unterkunft (freischaltbar), Akademie-Bibliothek |

---

## 3.4 Biotech-Ökologie

### Prinzip

In RELICS gibt es keinen Steampunk, keine Dampfmaschinen, keine Zahnräder. Die Technologie der Insel ist **biologisch** — gewachsen, destilliert, fermentiert, extrahiert. Das ist kein Flavor; das ist ein Designprinzip, das jede Textur, jedes Item, jede Werkbank betrifft.

### Woher kommen die Substanzen?

Die Insel hat eine einzigartige biochemische Grundlage. Der Vulkan im Nordosten produziert nicht nur Hitze und Mineralien, sondern auch **Schwellstellen** — Orte, an denen organisches Material aus der Tiefe an die Oberfläche tritt. Dieses Material ist alt. Sehr alt. Was genau es ist, darüber streiten sich die Fraktionen (natürlich).

**Die Produktionskette**:

```
Schwellstellen (Vulkan, tief)
    │
    ▼
Rohmaterial — Mineralien, thermophile Pilze, Schwellflüssigkeit
    │
    ├──→ Vulkansiedlungen: Erz-Verhüttung, Obsidian-Werkzeuge
    │
    ├──→ Höhlenvolk-Distribution: Transport in alle Zonen
    │
    ▼
Innenvolk-Labore (verteilt)
    │
    ├──→ VERSTÄRKER (Sporen): Temporäre Buffs
    │    Beispiel: "Wolfslunge" — +30% Ausdauer, 4h, leichte Übelkeit
    │
    ├──→ GIFTE (Tinkturen): Waffen-Coating, Fallen
    │    Beispiel: "Stille Zunge" — Paralyse, 30 Sek., beschaffbar beim Höhlenvolk
    │
    ├──→ DROGEN (Tiefstoffe): Bewusstseinsveränderung, Nervensystem-Zugang
    │    Beispiel: "Tiefblick" — zeigt das eigene Nervensystem (Leveling-UI!), 1h, Suchtrisiko
    │
    └──→ HEILMITTEL (Balsame): Wundheilung, Entgiftung, Regeneration
         Beispiel: "Fleischwort" — heilt 50% HP über 30 Sek., teuer, schmeckt bitter
```

### Nervensystem-Leveling und Biotech

Das **Nervensystem-Leveling** (siehe GDD Kapitel 5) ist nicht nur eine UI-Mechanik — es ist im Worldbuilding verankert:

- Das Innenvolk hat entdeckt, dass der Körper "Schichten" hat, die normalerweise unzugänglich sind
- Durch gezielte Substanzen (Tiefstoffe) können diese Schichten sichtbar und trainierbar gemacht werden
- Was der Spieler als **Leveling-UI** sieht (halbtransparente Nervensystem-Sicht, drei Bahnen: Kardio, Muskel-Skelett, Lymph), ist IN DER SPIELWELT eine Innenvolk-Technik
- NPCs anderer Fraktionen reagieren unterschiedlich darauf:
  - Siedlervolk: "Nützlich. Was kostet es?"
  - Küstenvolk: "Faszinierend. Was bedeutet es?"
  - Höhlenvolk: "Tiefstoffe? Kann ich dir besorgen. Hat seinen Preis."
  - Zerbrochene: "Ich habe das mal gemacht. Ich kann mich nicht erinnern warum."

### Sucht und Risiko

Biotech-Substanzen sind nicht kostenlos. Das Lymphsystem im Leveling-UI trackt die **Belastung**:

| Belastungsstufe | Lymph-Zustand | Effekt |
|---|---|---|
| 0 — Sauber | Klar, ruhig | Keine Debuffs |
| 1 — Angereichert | Leicht verfärbt | +5% Substanz-Wirkung, -5% Regeneration |
| 2 — Belastet | Sichtbare Schwellung | Abhängigkeit beginnt: ohne Nachschub Debuffs |
| 3 — Vergiftet | Dunkel, pulsierend | Permanente Stat-Reduktion ohne Innenvolk-Behandlung |
| 4 — Zerbrochen | Schwarz, rissig | Fraktionswechsel erzwungen: Du wirst Zerbrochener |

**Designprinzip**: Biotech ist mächtig, aber es hat Konsequenzen. Das ist kein Moralsystem — es ist Biologie. Der Körper erinnert sich an alles, was man ihm antut.

---

## 3.5 Germanische Mythologie — Wie sie in der Welt lebt

### Designprinzip

Germanische Mythologie in RELICS ist **kein Setting-Dressing**. Die Götter existieren nicht — oder: es gibt keine Beweise dafür. Was existiert, sind die Geschichten, die die Inselbewohner sich erzählen. Mythen sind Erklärungsversuche für Dinge, die biologisch oder geologisch erklärbar WÄREN — wenn jemand die richtige Erklärung hätte. Niemand hat sie.

Das ist **Low Fantasy, germanisch, dekonstruiert**: Die Mythologie wird ernst genommen als kulturelle Kraft, ohne dass sie buchstäblich wahr sein muss.

### Mythologische Schichten in der Spielwelt

**Schicht 1 — Ymir und die Schöpfung**
- Die Insel selbst wird von manchen (besonders dem Küstenvolk) als Fragment eines Urwesens gedeutet — eines Riesen, aus dessen Körper die Welt entstand
- Die Schwellstellen? "Ymirs Adern." Die Vulkanaktivität? "Ymirs letzter Atemzug." Das Grundstein-Material der Festung? "Ymirs Knochen."
- Das Siedlervolk nennt das Aberglaube. Das Innenvolk findet es interessant, weil die biochemische Zusammensetzung der Schwellstellen tatsächlich organischen Ursprungs zu sein scheint
- **Design**: Nie aufgelöst. Der Spieler findet Hinweise in beide Richtungen. Die Wahrheit bleibt offen

**Schicht 2 — Die Drei Nornen und das Schicksal**
- Das Küstenvolk verehrt drei Schwestern-Figuren — die Lesenden, die Spinnenden, die Schneidenden — die angeblich in der ältesten Ruine der Insel leben. Oder lebten. Oder nie existiert haben
- Spielrelevant: Drei Schlüssel-NPCs an der Küste, die den Spieler in die Lore einführen. Sie widersprechen sich. Absichtlich
- Die Nornen als Metapher für: Die Vergangenheit (was gelesen wird), die Gegenwart (was gesponnen wird) und die Zukunft (was abgeschnitten wird)

**Schicht 3 — Odin als Wanderer**
- Der Spielercharakter als Odin-Echo: Ein Fremder, der auf die Insel kommt, alles beobachtet, Wissen sammelt — und einen Preis dafür zahlt
- Parallele zum Selbstopfer: Das Nervensystem-Leveling als Odins Aufhängung an Yggdrasil — Wissen durch Selbstverletzung
- Der einäugige Wanderer als wiederkehrendes Motiv in NPC-Dialogen: "Ein Auge für die Wahrheit. Was gibst du?"

**Schicht 4 — Ragnarök als Ticking Clock**
- Ragnarök ist kein kosmisches Ereignis, sondern eine **biologische Eskalation**: Die Schwellstellen werden aktiver. Der Vulkan unruhiger. Etwas unter der Insel wacht auf — oder stirbt endgültig
- Kein Weltuntergang durch Götterkrieg, sondern durch tektonisch-biochemische Kettenreaktion
- Der Spieler erlebt die Anzeichen im Spielverlauf: Erst subtil (NPCs reden über seltsame Erdbeben), dann deutlich (Schwellstellen brechen in besiedelten Gebieten auf), dann drängend (die Festung selbst zeigt Risse im Grundstein)
- **Die zentrale Frage der Hauptquest**: Kann Ragnarök aufgehalten werden? Soll es? Was, wenn das Ende der Insel auch ein Anfang ist?

**Schicht 5 — Loki und die Grenzüberschreitung**
- Loki ist kein Charakter, sondern ein **Prinzip**: Die Grenzüberschreitung, die Verwandlung, der Betrug, der auch Wahrheit ist
- Das Innenvolk verkörpert Loki am stärksten — ihre Selbstexperimente sind Grenzüberschreitungen. Aber auch das Höhlenvolk (Trickster-Handel) und die Zerbrochenen (unfreiwillige Verwandlung)
- Spieler, die sich dem Innenvolk nähern, begegnen Loki-Motiven: Veränderung, Verlust der Form, die Frage ob Identität an den Körper gebunden ist

### Mythos vs. Realität — Tabelle für Level Designer

| Mythologisches Motiv | In-World-Deutung (gläubig) | In-World-Deutung (rational) | Design-Einsatz |
|---|---|---|---|
| Ymir | Insel ist Riesenkörper | Geologische Formation | Environmental Storytelling, Schwellstellen-Design |
| Nornen | Drei Schicksalsfrauen in der Ruine | Drei Akademikerinnen, die Geschichte kontrollieren | Quest-NPCs an der Küste |
| Odin | Der einäugige Wanderer kehrt zurück | Fremder mit zu vielen Fragen | Spielercharakter-Echo |
| Ragnarök | Die Welt endet im Feuer | Vulkanische Aktivität eskaliert | Hauptquest Ticking Clock |
| Loki | Gott der Verwandlung lebt in uns | Biotech verändert den Körper | Innenvolk-Quests, Nervensystem-Leveling |
| Midgardschlange | Etwas lebt unter der Insel | Tektonische Verwerfungen | Kern-Mysterium der Festung |

---

## 3.6 Fraktionsbeziehungen — Übersicht

```
               KÜSTENVOLK
              /    |     \
       Respekt  Misstrauen  Neugier
        /          |          \
HÖHLENVOLK ──Handel── SIEDLERVOLK
        \          |          /
      Versorgung  Verbot   Abhängigkeit
        \          |          /
              INNENVOLK
                 |
            Verachtung/Mitleid
                 |
            ZERBROCHENE
```

| Fraktion A | Fraktion B | Beziehung | Kern des Konflikts |
|---|---|---|---|
| Höhlenvolk | Siedlervolk | Zweckbündnis | Kontrolle vs. Freiheit. Siedler wollen regulieren, Höhlenvolk will handeln |
| Höhlenvolk | Küstenvolk | Respekt | Wissen gegen Waren. Funktioniert meistens, solange keiner betrügt |
| Höhlenvolk | Innenvolk | Lieferkette | Das Höhlenvolk transportiert, was das Innenvolk braucht. Beide profitieren. Beide misstrauen |
| Küstenvolk | Siedlervolk | Spannung | Vergangenheit vs. Fortschritt. Küstenvolk will konservieren, Siedler wollen nutzen |
| Küstenvolk | Innenvolk | Faszination | Beide forschen — einer in Büchern, der andere in Körpern. Begegnung auf Augenhöhe, aber fundamental verschiedene Methoden |
| Siedlervolk | Innenvolk | Heuchelei | Offiziell verboten, inoffiziell Hauptkunde. Die Festung braucht Balsame und Sporen, aber verbietet Tiefstoffe |
| Alle | Zerbrochene | Ignoranz | Zerbrochene existieren nicht. Offiziell |

---

## Anhang: Vertical-Slice-Reduktion

Für den Vertical Slice (Hauptquest + 2 Nebenquests in einer Region) wird **die Festung und ihr unmittelbares Umland** als Startregion vorgeschlagen:

**Aktive Fraktionen im Slice**: Siedlervolk (dominant), Höhlenvolk (Händler-Karawane am Markt), Küstenvolk (Akademie-Außenstelle)

**Angedeutete Fraktionen**: Innenvolk (eine "Apotheke" im Mittleren Ring, ein NPC, ein Hinweis auf die Unterwelt), Zerbrochene (die Scherben als begehbares Armenviertel)

**Hauptquest-Hook**: Der Spieler kommt als Fremder zur Festung. Der Kern ist verschlossen. Jemand will ihn öffnen. Jemand will ihn versiegelt lassen. Der Spieler muss entscheiden, wem er vertraut — und was er dafür aufgibt.

---

*Dieses Kapitel wurde im Besprechungsraum erarbeitet, Tag 3 Vormittag, mit drei Tassen Tee (Emre) und zwei Flat Whites (Nami). Der Kompromiss Innenvolk/Destillateure wurde um 10:47 erreicht, nach 23 Minuten produktivem Streit. Die Festungs-Frage ("Wer hat gebaut?") ist absichtlich offen — wir haben beschlossen, dass sie es bleiben soll.*

*— E. Yilmaz & N. Okafor*
