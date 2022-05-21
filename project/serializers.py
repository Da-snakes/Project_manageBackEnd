from rest_framework import serializers

from .models import *

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'first_name', 'last_name', 'email', 'password',]

class PositionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Position
        fields = ['id', 'name',]

class PortfolioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Portfolio
        fields = ['id', 'name',]

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'description']

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Position
        fields = ['id', 'name', 'status', 'description', 'date', 'dead_line',]

class WidgetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Position
        fields = ['id', 'name',]

   