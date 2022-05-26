from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todolists/', include('todolists.urls', namespace='todolists')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    # path('', 'index.html', name='index'),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)