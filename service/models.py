# Credit: Code-Institute
from django.db import models
from django.contrib.auth.models import User


class UserQuestion(models.Model):
    """
    A model for recieving customer questions
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_full_name = models.CharField(max_length=20, null=True, blank=True)
    default_email = models.CharField(max_length=20, null=True, blank=True)
    default_message = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.user.username
