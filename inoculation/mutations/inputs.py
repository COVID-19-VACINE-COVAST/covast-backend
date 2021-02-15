import graphene


class CreateReservationInput(graphene.InputObjectType):
    hospital = graphene.UUID(required=True)
    vaccine = graphene.UUID(required=True)
    reservation_time = graphene.DateTime(required=True)


class UpdateReservationInput(graphene.InputObjectType):
    reservation_uid = graphene.UUID(required=True)
    hospital = graphene.UUID()
    vaccine = graphene.UUID()
    reservation_time = graphene.DateTime()


class DestroyReservationInput(graphene.InputObjectType):
    reservation_uid = graphene.UUID(required=True)
