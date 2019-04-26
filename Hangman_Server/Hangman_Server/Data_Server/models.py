from django.db import models

class User(models.Model):
    alias = models.CharField(unique = True, primary_key = True, max_length = 20)
    avatar = models.ImageField(upload_to = 'user_Images/', blank = True, null = True)
    email = models.EmailField(blank = False, unique = True)
    password = models.CharField(max_length = 50)

    def __str__(self):
        return self.alias

class Achievement(models.Model):
    alias = models.ForeignKey('User', on_delete = models.CASCADE)

