from django.db import models


# Create your models here.

class Service(models.Model):
    facilities = models.CharField(max_length=500, blank=False)
    level = models.IntegerField()

    choices = (
        ('In progress', 'Work in Progress'),
        ('Not done', 'Work are not done yet'),
        ('Done', 'Problem are solved')
    )

    status = models.CharField(max_length=200, choices=choices, default='Not done')
    issues = models.CharField(max_length=500, default="No Issues")

    class Meta:
        abstract = True

    def __str__(self):
        return 'Facilities: {0} Level: {1}'.format(self.facilities, self.level)


class Electrical(Service):
    pass


class Mechanical(Service):
    pass


class Cleaning(Service):
    pass
