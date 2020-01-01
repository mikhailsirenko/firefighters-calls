# P2000
Exploring and visualizing P2000 data, Dutch emergency services pager network.

Data are scraped from [http://www.p2000-online.net/](http://www.p2000-online.net/)

## Car fires in Haglanden on New Years Eve 2020
Directory NewYearsEve220 contains fire brigade messages in [Veiligheidsregio Haaglanden](https://www.vrh.nl/). Dataset retrieved ~9:30 on 1/1/2020, latest message on 07:31:24 1/1/2020, earliest message 22:41:48 on 29/12/2019.
events.txt file contains the table rows filtered out of the html pages, which contain Md OR Mdx tags, describing the main headline of the events, type, streetname, municipality and capcode.

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
    645    8981  137642
```
645 events in total, of which
```bash
$ grep Voertuigbrand events.txt | wc
    102    1300   20786
```
102 events are "Voertuigbrand" or vehicle fire, of which
```bash
$ grep -E 'Voertuigbrand.*SGRAVH'  events.txt  | wc
     82    1040   16692
```
are within The Hague municipality.
