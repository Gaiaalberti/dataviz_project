# Data Visualization Project

## Gender Gap in European Union Parliament

This project aims to provide insights into the evolving nature of the European Parliament and the challenges that it faces in achieving gender equality, with a final focus on the Italian EU representatives.

Here [our website on the Gender Gap in the European Union Parliament](https://gendergap-eu.herokuapp.com/).

(_The website is not mobile-friendly_. We strongly advise to navigate the website using the laptop)

## Source of data
All the information to create the dataset have been retrieved from the [website of the Members of the European Parliament](https://www.europarl.europa.eu/meps/en/home) using BeautifulSoup


### Steps for the creation of the final merged dataset 

- Download of an XML file for each term from the section [Directory](https://www.europarl.europa.eu/meps/en/directory) of the European website. Each XML file contains the name and the Id of each Member of the European Parliament (MEP) for that specific term.
- XML files conversion into JSON files
- We used the name and the Id contained in the JSON file as variables to be inserted in the url of the EU webpage to get to the individual webpages of each MEPs for each term. 
- To retrieve the information from each webpage of each MEP, we used BeautifulSoup library. We retrieved data about the country of origin, EU Parliamentary group affiliation, the National Party affiliation and the starting month and year of mandate.
- Adding a column specyfing which term each member belongs to 
- Adding a gender column with the API Genderize. 

All the files needed to create the datasets for each term are in the folder "terms". We advise **not to run the code** since it takes a long time to retrieve all the information. Moreover for the gender column, we used the API genderize which allows only 1000 calls per day. 

- Merging all the single csv files for each term into one merged dataframe. 
- Adding the column "orientation" that specify the political orientation (right, right-center, center, center-left, left, non-alligned) of each european political party.

The final csv of the merged dataframe can be found in the main file section of this repository.


## Folder details

_Dashboard_ folder: contains all the images, code, and csv files to run our dashboard app
- assets: contains the favicon for our website
- pages: contains a folder "dataset" with the datsets used, a folder "static" with the static images and the three pages of our dashboard. 
- app.py: the main app in which all the general layout of the dashboard is set 

_r-visualization_ folder:
- r file for creating the parliament chart visualization displayed in the home page of the Dash app 
- csv file used for plotting the r visualization

_terms_ folder: 
- json files: json files of each term 
- python files: for each term containing the code to retrieve information from the [EU MEPs webisite](https://www.europarl.europa.eu/meps/en/home) with BeutifulSoup
- term csv: final dataset for each term 

_csv_joiner.ipynb_: 
- python file where all the csv relative to each term have been merged and further cleaning and processing has been made 

_merged_coalition.csv_:
- final merged dataset with all the terms and all the information retrieved

_network_dep.ipynb_:
- python file for creating the network of MEPs displayed in the Dash app



## Contributors
This project has been carried out by Gaia Alberti, Claudia Compagnone and Vincenzo Musto

