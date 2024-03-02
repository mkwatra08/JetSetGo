from django.contrib import admin
from django.urls import path, include
from travel import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home  ,name='home'),
    path('about/',views.about  ,name='about'),
    path('blog/',views.blog  ,name='blog'),
    path('contact/',views.Contact ,name='contact'),
    path('portfolio/',views.portfolio  ,name='portfolio'),
    path('services/',views.services ,name='services'),
    path('team/',views.team  ,name='team')
]
