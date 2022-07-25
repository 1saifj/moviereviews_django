
from unicodedata import name
from django.contrib import admin
from django.urls import path
from movie import views as movieViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',movieViews.home, name='home'),
    path('about/',movieViews.about),
    path('signup/',movieViews.signup, name='signup'),
]
