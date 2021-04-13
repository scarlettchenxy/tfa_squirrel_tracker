
IEOR E4501 - Tools for Analytics Project
Squirrel Tracker: Django-based visualization for squirrel sightings
Project Introduction
We created a Squirrel Tracker using Django to import, export associated data about and provide visualization for sightings of squirrels found in Central Park, New York.

Data Source
In this project,we have used the 2018 Central Park Squirrel Census dataset published by Squirrel Census.This data set contains information pertaining to the number of sightings, including location coordinates, age, physical features and so on.

Management Commands
Import: is a command that can import the data from the csv file, 2018 Central Park Squirrel Census. Specifically, the file path should be included after the management command in the command line.

python manage.py import_squirrel_data /path/to/file.csv
Export: is a command that can be used to export the data in a CSV format. Also, the file path should be added at the command line after the management command.

python manage.py export_squirrel_data /path/to/file.csv
API
Map
Sightings
Stats of squirrels
Add squirrels
Edit a specific squirrel
Dependencies used in this project
Django
Django-Leaflet
Project Prompt
The official description for this project is in Squirrel Tracker

Contributors
Group Name: Project Group 39

Contributors: Abhinaya Shankar, Yunan Shi, Xiaoyi Chen

UNIs: [as6166], [ys3389]，
