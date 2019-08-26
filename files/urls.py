from django.urls import include, path
from rest_framework import routers
from files import views

router = routers.DefaultRouter()
router.register(r'', views.FileItemViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('history/uploaded/', views.upload_history_file_list),
    path('history/downloaded/', views.download_history_file_list),
]