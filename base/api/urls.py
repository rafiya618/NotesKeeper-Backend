from django.urls import path
from . import views
from .views import MyTokenObtainPairView


from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
urlpatterns=[
    path('',views.getRoutes),
    path('notes/',views.getNotes),
    path('notes/create/', views.createNote),
    path('notes/update/<int:pk>/', views.updateNote),
    path('notes/delete/<int:pk>/', views.deleteNote),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]