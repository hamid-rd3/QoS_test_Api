
from django.contrib import admin,admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/products/', include('products.urls')),
]
