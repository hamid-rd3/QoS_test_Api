from . import views
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import permissions

from drf_yasg.views import get_schema_view as swagger_get_schema_view
from drf_yasg import openapi

schema_view = swagger_get_schema_view(
    openapi.Info(
        title="QoS API",
        default_version='1.0.0',
        description="API documentation \n github link :https://github.com/hamid-rd3/QoS_test_Api",
        contact=openapi.Contact(
            email="h.dashtabadi@gmail.com"),
        terms_of_service="https://www.google.com/policies/terms/",
    ),
    public=True,
    url="http://185.130.78.174:5201/api/swagger/",
    permission_classes=[permissions.AllowAny],

)

urlpatterns = [
    path('', views.api_home),
    path('auth/', obtain_auth_token),
    path('register/', views.RegisterUserAPIView.as_view()),
    path('swagger-json/', schema_view.without_ui(
        cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
]
