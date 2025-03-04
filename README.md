# Weather Forecast App

This is a simple weather forecast web application built using **Django** that allows users to get the current weather information of cities worldwide.

## Features
- Users can search for the weather forecast by entering the name of the city.
- Displays current weather details such as temperature, humidity, weather description, and wind speed.
- Provides a clean and simple user interface to interact with the weather data.
- Built using Django and integrated with the OpenWeather API.

## Requirements

Before running the application, make sure you have the following installed:
- Python 3.x
- Django
- Requests library

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/weatherforecast.git
   cd weatherforecast

## Create and activate a virtual environment (if you don't have one):
Using venv:

python -m venv env
source env/bin/activate  # On macOS/Linux
.\env\Scripts\activate  # On Windows

## Install the required dependencies:
Using pip:
pip install -r requirements.txt

## Get an API Key from OpenWeather:
Go to OpenWeather and sign up to get a free API key.
Add the API key to your Django settings or .env file (if you're using django-environ).

## Run migrations: Make sure your database is set up by running:
python manage.py migrate

## Start the Django development server:
python manage.py runserver

Visit the app: Open your web browser and go to http://127.0.0.1:8000/ to see the weather app in action.

## Usage
Upon opening the app, you will see a search box where you can type the name of any city.
Once you submit the city name, the app will display the current weather forecast for that city.
The weather data includes:
Temperature (in Celsius)
Humidity percentage
Weather description (clear, cloudy, rainy, etc.)
Wind speed
Contributing
Feel free to fork the repository, make changes, and create a pull request.

## Steps to contribute:
Fork the repository
Create a new branch for your changes
Implement your changes
Test your changes
Create a pull request

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
The weather data is provided by the OpenWeather API.
Thanks to the Django framework for powering this web app.

### **Instructions:**
1. **Personalize the repository URL**: In the "Installation" section, replace `your-username` with your actual GitHub username in the clone URL.
2. **Add your OpenWeather API key**: In the "Installation" section, make sure you have added your OpenWeather API key in your Django settings or `.env` file.
3. **Additional customization**: If your project has extra configuration steps or unique features, you can modify this README to reflect those changes.
