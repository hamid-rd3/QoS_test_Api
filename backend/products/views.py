
from rest_framework import generics
from .models import QoS
from .serializer import QoSSerializer
from drf_yasg.utils import swagger_auto_schema
from .examples import request_schema_dict, responce_schema_dict


class QoSDetailView(generics.RetrieveAPIView):
    queryset = QoS.objects.all()
    serializer_class = QoSSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


qos_detail_view = QoSDetailView.as_view()


class QoSListCreateView(generics.ListCreateAPIView):

    queryset = QoS.objects.all()
    serializer_class = QoSSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


qos_list_create_view = QoSListCreateView.as_view()


class QoSUpdateView(generics.UpdateAPIView):
    queryset = QoS.objects.all()
    serializer_class = QoSSerializer
    lookup_field = 'pk'

    # @ swagger_auto_schema(operation_summary="change allarguments of a existed id  ", operation_discription="remove the previous version and give new arguments to a specified id", request_body=request_schema_dict, responses={200: responce_schema_dict})
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)


qos_update_view = QoSUpdateView.as_view()


class QoSDeleteView(generics.DestroyAPIView):
    queryset = QoS.objects.all()
    serializer_class = QoSSerializer
    lookup_field = 'pk'

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


qos_delete_view = QoSDeleteView.as_view()
