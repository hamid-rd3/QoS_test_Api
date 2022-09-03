
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializer import QoSSerializer
from products.models import QoS
from time import time

from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer
from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema
from products.examples import responce_schema_dict, register_responce


class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    @swagger_auto_schema(operation_description="email and username myst be unique ", operation_summary="register user ", responses={200: register_responce})
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


@swagger_auto_schema(method='get', operation_description="last site qos parameters been created  ", operation_summary="get qos params ", responses={200: responce_schema_dict})
@api_view(["GET"])
def api_home(request, *args, **kwargs):
    start = time()
    instance = QoS.objects.all().last()
    data = QoSSerializer(instance).data
    end = time()
    data["total_extraction_time"] = end-start
    return Response(data)


