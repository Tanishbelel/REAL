"""
URL configuration for name project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from veggie.views import *
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from veggie import views



urlpatterns = [
    path('' , home , name="home"),
    path('delete/<id>/', delete , name = "delete"),
    path('update/<id>/', update , name = "update"),
    path('recipes/' , recipes , name = "recipes"),
    path('login/' , login_page , name="login"),
    path('register/' , register_page , name="register"),
    path('logout/' , logout_page , name="logout"),
    path('dashboard/' , dashboard , name="dashboard"),
    path('toggle-favorite/<int:recipe_id>/', views.toggle_favorite, name='toggle_favorite'),
    path('favorites/', views.favorites_view, name='favorites'),
    path('profiles/', profile_view, name='profile'),
    path('buy-token/', buy_token, name='buy_token'),
    path('favorites/view-skill/', views.view_skill, name='view-skill'),
    path('trade/<int:recipe_id>/', views.trade_skill, name='trade_skill'),
    






    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, 
                          document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
