from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.ListReleaseView.as_view(), name='Release_list'),
    path('add/', views.CreateReleaseView.as_view(), name='Release_create'),
    path('<pk>/update/', views.UpdateReleaseView.as_view(), name='Release_update'),
    path('<pk>/delete/', views.DeleteReleaseView.as_view(), name='Release_delete'),
]
