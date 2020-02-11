from django.db import models


class ChoiceInfo(models.Model):
    """选项模型"""

    name = models.CharField(max_length = 50)
    belong_to = models.ForeignKey('self', related_name = 'areas',null=True,
                                 blank=True, on_delete = models.SET_NULL)
    choice_code = models.CharField(max_length=1, null = True)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'choiceinfo'
        
        #verbose_name = '选项信息'
        #verbose_name_plural = verbose_name


class Position(models.Model):
    """地点模型"""

    code = models.CharField(max_length = 7, blank = True, null = True, unique = True)
    name = models.CharField(max_length=15)
    banguaci = models.CharField(max_length = 40, blank = True, null = True)
    POSITION_ZONE = (('01','鼓楼'), ('02','台江'), ('03','仓山'), ('04','马尾'),
                     ('05','晋安'), ('06','长乐'), ('07','闽侯'), ('08','连江'),
                     ('09','罗源'), ('10','闽清'), ('11','永泰'), ('12','平潭'),
                     ('13','福清'), ('14','古田'), ('15','屏南'))
    zone = models.CharField(max_length = 2, choices = POSITION_ZONE)
    first_choice = models.ForeignKey(ChoiceInfo, related_name = 'first_type',
                            null=True, blank=True, on_delete = models.SET_NULL)
    second_choice = models.ForeignKey(ChoiceInfo, related_name = 'second_type',
                            null=True, blank=True, on_delete = models.SET_NULL)
    location = models.CharField(max_length = 30, blank=True, null=True)
    coordination = models.CharField(max_length = 21, blank=True, null=True)
    note = models.CharField(max_length = 30, blank = True, null = True)

    def __str__(self):
        return self.name+"(%s)"%self.code

    def save(self, *args, **kwargs):
        if not self.code:
            #起始编码的计算
            self.code = self.zone + str(self.first_choice.choice_code) + \
                str(self.second_choice.choice_code)
            #末尾编码的计算
            end_code = str(Position.objects.filter(\
                code__startswith=self.code).count()+1).zfill(3)
            self.code += end_code
        super().save(*args, **kwargs)


class Sound(models.Model):
    """录音模型"""

    sound_position = models.ForeignKey(Position, on_delete = models.DO_NOTHING)
    sound_id = models.CharField(max_length = 9, blank=True)
    #sound_url = models.URLField()
    sounder = models.CharField(max_length =10)
    birthplace = models.CharField(max_length = 10)
    birth = models.CharField(max_length = 4)
    recorded_time = models.DateField()
    created_time = models.DateTimeField(auto_now_add = True)
    last_updated_time = models.DateTimeField(auto_now = True)
    
    def save(self, *args, **kwargs):
        if not self.sound_id:
            end_code = str(Sound.objects.filter(\
                sound_id__startswith = self.sound_id).count())
            self.sound_id = self.sound_position.code + '_' + end_code
        super().save(*args, **kwargs)


class Photo(models.Model):
    """照片模型"""

    photo_position = models.ForeignKey(Position, on_delete = models.DO_NOTHING)
    text = models.TextField()
    image = models.ImageField()
