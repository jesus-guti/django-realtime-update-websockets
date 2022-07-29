from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('rooms/', views.RoomsList.as_view()),
]
