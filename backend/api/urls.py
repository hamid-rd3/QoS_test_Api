from . import views
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token


from drf_yasg.views import get_schema_view as swagger_get_schema_view
from drf_yasg import openapi

schema_view = swagger_get_schema_view(
    openapi.Info(
        title="QoS API",
        default_version='1.0.0',
        description="API documentation of App",
    ),
    public=True,
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
