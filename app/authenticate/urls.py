from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='authenticate-home'),
    path('login', views.login_user, name='authenticate-login'),
    path('logout', views.logout_user, name='authenticate-logout'),
]
