from django.shortcuts import render
from rest_framework import filters
# Create your views here.
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin,\
    DestroyModelMixin,UpdateModelMixin,RetrieveModelMixin

from empapp.models import Employee
from empapp.serializers import EmployeeModelSerializer
from utils.response import APIResponse


class EmployeeGenericAPIView(ListModelMixin, CreateModelMixin,
                             GenericAPIView,DestroyModelMixin,
                             UpdateModelMixin,RetrieveModelMixin):
    permission_classes = []
    authentication_classes = []
    queryset = Employee.objects.all()
    serializer_class = EmployeeModelSerializer
    lookup_field = 'id'
    def get(self, request, *args, **kwargs):
        if "id" in kwargs:
            response = self.retrieve(request, *args, **kwargs)
            return APIResponse(200, True, results=response.data)
        print('333')
        response = self.list(request, *args, **kwargs)
        return APIResponse(200, True, results=response.data)

    def post(self, request, *args, **kwargs):
        emp_obj = self.create(request, *args, **kwargs)
        return APIResponse(200, True, results=emp_obj.data)

    def delete(self, request, *args, **kwargs):
        emp_obj = self.destroy(request, *args, **kwargs)
        queryset = self.list(request, *args, **kwargs)
        return APIResponse(200, True, results=queryset.data)

    def patch(self, request, *args, **kwargs):
        response = self.partial_update(request, *args, **kwargs)
        return APIResponse(200, True, results=response.data)