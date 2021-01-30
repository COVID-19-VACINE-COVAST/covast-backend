import graphene

from django.core.validators import ValidationError

from inoculation.models.vaccine import Vaccine
from inoculation.schemas import VaccineType

from utils.decorators import login_required


class Query(graphene.ObjectType):
    get_vaccine_list = graphene.List(VaccineType, token=graphene.String(required=True))
    get_vaccine_detail = graphene.Field(VaccineType, token=graphene.String(required=True), vaccine_uid=graphene.UUID())

    @classmethod
    @login_required
    def resolve_get_vaccine_list(cls, root, info, token):
        return Vaccine.objects.all()

    @classmethod
    @login_required
    def resolve_get_vaccine_detail(cls, root, info, token, vaccine_uid):
        return Vaccine.objects.get(uid=vaccine_uid)
