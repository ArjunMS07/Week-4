from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics

from .models import Course
from .serializers import CourseSerializer
from django.http import HttpResponse


def home_view(request):
    context = {
        "title": "Klaw Courses",
        "user_name": "Arjun",
        "courses": ["Python", "Django", "AI", "Web Development"]
    }
    return render(request, "courses/course_list.html", context)
def detail_view(request, name):
    return HttpResponse(f"Course Name: {name}")

@api_view(['GET', 'POST'])
def course_list(request):

    if request.method == 'GET':
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

from rest_framework import viewsets

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer