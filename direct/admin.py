from django.contrib import admin
from .models import Position, Sound, Photo

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'location', 'coordination',
                    'created_time','last_updated_time')

@admin.register(Sound)
class SoundAdmin(admin.ModelAdmin):
    list_display = ('sound_position', 'sounder', 'birthplace', 'birth',
                    'recorded_time','created_time', 'last_updated_time')

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('photo_position', 'text', 'image')