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
