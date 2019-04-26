from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Data_Server', views.user_View, views.achievement_View)

urlpatterns = [
    path('', include(router.urls))
]
