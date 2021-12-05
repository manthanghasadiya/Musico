from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),
    path('index', views.index, name='index'),
    path('add_song', views.add_song, name='add_song'),
    path('my_song', views.my_song, name='my_song'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    path('elements', views.elements, name='elements'),
    path('track', views.track, name='track'),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'),    
    # path('indexout', views.indexout, name='indexout'),
    path('loginnew', views.loginnew, name='loginnew'),
    path('public_song', views.public_song, name='public_song'),
    path('verify', views.verify, name='verify'),
    path('check_otp', views.check_otp, name='check_otp'),
    path('error', views.error, name='error'),
]
