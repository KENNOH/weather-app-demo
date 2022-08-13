# WEATHER APP DEMO README

# .env file
Create a .env file in the root folder of the project with the following keys along with their appropriate values
    SECRET_KEY = 
    DB_NAME = 
    DB_USER = 
    DB_PASSWORD = 
    DB_HOST = 
    DB_PORT = 
    DEBUG = 
    WEATHER_API_KEY = 
    WEATHER_API_BASE_URL = https://api.weatherapi.com/v1



# 1. METHOD ONE
# Create a database in POSTGRESQL
Create a database in POSTGRESQL and input the correct env values in the .env file
This is mentioned under the .env file section

# Virtual environment
I recommend creating a virtual env for all the python dependencies.
Python3.10 was used to develop the project, check the Pipfile
	
# Open your shell Install the dependencies from requirements.txt
	pip install -r requirements.txt

# Run the database migrations 
	python manage.py migrate

# To start the server
	python manage.py runserver




# 2. METHOD TWO
Make sure you have docker and docker-compose installed
# Pull and build Docker Images
    docker-compose build

After the above command executes successfully:
# Run the images to run the system as daemon
    docker-compose up -d



Access the system on: http://127.0.0.1:8000/





