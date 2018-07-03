from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    """docstring for UserSerializer."""
    class Meta:
        model = models.CustomUser
        fields = ('email', 'username', )
