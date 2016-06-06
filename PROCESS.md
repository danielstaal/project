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
#### June 4
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


#### June 5
 
#### June 6
 
#### June 7
 
#### June 8
 
## Week 24
#### June 9
 
#### June 10
 
#### June 11
 
#### June 12
 
#### June 13
 

## Week 25
#### June 14
 
#### June 15
 
#### June 16
 
#### June 17

#### June 18
 
