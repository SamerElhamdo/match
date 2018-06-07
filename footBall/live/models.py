from django.db import models
from django.urls import reverse_lazy
# Create your models here.
from django.utils.text import slugify
import datetime


class Channel(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True, blank=True)




    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('match_detail', args=[self.slug])




class Lig(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True, blank=True)


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('match_detail', args=[self.slug])





class Match(models.Model):
    home_team_1 = models.CharField(max_length=100)
    guest_team_2 = models.CharField(max_length=100)
    stadium = models.CharField(blank=True,max_length=100)
    commentator = models.CharField(blank=True,max_length=100)
    link_1 = models.TextField(blank=True)
    link_2 = models.TextField(blank=True)
    link_3 = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    match_Date = models.DateField(auto_now_add=False)
    match_time = models.TimeField(auto_now_add=False)
    lig = models.ForeignKey(Lig, related_name='match', on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel, related_name='match', on_delete=models.CASCADE)
    name = models.CharField(blank=True, max_length=200)
    slug = models.SlugField(unique=True, blank=True)





    def __str__(self):
        return self.home_team_1

    def save(self, *args, **kwargs):
        if not self.id:
            self.name = self.home_team_1 + 'vs' + self.guest_team_2
            self.slug = self.name
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('match_detail', args=[self.slug])


print(models.DateField(auto_now_add=True))