from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from authentication.views import *
from home.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('shift/', shift, name='shift'),
    path('delshift/<int:id>', delete_shift, name='delshift'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)