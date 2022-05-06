from django.urls import path

from .views import SignUpView, LogInView, EmailSearchView, TokenValidateView

urlpatterns = [
    path('', TokenValidateView.as_view()),
    path('signup', SignUpView.as_view()),
    path('search', EmailSearchView.as_view()),
    path('login', LogInView.as_view()),
]