"""recicle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('paginas.urls')),
    path('', include('contatos.urls')),
    path('blog/', include('posts.urls')),
    path('mensagens/', include('mensagens.urls')),
    path('perfil/', include('usuarios.urls')),
    path('admin/', admin.site.urls),
]

# configura a pagina de erro 404
handler404 = "paginas.views.view_404"

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'ADMINISTRAÇÃO DO SISTEMA RECICLE!'
admin.site.site_title = 'RECICLE ADMIN'
