from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.artist_list_view, {'my_template_name': 'index'}, name='index'),
    path('history/', views.artist_list_view, {'my_template_name': 'history'}, name='history'),
    path('about/', views.about_and_feedback, name='about'),
    re_path(r'^artist/(?P<pk>\d+)$', views.ArtistView.as_view(), name='artist'),
]

