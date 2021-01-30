import graphene

from django.core.validators import ValidationError

from inoculation.models.vaccine import Vaccine
from inoculation.schemas import VaccineType


class Query(graphene.ObjectType):
    get_vaccine_list = graphene.List(VaccineType, auth_token=graphene.String())
    get_vaccine_detail = graphene.Field(VaccineType, auth_token=graphene.String(), vaccine_uid=graphene.UUID())

    @classmethod
    def resolve_get_vaccine_list(cls, root, info, auth_token):
        return Vaccine.objects.all()

    @classmethod
    def resolve_get_vaccine_detail(cls, root, info, auth_token, vaccine_uid):
        return Vaccine.objects.get(uid=vaccine_uid)
