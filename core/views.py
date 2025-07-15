from rest_framework import viewsets
from .models import WorkoutProgram, WorkoutSession, DietPlan, DietMeal
from .serializers import WorkoutProgramSerializer, WorkoutSessionSerializer, DietPlanSerializer, DietMealSerializer

class WorkoutProgramViewSet(viewsets.ModelViewSet):
    queryset = WorkoutProgram.objects.all()
    serializer_class = WorkoutProgramSerializer

class WorkoutSessionViewSet(viewsets.ModelViewSet):
    queryset = WorkoutSession.objects.all()
    serializer_class = WorkoutSessionSerializer

class DietPlanViewSet(viewsets.ModelViewSet):
    queryset = DietPlan.objects.all()
    serializer_class = DietPlanSerializer

class DietMealViewSet(viewsets.ModelViewSet):
    queryset = DietMeal.objects.all()
    serializer_class = DietMealSerializer
