from django.urls import path
from .views import (
    HomeView,
    ReadStudentView,
    CreateStudentView,
    UpdateStudentView,
    DeleteStudentView,
    ReadCourseView,
    CreateCourseView,
    UpdateCourseView,
    DeleteCourseView,
)


urlpatterns = [
    path("", HomeView.as_view(), name="index"),
    path("students", ReadStudentView.as_view(), name="student_list"),
    path("students/create/", CreateStudentView.as_view(),
         name="student_create"),
    path(
        "students/<int:id>/update/", UpdateStudentView.as_view(),
        name="student_update"
    ),
    path(
        "students/<int:id>/delete/", DeleteStudentView.as_view(),
        name="student_delete"
    ),
    # -------------------course----------------
    path("course", ReadCourseView.as_view(), name="course_list"),
    path("course/create/", CreateCourseView.as_view(), name="course_create"),
    path("course/<int:pk>/update/", UpdateCourseView.as_view(),
         name="course_update"),
    path("course/<int:id>/delete/", DeleteCourseView.as_view(),
         name="delete_course"),
]
