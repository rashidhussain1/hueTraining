from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
  TokenObtainPairView,
  TokenRefreshView,
)

urlpatterns = [
    #path('getuser', views.getUser),
    #path('setuser', views.setUser),
    #path('user', UserView.as_view()),
    path('user/', views.UserView.as_view()),
    path('issue/', views.IssueView.as_view()),
    path('project/', views.ProjectView.as_view()),
    path('comment/', views.CommentView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]