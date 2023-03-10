from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Client
from .serializer import ClientSerializer
from dotenv import load_dotenv
import os
import yagmail

load_dotenv()

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

yag = yagmail.SMTP(email, password)


# Create your views here.
@api_view(['GET'])
def getClient(request):
    client = Client.objects.all()
    serializer = ClientSerializer(client, many=True)
    return Response(serializer.data)

# Create your views here.
@api_view(['POST'])
def postClient(request):
    serializer = ClientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        print(serializer.errors)
    data = serializer.data
    content = f"New Website request. see details {data}"
    try:
        yag.send(to=email, subject = data["subject"], contents=content  )
        print("email sent")
    except:
        print("error, email not sent")
    return Response(data)