from django.apps import AppConfig

class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

    def ready(self):
        from .models import MeetingRoom
        default_rooms = ["Conference 1", "Conference 2", "Conference 3", "Conference 4", "Conference 5"]
        for room_name in default_rooms:
            MeetingRoom.objects.get_or_create(name=room_name)
# 