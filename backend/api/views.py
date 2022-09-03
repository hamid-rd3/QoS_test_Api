
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

# @ swagger_auto_schema(operation_summary="change allarguments of a existed id  ", operation_discription="remove the previous version and give new arguments to a specified id", request_body=request_schema_dict, responses={200: responce_schema_dict})


class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


@extend_schema(
    # extra parameters added to the schema
    parameters=[
        OpenApiParameter(
            name='artist', description='Filter by artist', required=False, type=str),
        OpenApiParameter(
            name='release',
            type=OpenApiTypes.DATE,
            location=OpenApiParameter.QUERY,
            description='Filter by release date',
            examples=[
                OpenApiExample(
                        'Example 1',
                        summary='short optional summary',
                        description='longer description',
                        value='1993-08-23'
                ),
                ...
            ],
        ),
    ],
    # override default docstring extraction
    description='More descriptive text',
    # provide Authentication class that deviates from the views default
    auth=TokenScheme,
    # change the auto-generated operation name
    operation_id=None,
    # or even completely override what AutoSchema would generate. Provide raw Open API spec as Dict.
    operation=None,
    # attach request/response examples to the operation.
    examples=[
        OpenApiExample(
                'Example 1',
                description='longer description',
                value=...
        ),
        ...
    ],
)
@api_view(["GET"])
def api_home(request, *args, **kwargs):
    start = time()
    instance = QoS.objects.all().last()
    data = QoSSerializer(instance).data
    end = time()
    data["total_extraction_time"] = end-start
    return Response(data)
