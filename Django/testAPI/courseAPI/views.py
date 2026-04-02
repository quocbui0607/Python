from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course
from .serializers import getAllCourseSerializer, CourseSerializer
# Create your views here.

class getAllCourses(APIView):
    def get(self,request):
        list_course = Course.objects.all()
        all_courses = getAllCourseSerializer(list_course, many=True)
        return Response(all_courses.data, status=status.HTTP_200_OK)

    def post(self,request):
        my_data = CourseSerializer(data=request.data)
        if not my_data.is_valid():
            return Response('Sai du lieu', status=status.HTTP_400_BAD_REQUEST)
        title = my_data.data['title1']
        content = my_data.data['content1']
        price= my_data.data['price1']
        cs = Course.objects.create(title=title, content=content, price=price)
        return Response(data=cs.id, status=status.HTTP_200_OK)