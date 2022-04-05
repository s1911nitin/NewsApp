from django import views
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('bbc/', views.BBCNewsView.as_view(), name='bbc'),
    path('india/', views.IndiaNewsView.as_view(), name='india'),
    path('sports/', views.SportsNewsView.as_view(), name='sports'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)