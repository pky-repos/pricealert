from collections import OrderedDict

from rest_framework.response import Response
from rest_framework.pagination import CursorPagination


class BaseCursorSetPagination(CursorPagination):
    page_size = 10
    page_size_query_param = "page_size"
    ordering = "-created_at"

    def __init__(self):
        self.query = None
        self.count = None

    def paginate_queryset(self, queryset, request, view=None):
        self.query = request.GET.get('query', None)
        self.count = self.get_count(queryset)
        return super().paginate_queryset(queryset, request, view)

    def get_count(self, queryset):
        """
        Determine an object count, supporting either querysets or regular lists.
        """
        try:
            return queryset.count()
        except (AttributeError, TypeError):
            return len(queryset)

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('query', self.query),
            ('count', self.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('results', data),
        ]))