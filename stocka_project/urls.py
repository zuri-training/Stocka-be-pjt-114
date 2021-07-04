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
from rest_auth.views import PasswordResetConfirmView
from allauth.account.views import confirm_email
from django.conf.urls import url
from users import views
from rest_framework import permissions


# Schema and documentation
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

API_TITLE = "Stocka API"  
API_DESCRIPTION = "A Web API to the Stocka Project."
coreapi_schema_view = get_schema_view(title=API_TITLE)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('stocka_api/v1/', include('stocka_api.urls')),
    path('stocka_api/v1/', include('users.urls')),
    path('stocka_api/v1/rest-auth/', include('rest_auth.urls')),  # login & logout endpoints
    path('stocka_api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),    # signup endpoints
    path('accounts/', include('allauth.urls')),

    # urls to password reset and registration verification
    url(r"stocka_api/v1/accounts-rest/registration/account-confirm-email/(?P<key>.+)/$", confirm_email,name="account_confirm_email"),
    url(r"^stocka_api/v1/registration/complete/$", views.success_view, name="account_confirm_complete"),
    path("stocka_api/v1/password_reset/",include("django_rest_passwordreset.urls", namespace="password_reset")),
    
    # urls to the schema and doc
    path('docs/', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    path("schema/", coreapi_schema_view),

]
