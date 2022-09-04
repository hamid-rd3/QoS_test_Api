from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializer import QoSSerializer
from products.models import QoS
from time import time

from .authentication import TokenScheme
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer
from rest_framework import generics
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes


class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)



@api_view(["GET"])
def api_home(request, *args, **kwargs):
    start = time()
    instance = QoS.objects.all().last()
    data = QoSSerializer(instance).data
    end = time()
    data["total_extraction_time"] = end-start
    return Response(data)
