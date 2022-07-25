
from django.contrib import admin
from django.urls import path
from movie import views as movieViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',movieViews.home),
    path('about/',movieViews.about)
]
