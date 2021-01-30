import graphene

from django.core.validators import ValidationError

from inoculation.models.reservation import Reservation
from inoculation.schemas import ReservationType


class Query(graphene.ObjectType):
    get_reservation_list = graphene.List(ReservationType, auth_token=graphene.String())
    get_reservation_detail = graphene.Field(ReservationType, auth_token=graphene.String(),
                                            reservation_uid=graphene.UUID())

    @classmethod
    def resolve_get_reservation_list(cls, root, info, auth_token):
        return Reservation.objects.all()

    @classmethod
    def resolve_get_reservation_detail(cls, root, info, auth_token, reservation_uid):
        return Reservation.objects.get(uid=reservation_uid)
