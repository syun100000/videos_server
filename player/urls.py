from django.urls import path
from . import views

urlpatterns = [
    path('video/<int:video_id>/', views.stream_video, name='stream_video'),
]