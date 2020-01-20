from django.db import models


class Position(models.Model):
    id = models.CharField(max_length = 7 , primary_key = True)
    name = models.CharField(max_length=10)
    POSITION_TYPE = (('1','行政区划'), ('2','道路'), ('3','村'), ('4','人工建筑'),
                     ('5','自然实体'))
    type = models.CharField(max_length = 1, choices = POSITION_TYPE)
    location = models.CharField(max_length = 30)
    coordination = models.CharField(max_length = 21)
    created_time = models.DateTimeField(auto_now_add = True)
    last_updated_time = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name+"(%s)"%self.id

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Sound(models.Model):
    sound_position = models.ForeignKey(Position, on_delete = models.DO_NOTHING)
    sound_id = models.CharField(max_length = 9, blank=True)
    #sound_url = models.URLField()
    sounder = models.CharField(max_length =10)
    birthplace = models.CharField(max_length = 10)
    birth = models.CharField(max_length = 4)
    recorded_time = models.DateField()
    created_time = models.DateTimeField(auto_now_add = True)
    last_updated_time = models.DateTimeField(auto_now = True)
    
    #def save(self, *args, **kwargs):
    #    self.sound_id = str(Sound.objects.count())
    #    super().save(*args, **kwargs)

class Photo(models.Model):
    photo_position = models.ForeignKey(Position, on_delete = models.DO_NOTHING)
    text = models.TextField()
    image = models.ImageField()
