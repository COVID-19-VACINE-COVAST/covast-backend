import graphene

from django.core.exceptions import ValidationError

from inoculation.models.hospital import Hospital
from inoculation.models.reservation import Reservation
from inoculation.models.vaccine import Vaccine
from inoculation.mutations.inputs import CreateReservationInput, UpdateReservationInput, DestroyReservationInput
from inoculation.schemas import ReservationType

from utils.decorators import login_required


class CreateReservation(graphene.Mutation):
    class Arguments:
        token = graphene.String(required=True)
        create_reservation_data = CreateReservationInput(required=True)

    success = graphene.Boolean()
    reservation = graphene.Field(ReservationType)

    @classmethod
    @login_required
    def mutate(cls, root, info, token, **input):
        create_reservation_data = input['create_reservation_data']
        try:
            create_reservation_data['user'] = info.context.user
            create_reservation_data['hospital'] = Hospital.objects.get(uid=create_reservation_data['hospital'])
            create_reservation_data['vaccine'] = Vaccine.objects.get(uid=create_reservation_data['vaccine'])
            reservation_obj = Reservation.objects.create(**create_reservation_data)
            print(reservation_obj)
        except Hospital.DoesNotExist:
            raise ValidationError('Not found hospital')
        except Vaccine.DoesNotExist:
            raise ValidationError('Not found vaccine')
        except Exception as e:
            raise ValidationError(e)

        return cls(success=True, reservation=reservation_obj)


class UpdateReservation(graphene.Mutation):
    class Arguments:
        token = graphene.String(required=True)
        update_reservation_data = UpdateReservationInput(required=True)

    success = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, token, **input):
        update_reservation_data = input['update_reservation_data']
        reservation_obj = Reservation.objects.filter(uid=update_reservation_data.pop('reservation_uid'))
        if reservation_obj.exists():
            update_reservation_data['hospital'] = Hospital.objects.get(uid=update_reservation_data['hospital'])
            update_reservation_data['vaccine'] = Vaccine.objects.get(uid=update_reservation_data['vaccine'])
            reservation_obj.update(**update_reservation_data)

        return cls(success=True)


class DestroyReservation(graphene.Mutation):
    class Arguments:
        token = graphene.String(required=True)
        destroy_reservation_data = DestroyReservationInput(required=True)

    success = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, token, **input):
        destroy_reservation_data = input['destroy_reservation_data']
        try:
            reservation_obj = Reservation.objects.get(uid=destroy_reservation_data['reservation_uid'])
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
