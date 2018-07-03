
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
]

# from django.urls import include, path
#
# from . import views
#
# urlpatterns = [
#     path('', views.UserListView.as_view()),
# ]
