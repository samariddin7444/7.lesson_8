from django.urls import path
from .views import LandingPageView, logout_view, login_view, register_view


urlpatterns = [
    path('', LandingPageView.as_view(), name='landing'),
    path('logout/',logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
]

