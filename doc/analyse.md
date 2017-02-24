# Analyse

## Mindmap 
![mindmappic](https://cloud.githubusercontent.com/assets/22319940/23060902/0067042a-f500-11e6-91d0-1471b1209be6.PNG)

###Mindmap PDF: [mind map.pdf](https://github.com/AP-Elektronica-ICT/ssys17-den-hollanders/files/782845/mind.map.pdf)

## Beschrijving

Voor het vak Smart Systems gaan wij een sturing maken voor een voertuig. Dit voertuig moet enige vorm van intelligentie en draadloze communicatie hebben.
Het voertuig wordt gebouwd op een chassis dat we gaan maken met behulp van een 3D printer, deze beweegt zich voort door middel van 4 banden omhulst door 2 rupsbanden, twee hier van zijn aangedreven en twee hiervan zijn zwenk wielen. De aangedreven wielen worden aangedreven door 2 DC motoren en de wagen kan in elke richting bewegen. Dit wordt gedaan door met de ene motor naar achteren te draaien en met de andere motor naar voren waardoor er 360 graden gedraait kan worden rond de as. Daarnaast moet het voertuig ook kunnen versnellen en afremmen. De sturing van het voertuig wordt gebaseerd op een h-brug, Voeding voor de motoren:

-	2x AA Batterijen = 3V

Deel van de opdracht is om het voertuigje obstakels laten vermijden, dit komt aan bod Door middel van Sensoren.
Door middel van draadloze communicatie, gebruikmakend van een arduino nano (die aangesloten is aan de computer) en een teensy (die aangesloten is aan het voertuig), sturen wij commando’s naar het voertuig, hier maken we gebruik van nrf24l01:
![nrf](https://cloud.githubusercontent.com/assets/22319940/23299416/cc8206f0-fa81-11e6-8a1e-f898fcdf546e.png)

waardoor het zich kan voort bewegen en vervolgens debug informatie kan terug sturen. Voeding voor de Arduino:

-	1x 6IR61 Batterij = 9V

Het project wordt Agile ontwikkeld door gebruik te maken van de scrum methodologie. Dit wordt uitgewerkt op github met behulp van zenhub.
Tijdens het project wordt er gedocumenteerd in een portfolio format, dit heeft mogelijk betrekking op:

-	Datasheets
-	Project plan
-	Feedback
-	Bronnen
-	Logboek
-	Testresultaten
-	Eigen inbreng
-	presentaties


## Blokdiagram
![flowchart_algemeen](https://cloud.githubusercontent.com/assets/22319940/23299270/3a9b28b6-fa81-11e6-9a4e-bf54b72bb7b8.PNG)

[Blokdiagram_Algemeen.pdf](https://github.com/AP-Elektronica-ICT/ssys17-Timmy-Tommy-Steven-4/files/798918/Blokdiagram_Algemeen.pdf)



![flowchart_hardware](https://cloud.githubusercontent.com/assets/22319940/23299165/bd56ff24-fa80-11e6-8a06-9107d752781a.PNG)

[Blokdiagram_Hardware.pdf](https://github.com/AP-Elektronica-ICT/ssys17-Timmy-Tommy-Steven-4/files/798907/Blokdiagram_Hardware.pdf)
