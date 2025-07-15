from rest_framework import serializers
from .models import WorkoutProgram, WorkoutSession, DietPlan, DietMeal

class WorkoutSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutSession
        fields = '__all__'

class WorkoutProgramSerializer(serializers.ModelSerializer):
    sessions = WorkoutSessionSerializer(many=True, read_only=True)

    class Meta:
        model = WorkoutProgram
        fields = '__all__'


class DietMealSerializer(serializers.ModelSerializer):
    class Meta:
        model = DietMeal
        fields = '__all__'

class DietPlanSerializer(serializers.ModelSerializer):
    meals = DietMealSerializer(many=True, read_only=True)

    class Meta:
        model = DietPlan
        fields = '__all__'
