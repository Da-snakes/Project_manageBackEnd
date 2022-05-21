from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import *
from .serializers import *

class PersonAPIView(APIView):
    def get(self, request, format=None):
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_created)

class ProjectAPIView(APIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class TaskAPIView(APIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class PortfolioAPIView(APIView):
    queryset = Person.objects.all()
    serializer_class = PortfolioSerializer

class WidgetAPIView(APIView):
    queryset = Person.objects.all()
    serializer_class = WidgetSerializer

class PositionAPIView(APIView):
    queryset = Person.objects.all()
    serializer_class = WidgetSerializer

    