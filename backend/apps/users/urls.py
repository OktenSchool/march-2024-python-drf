from django.urls import path
from .views import UsersListCreateView,UserMeView

urlpatterns = [
    path('', UsersListCreateView.as_view(), name='users_list_create'),
    path('/me', UserMeView.as_view(), name='user_me'),
]
