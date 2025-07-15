# core/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WorkoutProgramViewSet, WorkoutSessionViewSet, DietPlanViewSet, DietMealViewSet

router = DefaultRouter()
router.register(r'workout-programs', WorkoutProgramViewSet)
router.register(r'workout-sessions', WorkoutSessionViewSet)
router.register(r'diet-plans', DietPlanViewSet)
router.register(r'diet-meals', DietMealViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
