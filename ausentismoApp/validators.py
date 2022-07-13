import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validador_fecha_futura(value):
    if value > datetime.date.today():
        raise ValidationError(
            _('%(value)s es superior a la fecha actual'),
            params={'value': str(value)},
        )

def validador_valor_positivo(value):
    if value <= 0.0:
        raise ValidationError(
            _('%(value)s es inferior o igual a 0'),
            params={'value': str(value)},
        )