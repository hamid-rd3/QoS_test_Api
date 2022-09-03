from . import views
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from .authentication import TokenScheme
# schema_view = swagger_get_schema_view(
#     openapi.Info(
#         title="QoS API",
#         default_version='1.0.0',
#         description="API documentation \n github link :https://github.com/hamid-rd3/QoS_test_Api",
#         contact=openapi.Contact(
#             email="h.dashtabadi@gmail.com"),
#         terms_of_service="https://www.google.com/policies/terms/",
#     ),
#     public=True,
#     url="http://185.130.78.174:5201/api/swagger/",
#     permission_classes=[permissions.AllowAny],

# )

urlpatterns = [
    path('', views.api_home),
    path('auth/', TokenScheme),
    path('register/', views.RegisterUserAPIView.as_view()),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('schema/swagger-ui/',
         SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/',
         SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
