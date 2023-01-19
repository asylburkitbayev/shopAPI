from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Branch
from .serializers import BranchSerializer, ListBranchSerializer


class BranchModelViewSet(ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = ListBranchSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = ListBranchSerializer(queryset, many=True)
        return Response(serializer.data)

    # def get_serializer_class(self):
    #     if self.request.method == 'GET':
    #         return ListBranchSerializer
    #     return BranchSerializer
