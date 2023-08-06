from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from ms_identity_web.django.msal_views_and_urls import MsalViews

from . import views

msal_urls = MsalViews(settings.MS_IDENTITY_WEB).url_patterns()

urlpatterns = [
    path('', views.home, name='authenticate-home'),
    path('login', views.login_user, name='authenticate-login'),
    path('login', views.login_user, name='index'),
    path('logout', views.logout_user, name='authenticate-logout'),
    path(f'{settings.AAD_CONFIG.django.auth_endpoints.prefix}/', include(msal_urls)),
]
