from django.urls import path

from .views import SignUpView, LogInView, EmailSearchView

urlpatterns = [
    path('signup', SignUpView.as_view()),
    path('search', EmailSearchView.as_view()),
    path('login', LogInView.as_view()),
]