
from unicodedata import name
from django.conf import settings
from django.contrib import admin
from django.urls import path
from movie import views as movieViews
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',movieViews.home, name='home'),
    path('about/',movieViews.about),
    path('signup/',movieViews.signup, name='signup'),
]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)