[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/mikhailsirenko/P2000/master?filepath=notebooks%2Fmain.ipynb)

# P2000
An exploratory data analysis (EDA) of New Year's Eves firefighter calls in the Netherlands.

## Introduction
The New Year's Eve period in the Netherlands involves many fireworks, fire damage, and increasing violence directed at first responders. There is an active societal debate about whether consumer fireworks should be banned. In order to support this debate, we have analyzed the data from the national emergency network called __P2000__, which is publicly available. We are focusing on __firefighters__ and will not consider police and medical services. The data sets were scraped and downloaded from two websites [p2000-online.net](http://p2000-online.net/) and [www.112-nederland.nl](www.112-nederland.nl).

The analysis was made for __The Hague__. However, the data for Rotterdam and Amsterdam is also available (see data folder). The GIF below demonstrates how firefighter calls evloved during 2020 New Year's Eve.  

![](https://github.com/mikhailsirenko/P2000/blob/master/visualizations/kepler.gl.gif)

## How to use this repo
The main body of the project has the following structure. 
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
├── visualizations            
│   ├── kepler.gl.html       <- Interactive visualization created with Kepler.gl
```

If you would like to run the main notebook yourself, please, use the binder bage on the top of the page. 

## Contributing & authors
If you are interested in the project, please, either fork it and submit a pull request, or contact us via Twitter or email.

_Mikhail Sirenko_ [@mikhailsirenko](https://twitter.com/mikhailsirenko), _Trivik Verma_ [@TrivikV](https://twitter.com/TrivikV) and _Igor Nikolic_ [@ComplexEvo](https://twitter.com/ComplexEvo)

## License
[BSD-3-Clause](https://opensource.org/licenses/BSD-3-Clause)

