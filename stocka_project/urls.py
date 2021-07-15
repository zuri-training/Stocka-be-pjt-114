"""stocka_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView, RedirectView
from django.conf.urls import url
from django.contrib.auth import views
from allauth.account.views import confirm_email

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
#from rest_auth.views import PasswordResetConfirmView
from rest_framework import permissions
#  Documentation
from rest_framework.documentation import include_docs_urls

API_TITLE = "Stocka API"
API_DESCRIPTION = "A Web API to the Stocka Project."


schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stocka_api/v1/', include('stocka_api.urls')),
    path('stocka_api/v1/', include('users.urls')),
    # login & logout endpoints
    path('stocka_api/v1/rest-auth/', include('rest_auth.urls')),
    path('stocka_api/v1/rest-auth/registration/',
         include('rest_auth.registration.urls')),    # signup endpoints
    path('accounts/', include('allauth.urls')),

    # urls to password reset and registration verification


    url(
        r'^stocka_api/v1/accounts-rest/password_change/$', views.PasswordChangeView.as_view(),
        name='password_change'),
    url(
        r'^stocka_api/v1/accounts-rest/password_change/done/$',
        views.PasswordChangeDoneView.as_view(),
        name='password_change_done'),
    url(
        r'^stocka_api/v1/accounts-rest/password_reset/$', views.PasswordResetView.as_view(),
        name='password_reset'
        ),
    url(
        r'^stocka_api/v1/accounts-rest/done/$',
        views.PasswordResetDoneView.as_view(),
        name='password_reset_done'),
    url(
        r'^stocka_api/v1/accounts-rest/password_reset/done/$',
        views.PasswordResetDoneView.as_view(),
        name='password_reset_done'),

    
    url(
        r'^password-reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    url(
        r'^stocka_api/v1/accounts-rest/registration/account-confirm-email/(?P<key>.+)/$',
        confirm_email, name='account_confirm_email'),

    # urls to the doc
    path('docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),


    # Swagger Documentation
    path('swagger/', schema_view.with_ui('swagger',
                                         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
                                       cache_timeout=0), name='schema-redoc'),
]
