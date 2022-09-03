
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializer import QoSSerializer
from products.models import QoS
from time import time

from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer
from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema


class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


@swagger_auto_schema(method='get', operation_description="last site qos parameters been created  ", operation_summary="get qos params ")
@api_view(["GET"])
def api_home(request, *args, **kwargs):
    start = time()
    instance = QoS.objects.all().last()
    data = QoSSerializer(instance).data
    end = time()
    data["total_extraction_time"] = end-start
    return Response(data)
