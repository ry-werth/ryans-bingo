from django.urls import path

from . import views

urlpatterns = [
    path('card/<int:card_number>/', views.cardView),
    path('caller/', views.caller),
    path('', views.landing),
]
