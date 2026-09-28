from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include('employees.urls')),
    path('api/', include('categories.urls')),
    path('api/', include('tickets.urls')),
]