from django.urls import path
from .views import MenuVoteView, TodaysMenusAPIView


urlpatterns = [
    path("vote/", MenuVoteView.as_view(), name="get_current_day_menu"),
    path("current/", TodaysMenusAPIView.as_view(), name="vote_for_menu"),
    #Other URLs ...
]