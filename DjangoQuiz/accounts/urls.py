from accounts.views import LoginView, RegisterView, UserView
from django.urls import path

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('register/', RegisterView.as_view()),
    path('user/', UserView.as_view()),
]