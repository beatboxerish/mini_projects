# Restaurant Dashboard

## About :

This is a small project I was working on and contains a 
dashboard made using python, flask and bootstrap. I used an open 
source POS software for restaurants : Floreant POS, to artificially
generate data and have given some suitable plotting functions to
generate plots for which I have used plotly. 

I created the data used here by sitting and spending time on the above
mentioned software and actually placing orders. It was fun and a 
little irritating but I wasn't able to find raw POS data anywhere on 
the net and thus, this seemed like a good idea.

## Usage :

To check this app out you must `cd` into the app folder and then 
enter `python routes.py`

This will start the dashboard and you must now go to the url 
specified in output of the above command to view it.

## Files/Folders :

1. data - Contains both the raw and the clean data
2. app - Contains the main plotting functions, the templates and
 related files along with the main file that runs the dashboard
3. imgs - Contains the screenshots used below

## Requirements :

1. flask
2. plotly
3. pandas

## Screenshots :

![yo](https://github.com/beatboxerish/mini_projects/blob/master/restaurant_dashboard/imgs/dashboard_1.png)

![woooho](https://github.com/beatboxerish/mini_projects/blob/master/restaurant_dashboard/imgs/dashboard_2.png)

![woooho](https://github.com/beatboxerish/mini_projects/blob/master/restaurant_dashboard/imgs/dashboard_3.png)

*Note that graphs haven't been given for the employees and customers
section as the goal was to create a template or layout and show how 
graphs could be used, which have been shown in the food tab. One 
could replace the text in the employees and customers sections by 
the plots as is done in the foods section.*
