from django.db import models

class User(models.Model):
    alias = models.CharField(unique = True, primary_key = True, max_length = 20)
    avatar = models.ImageField(upload_to = 'user_Images/', blank = True, null = True)
    email = models.EmailField(blank = False, unique = True)
    password = models.CharField(max_length = 100)

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

class Game_Data(models.Model):
    #gameID = models.IntegerField(blank = True)
    word = models.CharField(max_length = 50, blank = True)
    p1_ip =  models.GenericIPAddressField(protocol='both', unpack_ipv4=False, blank = True, null = True)
    p2_ip =  models.GenericIPAddressField(protocol='both', unpack_ipv4=False, blank = True, null = True)
    hit_p1 = models.IntegerField(default = 0, blank = True)
    hit_p2 = models.IntegerField(default = 0, blank = True)
    gameStart = models.BooleanField(default = False)
    Winner = models.ForeignKey('User', on_delete = models.CASCADE, related_name='Winner', default = None, null = True)

class Leader_Board(models.Model):
    player = models.ForeignKey('User', on_delete = models.CASCADE)
    Days = models.IntegerField(blank = True)

    achievement = models.ForeignKey('Achievement', on_delete = models.CASCADE, related_name='Player_1', default = None)