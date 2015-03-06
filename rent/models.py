import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

GARDEN = 'Garden'
STREET = 'Street'
TOP = 'Top'
LEVEL_CHOICES = (
    (GARDEN, 'Garden Level'),
    (STREET, 'Street Level'),
    (TOP, 'Top Floor'),
)

class Rate(models.Model):
    title = models.CharField(max_length=40)
    rate = models.FloatField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    startdate = models.DateField(blank=True)
    enddate = models.DateField(blank=True)
    level = models.CharField(max_length=6,
        choices=LEVEL_CHOICES,
        default=STREET)

    def __str__(self):
        return  self.title

class Booking(models.Model):
    title = models.CharField(max_length=40)
    body = models.TextField(max_length=10000, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    startdate = models.DateField(blank=True)
    enddate = models.DateField(blank=True)
    level = models.CharField(max_length=6,
        choices=LEVEL_CHOICES,
        default=STREET)

    def __str__(self):
        return  self.title

    def was_created_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.created <= now

    was_created_recently.admin_order_field = 'created'
    was_created_recently.boolean = True
    was_created_recently.short_description = 'Created recently?'

