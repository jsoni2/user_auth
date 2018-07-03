# from django.shortcuts import render
# from rest_framework import generics
#
# from . import models
# from . import serializers
#
# class UserListView(generics.ListCreateAPIView):
#     """docstring for UserListView."""
#     queryset = models.CustomUser.objects.all()
#     serializer_class = serializers.UserSerializer
#

from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm

class SignUp(generic.CreateView):
    """docstring for SignUp."""
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
     
