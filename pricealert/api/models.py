from django.db import models

from core.models import BaseModelMixin

PRICE_ALERT_CHOICES = (
    ("CR", "Created"),
    ("DE", "Deleted"),
    ("TR", "Trigerred"),
    ("IA", "Inactive"),
)

class PriceAlert(BaseModelMixin):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    symbol = models.CharField(max_length=10)
    price_limit = models.FloatField()
    lower_higher = models.CharField(max_length=2, choices=(('l', 'lower'), ('h', 'higher')))
    status = models.CharField(max_length=2, choices=PRICE_ALERT_CHOICES, default="CR")