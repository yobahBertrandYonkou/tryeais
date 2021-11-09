"""tryeais URL Configuration

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
from django.urls import path
from tryeaisapp.views import delete_record, home, login_user, dashboard, accounts, logout_user, save_records, settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", view=home, name="home"),
    path("login", view=login_user, name="login"),
    path("dashboard", view=dashboard, name="dashboard"),
    path("accounts", view=accounts, name="accounts"),
    path("settings", view=settings, name="settings"),
    path("save_records", view=save_records, name="save_records"),
    path("logout", view=logout_user, name="logout"),
    path("delete_record/<int:id>", view=delete_record, name="delete_record"),
]
