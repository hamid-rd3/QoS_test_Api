from . import views
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import permissions
from drf_yasg.views import get_schema_view as swagger_get_schema_view
from drf_yasg import openapi
from .views import UserDetailAPI, RegisterUserAPIView

schema_view = swagger_get_schema_view(
    openapi.Info(

        title="QoS API",
        default_version='1.0.0',
        description="quality of service measurement tool using ping,curl,selenium chrome driver and ddosify to extract some parameters such as latency,page load timing,jitter,throughput,hopcount ...",
        contact=openapi.Contact(
            email="h.dashtabadi@gmail.com"),
        terms_of_service="https://www.google.com/policies/terms/",

    ),
    public=True,
    permission_classes=[permissions.IsAuthenticatedOrReadOnly],

)

urlpatterns = [
    path('', views.api_home),
    path('auth/', views.obtain_auth_token_api),
    path('swagger-json/', schema_view.without_ui(
        cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
    path("get-details", UserDetailAPI.as_view()),
    path('api-register', RegisterUserAPIView.as_view()),
]
