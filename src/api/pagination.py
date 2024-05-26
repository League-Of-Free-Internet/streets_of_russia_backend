from rest_framework import pagination
from rest_framework.response import Response


class NewsPagination(pagination.PageNumberPagination):
    page_size = 3
    page_size_query_param = "page_size"

    def get_paginated_response(self, data):
        return Response({
            "count": self.page.paginator.count,
            "news": data
        })


class EventsPagination(pagination.CursorPagination):
    page_size = 4
    page_size_query_param = "page_size"
    ordering = "-start_date"
    cursor_query_param = "last_events"

    def get_paginated_response(self, data):
        return Response({
            "events": data
        })
