
from django.contrib import admin
from django.urls import path, include
from api import views as api_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/products/', include('products.urls')),
]
