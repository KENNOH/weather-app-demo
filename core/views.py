from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, generics, filters
import json
from  drf_yasg.utils import swagger_auto_schema
from  django.utils.decorators import method_decorator
from drf_yasg import openapi
from .serializers import *




class WeatherComputeView(generics.ListAPIView):
    authentication_classes = []
    permission_classes = []

    @method_decorator(
        name='Compute statistical temparature values',
        decorator=swagger_auto_schema(
            manual_parameters=[openapi.Parameter('days', openapi.IN_QUERY, "number of days to the query data for", type=openapi.TYPE_INTEGER),],
            responses= {200: TemparatureComputeSerializer(), 400: ErrorResponseSerializer(), 403: ErrorResponseSerializer()},
            operation_id='Compute statistical temparature values for a given city spread across days provided',
            operation_description="""This endpoint is supposed to be used to fetch and compute weather metrics such as maximum, minimum, average, median temparature values for a given city in a particular time span using data from https://www.weatherapi.com/.
            Days parameter can be included after the url slash. To be given as '&days=5' to fetch and compute values for up to 5 days
            """
        ),
    )
    def get(self, request, city):
        serializer = TemparatureComputeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.context["city"] = city
        if 'days' in request.GET:
            days = request.GET['days']
            serializer.context["days"] = days
        else:
            serializer.context["days"] = None 
        results = serializer.compute()
        return Response(results)