
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializer import QoSSerializer
from products.models import QoS
from time import time
from rest_framework.authtoken.serializers import AuthTokenSerializer
from drf_yasg.utils import swagger_auto_schema
from products.examples import responce_schema_dict, register_responce
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.parsers import MultiPartParser

from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from .serializers import UserSerializer, RegisterSerializer
from django.contrib.auth.models import User
from rest_framework import generics
from .authentication import TokenAuthentication


class ObtainAuthTokenAPIView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer
    parser_classes = [MultiPartParser]
    permission_classes = (AllowAny,)

    @swagger_auto_schema(operation_summary="Bearer Token ", responses={200: 'authenticated, Bearer token is here ! '})
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


obtain_auth_token_api = ObtainAuthTokenAPIView.as_view()


class UserDetailAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    @swagger_auto_schema(operation_summary="user detail", operation_description="token authentication needed")
    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

# Class based view to register user


class RegisterUserAPIView(generics.CreateAPIView):
    parser_classes = [MultiPartParser]
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
