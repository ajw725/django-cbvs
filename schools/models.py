from django.db import models
from django.urls import reverse


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class School(BaseModel):
    name = models.CharField(max_length=255)
    principal = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('schools:detail', kwargs={'pk': self.pk})


class Student(BaseModel):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, related_name='students', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
