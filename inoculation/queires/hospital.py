import graphene

from django.core.validators import ValidationError

from inoculation.models.hospital import Hospital
from inoculation.schemas import HospitalType

from utils.decorators import login_required


class Query(graphene.ObjectType):
    get_hospital_list = graphene.List(HospitalType, token=graphene.String(required=True))
    get_hospital_detail = graphene.Field(HospitalType, token=graphene.String(required=True),
                                         hospital_uid=graphene.UUID())

    @classmethod
    @login_required
    def resolve_get_hospital_list(cls, root, info, token):
        return Hospital.objects.all()

    @classmethod
    @login_required
    def resolve_get_hospital_detail(cls, root, info, token, hospital_uid):
        return Hospital.objects.get(uid=hospital_uid)
