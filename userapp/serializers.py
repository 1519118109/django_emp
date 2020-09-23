from rest_framework.serializers import ModelSerializer
from rest_framework import exceptions

from userapp.models import User


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

        extra_kwargs = {
            "username": {
                'required': True,
                'min_length': 2,
                "error_messages": {
                    'required': '用户名必填',
                    'min_length': '用户长度不够'
                }
            }
        }

    # 局部钩子
    def validate_username(self, attrs):
        user = User.objects.filter(username=attrs).first()
        if user:
            raise exceptions.ValidationError("用户名已存在")

        return attrs

    # 全局钩子
    def validate(self, attrs):
        request = self.context.get("request")
        if request.data.get('password')!=request.data.get('re_pwd'):
            raise exceptions.ValidationError('两次密码不匹配')
        return attrs
