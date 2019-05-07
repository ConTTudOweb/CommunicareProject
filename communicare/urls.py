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
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.views.generic import RedirectView

from .sitemaps import StaticViewSitemap
from .core.views import HomeTemplateView, contact, EventDetailView, registration, send_contract, \
    PrivacyPolicyTemplateView, CookiesStatementTemplateView, GalleryTemplateView, TreinamentoOratoriaTemplateView, \
    CursoHipnoseTemplateView, TreinamentoInteligenciaEmocionalTemplateView, contact_whatsapp, \
    AtendimentoCoachingTemplateView, AtendimentoHipnoterapiaTemplateView, PalestraInteligenciaEmocionalTemplateView, \
    InterestedView, interested

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url=settings.STATIC_URL + 'images/favicon.ico')),
    path('admin/', admin.site.urls),

    # Páginas
    path('', HomeTemplateView.as_view(), name='home'),
    path('galeria-de-fotos/', GalleryTemplateView.as_view(), name='gallery'),
    path('politica-de-privacidade/', PrivacyPolicyTemplateView.as_view(), name='privacy_policy'),
    path('declaracao-de-cookies/', CookiesStatementTemplateView.as_view(), name='cookies_statement'),
    path('evento/<slug:slug>/', EventDetailView.as_view(), name='event-detail'),

    # Ajax
    path('contact/', contact, name='contact'),
    path('contact_whatsapp/', contact_whatsapp, name='contact_whatsapp'),
    path('registration/', registration, name='registration'),
    path('interested/', interested, name='interested'),
    path('send_contract/', send_contract, name='send_contract'),

    # Cursos / Treinamentos
    path('treinamento-de-oratoria/', TreinamentoOratoriaTemplateView.as_view(), name='treinamento_oratoria'),
    path('curso-de-hipnose/', CursoHipnoseTemplateView.as_view(), name='curso_hipnose'),
    path('treinamento-de-inteligencia-emocional/', TreinamentoInteligenciaEmocionalTemplateView.as_view(), name='treinamento_inteligencia_emocional'),

    # Atendimentos
    path('atendimento-coaching/', AtendimentoCoachingTemplateView.as_view(), name='atendimento_coaching'),
    path('atendimento-hipnoterapia/', AtendimentoHipnoterapiaTemplateView.as_view(), name='atendimento_hipnoterapia'),

    # Palestras
    path('palestra-inteligencia-emocional/', PalestraInteligenciaEmocionalTemplateView.as_view(), name='palestra_inteligencia_emocional'),
    path('solicitar-palestra/', InterestedView.as_view(), name='solicitar_palestra'),

    path('select2/', include('django_select2.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
