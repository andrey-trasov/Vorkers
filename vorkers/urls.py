from vorkers.apps import VorkersConfig
from vorkers.views import VorkersRetrieveAPIView, TeamVorkersListAPIView

from django.urls import path

app_name = VorkersConfig.name




urlpatterns = [
    path("v1/worker/<int:pk>/", VorkersRetrieveAPIView.as_view(), name="vorker"),
    path("v1/team/<int:team_id>/WorkerList/", TeamVorkersListAPIView.as_view(), name="team_vorkers"),
]