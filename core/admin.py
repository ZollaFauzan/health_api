# core/admin.py
from django.contrib import admin
from .models import WorkoutProgram, WorkoutSession, DietPlan, DietMeal

admin.site.register(WorkoutProgram)
admin.site.register(WorkoutSession)
admin.site.register(DietPlan)
admin.site.register(DietMeal)
