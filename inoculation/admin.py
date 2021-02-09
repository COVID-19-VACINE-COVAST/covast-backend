from django.contrib import admin

from inoculation.models.hospital import Hospital
from inoculation.models.reservation import Reservation
from inoculation.models.vaccine import Vaccine


@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    pass


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    pass


@admin.register(Vaccine)
class VaccineAdmin(admin.ModelAdmin):
    pass
