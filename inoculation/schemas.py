from graphene_django.types import DjangoObjectType

from inoculation.models.hospital import Hospital
from inoculation.models.reservation import Reservation
from inoculation.models.vaccine import Vaccine


class HospitalType(DjangoObjectType):
    class Meta:
        model = Hospital
        fields = ('uid', 'name', 'address', 'road_address', 'contact', 'place_url', 'start_business_hours',
                  'end_business_hours', 'latitude', 'longitude', )


class ReservationType(DjangoObjectType):
    class Meta:
        model = Reservation
        fields = ('uid', 'user', 'hospital', 'vaccine', 'reservation_time', )


class VaccineType(DjangoObjectType):
    class Meta:
        model = Vaccine
        fields = ('uid', 'name', 'development_country', 'development_company', 'release_date', 'kind',
                  'clinical_trial_stage', )
