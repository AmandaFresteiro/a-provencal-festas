from django.conf import settings
from django.urls import path
from .views import contact, home, cakes, party, candy, about, partykit, cakes_photo, start
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='index'),
    path('inicio', start, name='start'),
    path('contato/', contact, name='contact'),
    path('bolos-videos/', cakes, name='cakes'),
    path('festas/', party, name='party'),
    path('doces/', candy, name='candy'),
    path('quemsomos/', about, name='about'),
    path('kitfesta', partykit, name='partykit'),
    path('bolos-fotos', cakes_photo, name='cakes-photo'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)