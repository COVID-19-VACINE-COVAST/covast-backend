import graphene

from django.core.validators import ValidationError

from inoculation.models.reservation import Reservation
from inoculation.schemas import ReservationType

from utils.decorators import login_required


class Query(graphene.ObjectType):
    get_reservation_list = graphene.List(ReservationType, token=graphene.String(required=True))
    get_reservation_detail = graphene.Field(ReservationType, token=graphene.String(required=True),
                                            reservation_uid=graphene.UUID())

    @classmethod
    @login_required
    def resolve_get_reservation_list(cls, root, info, token):
        return Reservation.objects.all()

    @classmethod
    @login_required
    def resolve_get_reservation_detail(cls, root, info, token, reservation_uid):
        return Reservation.objects.get(uid=reservation_uid)
