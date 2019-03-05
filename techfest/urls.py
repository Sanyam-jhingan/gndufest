
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home,name="home"),
    path("/",include("accounts.urls",namespace="accounts")),
    path("about",views.about,name="about"),
    path("privacy",views.privacy,name="privacy"),
    path("events/",include("events.urls",namespace="events")),
    path("logout",views.log_out,name="logout"),
    path("placement",views.placement,name="placement"),
    path("announcement", views.announcement, name="announcement"),
    path("announcement2/<int:id>/", views.announce, name="announcement2"),
      path("reg",views.reg,name="reg"),


]
