from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todolists/', include('todolists.urls', namespace='todolists')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
]
