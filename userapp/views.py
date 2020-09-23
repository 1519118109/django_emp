from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from userapp.models import User
from userapp.serializers import UserModelSerializer
from utils.response import APIResponse


class RegieterAPIView(APIView):

    permission_classes = []
    authentication_classes = []
    def post(self, request, *args, **kwargs):
        request_data = request.data
        serializer = UserModelSerializer(data=request_data,context={"request": request},)
        serializer.is_valid(raise_exception=True)
        user_obj = serializer.save()
        data = UserModelSerializer(user_obj).data

        return APIResponse(200, True, results=data)

class LoginAPIView(APIView):
    permission_classes = []
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")

        user_obj = User.objects.filter(username=username, password=password).first()
        if user_obj:
            data = UserModelSerializer(user_obj).data
            return APIResponse(200, True, results=data)

        return APIResponse(400, False)




# class UserAPIView(APIView):
#
#     def post(self, request, *args, **kwargs):
#         """
#         处理用户注册逻辑
#         :param request: 前端传递的用户的数据
#         :return:  注册成功与否
#         """
#
#         request_data = request.data
#         serializer = UserModelSerializer(data=request_data)
#         serializer.is_valid(raise_exception=True)
#         user_obj = serializer.save()
#         data = UserModelSerializer(user_obj).data
#
#         return APIResponse(200, True, results=data)
#
#     def get(self, request, *args, **kwargs):
#         """
#         用户的登录请求
#         :param request:
#         :return:
#         """
#         username = request.query_params.get("username")
#         password = request.query_params.get("password")
#
#         user_obj = User.objects.filter(username=username, password=password).first()
#         if user_obj:
#             data = UserModelSerializer(user_obj).data
#             return APIResponse(200, True, results=data)
#
#         return APIResponse(400, False)