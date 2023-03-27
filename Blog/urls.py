
from django.contrib import admin
from django.urls import path
from cms.views import *

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostView.as_view(), name="index"),
    path('insert/', PostCreateView.as_view(), name="insert"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)