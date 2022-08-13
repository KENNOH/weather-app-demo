from statistics import median
from rest_framework import serializers
import requests
from django.conf import settings
from rest_framework import status
from .utils import *



class ErrorResponseSerializer(serializers.Serializer):
    error_message = serializers.CharField(required=False)
    status = serializers.IntegerField(required=False)
    
    class Meta:
        fields = ["error_message", "status"]





class TemparatureComputeSerializer(serializers.Serializer):
    maximum = serializers.DecimalField(max_digits=3, decimal_places=1, required=False)
    minimum = serializers.DecimalField(max_digits=3, decimal_places=1, required=False)
    average = serializers.DecimalField(max_digits=3, decimal_places=1, required=False)
    median = serializers.DecimalField(max_digits=3, decimal_places=1, required=False)
    
    class Meta:
        fields = ["maximum", "minimum","average","median"]

    
    def compute(self):
        processed_data = {}
        max_temps = []
        min_temps = []
        average_temps = []
        median_temps = []
        try:
            city = self.context["city"]
            days = self.context["days"]
            """Prepare Url with api key and append necessary parameters"""
            url = '{}{}{}{}'.format(settings.WEATHER_API_BASE_URL, "/forecast.json?key="+settings.WEATHER_API_KEY,"&q=",city)
            """Logic to check if number of days are provided from the parameters or not"""
            if days != None:
                endpoint = '{}{}{}'.format(url,"&days=",days)
            else:
                endpoint = url
            response = requests.get(endpoint)
            if response.status_code == 200:
                data = response.json()['forecast']
                for day in data['forecastday']:
                    """Extract all maximum temparatures for the given days"""
                    max_temps.append(day['day']['maxtemp_c'])
                    """Extract all minimum temparatures for the given days"""
                    min_temps.append(day['day']['mintemp_c'])
                    """Extract all average temparates for the given days"""
                    average_temps.append(day['day']['avgtemp_c'])
                """merge all maximum and minimum values extracted for the various days into one list"""
                median_temps.extend(max_temps)
                median_temps.extend(min_temps)
                """Calculate average maximum temparatures and append it to dictionary"""
                processed_data['maximum'] = Average(max_temps)
                """Calculate average minimum temparatures and append it to dictionary"""
                processed_data['minimum'] = Average(min_temps)
                """Calculate average average temparatures and append it to dictionary"""
                processed_data['average'] = Average(average_temps)
                """Calculate media of maximum and minimum temparatures and append it to dictionary"""
                processed_data['median'] = Median(median_temps)
                return processed_data
            else:
                return {'error_message': 'An error occured fetching the data, from the weather API, please try again','status':status.HTTP_403_FORBIDDEN}
        except:
            return {'error_message':'An error occured processing your response, make sure all inputs are provided and check your internet connection.','status':status.HTTP_400_BAD_REQUEST}
            