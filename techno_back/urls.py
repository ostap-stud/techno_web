from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('history/', views.history, name='history'),
    # path('about/', views.about, name='about'),
    path('artist1/', views.artist1, name='artist1'),
    path('artist2/', views.artist2, name='artist2'),
    path('artist3/', views.artist3, name='artist3'),
    path('about/', views.about_and_feedback, name='about')
]

