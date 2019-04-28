from django.db import models

class User(models.Model):
    alias = models.CharField(unique = True, primary_key = True, max_length = 20)
    avatar = models.ImageField(upload_to = 'user_Images/', blank = True, null = True)
    email = models.EmailField(blank = False, unique = True)
    password = models.CharField(max_length = 50)

    def __str__(self):
        return self.alias

class Achievement(models.Model):
    player = models.ForeignKey('User', on_delete = models.CASCADE)
    experience = models.IntegerField(default = 0)
    points = models.IntegerField(default = 0)
    achievement = models.CharField(max_length = 30, blank = True)

    def __str__(self):
        return self.alias

class Match(models.Model):
    #gameID = models.IntegerField(blank = True, default = None)
    Player_1 = models.ForeignKey('User', on_delete = models.CASCADE, related_name='Player_1')
    Player_2 = models.ForeignKey('User', on_delete = models.CASCADE, related_name='Player_2')
    level = models.CharField(max_length = 8, default = None)
    seed = models.IntegerField(blank = True)
    Winner = models.ForeignKey('User', on_delete = models.CASCADE, related_name='Winner')

class Game_Data(models.Model):
    gameID = models.IntegerField(blank = True, default = None)
    word = models.CharField(max_length = 50, blank = True)