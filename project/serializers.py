from rest_framework import serializers

from .models import *

class PositionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)

    class Meta:
        model = Portfolio
        fields = ['id', 'name',]

class PersonSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
    position_id = serializers.CharField(source='position.id')

    class Meta:
        model = Person
        fields = '__all__'


class PortfolioSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)

    class Meta:
        model = Portfolio
        fields = '__all__'

class ProjectSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    status = serializers.ChoiceField(required=True, choices=STATUS_CHOICES)
    portfolio_id = serializers.IntegerField(source='portfolio.id')
    
    class Meta:
        model = Project
        fields = '__all__'

class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    date = serializers.DateField(required=True)
    dead_line = serializers.DateField(required=True)
    status = serializers.ChoiceField(required=True, choices=STATUS_CHOICES)
    project_id = serializers.IntegerField(source='project.id')

    class Meta:
        model = Position
        fields = '__all__'

class WidgetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    task_id = serializers.IntegerField(source='task.id')

    class Meta:
        model = Position
        fields = '__all__'
   