from django.urls import path, include
from . import views

urlpatterns = [
    path('hello', views.Hello.as_view()),
    path('goodbye', views.goodbye),
    path('lotto', views.make_lotto_number)
]
