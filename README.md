# IEOR E4501 - Tools for Analytics  Project
# Squirrel Tracker: Django-based visualization for squirrel sightings


# Project Introduction

We created a **Squirrel Tracker** using *Django* to import, export associated data about and provide visualization for sightings of squirrels found in Central Park, New York.


# Data Source
In this project,we have used the [*2018 Central Park Squirrel Census*](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw) dataset published by [*Squirrel Census*](https://www.thesquirrelcensus.com/).This data set contains information pertaining to the number of sightings, including location coordinates, age, physical features and so on. 


# Management Commands 
Import: is a command that can import the data from the csv file, 2018 Central Park Squirrel Census. Specifically, the file path should be included after the management command in the command line. 

```sh
python manage.py import_squirrel_data /path/to/file.csv
```

Export: is a command that can be used to export the data in a CSV format. Also, the file path should be added at the command line after the management command.

```sh
python manage.py export_squirrel_data /path/to/file.csv
```

# API

# Map     
Shows a map that displays the location of the squirrel sightings on an OpenStreets map.   
>Located at: /map   
Method: GET   
Use the [leaflet](https://leafletjs.com/) library for plotting   

# Sightings 
Shows a list view that lists all squirrel sightings with links to edit and add sightings   
>Located at: /sightings   
	Method: GET  

# Update View   
Update view to update a particular sighting.    
>Located at: /sightings/<unique-squirrel-id>   
	Method: GET & POST   

# Add squirrels
Add squirrel to create a new sighting   
>Located at: /sightings/add   
	Method: GET & POST   

# Stats of squirrels
General stats about the sightings
Stats include five of the attributes listed in the initial CSV download.    
>Located at: /sightings/stats   
Method: GET 


# Dependencies used in this project
- [Django](https://www.djangoproject.com)
- [Django-Leaflet](https://django-leaflet.readthedocs.io/en/latest/)  

# Project Prompt
The official description for this project is in [*Squirrel Tracker*](https://docs.google.com/document/d/1SPv3fMDKiemrR86rD-S9ecvI2npz3PljDzwCfxK2x5g/edit)

# Contributors

Group Name: Project Group 39

Contributors: Abhinaya Shankar, Yunan Shi, Xiaoyi Chen

UNIs: [**[as6166]**](https://github.com/as6166), [ys3389]，xc2560
