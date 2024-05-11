from rest_framework import viewsets
from rest_framework.response import Response
from .models import OrderRecieved
from .serializer import OrderRecievedSerializers

class OrderView(viewsets.ModelViewSet):
    queryset = OrderRecieved.objects.all()
    serializer_class = OrderRecievedSerializers

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)
