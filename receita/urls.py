from django.contrib import admin
from django.urls import path
from django.urls.conf import include

import receitas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('receitas/', include('receitas.urls')),
    path('produto/', include('produto.urls')),
    path('sobre/', include('sobre.urls')),
]
