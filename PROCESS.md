# Process logbook

## Week 22

#### May 30
- proposal deadline
- gitrepo aangemaakt

#### May 31
- maximale grootte van de openlist aangepast van 200 naar 300, lijkt bug te voorkomen bij het remaken (hill climbing) van de path

#### June 1
Werkafspraken week #1

* Stap 1: werkende applicatie maken die circuit boards + netlists als input neemt, en als output een oplossing geeft OF "er is geen oplossing binnen x tijd gevonden"(plus de benodigde rekentijd (stappen en kloktijd)).
* Stap 2: je applicatie *visualiseert* de oplossing
* Stap 3: we gaan je applicatie testen met een testset van een circuit board met een aantal random gegenereerde netlists met voorzichtig oplopende aantallen nets in de list.
* Stap 4: je synct met Martijn en Wouter of het project voldoet aan het programmeerproject.

visualisatie verbeteren

#### June 2
- werken aan GUI met gebruik van Tkinter Canvas widget
<img src="https://github.com/danielstaal/project/blob/master/doc/gui.PNG?raw=true" width="320">
- proberen de visualisatie in Tkinter te embedden
- wellicht beter alleen een grafiek in tkinter te embedden en de figuur los te houden

#### June 3
- verder aan applicatie gewerkt:
<img src="https://github.com/danielstaal/project/blob/master/doc/gui2.PNG?raw=true" width="480">

## Week 23
#### June 6
<img src="https://github.com/danielstaal/project/blob/master/doc/gui3.PNG?raw=true" width="480">
- code design verbeteren
- nu mogelijk om random netlists te genereren
- kijken waar het pad meestal geblokkeerd wordt

- fout ontdekt: er wordt nu gecheckt hoe groot de openList is om te kijken of de blokkade aan de andere kant zit. Dit moet de closedList zijn.
 - maar: bij welke grootte moet aan de andere kant een pad verwijderd worden?

- met regelmaat ook niet direct bij de gate geblokkeerd

- netlist 3 opgelost!:
<img src="https://github.com/danielstaal/project/blob/master/doc/sol50.PNG?raw=true" width="320">

tijd: 195.9 sec
totale lengte: 1060
- blijft nu nieuwe oplossingen vinden voor netlist 3
- met shortfirst en remaking een totale lengte van 981

- random netlist zorgt nu ervoor dat meer dan 5 connecties bij 1 gate niet voorkomt
- hoe weet ik zeker of een netlist niet oplosbaar is?

##### Daanupdates:
visualisatie verbeteren
- range bepaalde punten laten zien binnen een zekere lengte met twee sc huifjes. Net als op marktplaats, prijs van ... tot
- weg met die  bolletjes, allen duidelijke lijnen (kijk even naar de kleurstelling (meest onderscheidend)
- Gates zelf: zwarte blokjes

Results:
- die netlists van verschillende aantallen, van ieder aantal 20 random maken.
- oplosbaarheid, lengte, manhattanlengte. PLotten maarrrrrrrrrrrr. Dan gaan we leuk kijken!

#### June 7
- visualisatie verbeteren
- er kunnen nu paden tussen bepaalde lengte worden laten zien
- morgen: werken aan resultaten en verbeteren visualisatie (absolute positie van de grafiek van connecties)
 
#### June 8
- kleine bug in code gefixt: niet meer door ongebruikte gates heen
- er kunnen slechts paden van bepaalde lengte worden geshowd
- er kan data uit de database folder worden opgehaald
- applicatie opgesplitst in een losse solver en de GUI
- morgen: database gaan vullen, resultaten beter visualiseren:
 - van elke x aantal iteraties van elk aantal random connecties de gemiddelde totale lengte en tijd plotten
 - op een schaal van rood naar groen de successrate van het oplossen van een aantal random connecties
 
#### June 9
visualisatie gaat vooruit:
<img src="https://github.com/danielstaal/project/blob/master/doc/gui4.PNG?raw=true" width="320">

- de applicatie is geen solver meer, haalt alleen data uit de database
- eerste iteratie wordt getoond op aanvraag van de user
- grafiek laat gemiddelde resultaten van 10 gepoogde iteratie per aantal connecties zien
- netlists waarbij een of meer gates meer dan 5 verbindingen maakt worden weggegooid zonder mee te tellen

#### June 10
 
## Week 24
#### June 13

##### Daanupdates:
* pre: zien van de spreiding van de 10 trials.
* pre: gaan naar 20 trials
* punten verbinden
* Huidige resultaten uitbreiden naar 3 prints van het huidige formaat (poortjes verschuiven)
* Huidige resultaten uitbreiden naar 3 grote prints (het origineel) 

*  Doe een voorstel voor makkelijke en moeilijke netlists.

* Met Julian kijken of we die dingen kunnen 3D printen
 
#### June 14
- op lisa aansluiten 
- als het goed is doet lisa nu batch jobs om resultaten te verkrijgen
- Huidige visualisatie:
<img src="https://github.com/danielstaal/project/blob/master/doc/gui5.PNG?raw=true" width="320">

- twee nieuwe prints op (18*13) grid:
 - (print 2) een op het oog optimale print
 - (print 3) de originele print 1, met 4 gates verschoven

- veel gebeurd: visualisatie is weer een stuk beter, code nu wellicht wat rommelig, moet weer verbeterd worden

#### June 15
- meer resultaten ophalen met lisa
- grid embed in dezelfde tkinter als de grafiek
<img src="https://github.com/danielstaal/project/blob/master/doc/gui6.PNG?raw=true" width="480">

#### June 16
- werken aan visualisatie:
  - grafiek is nu interactief: de pijltjestoetsen kunnen gebruikt worden, of een bepaald punt in de grafiek kan met de muis geselecteerd worden 
 
#### June 17
- resultaten met Lisa ophalen voor de 3 verschillende prints

## Week 25
#### June 20
- beginnen te werken aan het maken van een 3d print
- dit blijkt redelijk lastig, een .stl file type is nodig, dus er moet een nieuwe visualisatie gemaakt worden, de python visualisatie kan niet zomaar omgezet worden

#### June 21
- aangezien python niet handig blijkt, overgeschakeld naar mathematica. Hierin even wennen, lijnen kunnen niet worden uitgeprint want oneindig dun

#### June 22
- Een combinatie van cylinders en bollen blijken een model te kunnen geven dat kan worden uitgeprint. Demo (door Daan gemold):
<img src="https://github.com/danielstaal/project/blob/master/doc/demo.jpg?raw=true" width="480">

 
#### June 23
- python programma geschreven om een paths oplossing gemakkelijk om te zetten in een model wat door mathematica in elkaar wordt gezet

#### June 24
 
