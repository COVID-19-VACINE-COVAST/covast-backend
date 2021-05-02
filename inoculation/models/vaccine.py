import uuid

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _

from utils.models import AbstractBaseModel


class Vaccine(AbstractBaseModel):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, verbose_name=_('uid'))  # 고유 번호
    name = models.CharField(max_length=50, verbose_name=_('name'))  # 백신 이름
    detail_name_code = models.CharField(max_length=50, verbose_name=_('detail_name_code'))  # 실제 백신 코드 이름
    development_country = models.CharField(max_length=30, verbose_name=_('development_country'))  # 제조 국가
    development_company = models.CharField(max_length=30, verbose_name=_('development_company'))  # 제조사
    release_date = models.DateField(null=True, blank=True, verbose_name=_('release_date'))
    kind = models.CharField(max_length=30, verbose_name=_('kind'))  # 백신 유형
    clinical_trial_stage = models.PositiveIntegerField(null=True, blank=True,
                                                       validators=[MaxValueValidator(3), MinValueValidator(1)],
                                                       verbose_name=_('clinical_trial_stage'))  # 임상 실험 단계
    inoculation_count = models.CharField(max_length=30, verbose_name=_('inoculation_count'))  # 접종 횟수

    class Meta:
        db_table = 'vaccine'
        verbose_name = 'Vaccine'
        verbose_name_plural = '{} {}'.format(verbose_name, _('List'))

    def __str__(self):
        return f'ID({self.id}) name is {self.name} kind is {self.kind}'


