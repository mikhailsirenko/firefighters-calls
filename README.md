[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/mikhailsirenko/P2000/master?filepath=notebooks%2Fmain.ipynb)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mikhailsirenko/P2000/blob/master/notebooks/main.ipynb)

# firefighters-calls
An exploratory data analysis of New Year's Eves firefighters calls in the Netherlands.

## Introduction
The New Year's Eve period in the Netherlands involves many fireworks, fire damage, and increasing violence directed at first responders. There is an active societal debate about whether consumer fireworks should be banned. In order to support this debate, we have analyzed the data from the national emergency network called __P2000__, which is publicly available. We are focusing on __firefighters__ and will not consider police and medical services. The data sets were scraped and downloaded from two websites [p2000-online.net](http://p2000-online.net/) and [www.112-nederland.nl](https://112-nederland.nl).

The analysis was made for __The Hague__. However, the data for __Rotterdam__, __Amsterdam__, and __the Netherlands__ (yes, the whole country!) as well as interactive visualizations are also available (see data and visualizations folders). The GIF below demonstrates how firefighter calls evloved during 2020 New Year's Eve.  

![](https://github.com/mikhailsirenko/P2000/blob/master/visualizations/den_haag_2020.gif)

## How to use this repo
The main body of the project has the following structure:
```
├── data
│   ├── processed            <- The final data sets used for the analysis
│
├── figures                  <- High quality figures 
│
├── notebooks                
│   ├── main.ipynb           <- The main notebook used for EDA
│
├── src                      <- Standalone scripts used for data gathering, preprocessing and visualization
│
├── visualizations           <- Interactive visualizations created with Kepler.gl and GIFs            
│   ├── den_haag.html        <- 2018, 2019 and 2020 New Year's Eve firefigther calls in The Hague
│   ├── den_haag_2020.html   <- 2020 New Year's Eve firefigther calls in The Hague
│   ├── rottedam_2020.html   <- 2020 New Year's Eve firefigther calls in Rotterdam  
│   ├── amsterdam_2020.html  <- 2020 New Year's Eve firefigther calls in Amsterdam
```

If you would like to run the main notebook yourself, please, use the binder or Google Colab (faster option) bages on the top of the page.

Feel free to experiment with the interactive visualization created with [Kepler.gl](https://kepler.gl). Just open the [visualization folder](https://github.com/mikhailsirenko/P2000/tree/master/visualizations), right-click on `den_haag.html` file to save it, open the downloaded file on your computer with any browser. There you can select the year, explore the regions of the calls and the corresponding message more closely. If you interested only in 2020 New Year's Eve, check `den_haag_2020.html` file.

## Main findings
From the data we found that (see the figure below):
1. The number of firefigther calls made during New Year's Eve period is significantly higher than on average.
2. This number is increasing from 2018 to 2020.   
3. Based on the reason for the call, we can attempt to estimate the potential damage.

![](https://github.com/mikhailsirenko/P2000/blob/master/figures/fig5.png)

## Contributing & authors
If you are interested in the project, please, either fork it and submit a pull request, or contact us via Twitter or email.

_Mikhail Sirenko_ [@mikhailsirenko](https://twitter.com/mikhailsirenko), _Trivik Verma_ [@TrivikV](https://twitter.com/TrivikV) and _Igor Nikolic_ [@ComplexEvo](https://twitter.com/ComplexEvo)

## License
[MIT](https://opensource.org/licenses/MIT)

## Acknowledgements
We would like to thank people who are running the website [p2000-online.net](https://p2000-online.net) and _Ton Snoei_ with the team of [112-nederland.nl](https://112-nederland.nl).
