from django.db import models

# Create your models here.


class Questions(models.Model):

    class Meta:
        verbose_name_plural = 'Questions'

    # Credit: https://www.fullstackpython.com/django-db-models-autofield-examples.html
    question_number = models.AutoField(verbose_name='item_number',
                                       serialize=True,
                                       auto_created=True,
                                       primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=254, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    question = models.CharField(max_length=254)

    def __str__(self):
        return self.name