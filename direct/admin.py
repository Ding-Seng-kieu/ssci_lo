from django.contrib import admin
from .models import Position, Sound, Photo, ChoiceInfo, AreaInfo

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'location', 'province', 'city','coordination',
                    'created_time','last_updated_time')
    change_form_template = 'area.html'

@admin.register(Sound)
class SoundAdmin(admin.ModelAdmin):
    list_display = ('sound_position', 'sounder', 'birthplace', 'birth',
                    'recorded_time','created_time', 'last_updated_time')

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('photo_position', 'text', 'image')

@admin.register(ChoiceInfo)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'belong_to')

###############################################################################
@admin.register(AreaInfo)
class AreaAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'pid')