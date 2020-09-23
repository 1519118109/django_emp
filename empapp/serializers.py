from rest_framework.serializers import ModelSerializer
from rest_framework import exceptions

from empapp.models import  Employee



class EmployeeModelSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

        extra_kwargs = {
            "emp_name": {
                'required': True,
                'min_length': 2,
                "error_messages": {
                    'required': '用户名必填',
                    'min_length': '用户长度不够'
                }
            }
        }
