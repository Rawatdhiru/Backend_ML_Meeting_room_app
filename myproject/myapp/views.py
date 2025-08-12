from django.shortcuts import render, redirect
from .models import Booking
from .forms import BookingForm
from datetime import timedelta, datetime
from django.contrib import messages

def home(request):
    return render(request, 'myapp/home.html')

def book_room(request):
    if request.method == 'POST':
        print("Form Submitted!")
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            print("form validate successfully")

            # Auto-set end_time = start_time + 30 minutes
            booking.end_time = (
                datetime.combine(datetime.today(), booking.start_time) + timedelta(minutes=30)
            ).time()

            print(f"Trying to book Room: {booking.room}, Date: {booking.date}, Start: {booking.start_time}, End: {booking.end_time}")

            print(" Filtering with Django ORM using time comparisons:")
            # Check for conflicts
            conflict = Booking.objects.filter(
                room=booking.room,
                date=booking.date,
                start_time__lt=booking.end_time,
                end_time__gt=booking.start_time
            ).exists()

            print("Conflict exists?", conflict)

            if conflict:
                messages.error(request, "⚠️ This time slot is already booked.")
            else:
                booking.save()
                print("✅ Booking saved:", booking)
                messages.success(request, "✅ Room booked successfully!")
                return redirect('booking_list')
        else:
            print("❌ Form invalid:", form.errors)
    else:
        form = BookingForm()

    return render(request, 'myapp/booking_form.html', {'form': form})



def booking_list(request):
    bookings = Booking.objects.all().order_by('-date')
    return render(request, 'myapp/booking_list.html', {'bookings': bookings})
