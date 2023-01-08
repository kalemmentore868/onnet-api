from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Client
from .serializer import ClientSerializer
from dotenv import load_dotenv
import os

load_dotenv()

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

# Create your views here.
@api_view(['GET'])
def getClient(request):
    print(email, password)
    client = Client.objects.all()
    serializer = ClientSerializer(client, many=True)
    return Response(serializer.data)

# Create your views here.
@api_view(['POST'])
def postClient(request):
    serializer = ClientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)