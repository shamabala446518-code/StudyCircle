from django.contrib.auth.models import User
from django.db import models


class StudyGroup(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    members = models.ManyToManyField(User, blank=True)

    def _str_(self):
        return self.name


class StudySession(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField(blank=True)

    def _str_(self):
        return self.title

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.title

class Task(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class StudyFile(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='study_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + " - " + self.subject

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    study_streak = models.PositiveIntegerField(default=0)
    last_study_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username