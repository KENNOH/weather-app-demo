from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, generics, filters
import json
from  drf_yasg.utils import swagger_auto_schema
from  django.utils.decorators import method_decorator
from .serializers import *






class WeatherComputeView(generics.CreateAPIView):
    authentication_classes = []
    permission_classes = []

    @method_decorator(
        name='Computer statistical temparature values',
        decorator=swagger_auto_schema(
            responses= {200: TemparatureSerializer(), 400: ErrorResponseSerializer(), 403: ErrorResponseSerializer()},
            operation_id='Computer statistical temparature values',
            operation_description="""This endpoint is supposed to be used to fetch and compute weather metrics such as maximum, minimum, average, median temparature values for a given city in a particular time span using data from https://www.weatherapi.com/
            """
        ),
    )
    def post(self, request, city):
        serializer = TemparatureSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.context["city"] = city
        if 'days' in request.GET:
            days = request.GET['days']
            serializer.context["days"] = days
        else:
            serializer.context["days"] = None 
        results = serializer.compute()
        return Response(results)