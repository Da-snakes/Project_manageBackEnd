from .models import *
from rest_framework.generics import ListAPIView
from .serializers import *

class PersonAPIView(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class ProjectAPIView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class TaskAPIView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class PortfolioAPIView(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PortfolioSerializer

class WidgetAPIView(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = WidgetSerializer

class PositionAPIView(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = WidgetSerializer

    