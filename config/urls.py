from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import login_view
from todolists.views import myToDoList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),
    path('index/', myToDoList, name='index'),
    path('todolists/', include('todolists.urls', namespace='todolists')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)