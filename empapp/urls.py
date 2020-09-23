from django.urls import path

from empapp import views

urlpatterns = [

    path('emp/', views.EmployeeGenericAPIView.as_view()),
    path('emp/<str:id>/', views.EmployeeGenericAPIView.as_view()),

]