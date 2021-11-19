from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from home import views


urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('sobre/', include('sobre.urls')),
]
