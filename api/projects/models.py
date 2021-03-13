from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=80)
    cost = models.FloatField()

    def __str__(self):
        return f"{self.name} with a cost of {self.cost}"
