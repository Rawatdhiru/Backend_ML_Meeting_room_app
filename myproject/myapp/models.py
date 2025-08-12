from django.db import models

class MeetingRoom(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Room Name")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Meeting Room"
        verbose_name_plural = "Meeting Rooms"
        ordering = ['name']

class Booking(models.Model):
    room = models.ForeignKey(MeetingRoom, on_delete=models.CASCADE, related_name='bookings')
    date = models.DateField(verbose_name="Booking Date")
    start_time = models.TimeField(verbose_name="Start Time")
    end_time = models.TimeField(verbose_name="End Time")
    user_name = models.CharField(max_length=100, verbose_name="Booked By")

    def __str__(self):
        return f"{self.user_name} - {self.room.name} - {self.date} ({self.start_time} - {self.end_time})"

    class Meta:
        ordering = ['-date', 'start_time']
