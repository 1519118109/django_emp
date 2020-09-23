from django.conf.urls import url
from django.urls import path
from rest_framework_jwt.views import ObtainJSONWebToken, obtain_jwt_token

from userapp import views


urlpatterns=[
    # path('users/', views.UserAPIView.as_view()),
    # path('users/<str:id>/', views.UserAPIView.as_view()),
    # url(r'^login_out/', obtain_jwt_token),
    path('register/', views.RegieterAPIView.as_view()),
    path('register/<str:id>/', views.RegieterAPIView.as_view()),
    path('login_out/', views.LoginAPIView.as_view()),
    path('login_out/<str:id>/', views.LoginAPIView.as_view()),
    #点击obtain_jwt_token，等效于ObtainJSONWebToken.as_view()
    # 效果同上
    # path("login_out/", ObtainJSONWebToken.as_view()),


]