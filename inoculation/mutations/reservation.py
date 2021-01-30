import graphene

from django.core.exceptions import ValidationError

from inoculation.models.hospital import Hospital
from inoculation.models.reservation import Reservation
from inoculation.models.vaccine import Vaccine
from inoculation.mutations.inputs import ReservationInput

from utils.decorators import login_required


class CreateReservation(graphene.Mutation):
    class Arguments:
        token = graphene.String(required=True)
        reservation_data = ReservationInput(required=True)

    success = graphene.Boolean()

    @classmethod
    @login_required
    def mutate(cls, root, info, token, reservation_data):
        try:
            reservation_data['user'] = info.context.user
            reservation_data['hospital'] = Hospital.objects.get(uid=reservation_data['hospital'])
            reservation_data['vaccine'] = Vaccine.objects.get(uid=reservation_data['vaccine'])
            Reservation.objects.create(**reservation_data)
        except Hospital.DoesNotExist:
            raise ValidationError('Not found hospital')
        except Vaccine.DoesNotExist:
            raise ValidationError('Not found vaccine')
        except Exception as e:
            raise ValidationError(e)

        return cls(success=True)


class UpdateReservation(graphene.Mutation):
    class Arguments:
        token = graphene.String(required=True)
        reservation_data = ReservationInput(required=True)

    success = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, token, reservation_data):
        reservation_obj = Reservation.objects.filter(uid=reservation_data['uid'])
        print(reservation_obj)
        if reservation_obj.exists():
            reservation_data['hospital'] = Hospital.objects.get(uid=reservation_data['hospital'])
            reservation_data['vaccine'] = Vaccine.objects.get(uid=reservation_data['vaccine'])
            reservation_obj.update(**reservation_data)

        return cls(success=True)


class DestroyReservation(graphene.Mutation):
    class Arguments:
        token = graphene.String(required=True)
        reservation_uid = graphene.UUID(required=True)

    success = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, token, reservation_uid):
        try:
            reservation_obj = Reservation.objects.get(uid=reservation_uid)
            reservation_obj.delete()
        except Reservation.DoesNotExist:
            raise ValidationError('Reservation not found')
        except Exception as e:
            raise ValidationError(e)

        return cls(success=True)


class Mutation(graphene.ObjectType):
    create_reservation = CreateReservation.Field()
    update_reservation = UpdateReservation.Field()
    destroy_reservation = DestroyReservation.Field()
