from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('user', views.user_View)
router.register('achievement', views.achievement_View)
router.register('match', views.match_View)
router.register('Game', views.game_View)
router.register('leaderboard', views.leaderboard_View)

urlpatterns = [
    path('', include(router.urls)),
    path('matchID/', views.get_match_id),
    path('getword/', views.get_word),
]
