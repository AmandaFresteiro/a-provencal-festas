from django.urls import path
from .views import contact, home, cakes, party, candy, about
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='index'),
    path('contato/', contact, name='contact'),
    path('bolos/', cakes, name='cakes'),
    path('festas/', party, name='party'),
    path('doces/', candy, name='candy'),
    path('quemsomos/', about, name='about')
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)