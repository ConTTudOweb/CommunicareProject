"""communicare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include

from .core.views import HomeTemplateView, contact, EventDetailView, registration, send_contract, \
    PrivacyPolicyTemplateView, CookiesStatementTemplateView, GalleryTemplateView, TreinamentoOratoriaTemplateView, \
    CursoHipnoseTemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeTemplateView.as_view(), name='home'),
    path('contact/', contact, name='contact'),
    path('event/<slug:slug>/', EventDetailView.as_view(), name='event-detail'),
    path('registration/', registration, name='registration'),
    path('send_contract/', send_contract, name='send_contract'),
    path('treinamento-de-oratoria/', TreinamentoOratoriaTemplateView.as_view(), name='treinamento_oratoria'),
    path('curso-de-hipnose/', CursoHipnoseTemplateView.as_view(), name='curso_hipnose'),
    path('galeria-de-fotos/', GalleryTemplateView.as_view(), name='gallery'),
    path('politica-de-privacidade/', PrivacyPolicyTemplateView.as_view(), name='privacy_policy'),
    path('declaracao-de-cookies/', CookiesStatementTemplateView.as_view(), name='cookies_statement'),

    path('select2/', include('django_select2.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
