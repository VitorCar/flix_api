
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    # Faz a leitura das URLs
    path('api/v1/', include('genres.urls')),   # Versionamento de API. Caso tenha a versão 2 path('api/v2/', include('genres.urls_v2'))
    path('api/v1/', include('actors.urls')),
    path('api/v1/', include('directors.urls')),
    path('api/v1/', include('movies.urls')),
    path('api/v1/', include('reviews.urls')),
    path('api/v1/', include('authentication.urls')),
]
