from rest_framework import status, viewsets
from rest_framework.response import Response
from .models import WHThings
from .serializers import WHThingsSerializer
from .pagination import CustomPagination
from .tasks import fetch_and_save_product


class ApiViewSet(viewsets.ViewSet):
    pagination_class = CustomPagination

    def list(self, request):
        products = WHThings.objects.all()
        paginator = self.pagination_class()
        paginated_products = paginator.paginate_queryset(products, request)
        serializer = WHThingsSerializer(paginated_products, many=True)
        return paginator.get_paginated_response(serializer.data)

    def create(self, request):
        articules = request.data.get('articules', '')
        if not articules:
            return Response(
                {"error": "Не переданы артикули для запроса"},
                status=status.HTTP_400_BAD_REQUEST)

        # Запускаем Celery задачу
        task = fetch_and_save_product.delay(articules)

        return Response(
            {"task_id": task.id},
            status=status.HTTP_202_ACCEPTED)