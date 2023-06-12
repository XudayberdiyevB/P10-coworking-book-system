from django.db import models
from django.utils.translation import gettext_lazy as _


class Book(models.Model):
    resident = models.ForeignKey("bookings.Resident", on_delete=models.CASCADE, related_name="bookings")
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE, related_name="bookings")
    start = models.DateTimeField(_("Start date"))
    end = models.DateTimeField(_("End date"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.resident} - {self.room}"
