from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status, filters
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from api.models import PriceAlert
from api.serializers import PriceAlertSerializer
from django_filters.rest_framework import DjangoFilterBackend

from core.pagination import BaseCursorSetPagination


class PriceAlertViewSet(viewsets.ModelViewSet):
    pagination_class = BaseCursorSetPagination
    permission_classes = [AllowAny]
    queryset = PriceAlert.objects.all()
    serializer_class = PriceAlertSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["symbol", "status"]
    search_fields = ["symbol", "status"]

    def perform_destroy(self, instance):
        instance.status = "DE"
        instance.save()
