from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class StandardPagination(PageNumberPagination):

    page_size = 20

    page_size_query_param = "page_size"

    max_page_size = 100

    page_query_param = "page"

    def get_paginated_response(self, data):

        return Response({
            "success": True,
            "message": "Success.",
            "pagination": {
                "page": self.page.number,
                "page_size": self.get_page_size(self.request),
                "total_pages": self.page.paginator.num_pages,
                "total_records": self.page.paginator.count,
                "has_next": self.page.has_next(),
                "has_previous": self.page.has_previous(),
            },
            "results": data,
        })