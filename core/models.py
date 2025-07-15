from django.db import models

class WorkoutProgram(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    level = models.CharField(max_length=50)
    duration_weeks = models.IntegerField()
    target = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class WorkoutSession(models.Model):
    program = models.ForeignKey(WorkoutProgram, related_name='sessions', on_delete=models.CASCADE)
    day = models.IntegerField()
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration_minutes = models.IntegerField()

    def __str__(self):
        return f"{self.program.name} - Day {self.day}"


class DietPlan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    goal = models.CharField(max_length=100)
    total_calories = models.IntegerField()

    def __str__(self):
        return self.name


class DietMeal(models.Model):
    diet_plan = models.ForeignKey(DietPlan, related_name='meals', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    calories = models.IntegerField()

    def __str__(self):
        return f"{self.diet_plan.name} - {self.name}"
