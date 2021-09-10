from django.urls import path

from users import views


urlpatterns = [
    path('login/', views.UserLoginAPIView.as_view(), name='login'),
    path('groups/', views.GroupAPIView.as_view(), name='group-list'),
]
