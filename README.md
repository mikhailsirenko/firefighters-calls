[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/mikhailsirenko/P2000/new?filepath=notebooks%2Fmain.ipynb)

# P2000
Exploring and visualizing P2000 data, Dutch emergency services pager network.

Data are scraped from [http://www.p2000-online.net/](http://www.p2000-online.net/) The website says "Op de juistheid van de berichten en de beschikbaarheid van de site worden geen
garanties gegeven." i.e. there are no guarantees for the accuracy of the data. Same goes fo analysis, take it as is.

## Car fires in Haaglanden on New Years Eve 2020
Directory NewYearsEve220 contains fire brigade messages in [Veiligheidsregio Haaglanden](https://www.vrh.nl/). Dataset retrieved ~9:30 on 1/1/2020, latest message on 07:31:24 1/1/2020, earliest message 22:41:48 on 29/12/2019.
events.txt file contains the table rows filtered out of the html pages, which contain Md OR Mdx tags, describing the main headline of the events, type, streetname, municipality and capcode, between ~9:30 and ~9:39, so almost precisely 24 hours.

Example row :
```html
<tr><td class="DT">01-01-20</td><td class="DT">00:49:15</td><td class="Br">Brandweer</td><td class="Regio">Haaglanden</td><td class="Md">P 1 BDH-05 Buitenbrand Vegelinsbos ZOETMR 155230</td></tr>
<tr><td class="DT">01-01-20</td><td class="DT">00:49:06</td><td class="Br">Brandweer</td><td class="Regio">Haaglanden</td><td class="Md">P 1 BDH-09 Voertuigbrand Slijpmolen Gortmolen SGRAVH 159635</td></tr>
<tr><td class="DT">01-01-20</td><td class="DT">00:48:05</td><td class="Br">Brandweer</td><td class="Regio">Haaglanden</td><td class="Md">P 2 BDH-16 Buitenbrand afval/rommel Scheepmakersingel DELFGW 155430</td></tr>
<tr><td class="DT">01-01-20</td><td class="DT">00:44:59</td><td class="Br">Brandweer</td><td class="Regio">Haaglanden</td><td class="Md">P 1 BDH-08 Buitenbrand afval/rommel Marktweg SGRAVH 157630</td></tr>
<tr><td class="DT">01-01-20</td><td class="DT">00:44:02</td><td class="Br">Brandweer</td><td class="Regio">Haaglanden</td><td class="Md">P 1 BDH-05 Autom. brand OMS Middin - Heemburgh Schiebroekstraat ZOETMR 155330</td></tr>
<tr><td class="DT">01-01-20</td><td class="DT">00:43:14</td><td class="Br">Brandweer</td><td class="Regio">Haaglanden</td><td class="Md">P 1 BDH-06 Voertuigbrand Sasboutstraat Van Kinschotstraat DELFT 155530</td></tr>
<tr><td class="DT">01-01-20</td><td class="DT">00:42:54</td><td class="Br">Brandweer</td><td class="Regio">Haaglanden</td><td class="Md">P 1 BDH-05 Buitenbrand afval/rommel Veursestraatweg LEIDDM 155130</td></tr>
```

There are 
```bash
$ cat events.txt | wc
    515    7150  109747
```
515 events in total, of which
```bash
$ grep Voertuigbrand events.txt | wc
     92    1175   18765
```
92 events are "Voertuigbrand" or vehicle fire,
```bash
$ grep -E 'Voertuigbrand.*SGRAVH'  events.txt  | wc
     74     940   15076
```
of which 74 are within The Hague municipality.

Accoring to [GemiddeldGezien.nl](https://gemiddeldgezien.nl/gemiddelde-prijs-auto) an average new car in NL costs 25K Euro. In total about 2.3 M Euros worth of cars went up in flames in 24 hours. 

![Histogram of car fires](https://github.com/igornikolic/P2000/blob/master/NewYearsEve2020/Autobranden_histogram.png)

![Cummulaative plot of car fires](https://github.com/igornikolic/P2000/blob/master/NewYearsEve2020/Autobranden_cumulatief.png)

![Total firebrigate](https://github.com/igornikolic/P2000/blob/master/NewYearsEve2020/Brandweer_uitruk_cumulatief.png)
