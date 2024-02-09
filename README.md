# Explorative Information Visualization - Finland's energy production and consumption's relation to time

This is the visualization tool created for course CS-E4450 - Explorative Information Visualization. 

![Visualization of the tool as a gif](https://github.com/oboisti/explorative_information_visualization/blob/main/visualization_gif.gif)

The content of this README
* Motivation
* How was this project done
* How to run this locally

## Motivation
In Finland, electricity consumption and production differ based on the season. In general,
more energy is consumed in winter than in summer as energy is used for heating. Within one month, the consumption
stays mostly at the same level, although between seasons the average consumption
differs greatly.

Finland also uses different electricity sources and some of them are affected by the
weather. Last year, more wind power was produced during the winter months than during
the summer months. Solar power is naturally more produced in summer than winter, due
to Finland’s northern location. Importing electricity from other countries can be affected by
construction. In general, the amount of electricity produced varies more than the amount
consumed.

As electricity is used everywhere from healthcare to heating and communication, it is
extremely important to maintain the electricity production higher than the consumption to
guarantee safety. This can be achieved by having a good combination of different energy
production forms. Although renewable energy sources can have a tendency to be more
weather- and season-dependent, it is possible to find energy production combinations with
those that still produce stable production sum.

This project's goal was to create a tool that
* Visualizes the trends in energy consumption and production that differ based on time 
of day and year
* Can be used to see different options, how Finland's need for electricity could be 
fulfilled by altering the percentages of different energy types


## How was this project done

The tools used:
* Python was chosen as the programming language as it has nice tools for data science 
and was the most familiar language for the developer
* Bokeh was used for interactive visualization, as it provides some nice widgets and 
therefore decreases the development time
* Numpy was crucial as fast enough calculations were needed to process the data 
while animating
* Data is saved as CSV files, in case in future I want to update the data to a more recent one
* Docker was used for allowing the course project reviewers easy way of running the project locally


Data is imported from Fingrid's [open data service](https://data.fingrid.fi/en). The functions 
for importing data can be found in _helper_functions/data_importing_ and the importing process 
itself from the notebook TO BE ADDED

The file _app.py_ contains the running application. To improve readability the app was formed as 
a class with different parts of the visualization process separated into functions. To improve 
readability even further, functionalities relating to calculations on data frames were separated 
into _helper_functions/dataframe_helper.py_ and elements containing text into _helper_functions/page_texts.py_. 
The file helper_functions/constants.py contains the data column names, addresses, and colors so 
that all files import them from the same source and they can be easily changed centrally when needed. 


## How to run this locally
To run this project on your local machine do the following steps:
1. Copy this project folder to your local computer either by using git tools or by extracting the folder from the webpage
2. Make sure you have the latest docker desktop downloaded to your computer and that it is running
3. Open in the command line (or other similar tool) the root folder of this project
4. run the code snippet `docker compose up --build` to build the solution and start the docker container. Depending on your computer this can take several minutes.
5. open the location http://localhost:5006/visualization_with_param in your web browser to see and interact with the visualization. This can also take some time.
6. To close the visualization, open another command line (or similar tool) in this project root folder and run `docker compose down`
