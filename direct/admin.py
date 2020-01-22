from django.contrib import admin
from .models import Position, Sound, Photo, ChoiceInfo

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'zone', 'location',
                   'first_choice', 'second_choice','coordination',
                   'created_time','last_updated_time')

    change_form_template = 'choice.html'

@admin.register(Sound)
class SoundAdmin(admin.ModelAdmin):
    list_display = ('sound_position', 'sounder', 'birthplace', 'birth',
                    'recorded_time','created_time', 'last_updated_time')

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('photo_position', 'text', 'image')

@admin.register(ChoiceInfo)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'choice_code', 'belong_to')
