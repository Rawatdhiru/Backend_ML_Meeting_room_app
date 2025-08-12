from django.contrib import admin
from .models import MeetingRoom, Booking

@admin.register(MeetingRoom)
class MeetingRoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'room', 'date', 'start_time', 'end_time', 'user_name']
    list_filter = ['room', 'date']
