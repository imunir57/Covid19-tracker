from django.db import models

# Create your models here.
class Cases(models.Model):
    date = models.DateField(auto_now=False)
    new_cases = models.IntegerField()
    new_deaths = models.IntegerField()
    new_recovered = models.IntegerField()
    no_of_test = models.IntegerField()

    def __str__(self):
        title = str(self.date) + ": " + str(self.new_cases)
        return title
