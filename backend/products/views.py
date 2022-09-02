
from rest_framework import generics
from .models import QoS
from .serializer import QoSSerializer


class QoSDetailView(generics.RetrieveAPIView):
    queryset = QoS.objects.all()
    serializer_class = QoSSerializer


qos_detail_view = QoSDetailView.as_view()


class QoSListCreateView(generics.ListCreateAPIView):

    queryset = QoS.objects.all()
    serializer_class = QoSSerializer


qos_list_create_view = QoSListCreateView.as_view()


class QoSUpdateView(generics.UpdateAPIView):
    queryset = QoS.objects.all()
    serializer_class = QoSSerializer
    lookup_field = 'pk'


qos_update_view = QoSUpdateView.as_view()


class QoSDeleteView(generics.DestroyAPIView):
    queryset = QoS.objects.all()
    serializer_class = QoSSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)


qos_delete_view = QoSDeleteView.as_view()
