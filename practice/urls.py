from django.urls import path

from empapp import views

urlpatterns = [

    path('pra/', views.EmployeeGenericAPIView.as_view()),
    path('pra/<str:id>/', views.EmployeeGenericAPIView.as_view()),

]