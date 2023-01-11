from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Employee
from .serializer import EmployeeSerializer
from dotenv import load_dotenv
import os
import yagmail
from pathlib import Path

load_dotenv()

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

yag = yagmail.SMTP(email, password)


# Create your views here.
@api_view(['GET'])
def getEmployee(request):
    employee = Employee.objects.all()
    serializer = EmployeeSerializer(employee, many=True)
    return Response(serializer.data)

# Create your views here.
@api_view(['POST'])
def postEmployee(request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    data = serializer.data
    content = f"New Website request. see details {data}"
    file = data["resume"]
    relative = Path(file)
    yag.send(to=email, subject = "New Employee application", contents=content, attachments=f"{Path().absolute()}{relative}"  )
    print("email sent")
    return Response(data)