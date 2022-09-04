
from rest_framework import generics
from .models import QoS
from .serializer import QoSSerializer
from drf_yasg.utils import swagger_auto_schema
from .examples import request_schema_dict, responce_schema_dict


class QoSDetailView(generics.RetrieveAPIView):
    queryset = QoS.objects.all()
    serializer_class = QoSSerializer
    lookup_field = 'pk'

    @swagger_auto_schema(operation_description="qos parameters of specified id ", operation_summary="get id qos params ", responces={200: responce_schema_dict})
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


qos_detail_view = QoSDetailView.as_view()


class QoSListCreateView(generics.ListCreateAPIView):

    queryset = QoS.objects.all()
    serializer_class = QoSSerializer

    @swagger_auto_schema(operation_summary="qos parameters of all ids ", operation_description="get paginated list of all id qos params  ", responses={200: responce_schema_dict})
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="extract qos parameters of a site  ", operation_discription="test qos of a new website url and create object with specified id  ", request_body=request_schema_dict, responses={200: responce_schema_dict})
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


qos_list_create_view = QoSListCreateView.as_view()


class QoSUpdateView(generics.UpdateAPIView):
    queryset = QoS.objects.all()
    serializer_class = QoSSerializer
    lookup_field = 'pk'

    @ swagger_auto_schema(operation_summary="change allarguments of a existed id  ", operation_discription="remove the previous version and give new arguments to a specified id", request_body=request_schema_dict, responses={200: responce_schema_dict})
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @ swagger_auto_schema(operation_summary="change only declared arguments  ", operation_discription="change the declared property for a specified id", request_body=request_schema_dict, responses={200: responce_schema_dict})
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)


qos_update_view = QoSUpdateView.as_view()


class QoSDeleteView(generics.DestroyAPIView):
    queryset = QoS.objects.all()
    serializer_class = QoSSerializer
    lookup_field = 'pk'

    @ swagger_auto_schema(operation_summary="complete remove id object", operation_discription="remove all stuff of specified id and set not found to it but id remains by itself", responses={204: 'onject deleted successfully'})
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


qos_delete_view = QoSDeleteView.as_view()
