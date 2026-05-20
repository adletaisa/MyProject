from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Difficulty(models.TextChoices):
    EASY = 'easy'
    MEDIUM = 'medium'
    HARD = 'hard'


class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    difficulty = models.CharField(
        max_length=10,
        choices=Difficulty.choices
    )

    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(default=timezone.now)  # 👈 НОВОЕ
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title