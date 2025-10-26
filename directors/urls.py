from django.urls import path
from . import views


urlpatterns = [
    path('directors/', views.DirectorCreatListView.as_view(), name='director-creat-list'),
    path('directors/<int:pk>/', views.DirectorRetrieveUpdateDestroyView.as_view(), name='director-detail-view'),
]
