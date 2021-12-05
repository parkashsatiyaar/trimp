import string
import random
from django.db import models

# Create your models here.


class Urls(models.Model):
    original_url = models.URLField(max_length=2000)
    short_char = models.CharField(max_length=6, blank=True, null=True)

    def __str__(self):
        return self.short_char

    def shortner(self):
        while True:
            ran_string = ''.join(random.choices(string.ascii_uppercase +
                                                string.digits, k=6))
            if not Urls.objects.filter(short_char=ran_string).exists():
                return ran_string

    def save(self, *args, **kwargs):
        short_string = self.shortner()
        self.short_char = short_string
        super(Urls, self).save(*args, **kwargs)
