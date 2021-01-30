import graphene

from django.core.validators import ValidationError

from inoculation.models.hospital import Hospital
from inoculation.schemas import HospitalType


class Query(graphene.ObjectType):
    get_hospital_list = graphene.List(HospitalType, auth_token=graphene.String())
    get_hospital_detail = graphene.Field(HospitalType, auth_token=graphene.String(), hospital_uid=graphene.UUID())

    @classmethod
    def resolve_get_hospital_list(cls, root, info, auth_token):
        return Hospital.objects.all()

    @classmethod
    def resolve_get_hospital_detail(cls, root, info, auth_token, hospital_uid):
        return Hospital.objects.get(uid=hospital_uid)
