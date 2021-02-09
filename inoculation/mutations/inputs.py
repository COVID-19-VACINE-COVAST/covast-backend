import graphene


class ReservationInput(graphene.InputObjectType):
    uid = graphene.UUID()
    hospital = graphene.UUID()
    vaccine = graphene.UUID()
    reservation_time = graphene.DateTime(required=True)
