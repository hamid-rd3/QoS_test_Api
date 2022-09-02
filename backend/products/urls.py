from django.urls import path
from .views import qos_detail_view, qos_list_create_view, qos_update_view, qos_delete_view


urlpatterns = [
    path('<int:pk>/', qos_detail_view),
    path('', qos_list_create_view),
    path('<int:pk>/update/', qos_update_view),
    path('<int:pk>/delete/', qos_delete_view),

]
