from django.db import models

class User(models.Model):
    alias = models.CharField(max_length = 20)
    email = models.EmailField(blank = False, unique = True)
    password = models.CharField(max_length = 50)

    def __str__(self):
        return self.alias
