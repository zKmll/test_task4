from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='main'),
    path('config/', views.stripe_config),
]
