from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin


class Studentlistcreate(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=Students.objects.all()
    serializer_class=BookSerializer

    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)


class Studentretrieveupdatedestroy(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset=Students.objects.all()
    serializer_class=BookSerializer

    def get(self,request,**kwargs):
        return self.retrieve(request,**kwargs)  
    
    def post(self,request,**kwargs):
        return self.update(request,**kwargs)  
    
    def delete(self,request,**kwargs):
        return self.destroy(request,**kwargs)
