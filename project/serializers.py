from rest_framework import serializers

from .models import *

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ('id', 'name',)

class PersonSerializer(serializers.Serializer):
    position = PositionSerializer(many=True)
    class Meta:
        model = Person
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'position',)


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ('id', 'name',)

class ProjectSerializer(serializers.ModelSerializer):
    portfolio = PortfolioSerializer(many=True)
    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'status' 'portfolio',)

class TaskSerializer(serializers.ModelSerializer):
    person = PersonSerializer(many=True)
    project = ProjectSerializer(many=True)

    class Meta:
        model = Task
        fields = ('id', 'name', 'description', 'date', 'dead_line', 'status', 'project', 'person', )

class WidgetSerializer(serializers.ModelSerializer):
    task = TaskSerializer(many=True)
    class Meta:
        model = Position
        fields = ('id', 'name', 'task',)
   